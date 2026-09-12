// The early-access form: one POST to the license worker, Turnstile in
// front of it, plain words back. Without JavaScript the mail link in
// <noscript> stands in; when the endpoint or the widget is not
// reachable the same mail link is offered in the status line.
(function () {
  var ENDPOINT = "https://license.docenta.ai/v1/early-access";
  var SITE_KEY = "0x4AAAAAAEuUdAlBD_uMZVV0";
  var MAIL = "docenta@nios.net";
  var form = document.getElementById("early-access");
  if (!form) return;
  var status = form.querySelector(".ea-status");
  var button = form.querySelector("button[type=submit]");
  var mount = form.querySelector(".ea-turnstile");
  var token = "";
  var widget = null;
  var widgetFailed = false;

  function say(text, link) {
    status.textContent = text;
    if (link) {
      var a = document.createElement("a");
      a.href = "mailto:" + MAIL + "?subject=docenta%20early%20access%20(" + encodeURIComponent(form.dataset.audience || "site") + ")";
      a.textContent = MAIL;
      status.appendChild(document.createTextNode(" "));
      status.appendChild(a);
      status.appendChild(document.createTextNode("."));
    }
  }

  function renderWidget() {
    if (!mount || !window.turnstile) return;
    try {
      widget = window.turnstile.render(mount, {
        sitekey: SITE_KEY,
        callback: function (t) { token = t; },
        "error-callback": function () { widgetFailed = true; mount.hidden = true; },
        "expired-callback": function () { token = ""; }
      });
    } catch (e) {
      widgetFailed = true;
      mount.hidden = true;
    }
  }
  if (mount) {
    if (window.turnstile) {
      renderWidget();
    } else {
      var script = document.createElement("script");
      script.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
      script.async = true;
      script.onload = renderWidget;
      script.onerror = function () { widgetFailed = true; mount.hidden = true; };
      document.head.appendChild(script);
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var name = form.elements.name.value.trim();
    var email = form.elements.email.value.trim();
    if (!name) { say("Please tell us your name."); form.elements.name.focus(); return; }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) { say("That email address does not look right; please check it."); form.elements.email.focus(); return; }
    if (mount && !widgetFailed && !token) { say("Please finish the human check above the button, then click again."); return; }
    button.disabled = true;
    say("Sending ...");
    var body = {
      name: name,
      email: email,
      audience: form.elements.audience.value,
      message: form.elements.message.value.trim(),
      turnstile_token: token
    };
    fetch(ENDPOINT, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(body)
    }).then(function (response) {
      return response.json().then(function (data) { return { ok: response.ok, status: response.status, data: data }; });
    }).then(function (result) {
      if (result.ok) {
        say("Thank you. We wrote it down and will write back to " + email + " when the door opens.");
        form.reset();
        if (widget !== null && window.turnstile) window.turnstile.reset(widget);
        token = "";
        return;
      }
      button.disabled = false;
      if (result.status === 403) {
        token = "";
        if (widget !== null && window.turnstile) window.turnstile.reset(widget);
        say("The human check did not pass. It has been reset; please complete it and click again.");
      } else if (result.status === 429) {
        say("Too many requests from this address just now. Please wait a minute and try once more.");
      } else if (result.status === 400) {
        say("Something in the form was not accepted (" + (result.data && result.data.field ? result.data.field : "a field") + "). Please check it and try again.");
      } else {
        say("The form is not open right now. Please write to", true);
      }
    }).catch(function () {
      button.disabled = false;
      say("The form is not open right now. Please write to", true);
    });
  });
})();
