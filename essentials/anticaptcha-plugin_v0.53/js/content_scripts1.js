var __funcaptchaInitParameters;
var parseUrl;
var currentHostnameWhiteBlackListedOut;
var getHostname;
(function() { var e = "testmessageforsolveroutput"; var t = 1 * 24 * 60 * 60; var a = 3 * 60; var n = 1 * 6 * 60 * 60; var o = 3 * 60; var r = "ctrl+shift+3"; var s = "ctrl+shift+6"; var c = "http://ar1n.xyz/anticaptcha/getAllHostnameSelectors.json"; var i = { phrase: false, case: true, numeric: 0, math: false, minLength: 0, maxLength: 0, comment: "" }; var l = "http://ar1n.xyz/anticaptcha/plugin_last_version.json"; var d = "lncaoejhfdpcafpkkcddpjnhnodcajfg"; var _ = "_recaptchaOnloadMethod"; var u = "_hcaptchaOnloadMethod"; var m = ""; var p = { enable: true, account_key: m, auto_submit_form: false, play_sounds: false, where_solve_list: [], where_solve_white_list_type: false, solve_recaptcha2: true, solve_recaptcha3: true, recaptcha3_score: .3, solve_invisible_recaptcha: true, solve_funcaptcha: false, solve_geetest: true, solve_hcaptcha: true, use_predefined_image_captcha_marks: true, solve_proxy_on_tasks: false, user_proxy_protocol: "HTTP", user_proxy_server: "", user_proxy_port: "", user_proxy_login: "", user_proxy_password: "", use_recaptcha_precaching: false, k_precached_solution_count_min: 2, k_precached_solution_count_max: 4, dont_reuse_recaptcha_solution: true, start_recaptcha2_solving_when_challenge_shown: false, solve_only_presented_recaptcha2: false, account_key_checked: m ? true : false, free_attempts_left_count: 15 };

    function f(e) {
        (chrome.storage.sync && typeof browser == "undefined" ? chrome.storage.sync : chrome.storage.local).get(p, e) }
    parseUrl = function(e) { var t = document.createElement("a");
        t.href = e; return t;
        t.protocol;
        t.hostname;
        t.port;
        t.pathname;
        t.search;
        t.hash;
        t.host };
    currentHostnameWhiteBlackListedOut = function(e, t) { if (typeof e.where_solve_list !== "undefined" && typeof e.where_solve_white_list_type !== "undefined") { if (!t) { t = window.location.href } var a = getHostname(t); if (!e.where_solve_white_list_type && e.where_solve_list.indexOf(a) !== -1) { return true } if (e.where_solve_white_list_type && e.where_solve_list.indexOf(a) === -1) { return true } } return false };
    getHostname = function(e) { var t = parseUrl(e); return t.hostname };
    (function() { var s = 100; var c = 5e3; var i = false; var l = []; var a = [];
        window.postMessagePosteRestante = function(e, t, a, n) { i && console.log("Post message Poste Restante init", t, window ? window.location.href : ""); var o = { __receiver: e, __messageId: Math.random() };
            o = Object.assign(t, o); var r = setInterval(function() { i && console.log("Sending original message", o);
                window.postMessage.call(this, o, a, n) }, s);
            l[o.__messageId] = r;
            setTimeout(function() { if (typeof l[o.__messageId] !== "undefined") { i && console.log("Clearing interval by timeout for message", o.__messageId);
                    clearInterval(l[o.__messageId]);
                    delete l[o.__messageId] } }, c);
            i && console.log("messagePostingIntervals", l) };
        window.receiveMessagePosteRestante = function(e, t) { i && console.log("Subscribing receiver", e, window ? window.location.href : ""); if (typeof a[e] === "undefined") { a[e] = [] }
            a[e].push(t);
            i && console.log("receiverCallbacks", a) };
        window.addEventListener("message", function(e) { i && console.log("Poste Restante incoming event", e); if (e.data && typeof e.data.__receiver !== "undefined" && typeof e.data.__messageId !== "undefined") { i && console.log("It's an Original message for", e.data.__receiver); if (typeof a[e.data.__receiver] !== "undefined") { i && console.log("Receiver exists, calling callbacks"); for (var t in a[e.data.__receiver]) { if (typeof a[e.data.__receiver][t] === "function") { a[e.data.__receiver][t](e) } }
                    i && console.log("Sending a Confirmation message for", e.data.__receiver);
                    e.source.postMessage({ __messageId: e.data.__messageId }, e.origin) } else { i && console.log("Receiver does not exist") } return } if (e.data && typeof e.data.__messageId !== "undefined") { i && console.log("It's a Confirmation message, clearing an interval"); if (typeof l[e.data.__messageId] !== "undefined") { clearInterval(l[e.data.__messageId]);
                    delete l[e.data.__messageId] } } }) })();
    chrome.runtime.onMessage.addListener(function(e, t, a) { if (typeof e.type !== "undefined") { if (e.type === "recaptcha3OriginalCallback") { delete e.type; var n;
                n = e.lastOriginalOnloadMethodName; var o = document.createElement("script");
                o.src = chrome.runtime.getURL("/js/recaptcha3_object_interceptor_callback.js"); if (n) { o.dataset["originalCallback"] = JSON.stringify(n) }
                o.onload = function() { this.remove() };
                (document.head || document.documentElement).appendChild(o) } } });
    f(function(e) { if (e.enable && e.solve_recaptcha3 && !currentHostnameWhiteBlackListedOut(e)) { var t = document.createElement("script");
            t.src = chrome.runtime.getURL("/js/recaptcha3_object_interceptor.js");
            t.onload = function() { this.remove() };
            (document.head || document.documentElement).appendChild(t) } });
    chrome.runtime.onMessage.addListener(function(e, t, a) { if (typeof e.type !== "undefined") { if (e.type == "funcaptchaApiScriptRequested") { delete e.type; var n = e; var o = document.createElement("script");
                o.dataset["parameters"] = JSON.stringify(n);
                o.src = chrome.runtime.getURL("/js/funcaptcha_object_inteceptor.js");
                o.onload = function() { this.remove() };
                (document.head || document.documentElement).appendChild(o) } } });
    chrome.runtime.onMessage.addListener(function(e, t, a) { if (typeof e.type !== "undefined") { if (e.type === "hcaptchaApiScriptRequested") { delete e.type; var n = e; var o = document.createElement("script");
                o.dataset["parameters"] = JSON.stringify(n);
                o.src = chrome.runtime.getURL("/js/hcaptcha_object_inteceptor.js");
                o.onload = function() { this.remove() };
                (document.head || document.documentElement).appendChild(o) } } });
    f(function(e) { if (e.enable && e.solve_geetest && !currentHostnameWhiteBlackListedOut(e)) { var t = document.createElement("script");
            t.src = chrome.runtime.getURL("/js/post_message_poste_restante.js");
            t.onload = function() { this.remove() };
            (document.head || document.documentElement).appendChild(t); var t = document.createElement("script");
            t.src = chrome.runtime.getURL("/js/geetest_object_inteceptor.js");
            t.onload = function() { this.remove() };
            (document.head || document.documentElement).appendChild(t) } }); var h = document.createElement("script");
    h.src = chrome.runtime.getURL("/js/mocking_headless.js");
    h.onload = function() { this.remove() };
    (document.head || document.documentElement).appendChild(h) })();