# Content from https://archive.vanityfair.com/article/2019/10/dating-the-monster

*Retrieved: 2025-09-15T02:14:05.058520*

---

<!DOCTYPE html>
<html lang="en-US" ng-app="issue">
    <head>
        <title>Dating the Monster | Vanity Fair | October 2019</title>

                                    <meta charset="utf-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=yes" />

                        <link rel="shortcut icon" href="https://vanityfair.archive.content.pugpig.com/vanityfair/favicon.png" />

            <meta name="robots" content="index,follow" />
            <meta name="googlebot" content="index,follow" />
            <meta name="google" content="notranslate" />

            <meta property="og:type" content="website" />
            <meta property="og:site_name" content="Vanity Fair | The Complete Archive" />
            <meta property="og:url" content="https://archive.vanityfair.com/article/2019/10/dating-the-monster" />



        <meta name="description" content="In rarefied New York circles, Jeffrey Epstein was the sociopath who proved the rule" />
<meta property="og:title" content="Dating the Monster | Vanity Fair" />
<meta property="og:description" content="In rarefied New York circles, Jeffrey Epstein was the sociopath who proved the rule" />
<meta property="article:author" content="Vanessa Grigoriadis" />
<meta property="og:image" content="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x600/40.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Dating the Monster | Vanity Fair | October 2019" />
<meta name="twitter:description" content="In rarefied New York circles, Jeffrey Epstein was the sociopath who proved the rule" />
<meta name="twitter:image" content="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x600/40.jpg" />
<meta name="twitter:image:alt" content="Dating the Monster | Vanity Fair | October 2019" />
<meta name="meterViewCount" content="1" />
                                        <link media="all" type="text/css" rel="stylesheet" href="https://archive.vanityfair.com/css/vanityfair/fonts.css?id=271fbb3cc3f12df11894">



                    <script type="text/javascript" async>
  let fidesHost = "https:\/\/privacy.condenastdigital.com\/fides.js";
  let fidesPropertyID = "FDS-0JCE2P";

  const fidesSrc = fidesHost + "?property_id=" + fidesPropertyID + "&";
  console.log(fidesSrc)

  var gtmOptions = {
    flag_type: "boolean",
    non_applicable_flag_mode: "include",
  };

  function insertFidesScript() {
    addEventListener("FidesInitializing", function() {
      window.Fides.gtm(gtmOptions);
    });
    addEventListener("FidesInitialized", function() {
      try {
        var experience = window.Fides.experience || {};
        var config = experience.experience_config || {};
        var id = config.id;
        if (id) {
          window.document.body.classList.add(id);
        }
      } catch (err) {
        console.warn("Couldn't apply Fides experience ID to body.", err);
      }
    });
    var fidesPrefix = "fides_";
    var searchParams = new URLSearchParams(location.search);
    var fidesSearchParams = new URLSearchParams();
    searchParams.forEach(function(key, value) {
      if (key.startsWith(fidesPrefix)) {
        fidesSearchParams.set(
          key.replace(fidesPrefix, ""),
          key === fidesPrefix + "cache_bust" ? Date.now().toString() : value
        );
      }
    });
    var src = fidesSrc + fidesSearchParams.toString();
    var script = document.createElement("script");
    script.async = false;
    script.defer = false;
    script.setAttribute("src", src);
    script.setAttribute("id", "fides-js");
    script.setAttribute("type", "text/javascript");
    document.head.appendChild(script);
  }

  insertFidesScript();
</script>;
<script type="text/javascript" async>
  (function(p, l, o, w, i, n, g) {
          if (!p[i]) {
              p.GlobalSnowplowNamespace = p.GlobalSnowplowNamespace || [];
              p.GlobalSnowplowNamespace.push(i);
              p[i] = function() {
                  (p[i].q = p[i].q || []).push(arguments)
              };
              p[i].q = p[i].q || [];
              n = l.createElement(o);
              g = l.getElementsByTagName(o)[0];
              n.async = 1;
              n.src = w;
              g.parentNode.insertBefore(n, g)
          }
      }(window, document, "script", "https://globalservices.conde.digital/p77xzrbz9z.js", "snowplowCN"));

      const appEnv = "production";
      const appID = "vanity-fair-archive";
      const collectorURL = "https:\/\/c.vanityfair.com";
      const siteAppVersion = "archive_laravel"
      console.log('App Environment: ' + appEnv, 'App ID: ' + appID, 'collectorURL: ' + collectorURL)
      //snowplow initial config
      window.snowplowCN(function() {
          const snowplowConfig = {
              appId: appID,
              contexts: {
                  performanceTiming: true,
                  clientHints: true,
                  webVitals: true
              },
              anonymousTracking: {
                  withSessionTracking: true,
                  withServerAnonymisation: true
              },
              stateStorageStrategy: 'cookieAndLocalStorage',
              discoverRootDomain: true,
              cookieSameSite: window.location.protocol === 'https:' ? 'None' : 'Lax',
              cookieSecure: window.location.protocol === 'https:',
              eventMethod: 'post',
              postPath: '/com.condenast/yv8'
          }

          const consentGroups = getConsentGroups()
          const anonymousConfig = consentGroups.includes('C0004') ?
              {
                  anonymousTracking: false,
                  stateStorageStrategy: 'cookieAndLocalStorage'
              } :
              {};

          // app Id and collector URL needs to be altered as per the domain
          snowplowCN('newTracker', 'sp', collectorURL, {
              ...snowplowConfig,
              ...anonymousConfig
          });

          //Entities that needs to be added to each event
          // Entities property definitions can be found below
          window.snowplowCN('addGlobalContexts', [userEntity, siteEntity, campaignEntity, contentEntity, pageEntity, referrerEntity, syndicationEntity]);

          snowplowCN('enableActivityTracking', {
              minimumVisitLength: 5,
              heartbeatDelay: 10
          });
          snowplowCN('enableLinkClickTracking');
          snowplowCN('trackPageView');

      })

      // ===== Snowplow Consent Handling ======
      var {
          dataLayer
      } = window;
      var cmpLoaded = false

      function onOneTrustGroupsUpdated(event) {
          const newGroups = getConsentGroups();
          if (userEntity && userEntity.data) {
              userEntity.data.onetrust_active_groups = newGroups;
              window.snowplowCN('removeGlobalContexts', [userEntity]);
              window.snowplowCN('addGlobalContexts', [userEntity]);
          }
          const otActiveGroups = Array.isArray(event?.detail) ? event?.detail : [];
          // The domain and network user Id gets generated when user accepts C0004 cookie
          const nonAnonymousConsentGroups = ['C0004'];
          const hasNonAnonymousConsent = !!otActiveGroups.some(function(item) {
              return nonAnonymousConsentGroups.includes(item)
          });
          if (hasNonAnonymousConsent) {
              window.snowplowCN('disableAnonymousTracking', {
                  stateStorageStrategy: 'cookieAndLocalStorage',
              });
          } else {
              window.snowplowCN('enableAnonymousTracking', {
                  options: {
                      withServerAnonymisation: true,
                      withSessionTracking: true
                  },
                  stateStorageStrategy: 'cookieAndLocalStorage',
              });
          }
          // tracking cmp_visible event
          trackCmpBanner()
          // tracking consent preferences event
          trackConsentPreferences(otActiveGroups)
      };

      window.addEventListener(
          'OneTrustGroupsUpdated',
          onOneTrustGroupsUpdated
      );

      function getCookie(name) {
          if (typeof document === 'undefined' || !name) {
              return '';
          }
          const cookiePieces = document.cookie.split(/;\s?/);
          let cookieValue = '';
          for (let i = 0; i < cookiePieces.length; i++) {
              const parts = cookiePieces[i].split('=');
              if (parts[0] === name) {
                  cookieValue = decodeURIComponent(parts.slice(1).join('='));
                  break;
              }
          }
          return cookieValue;
      };

      function getConsentGroups() {
          const otPayload = getCookie('OptanonConsent');
          if (window.OnetrustActiveGroups) {
              const OTGroup = window.OnetrustActiveGroups?.split(',')?.slice(1, -1);
              return OTGroup;
          } else if (otPayload) {
              const otGroupsMatch = otPayload.match(/groups=(.*)/g);
              const otGroups = otGroupsMatch?.[0] ?
                  otGroupsMatch[0].replace('groups=', '').split(',') :
                  null;
              const groupBuilder = [];
              otGroups?.forEach((group) => {
                  if (group.includes(':1')) {
                      groupBuilder.push(group.replace(':1', ''));
                  }
              });
              const OTGroup = groupBuilder.join(',').split('&')[0].split(',');
              return OTGroup;
          }

          return ['C0001'];
      };

      // ===== Snowplow Consent Handling End =====

      // we have global and adhoc entities. Global entities would be present in all the events. Adhoc entities
      // would be present only in specific custom events.
      // Entity Details - Default entities with basic properties. User and Site are some example entities.
      // Data Governance team can help in providing the details of the basic and custom events.
      var searchUrlParams = new URLSearchParams(window.location.search);
      var campaignEntity = {
          schema: 'iglu:com.condenast/campaign/jsonschema/4-0-1',
          data: {
              emailsource: searchUrlParams.get('esrc') || null,
              itm_campaign: searchUrlParams.get('itm_campaign') || null,
              itm_content: searchUrlParams.get('itm_content') || null,
              itm_medium: searchUrlParams.get('itm_medium') || null,
              itm_source: searchUrlParams.get('itm_source') || null,
              mkt_brand: searchUrlParams.get('utm_brand') || null,
              mkt_id: searchUrlParams.get('utm_id') || null,
              mkt_mailing: searchUrlParams.get('utm_mailing') || null,
              mkt_social_type: searchUrlParams.get('utm_social-type') || null,
              mkt_test: searchUrlParams.get('utm_test') || null,
          }
      };
      var contentEntity = {
          schema: 'iglu:com.condenast/content/jsonschema/2-0-1',
          data: {
              content_language: dataLayer?.[0]?.content?.contentLang || null,
              content_type: dataLayer?.[0]?.content?.contentType || null
          }
      };
      var urlArr = window.location?.pathname?.split('/');
      var pageEntity = {
          schema: 'iglu:com.condenast/page/jsonschema/6-0-1',
          data: {
              path_level_1: urlArr[1] || '',
              path_level_2: urlArr[2] || '',
              path_level_3: urlArr[3] || '',
              path_level_4: urlArr[4] || '',
              tab_active: window.document.visibilityState === 'visible',
              canonical_url: dataLayer?.[0]?.page?.canonical || null,
              ecommerce_targeter: searchUrlParams.get('source') || null,
              clean_url: window.location.origin + window.location.pathname,
          }
      };
      var referrerEntity = {
          schema: 'iglu:com.condenast/referrer/jsonschema/2-0-1',
          data: {
              refr_domain: document.referrer || ''
          }
      };
      var userEntity = {
          schema: 'iglu:com.condenast/user/jsonschema/9-0-2',
          data: {
              'browser': window?.navigator?.appName || null,
              'browser_version': window?.navigator?.appVersion || null,
              'is_logged_in': dataLayer?.[0]?.user?.amguuid ? true : false,
              'local_visit_hour': new Date().getHours(),
              'time_zone_offset': parseInt(new Date().getTimezoneOffset() / 60),
              'onetrust_active_groups': getConsentGroups(),
          }
      }
      var siteEntity = {
          schema: 'iglu:com.condenast/site/jsonschema/2-0-1',
          data: {
              org_app_id: dataLayer?.[0]?.site?.orgAppId || null,
              org_id: dataLayer?.[0]?.site?.orgId || null,
              site_app_version: siteAppVersion,
              site_data_source: dataLayer?.[0]?.site?.dataSource || null,
              site_env: appEnv,
              site_section: dataLayer?.[0]?.site?.section || null,
              site_subsection: dataLayer?.[0]?.site?.subsection || null,
              site_subsection_2: dataLayer?.[0]?.site?.subsection2 || null,
          }
      };
      var syndicationEntity = {
          schema: 'iglu:com.condenast/syndication/jsonschema/3-0-1',
          data: {
              is_syndication_content: dataLayer?.[0]?.syndication?.content || null
          }
      };
      // There might be adhoc entities also which would be expected to be added for specific events
      // Data Governance team will provide those details

      function trackCmpBanner() {
          if (
              !getCookie('OptanonAlertBoxClosed') &&
              window.OneTrust &&
              window.OneTrust.GetDomainData
          ) {
              const {
                  IsBannerLoaded,
                  ShowAlertNotice
              } =
              window.OneTrust.GetDomainData();
              if (ShowAlertNotice && !cmpLoaded) {
                  snowplowCN(`trackCmpVisible:sp`, {
                      /* Using the performance.now API to retrieve the elapsed time from the page navigation. */
                      elapsedTime: performance.now(),
                  });
                  cmpLoaded = true;
              }
          }
      }

      function trackConsentPreferences(otActiveGroups) {
          /*
          * Use OneTrust.GetDomainData().Groups which contains the available groups.
          */
          const optEvent = findLastOTAction(dataLayer)
          if (optEvent) {
              const optanonAction =
                  optEvent?.[2]?.optanonAction || optEvent?.optanonAction;
              const clickInfoEntity = [{
                  schema: 'iglu:com.condenast/click_info/jsonschema/2-0-0',
                  data: {
                      click_text: optanonAction
                  }
              }];
              const enhancedConsent = {
                  consentScopes: otActiveGroups,
                  basisForProcessing: 'consent',
                  consentUrl: window.location.href,
                  consentVersion: '1.0',
                  domainsApplied: [window.location.origin],
                  gdprApplies: true,
                  context: clickInfoEntity
              }
              switch (optanonAction) {
                  case 'Banner Accept Cookies':
                      snowplowCN(`trackConsentAllow:sp`, enhancedConsent)
                      break;
                  case 'Banner Reject All':
                      snowplowCN(`trackConsentDeny:sp`, enhancedConsent)
                      break;
                  case 'Preferences Allow All':
                      snowplowCN(`trackConsentAllow:sp`, enhancedConsent)
                      break;
                  case 'Preferences Reject All':
                      snowplowCN(`trackConsentDeny:sp`, enhancedConsent)
                      break;
                  case 'Banner - Continue without Accepting':
                      snowplowCN(`trackConsentDeny:sp`, enhancedConsent)
                      break;
                  case 'Preferences Save Settings':
                      snowplowCN(`trackConsentSelected:sp`, enhancedConsent)
                      break;
                  default:
                      break;
              }

          }

      }

      function findLastOTAction(dataLayer) {
          for (let i = dataLayer.length - 1; i >= 0; i--) {
              const event = dataLayer[i];
              if (event?.[2]?.optanonAction || event?.optanonAction) {
                  return event;
              }
          }
          return null; // Return null if no matching element is found
      }
</script>;
        <!-- Google Tag Manager Data Layer -->
    <script>
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({"event":"data-layer-loaded","user":{"amg_userId":null,"infinityId":null,"uID":null,"sID":null,"loginStatus":false,"accessPaywall":"REQUIRE_LOGIN","subscriberStatus":"not active","mdw_cnd_id":null},"content":{"pageTemplate":"article","pageType":"article","section":"Columns","subsection":"","contributor":"Vanessa Grigoriadis","contentID":0,"contentLength":2856,"display":"Dating the Monster","contentSource":"archive","pageAssets":null,"publishDate":null,"modifiedDate":null,"keywords":null,"dataSource":null},"marketing":[],"page":[],"search":[],"site":{"appVersion":"1.0.0"}});
    </script>
    <!-- End Google Tag Manager Data Layer -->


    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer', 'GTM-KSG89LT');</script>
    <!-- End Google Tag Manager -->

                            <link media="all" type="text/css" rel="stylesheet" href="https://archive.vanityfair.com/css/semantic.min.css?id=8fa68025438412570545">
            <script src="https://code.jquery.com/jquery-3.7.0.js"></script>
            <script src="https://archive.vanityfair.com/js/semantic.min.js?id=8402a17e01042067b993"></script>
            <script type="text/javascript">
                var ReactConfig = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.IntcImNsaWVudFwiOlwiVkZcIixcImJsb2JBY2NvdW50XCI6XCJ2YW5pdHlmYWlyXCIsXCJibG9iUHJlZml4XCI6XCJ2YW5pdHlmYWlyXCIsXCJwcm90b2NvbFwiOlwiaHR0cHNcIixcInRodW1iSGVpZ2h0XCI6XCIzNjBcIixcImNvbGxlY3Rpb25zUHJlZml4XCI6XCJib29rbWFya3NcIixcIm1lZGlhVGh1bWJGb3JtYXRcIjpcImh0dHBzOlxcXC9cXFwvdmFuaXR5ZmFpci5ibG9iLmNvcmUud2luZG93cy5uZXRcXFwvdmFuaXR5ZmFpciUlZHRodW1ibmFpbHNcXFwvTWVkaWFcXFwvMHgzNjBcXFwvJSVzXCIsXCJjb3ZlclRodW1iRm9ybWF0XCI6XCJodHRwczpcXFwvXFxcL3Zhbml0eWZhaXIuYmxvYi5jb3JlLndpbmRvd3MubmV0XFxcL3Zhbml0eWZhaXIlZHRodW1ibmFpbHNcXFwvQ292ZXJzXFxcLzB4MzYwXFxcLyVkLmpwZ1wiLFwiY3VycmVudF91cmxcIjpcImh0dHBzOlxcXC9cXFwvYXJjaGl2ZS52YW5pdHlmYWlyLmNvbVxcXC9hcnRpY2xlXFxcLzIwMTlcXFwvMTBcXFwvZGF0aW5nLXRoZS1tb25zdGVyXCIsXCJpc19hdXRoZW50aWNhdGVkXCI6ZmFsc2UsXCJ0b3BpY3NfZW5hYmxlZFwiOnRydWUsXCJwdWJsaWNhdGlvblwiOlwidmFuaXR5ZmFpclwiLFwicHVibGljYXRpb25fdGl0bGVcIjpcIlZhbml0eSBGYWlyXCIsXCJzaXRlVGl0bGVTdWZmaXhcIjpcInwgVGhlIENvbXBsZXRlIFZhbml0eSBGYWlyIEFyY2hpdmVcIixcImNkbkRvbWFpblwiOlwiaHR0cHM6XFxcL1xcXC92YW5pdHlmYWlyLmFyY2hpdmUuY29udGVudC5wdWdwaWcuY29tXCIsXCJhY2NvdW50XCI6e1widXBncmFkZV9lbmFibGVkXCI6dHJ1ZX0sXCJsaW5rXCI6e1wic3Vic2NyaWJlXCI6XCJodHRwczpcXFwvXFxcL3N1YnNjcmliZS52YW5pdHlmYWlyLmNvbVxcXC9zdWJzY3JpYmVcXFwvc3BsaXRzXFxcL3Zhbml0eWZhaXJcXFwvVllGX0FSQ0hJVkVTP3NvdXJjZT1WWUZfQVJDSElWRVNcIixcImxvZ2luXCI6XCJcXFwvbG9naW5cIixcImFjY291bnRcIjpcImh0dHBzOlxcXC9cXFwvd3d3LnZhbml0eWZhaXIuY29tXFxcL2FjY291bnRcXFwvcHJvZmlsZT9yZWRpcmVjdFVSTD1cIixcInZlcmlmeVwiOlwiaHR0cHM6XFxcL1xcXC93d3cudmFuaXR5ZmFpci5jb21cXFwvYWNjb3VudFxcXC9saW5rP3JlZGlyZWN0VVJMPVwiLFwibG9nb3V0XCI6XCJcXFwvbG9nb3V0XCIsXCJ1cGdyYWRlXCI6bnVsbH0sXCJmZWF0dXJlc1wiOntcImJvb2ttYXJrc1wiOmZhbHNlLFwiYXJ0aWNsZXNcIjp0cnVlLFwidG9waWNzXCI6dHJ1ZX0sXCJzdHJpcGVcIjp7XCJwdWJsaXNoYWJsZUtleVwiOm51bGx9LFwiYXV0aFwiOntcImVuYWJsZWRcIjp0cnVlLFwiY2hlYXRDb2RlXCI6bnVsbH0sXCJyZWNhcHRjaGFcIjp7XCJzaXRlS2V5XCI6bnVsbH0sXCJsYXRlc3RJc3N1ZVwiOntcIkNvdmVyWWVhclwiOjIwMjUsXCJDb3ZlckRhdGVcIjpcIjIwMjUtMDktMDFUMDA6MDA6MDBcIixcIkNvdmVyRGlzcGxheURhdGVcIjpcIlNFUFRFTUJFUlwiLFwiSXNzdWVLZXlcIjoyMDI1MDkwMSxcIkNvdmVyV2lkdGhcIjowLFwiQ292ZXJIZWlnaHRcIjowLFwiVm9sdW1lXCI6XCI2N18wOFwiLFwiSXNzdWVOdW1iZXJcIjpcIjc3MVwiLFwiSXNzdWVOYW1lXCI6XCJcIixcIkZyZWVcIjpmYWxzZSxcIkhhc0FjY2Vzc1wiOmZhbHNlLFwiTGF0ZXN0SXNzdWVcIjp0cnVlfX0i.wQc_3bXUeuHp7RrmaLwmbMER4nkG-BHj1TJap_V07-c';
                var tocConfig = null;
                var searchConfig = null;
            </script>

    <script type="text/javascript">

        $(function() {
            var loginForm = $(".loginForm");
                loginForm.submit(function(e) {
                    e.preventDefault();
                    var formData = loginForm.serialize();

                    loginForm.addClass('loading');

                    $.ajax({
                        url: '/login',
                        type: 'POST',
                        data: formData,
                        success: function(data) {
                            if (data.auth)
                                window.location.reload(true);
                            else {
                                $('.loginForm .error_list').html(sprintf('<li>%s</li>', data.message));
                                loginForm.removeClass('loading');
                            }
                        },
                        error: function (data) {
                            loginForm.removeClass('loading');
                        }
                    });
                });

            $('.user_login').modaal({
                content_source: '#bnd_subscribe_modaal',
                accessible_title: 'Subscribe or Login',
                type: 'inline',
                before_open: function() {
                    $('.bnd_mobilemenu_toggle').modaal('close');
                },
            });
        });

    </script>


    <link media="all" type="text/css" rel="stylesheet" href="https://archive.vanityfair.com/libs/flickity/flickity.css?v=2.4.9">

        <link media="all" type="text/css" rel="stylesheet" href="https://archive.vanityfair.com/css/article_base_compiled.css?id=2e383a24622f079b8dd2">

        <link media="all" type="text/css" rel="stylesheet" href="https://archive.vanityfair.com/css/vanityfair/core_bundle_vb.css?id=171844e1c547c983e481">

        <script src="https://archive.vanityfair.com/js/bondi.global.js?v=1.5.9"></script>
    <script src="https://archive.vanityfair.com/js/bondi.utils.js?id=22be739dc44740572a6f"></script>
    <script src="https://archive.vanityfair.com/libs/flickity/flickity.pkgd.min.js?v=1.5.9"></script>

        <script type="text/javascript">
        $(window).on("scroll", function() {
            var scrollwin = $(window).scrollTop();
            var articleheight = $('.bndwgt__bondi_article').outerHeight(true);
            var windowWidth = $(window).width();
            if(scrollwin >= $('.bndwgt__bondi_article').offset().top){
                if(scrollwin <= ($('.bndwgt__bondi_article').offset().top + articleheight)){
                    $('.read_progress').css('width', ((scrollwin - $('.bndwgt__bondi_article').offset().top) / articleheight) * 100 + "%"  );
                }else{
                    $('.read_progress').css('width',"100%");
                }
            }else{
                $('.read_progress').css('width',"0px");
            }
        });
    </script>

    <script type="text/javascript">
    	(function ($) {
            Bondi.appEnv = "production";
            Bondi.client = 'VF';
            Bondi.viewType = 'article';
            Bondi.issueKey = 20191001;
            Bondi.articleKey = 20191001056;
            Bondi.coverDisplay = 'October 2019';
            Bondi.imageFormat = 'https://archive.vanityfair.com/image/%s/20191001/%s/%s';
            Bondi.pageThumbFormat = 'https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Pages/0x90/%s.jpg';
            Bondi.spreadThumbFormat = 'https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x360/%s.jpg';
            Bondi.mediaThumbFormat = 'https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Media/0x360/%s.jpg';
            Bondi.thumbFormat = 'https://vanityfair.blob.core.windows.net/vanityfair%1$dthumbnails/%3$s/0x%2$d/%4$s';
            Bondi.publicationTitle = "Vanity Fair";
    		Bondi.spreads[20191001056] = [{"Spread":40,"StartPageKey":20191001078,"EndPageKey":20191001079,"PageRange":"74,75","PageCount":2,"Width":6400,"Height":4350,"ImageFormat":null,"SecureImageFormat":"\/image\/spread\/20191001\/40\/%s","TogglePage":"74","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"MaxHeight":4350,"TotalWidth":6400,"Pages":[{"PageKey":20191001078,"IssueKey":20191001,"Sequence":78,"Spread":40,"PageName":"74","Width":3200,"Height":4350,"SpreadSequence":1,"ImageFormat":null,"SecureImageFormat":null,"TogglePage":null,"HasText":false,"HasTextArticleKey":null,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":null,"TextArticles":null,"JumpLinks":null,"Articles":null},{"PageKey":20191001079,"IssueKey":20191001,"Sequence":79,"Spread":40,"PageName":"75","Width":3200,"Height":4350,"SpreadSequence":2,"ImageFormat":null,"SecureImageFormat":null,"TogglePage":null,"HasText":false,"HasTextArticleKey":null,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":null,"TextArticles":null,"JumpLinks":null,"Articles":null}],"PageSizes":[{"PageKey":40,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":2000,"DefaultHeight":1359,"MaxWidth":4400,"MaxHeight":2991,"SizeSequence":1,"Pages":null},{"PageKey":40,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":1600,"DefaultHeight":1088,"MaxWidth":4000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":40,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":1360,"DefaultHeight":924,"MaxWidth":3200,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":40,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":960,"DefaultHeight":653,"MaxWidth":2400,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":40,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1360,"DefaultHeight":924,"MaxWidth":4000,"MaxHeight":2719,"SizeSequence":5,"Pages":null},{"PageKey":40,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":1200,"DefaultHeight":816,"MaxWidth":3200,"MaxHeight":2175,"SizeSequence":6,"Pages":null},{"PageKey":40,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":960,"DefaultHeight":653,"MaxWidth":2400,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]},{"Spread":41,"StartPageKey":20191001080,"EndPageKey":20191001081,"PageRange":"76,77","PageCount":2,"Width":6400,"Height":4350,"ImageFormat":null,"SecureImageFormat":"\/image\/spread\/20191001\/41\/%s","TogglePage":"76","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"MaxHeight":4350,"TotalWidth":6400,"Pages":[{"PageKey":20191001080,"IssueKey":20191001,"Sequence":80,"Spread":41,"PageName":"76","Width":3200,"Height":4350,"SpreadSequence":1,"ImageFormat":null,"SecureImageFormat":null,"TogglePage":null,"HasText":false,"HasTextArticleKey":null,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":null,"TextArticles":null,"JumpLinks":null,"Articles":null},{"PageKey":20191001081,"IssueKey":20191001,"Sequence":81,"Spread":41,"PageName":"77","Width":3200,"Height":4350,"SpreadSequence":2,"ImageFormat":null,"SecureImageFormat":null,"TogglePage":null,"HasText":false,"HasTextArticleKey":null,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":null,"TextArticles":null,"JumpLinks":null,"Articles":null}],"PageSizes":[{"PageKey":41,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":2000,"DefaultHeight":1359,"MaxWidth":4400,"MaxHeight":2991,"SizeSequence":1,"Pages":null},{"PageKey":41,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":1600,"DefaultHeight":1088,"MaxWidth":4000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":41,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":1360,"DefaultHeight":924,"MaxWidth":3200,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":41,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":960,"DefaultHeight":653,"MaxWidth":2400,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":41,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1360,"DefaultHeight":924,"MaxWidth":4000,"MaxHeight":2719,"SizeSequence":5,"Pages":null},{"PageKey":41,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":1200,"DefaultHeight":816,"MaxWidth":3200,"MaxHeight":2175,"SizeSequence":6,"Pages":null},{"PageKey":41,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":960,"DefaultHeight":653,"MaxWidth":2400,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]}];
            Bondi.pages[20191001056] = [{"PageKey":20191001078,"IssueKey":20191001,"Sequence":78,"Spread":1,"PageName":"74","Width":3200,"Height":4350,"SpreadSequence":0,"ImageFormat":null,"SecureImageFormat":"\/image\/single\/20191001\/74\/%s","TogglePage":"74","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":[{"PageKey":20191001078,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":1000,"DefaultHeight":1359,"MaxWidth":2600,"MaxHeight":3534,"SizeSequence":1,"Pages":null},{"PageKey":20191001078,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":2000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":20191001078,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1600,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":20191001078,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":20191001078,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1400,"DefaultHeight":1903,"MaxWidth":2400,"MaxHeight":3263,"SizeSequence":5,"Pages":null},{"PageKey":20191001078,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1800,"MaxHeight":2447,"SizeSequence":6,"Pages":null},{"PageKey":20191001078,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]},{"PageKey":20191001079,"IssueKey":20191001,"Sequence":79,"Spread":1,"PageName":"75","Width":3200,"Height":4350,"SpreadSequence":0,"ImageFormat":null,"SecureImageFormat":"\/image\/single\/20191001\/75\/%s","TogglePage":"74","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":[{"PageKey":20191001079,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":1000,"DefaultHeight":1359,"MaxWidth":2600,"MaxHeight":3534,"SizeSequence":1,"Pages":null},{"PageKey":20191001079,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":2000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":20191001079,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1600,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":20191001079,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":20191001079,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1400,"DefaultHeight":1903,"MaxWidth":2400,"MaxHeight":3263,"SizeSequence":5,"Pages":null},{"PageKey":20191001079,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1800,"MaxHeight":2447,"SizeSequence":6,"Pages":null},{"PageKey":20191001079,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]},{"PageKey":20191001080,"IssueKey":20191001,"Sequence":80,"Spread":2,"PageName":"76","Width":3200,"Height":4350,"SpreadSequence":0,"ImageFormat":null,"SecureImageFormat":"\/image\/single\/20191001\/76\/%s","TogglePage":"76","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":[{"PageKey":20191001080,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":1000,"DefaultHeight":1359,"MaxWidth":2600,"MaxHeight":3534,"SizeSequence":1,"Pages":null},{"PageKey":20191001080,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":2000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":20191001080,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1600,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":20191001080,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":20191001080,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1400,"DefaultHeight":1903,"MaxWidth":2400,"MaxHeight":3263,"SizeSequence":5,"Pages":null},{"PageKey":20191001080,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1800,"MaxHeight":2447,"SizeSequence":6,"Pages":null},{"PageKey":20191001080,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]},{"PageKey":20191001081,"IssueKey":20191001,"Sequence":81,"Spread":2,"PageName":"77","Width":3200,"Height":4350,"SpreadSequence":0,"ImageFormat":null,"SecureImageFormat":"\/image\/single\/20191001\/77\/%s","TogglePage":"76","HasText":true,"HasTextArticleKey":20191001056,"HasTextArticleKeys":null,"CoverType":null,"PageSizes":[{"PageKey":20191001081,"Device":"desktop","MaxDeviceWidth":10000,"DefaultWidth":1000,"DefaultHeight":1359,"MaxWidth":2600,"MaxHeight":3534,"SizeSequence":1,"Pages":null},{"PageKey":20191001081,"Device":"desktop","MaxDeviceWidth":1900,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":2000,"MaxHeight":2719,"SizeSequence":2,"Pages":null},{"PageKey":20191001081,"Device":"desktop","MaxDeviceWidth":1400,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1600,"MaxHeight":2175,"SizeSequence":3,"Pages":null},{"PageKey":20191001081,"Device":"desktop","MaxDeviceWidth":1023,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":4,"Pages":null},{"PageKey":20191001081,"Device":"mobile","MaxDeviceWidth":1080,"DefaultWidth":1400,"DefaultHeight":1903,"MaxWidth":2400,"MaxHeight":3263,"SizeSequence":5,"Pages":null},{"PageKey":20191001081,"Device":"mobile","MaxDeviceWidth":768,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1800,"MaxHeight":2447,"SizeSequence":6,"Pages":null},{"PageKey":20191001081,"Device":"mobile","MaxDeviceWidth":640,"DefaultWidth":800,"DefaultHeight":1088,"MaxWidth":1200,"MaxHeight":1631,"SizeSequence":7,"Pages":null}],"TextArticles":null,"JumpLinks":[],"Articles":[{"Key":20191001056,"Title":"Dating the Monster","Section":"Columns","StartIndex":1,"Genre":"article","PageName":"74","Spread":40}]}];

                    Bondi.Viewer.enabled = true;

        Bondi.Viewer.bypass = true;

    	})(jQuery);
    </script>

            <script type="application/ld+json">
            {"@context":"http:\/\/schema.org","@type":"NewsArticle","name":"Dating the Monster","headline":"Dating the Monster","url":"https:\/\/archive.vanityfair.com\/article\/2019\/10\/dating-the-monster","thumbnailUrl":"https:\/\/vanityfair.blob.core.windows.net\/vanityfair20191001thumbnails\/Pages\/0x90\/74.jpg","section":"vf-archive","creator":[["Vanessa Grigoriadis"]],"keywords":["article","Columns"],"author":{"@type":"Person","name":"Vanessa Grigoriadis"},"dateCreated":"2019-10-01T00:00:00","datePublished":"2019-10-01T00:00:00","dateModified":"2019-10-01T00:00:00","image":{"@type":"ImageObject","url":"https:\/\/vanityfair.blob.core.windows.net\/vanityfair20191001thumbnails\/Spreads\/0x600\/40.jpg"},"publisher":{"@type":"Organization","name":"Vanity Fair","logo":{"@type":"ImageObject","url":"https:\/\/www.vanityfair.com\/images\/vanityfair-logo-small.png","width":198,"height":40}},"mainEntityOfPage":{"@type":"WebPage","@id":"https:\/\/archive.vanityfair.com\/article\/2019\/10\/dating-the-monster"},"isAccessibleForFree":"False","hasPart":{"@type":"WebPageElement","isAccessibleForFree":"False","cssSelector":".paywall"}}        </script>

        <script type="text/javascript">
(function (f, b) { if (!b.__SV) { var e, g, i, h; window.mixpanel = b; b._i = []; b.init = function (e, f, c) { function g(a, d) { var b = d.split("."); 2 == b.length && ((a = a[b[0]]), (d = b[1])); a[d] = function () { a.push([d].concat(Array.prototype.slice.call(arguments, 0))); }; } var a = b; "undefined" !== typeof c ? (a = b[c] = []) : (c = "mixpanel"); a.people = a.people || []; a.toString = function (a) { var d = "mixpanel"; "mixpanel" !== c && (d += "." + c); a || (d += " (stub)"); return d; }; a.people.toString = function () { return a.toString(1) + ".people (stub)"; }; i = "disable time_event track track_pageview track_links track_forms track_with_groups add_group set_group remove_group register register_once alias unregister identify name_tag set_config reset opt_in_tracking opt_out_tracking has_opted_in_tracking has_opted_out_tracking clear_opt_in_out_tracking start_batch_senders people.set people.set_once people.unset people.increment people.append people.union people.track_charge people.clear_charges people.delete_user people.remove".split( " "); for (h = 0; h < i.length; h++) g(a, i[h]); var j = "set set_once union unset remove delete".split(" "); a.get_group = function () { function b(c) { d[c] = function () { call2_args = arguments; call2 = [c].concat(Array.prototype.slice.call(call2_args, 0)); a.push([e, call2]); }; } for ( var d = {}, e = ["get_group"].concat( Array.prototype.slice.call(arguments, 0)), c = 0; c < j.length; c++) b(j[c]); return d; }; b._i.push([e, f, c]); }; b.__SV = 1.2; e = f.createElement("script"); e.type = "text/javascript"; e.async = !0; e.src = "undefined" !== typeof MIXPANEL_CUSTOM_LIB_URL ? MIXPANEL_CUSTOM_LIB_URL : "file:" === f.location.protocol && "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//) ? "https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js" : "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js"; g = f.getElementsByTagName("script")[0]; g.parentNode.insertBefore(e, g); } })(document, window.mixpanel || []);

  mixpanel.init('70aae71ca1c69ceab8d01f3e60411a76', {track_pageview: true, persistence: 'localStorage'});
  mixpanel.register({'Pugpig Archive Code': 'VF'});
  mixpanel.register({'Pugpig Archive Name': 'Vanity Fair'});
</script>

        <!--[if IE 10]>
        <script src="https://archive.vanityfair.com/js/html5-dataset.js"></script>
        <![endif]-->
    </head>
    <body class="page_issue page_article logged_out articlekey_20191001056 issuekey_20191001 year_2019 decade_2010 page_shared is_featured 1" ng-controller="issueController" ng-init="init(20191001)">
                <!-- Google Tag Manager (noscript) -->
    <noscript>
        <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KSG89LT" height="0" width="0" style="display:none;visibility:hidden"></iframe>
    </noscript>
    <!-- End Google Tag Manager (noscript) -->

                    <header role="banner">
    <a class="skip-main" href="#main_content" tabindex="0">Skip to main content</a>
    <div id="top"></div>
    <div id="main-header">
        <div class="user_menu_wrapper">
            <div role="navigation" aria-label="Primary" class="ui container">
                <a id="mblmenu_toggle" href="javascript:void(0);" class="bnd_mobilemenu_toggle" tabindex="0" aria-haspopup="true" aria-label="Open Mobile Menu Navigation"><i class="sidebar icon"></i></a>
                <ul class="user_menu main_nav">
                    <li class="menunav"><a class="nav_issues bndwgt_decades_trigger" href="javascript:void(0);" title="Browse Issues by Decade" tabindex="0" aria-haspopup="true" aria-label="Browse Issues">Issues</a></li>

                                        <li class="menunav"><a class="nav_topics bndwgt_topics_trigger" href="javascript:void(0);" title="Browse Collections" tabindex="0" aria-haspopup="true" aria-label="Browse Collections">Collections</a></li>
                    <li class="menunav"><a class="nav_authors bndwgt_authors_trigger" href="javascript:void(0);" title="Browse Featured Contributors" tabindex="0" aria-haspopup="true" aria-label="Browse Featured Contributors">Contributors</a></li>


                </ul>

                                                            <div class="promohead"><span class="hider early">The Complete Vanity Fair Archive </span><span class="highlight">FREE Article!</span></div>

                <a class="main_nav_logo" href="/" title="Vanity Fair Archive" tabindex="0" aria-label="Vanity Fair Archive Homepage">Vanity Fair Archive</a>

                <ul class="user_menu on_right">
                    <li class="menunav"><a href="https://www.vanityfair.com/">VF.com</a></li>



            <li class="user_menu_1 login"><a role="menuitem" class="" href="/login" tabindex="0" aria-label="Sign In">Sign In</a></li>
            <li class="user_menu_2"><a role="menuitem" href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_NAVBAR_0" class="link-subscribe" target="_blank" tabindex="0" aria-label="Subscribe"><span data-alt="Subscribe Now"><span>Subscribe</span></span></a></li>

                    <li class="menunav"><a class="nav_search ui icon bnd_search_overlay_trigger" href="javascript:void(0);" title="Search the Vanity Fair Archive" tabindex="0" aria-haspopup="true" aria-label="Search"><i class="search icon"></i></a></li>
                </ul>

            </div>
        </div>
    </div>


        <div id="bnd_mainmenu_modal"></div>
    <div id="bnd_search_modal"></div>

</header>
        <main role="main" id="main_content">
                                        <div id="viewerApp" style="display: none;" hidden></div>




                 <div class="bnd_article_header">


                    <div class="bnd_artpg_hero_wrap articlekey_20191001056" style="background: linear-gradient(rgba(10, 20, 30, 0.5),rgba(10, 20, 30, 0.85)), no-repeat top 30% center/cover url('https://archive.vanityfair.com/image/spread/20191001/40');">
            <div class="bndwgt__title_box">
    <div class="bndwgt__info">
        <a href="https://archive.vanityfair.com/sections/columns" class="bndwgt__section" title="Columns" aria-label="Columns">Columns</a>

        <h1 class="bndwgt__headline">Dating the Monster</h1>

                <h3 class="bndwgt__subhead"><p>In rarefied New York circles, Jeffrey Epstein was the sociopath who proved the rule</p></h3>

        <span class="bndwgt__meta">
            <span class="full_date">
                            October 2019
                    </span>

                    <span class="bndwgt__author role_author ">
            Vanessa Grigoriadis
            </span>
                    <span class="bndwgt__author role_illustrator role_2ndary">
            Philip Burke
            </span>

                      </span>

        <ul class="socials" style="margin-top: 20px;">


    <li><a aria-label="Share via facebook" class="ui circular facebook icon button " href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster&title=Dating+the+Monster" target="_blank"><i class="facebook icon"></i></a></li>
    <li><a aria-label="Share via twitter" class="ui circular twitter icon button " href="https://twitter.com/intent/tweet?text=Dating+the+Monster&url=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster" target="_blank"><i class="twitter icon"></i></a></li>
    <li><a aria-label="Share via mail" class="ui circular mail icon button " href="mailto:?subject=Dating%20the%20Monster&body=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster" target="_self"><i class="mail icon"></i></a></li>




</ul>

    </div>
</div>
        </div>
    </div>





        <div id="issue_toc" class="ui borderless main menu bnd_artpg_fixedhead">
        <div class="ui container">

            <a id="mblmenu_toggle" href="javascript:void(0);" class="bnd_mobilemenu_toggle" tabindex="0" aria-haspopup="true" aria-label="Open Mobile Menu Navigation"><i class="sidebar big icon"></i></a>

            <div class="bnd_artpg_keyspread  bondi__viewer bndwgt bndwgt__with-numbers widget-spread bndwgt__pagefx a20191001056">
                <div class="bndwgt__slide" data-issuekey="20191001" data-viewerkey="20191001056">
                    <a href="javascript:void(0)" class="bndwgt__slide-link bndwgt__issuecover_main_wrapper bndvwr__trigger" data-pid="74">
                                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x600/40.jpg" alt="Dating the Monster">
                                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span>
                        <span class="bndwgt__pgfx-shine bndwgt__hilite"><button class="bndwgt__icon ui icon button" aria-label="View this article" aria-haspopup="true"><i class="icon zoom"></i></button></span>
                    </a>
                </div>
            </div>

            <h3 class="bndwgt__headline">
                Dating the Monster
                <span class="bndwgt__meta">
                                            <span class="bndwgt__author">Vanessa Grigoriadis</span>
                                                                October 2019
                                    </span>
            </h3>

            <ul class="socials tocbar">


                <li><a aria-label="Share via facebook" class="ui circular facebook icon button " href="https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster&title=Dating+the+Monster" target="_blank"><i class="facebook icon"></i></a></li>
                <li><a aria-label="Share via twitter" class="ui circular twitter icon button " href="https://twitter.com/intent/tweet?text=Dating+the+Monster&url=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster" target="_blank"><i class="twitter icon"></i></a></li>
                <li><a aria-label="Share via mail" class="ui circular mail icon button " href="mailto:?subject=Dating%20the%20Monster&body=https%3A%2F%2Farchive.vanityfair.com%2Farticle%2F2019%2F10%2Fdating-the-monster" target="_self"><i class="mail icon"></i></a></li>


                                                        <li>
                        <a role="menuitem" href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_STICKY_TOPBAR _0" class="link-subscribe" target="_blank" tabindex="0" aria-label="Subscribe">
                            <span data-alt="Subscribe Now"><span>Subscribe</span></span>
                        </a>
                    </li>

            </ul>

        </div>
        <div class="read_progress_wrap">
            <div class="read_progress"></div>
        </div>
    </div>






    <div class="bndwgt__bondi_article_wrap ui container stackable grid">

                        <div class="bndwgt__bondi_article eleven wide column">

            <div class="container bndwgt__bondi_article_embed">

                <div class="bnd_artpg_keyspread ui container bondi__viewer bndwgt bndwgt__with-numbers widget-spread bndwgt__pagefx a20191001056">
                    <div class="bndwgt__slide" data-issuekey="20191001" data-viewerkey="20191001056">
                        <a href="javascript:void(0)" class="bndwgt__slide-link bndwgt__issuecover_main_wrapper bndvwr__trigger " data-pid="74" aria-label="View original article pages">
                                                    <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x600/40.jpg" alt="Dating the Monster">
                                                    <span class="bndwgt__pgfx-top"></span>
                            <span class="bndwgt__pgfx-left"></span>
                            <span class="bndwgt__pgfx-right"></span>
                            <span class="bndwgt__pgfx-btm"></span>
                            <span class="bndwgt__pgfx-shine bndwgt__hilite">
                                <button class="bndwgt__icon ui icon button" tabindex="-1" role="presentation" aria-hidden="true"><i class="icon zoom"></i></button>
                            </span>
                            <span class="bndwgt__slide_alt_trigger bndwgt__thumbnail-carousel" data-articlekey="20191001056">
                                <span><i class="icon zoom"></i> View Article Pages</span>
                            </span>
                        </a>
                    </div>
                </div>

                <div>
                                    <div class="bndwgt__title_box">
    <div class="bndwgt__info">
        <a href="https://archive.vanityfair.com/sections/columns" class="bndwgt__section" title="Columns" aria-label="Columns">Columns</a>
        <div class="bndwgt__headline">Dating the Monster</div>

                <h3 class="bndwgt__subhead"><p>In rarefied New York circles, Jeffrey Epstein was the sociopath who proved the rule</p></h3>

        <span class="bndwgt__meta">
            <span class="full_date">
                            October 2019
                    </span>

                    <span class="bndwgt__author role_author ">
            Vanessa Grigoriadis
            </span>
                    <span class="bndwgt__author role_illustrator role_2ndary">
            Philip Burke
            </span>

                      </span>

    </div>
</div>





<div class="bndwgt__article_body bndwgt__inline_text">

    <p><span class="drop">M</span>any moons ago, in the early 2000s, my friends spent a weekend in Southampton with a distinctive young blond who resembled Lady Gaga if Gaga were British. She was about 22 and said she was an interior designer, or a jewelry designer, or a motivational coach&mdash;I can't remember which, but in any case the job sounded semi-fake&mdash;and she lived in an apartment on the Upper East Side that her older boyfriend had given her, at least temporarily. He collected art, and they often attended auctions. He loved vegetarian food and playing unfamiliar concertos on his grand piano. As she strolled down Southampton's tree-lined streets, she was struck by their beauty and said she'd have to discuss getting a home there with her boyfriend. His name was Jeffrey Epstein.<br></p>
<p>Back then, as a cocky, petite, ink-stained wretch, I wasn't one of the young women in Manhattan whom Epstein and his friends approached for relationships, one-night stands, or abuse. But I was surrounded by a lot of them. They were always the most beautiful girls in the room, usually models or former models, with a slightly aloof <em>Stepford Wives</em> aura that masked a deeper vulnerability. Several names came up when they were around: Epstein, supermarket magnate Ron Burkle, film financier Steve Bing, and former president Bill Clinton, then in the prime of his post-presidential career and flying around on Epstein's jet, dubbed the Lolita Express, or Burkle's jet, dubbed Air Fuck One. (Clinton has not been accused of wrongdoing.) The women were often blond&mdash;Epstein, in particular, liked patrician blonds with a bit of a baby face. At his home on the Upper East Side, he kept a photo of '80s soap star Morgan Fairchild, whom he called his ideal woman, though considering they were both in their early 50s back then, she was far too old for him.</p>
<figure class="floatedimage"><img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Media/0x600/2019100156_1.jpg" data-verified="redactor" data-save-url="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Media/0x600/2019100156_1.jpg"><em class="caption" data-redactor-tag="em"></em></figure>
<p>Beyond allegedly running a pedophile ring, Epstein, who hanged himself in August, epitomized the transactional nature of fin de siecle New York society, the sociopath who proved the rule. As hedge funds began to create massive fortunes and the billionaire class outpaced entail and primogeniture, women like the one in Southampton were necessary accessories, and learning how to acquire them was part of many a high-level trader's skill set. There's a temptation to say that the world has always worked this way&mdash;ambitious, beautiful young women have often sought to climb rungs via powerful men, and powerful men have partly craved power in order to access beautiful women&mdash;but this era in New York was unique. A rapidly increasing workforce of women in black slip dresses, knee-high black boots, and flat-ironed hair had come to seek the <em>Sex and the City</em> lifestyle, not husbands&mdash;but with most of their professions (fashion, publicity, publishing) paying far less than men's, they were not averse to someone footing the bill.</p>
<blockquote>"He could <em>feel</em> energy very clearly.... Because he's a <em>sociopath, </em>he would <em>manipulate</em> that for his <em>own</em> needs."</blockquote>
<p>Beautiful women also had currency in the city's "models and bottles" scene, as the post-9/11 era of downtown nightlife was called. Manhattan's legendary club scene of hip-hop stars, painters, and graffiti artists, where one gained entree by virtue of one's art rather than the size of one's wallet, was going capitalist. A new nightclub formula had been devised: Ice buckets of Cristal and Ciroc bottles were set up at leather banquettes, alongside every kind of model&mdash;Victoria's Secret model, runway model, supermodel, "just-off-the-boat model"&mdash;and if you were a rich older guy who wanted to take a seat, it could cost up to $10,000, though Puffy and Leo didn't pay a thing.</p>
<p>Like his billionaire friends, Epstein ran a highly compartmentalized life. "He'd say he was going somewhere for work, and then I'd see pictures in a British tabloid of him on a yacht with supermodels," says a woman who dated one of his close friends. The women of consenting age with whom Epstein became involved weren't gold diggers, per se&mdash;they were models, or Amy Winehouse's "Gucci bag crew" flying to Miami for free, or postcollegiate women who didn't care about a 30-year age difference. Some wanted to open a door to the world of private planes and the global elite. In later years, he favored a different kind of Eastern European woman who was more expressly for sale. "There are almost as many people involved over 18 as under 18&mdash;it's not 50-50, but it's in that ballpark," says David Boies, the attorney for some of Epstein's accusers. He describes two different types of of-age women involved with Epstein. "There were women who were not underage, but usually in their younger 20s, who became part of what we're calling Epstein's sex-trafficking orbit&mdash;they'd either be trafficked or lent out, describe it as you will, to other people," he says. "Then there were young professional women of comparable age whom Epstein sort of dated, and then he might or might not recommend them to other people." Young women like the one I came across in Southampton were presumably part of that second set. (She did not return messages for further comment.) Epstein's recommendations for these young women were romantic, or professional, or some uneasy mix of both; Charlie Rose, disgraced after sexual assault allegations, received suggestions for several assistants on his TV show from Epstein.</p>
<p>The women who dated Epstein, many of whom now have high-profile careers, didn't want to be identified in this article, some because they feel the press would mangle their relationships and describe them as prostitutes, not a reputation a professional woman can surmount. Some were getting something from Epstein&mdash;a trip on a private plane with Bill Clinton is not without value. But more often they were, to some degree, the commodities&mdash;tradable objects. That was part of the grift. Epstein traded men for acceptance, always trying to show other men how many important people he knew: politicians, billionaires, former Harvard president Larry Summers, top scientists. Women were another instrumentality. Everyone had their price.</p>
<p><strong><span class="drop">E</span>pstein's ex-girlfriends say</strong> he was quiet and charming, for the most part, Jay Gatsby in a monogrammed sweatshirt. He spent most of the day on speakerphone, and he liked them to listen in, rolling calls from financiers to heads of state. He did not drink or take drugs or smoke, and he didn't like to be around people who did. He practiced Iyengar yoga. He showered many times a day. He abhorred restaurants and ate whole grains, proteins, and leafy greens 30 years before the rest of America. He tied body to mind, physical self to mental aptitude; he believed in transhumanism and had a theory that if you had too much muscle mass, you wouldn't be as smart as you could be. He liked to sleep in 54-degree chill because he believed you'd get the most restful sleep at that temperature. "I was like, 'I'm fucking freezing. I'm going to die of hypothermia,"' says an ex-girlfriend.</p>
<p>He also had an instinct for what people wanted. "Jeffrey was brilliant in understanding how people felt," says the same ex-girlfriend. "He could feel energy very clearly. But I think because he's a sociopath, he would manipulate that for his own needs. The average human population just doesn't operate that way, and thank God."</p>
<p>The man who contributed to Epstein's riches, Les Wexner, the owner of Victoria's Secret and the richest man in Ohio, for whom Epstein managed money and had some sort of deep emotional relationship, seemed as ill at ease as Epstein was forthright. Women who dined with Wexner found him awkward and without the gift of gab, which Epstein had in spades. A <em>Sports Illustrated</em> model says that in the 1990s, Epstein sent her, as a lark, to deliver Wexner's prenup at his office; the rumor was she went to Wexner's office, lay down on the table, and had him sign the prenup on her belly, but she says this isn't true. "Jeffrey told me to wear something sexy and that it would be a great practical joke, but when I got there, it was very uncomfortable, and Les was like, 'What are you doing here? Okay, I'll sign, and then you should go.' "</p>
<blockquote>A woman who <em>dated</em> Epstein says he <em>slept</em> with a <em>gun</em> in a holster on the side of the bed and was <em>always playing</em> "spy games."</blockquote>
<p>The longer these women dated Epstein, the stranger he became. A former girlfriend describes him as almost agoraphobic, with a fear of groups and a dislike of shaking people's hands; he preferred one-on-one relationships, which were more conducive to sharing secrets. Other than the trips he took on his private plane, Epstein preferred to socialize at home, where he could control the food, the conversation, the temperature. In Manhattan he lived in a $56 million town house that once housed the Birch Wathen prep school, with his initials emblazoned next to the door, and he hired a white-gloved butler to serve high tea. But underneath this pose lurked someone quite different. "He was so insecure&mdash;he had that outer-borough thing of always needing a model on his arm," says the <em>Sports Illustrated</em> model. "He was emotionally infantile, stunted, without an inner world." She describes Epstein watching her brush her hair and asking, "Do you use a Mason Pearson brush?"&mdash;the expensive brush favored by stylists in the fashion industry. She said yes, and he responded, excitedly, that he did too. "He said, 'Oh, yes, they're the best.' He was like a little boy who got his cool toy. And then he'd collect people just like that hairbrush. It was so odd."</p>
<p>Epstein was always talking about how well connected he was: "He was a total starfucker," says a woman in his orbit. In his secret life he was grotesque, but in society he was thought of as a practical joker who enjoyed messing with those he regarded as lower on the food chain. The <em>Sports Illustrated</em> model describes meeting Donald Trump at one of Trump's parties in the penthouse of the Plaza hotel back then. Trump goaded Epstein for her number. "Jeffrey said he wouldn't give it to him, and he had to get it from me," she says. She finally gave it to him on another occasion, but he lost it. "Trump called Jeffrey, trying to get it again, saying, 'She gave it to me! You know she gave it to me! You can give it to me now!' but Jeffrey wouldn't do it." She laughs. "Donald was such a joke to all of the models back then&mdash;we all knew he was bankrupt and had no game. I remember Jeffrey once saying he was going to be late to pick me up because he had to drop off food for Donald&mdash;he was at home crying under the covers."</p>
<p>Epstein always had a story to tell, even about his home. "He was obsessed with jewelry boxes and very detailed ornate designs&mdash;he told me the pope actually gave him artisans who teamed up with this one jewelry-box maker from Paris to make his dining room look like a giant version of the inside of a Parisian jewelry box," says an ex-girlfriend. Epstein also said that his friend Lynn Forester, now married to billionaire Evelyn de Rothschild, needed his financial help during her 1990s divorce from politician Andrew Stein, and that he had graciously floated her. "One hundred percent false," says a spokesperson for Forester. He claimed that the producers of <em>The Apprentice</em> had first approached him to make a show about a reclusive billionaire living an extravagant life, but he said no, and then introduced them to Trump. (A spokesperson for Mark Burnett denies this.)</p>
<p>Epstein liked having secrets and enjoyed the way those secrets kept people off-balance. "He always wanted to give the impression that he was an international man of mystery&mdash;'I control everyone and everything, I collect people, I own people, I can damage people,"' says an ex-girlfriend. One of the most mysterious parts of his life was his relationship with Ghislaine Maxwell, the favorite daughter of embezzling British press baron and rumored Mossad spy Robert Maxwell, who died when he fell, or was pushed, from his yacht, the <em>Lady Ghislaine.</em> Epstein told them the raven-haired A-lister Maxwell, who opened her Rolodex for him, was a former girlfriend who had fallen on hard times, and he had taken it upon himself to maintain her position in society; young women have since alleged that she was both part of the sex-trafficking ring, bringing underage girls to Epstein, and a sexual participant. "Ghislaine floated in and out of the house with the keys, and even though Jeffrey told me they didn't have a sexual relationship, she'd drop under her breath that she was sleeping in his bed from time to time," says an ex-girlfriend. A friend of Maxwell's says she used to joke about keeping herself rail-thin because Epstein liked thin girls. "She said, 'I do it the way Nazis did it with the Jews, the Auschwitz diet. I just don't eat.' "</p>
<p>On the weekends in the 1990s, Maxwell would have her Rollerblades FedExed to Jeffrey's island in the Caribbean, and she said that she got her helicopter pilot's license so she could transport anyone she liked on her rig, <em>Air Ghislaine 2,</em> without pilots knowing who they were. Maxwell also said the island had been wired for video; the friend thought that she and Epstein were videotaping everyone on the island as an insurance policy, as blackmail. A source close to Maxwell says she spoke glibly and confidently about getting girls to sexually service Epstein, saying this was simply what he wanted, and describing the way she'd drive around to spas in Florida to recruit them. She would claim she had a phone job for them, "and you'll make lots of money, meet everyone, and I'll change your life." The source continues, "Ghislaine was in love with Jeffrey the way she was in love with her father. She always thought if she just did one more thing for him, to please him, he would marry her." Maxwell also told this woman about the young girls in Epstein's life: "She said, 'They're nothing, these girls. They are trash.' "</p>
<p class="floatedimage"><img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Media/0x600/2019100156_2.jpg" data-verified="redactor" data-save-url="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Media/0x600/2019100156_2.jpg"><em class="caption" data-redactor-tag="em">Epstein with Ghislaine Maxwell.</em></p>
<p><strong><span class="drop">E</span>pstein's perversions have</strong> revealed much more than one man's sinister nature: He had a sprawling network of friends and acquaintances who may have participated in or simply overlooked his crimes. These women, however, say he saw himself as a savior of women, including Maxwell, and initiating them into his alternative lifestyle as a path forward in their lives. "One night after we were dating for six or seven months, he sat me down and presented what he wanted for a formal relationship going forward," says one woman. He told her he had a very high sex drive, and like many rich men, dated several women at a time&mdash;this was the way of kings and queens, "It was all about how if I was less conventional and pedestrian, I could have this relationship with him. It was a whole spiel about polyamory, and it made me really insecure&mdash;I wasn't a girl who had high self-esteem or self-worth at that time. I didn't think I could do an open relationship, and I also thought if I said I wouldn't do it, he would still go out with me, but he didn't."</p>
<p>Soon she started to receive strange messages nearly every week. They had pictures of her in them, as she was going about her life. "I didn't think that meant Jeffrey was pining for me and his life was ruined," she says. "I just knew he had legions of people around him to do things like that." Another woman who dated Epstein says he slept with a gun in a holster on the side of the bed and was always playing "spy games," as she calls it. She thinks he tapped her phone after they broke up. She came home to her doorman saying he'd let a repairman in to fix her cable, even though she hadn't requested service. "Then I had a weird sensation when I was talking to Jeffrey&mdash;he kept looking me in the eye in a creepy way and quoting something I'd said about him earlier on the phone to a girlfriend," she says. "I threw the phone out and cut off all contact with him."</p>
<p>These women weren't as powerless as the teenagers in Palm Beach, Florida, whom Epstein was paying a couple hundred dollars for massages that turned into sex. Nor were they sex slaves. And they largely weren't afraid of Epstein back then. But his death has freaked them out. Before he hanged himself, one of them told me, "I think Jeffrey will either get sentenced to prison for life, or if he's in prison, with all the people who don't want him to reveal his secrets, he's dead anyway."</p>
<p><em>This article incorporates materials from web posts published on July 18 and August 12.</em></p>
        <hr class="bnd_article_end" />

    </div>


                                </div>
            </div>

        </div>




                        <div class="five wide column bondi_article_sidebar">



            <div class="sbar_module_wrap shaded related_top5">
                <a class="sbar_cover" href="https://archive.vanityfair.com/issue/20191001" aria-label="View Full Issue">
                    <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Covers/0x420/20191001.jpg" alt="October 2019 | Vanity Fair">
                    <span class="button">View Full Issue</span>
                </a>


            <div class="sbar_module">
                <h2 class="sbar_module_title">More From This Issue</h2>
                <ul class="storypage--sidebar_list sbar_top10">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/upon-a-star" title="View Article: UPON A STAR, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/43.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">UPON A STAR</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Kimberly Drew</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/the-vanity-fair-best-dressed-list" title="View Article: The Vanity Fair Best-Dressed List, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/50.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">The Vanity Fair Best-Dressed List</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Maggie Bullock</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/goodbye-by-sunshine" title="View Article: Goodbye Mr. Sunshine, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Goodbye Mr. Sunshine</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Bethany Mclean</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/a-rakes-progress" title="View Article: A RAKE'S PROGRESS, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/62.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">A RAKE'S PROGRESS</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Aatish Taseer</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/dreads-rebellion" title="View Article: DREAD'S REBELLION, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/66.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">DREAD'S REBELLION</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Julian Lucas</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/future-perfect" title="View Article: FUTURE PERFECT, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/69.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">FUTURE PERFECT</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Sonia Saraiya</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>
                        </div>



                                    <div class="shared_substory_cta">
    <div class="vf_cta_slant_hed">
        <span class="vf_cta_slant_hed_inner">Join Today</span>
    </div>
    <h3 class="promohead">
        <span class="promodeck">Subscribers can unlock <strong>every article</strong> <em>Vanity Fair</em> has ever published</span>
        <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_RIGHTRAIL_0" target="_blank" class="link-subscribe">Subscribe</a>
    </h3>
</div>





            <div class="sbar_module mdtp_category">
                <h2 class="sbar_module_title"><a href="https://archive.vanityfair.com/sections/crime-punishment">Crime & Punishment</a></h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1993/10/dominick-dunnes-courtroom-notebook-the-menendez-murder-trial" title="View Article: Dominick Dunne's COURTROOM NOTEBOOK: The Menendez Murder Trial, October 1993 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19931001thumbnails/Spreads/0x420/152.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Dominick Dunne's COURTROOM NOTEBOOK: The Menendez Murder Trial</h3>
                        <span class="tpc_date">October 1993 <!--<span>1993</span>--></span>
                        <span class="tpc_byline">By <span class="author">Dominick Dunne</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1995/8/if-the-gloves-fit" title="View Article: IF THE GLOVES FIT..., August 1995 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19950801thumbnails/Spreads/0x420/35.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">IF THE GLOVES FIT...</h3>
                        <span class="tpc_date">August 1995 <!--<span>1995</span>--></span>
                        <span class="tpc_byline">By <span class="author">Dominick Dunne</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2022/7/scene-stealer" title="View Article: SCENE STEALER, July/August 2022 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20220701thumbnails/Spreads/0x420/38.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">SCENE STEALER</h3>
                        <span class="tpc_date">July/August 2022 <!--<span>2022</span>--></span>
                        <span class="tpc_byline">By <span class="author">EVGENIA PERETZ</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2021/4/the-case-of-the-purloined-books" title="View Article: The Case of the Purloined Books, April 2021 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20210401thumbnails/Spreads/0x420/47.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">The Case of the Purloined Books</h3>
                        <span class="tpc_date">April 2021 <!--<span>2021</span>--></span>
                        <span class="tpc_byline">By <span class="author">Marc Wortman</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2012/7/a-case-so-cold-it-was-blue" title="View Article: A Case So Cold It Was Blue, July 2012 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20120701thumbnails/Spreads/0x420/65.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">A Case So Cold It Was Blue</h3>
                        <span class="tpc_date">July 2012 <!--<span>2012</span>--></span>
                        <span class="tpc_byline">By <span class="author">Mark Bowden</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2003/6/legend-with-a-bullet" title="View Article: LEGEND WITH A BULLET, June 2003 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20030601thumbnails/Spreads/0x420/99.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">LEGEND WITH A BULLET</h3>
                        <span class="tpc_date">June 2003 <!--<span>2003</span>--></span>
                        <span class="tpc_byline">By <span class="author">Robert Sam Anson</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_author">
                <h2 class="sbar_module_title">Vanessa Grigoriadis</h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2011/6/ol-mark-pincus-had-a-farm" title="View Article: OL' MARK PINCUS HAD A FARM..., June 2011 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20110601thumbnails/Spreads/0x420/70.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">OL' MARK PINCUS HAD A FARM...</h3>
                        <span class="tpc_date">June 2011 <!--<span>2011</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2012/9/riding-high" title="View Article: Riding High, September 2012 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20120901thumbnails/Spreads/0x420/102.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Fanfair</span>
                        <h3 class="tpc_title">Riding High</h3>
                        <span class="tpc_date">September 2012 <!--<span>2012</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2012/12/tory-burchs-ex-factor" title="View Article: TORY BURCH'S EX FACTOR, December 2012 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20121201thumbnails/Spreads/0x420/102.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">TORY BURCH'S EX FACTOR</h3>
                        <span class="tpc_date">December 2012 <!--<span>2012</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2013/9/the-eyeful-tower" title="View Article: The EYEFUL TOWER, September 2013 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20130901thumbnails/Spreads/0x420/187.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">The EYEFUL TOWER</h3>
                        <span class="tpc_date">September 2013 <!--<span>2013</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2014/4/ok-glass-make-google-eyes" title="View Article: O.K., Glass: Make Google Eyes, April 2004 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20140401thumbnails/Spreads/0x420/83.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">O.K., Glass: Make Google Eyes</h3>
                        <span class="tpc_date">April 2004 <!--<span>2014</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2018/6/spring-forward" title="View Article: Spring Forward, Summer 2018 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20180601thumbnails/Spreads/0x420/56.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Spring Forward</h3>
                        <span class="tpc_date">Summer 2018 <!--<span>2018</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_illustrator">
                <h2 class="sbar_module_title">Philip Burke</h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2001/10/the-fox-factor" title="View Article: THE FOX FACTOR, October 2001 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20011001thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Letters</span>
                        <h3 class="tpc_title">THE FOX FACTOR</h3>
                        <span class="tpc_date">October 2001 <!--<span>2001</span>--></span>

                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1994/3/conversations-with-castro" title="View Article: Conversations with Castro, March 1994 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19940301thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Conversations with Castro</h3>
                        <span class="tpc_date">March 1994 <!--<span>1994</span>--></span>
                        <span class="tpc_byline">By <span class="author">Ann Louise Bardach</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1987/4/the-whole-robert-dole" title="View Article: The Whole ROBERT DOLE, April 1987 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19870401thumbnails/Spreads/0x420/59.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section"></span>
                        <h3 class="tpc_title">The Whole ROBERT DOLE</h3>
                        <span class="tpc_date">April 1987 <!--<span>1987</span>--></span>
                        <span class="tpc_byline">By <span class="author">Gail Sheehy</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1998/10/boys-in-babeland" title="View Article: BOYS IN BABELAND, October 1998 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19981001thumbnails/Spreads/0x420/86.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">BOYS IN BABELAND</h3>
                        <span class="tpc_date">October 1998 <!--<span>1998</span>--></span>
                        <span class="tpc_byline">By <span class="author">James Wolcott</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2005/11/meanwhile-in-an-undisclosed-location" title="View Article: MEANWHILE, IN AN UNDISCLOSED LOCATION..., November 2005 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20051101thumbnails/Spreads/0x420/102.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">MEANWHILE, IN AN UNDISCLOSED LOCATION...</h3>
                        <span class="tpc_date">November 2005 <!--<span>2005</span>--></span>
                        <span class="tpc_byline">By <span class="author">Michael Wolff</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2001/7/thunder-at-the-times" title="View Article: THUNDER AT THE TIMES, JULY 2001 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20010701thumbnails/Spreads/0x420/31.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">THUNDER AT THE TIMES</h3>
                        <span class="tpc_date">JULY 2001 <!--<span>2001</span>--></span>
                        <span class="tpc_byline">By <span class="author">Suzanna Andrews</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_section">
                <h2 class="sbar_module_title"><a href="https://archive.vanityfair.com/sections/columns">Columns</a></h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2007/11/the-people-vs-the-profiteers" title="View Article: The People vs. the Profiteers, November 2007 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20071101thumbnails/Spreads/0x420/114.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">The People vs. the Profiteers</h3>
                        <span class="tpc_date">November 2007 <!--<span>2007</span>--></span>
                        <span class="tpc_byline">By <span class="author">David Rose</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1987/7/being-and-somethingness" title="View Article: BEING AND SOMETHINGNESS, July 1987 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19870701thumbnails/Spreads/0x420/21.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">BEING AND SOMETHINGNESS</h3>
                        <span class="tpc_date">July 1987 <!--<span>1987</span>--></span>
                        <span class="tpc_byline">By <span class="author">James Atlas</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1990/5/la-dolce-two-seater" title="View Article: LA DOLCE TWO-SEATER, May 1990 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19900501thumbnails/Spreads/0x420/85.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">LA DOLCE TWO-SEATER</h3>
                        <span class="tpc_date">May 1990 <!--<span>1990</span>--></span>
                        <span class="tpc_byline">By <span class="author">Mark Ginsburg</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1990/11/playing-for-time" title="View Article: PLAYING FOR TIME, November 1990 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19901101thumbnails/Spreads/0x420/42.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">PLAYING FOR TIME</h3>
                        <span class="tpc_date">November 1990 <!--<span>1990</span>--></span>
                        <span class="tpc_byline">By <span class="author">Mark Macnamara</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1988/12/death-and-brotherhood" title="View Article: DEATH AND BROTHERHOOD, December 1988 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19881201thumbnails/Spreads/0x420/57.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">DEATH AND BROTHERHOOD</h3>
                        <span class="tpc_date">December 1988 <!--<span>1988</span>--></span>
                        <span class="tpc_byline">By <span class="author">Nicholas Goldberg</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1989/8/billys-blues" title="View Article: BILLY'S BLUES, August 1989 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19890801thumbnails/Spreads/0x420/29.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">BILLY'S BLUES</h3>
                        <span class="tpc_date">August 1989 <!--<span>1989</span>--></span>
                        <span class="tpc_byline">By <span class="author">Richard Merkin</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>






        </div>
    </div>


            <div class="article_substory_wrap">
            <div class="ui container article_substory">

                            <div class="sbar_module_wrap related_top5">

            <div class="sbar_module">
                <h2 class="sbar_module_title">More From This Issue</h2>
                <ul class="storypage--sidebar_list sbar_top10">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/upon-a-star" title="View Article: UPON A STAR, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/43.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">UPON A STAR</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Kimberly Drew</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/the-vanity-fair-best-dressed-list" title="View Article: The Vanity Fair Best-Dressed List, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/50.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">The Vanity Fair Best-Dressed List</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Maggie Bullock</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2019/10/goodbye-by-sunshine" title="View Article: Goodbye Mr. Sunshine, October 2019 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Goodbye Mr. Sunshine</h3>
                        <span class="tpc_date">October <span>2019</span></span>
                        <span class="tpc_byline">By <span class="author">Bethany Mclean</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>
                </div>



            <div class="sbar_module mdtp_category">
                <h2 class="sbar_module_title"><a href="https://archive.vanityfair.com/sections/crime-punishment">Crime & Punishment</a></h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1993/10/dominick-dunnes-courtroom-notebook-the-menendez-murder-trial" title="View Article: Dominick Dunne's COURTROOM NOTEBOOK: The Menendez Murder Trial, October 1993 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19931001thumbnails/Spreads/0x420/152.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Dominick Dunne's COURTROOM NOTEBOOK: The Menendez Murder Trial</h3>
                        <span class="tpc_date">October 1993 <!--<span>1993</span>--></span>
                        <span class="tpc_byline">By <span class="author">Dominick Dunne</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1995/8/if-the-gloves-fit" title="View Article: IF THE GLOVES FIT..., August 1995 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19950801thumbnails/Spreads/0x420/35.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">IF THE GLOVES FIT...</h3>
                        <span class="tpc_date">August 1995 <!--<span>1995</span>--></span>
                        <span class="tpc_byline">By <span class="author">Dominick Dunne</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2022/7/scene-stealer" title="View Article: SCENE STEALER, July/August 2022 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20220701thumbnails/Spreads/0x420/38.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">SCENE STEALER</h3>
                        <span class="tpc_date">July/August 2022 <!--<span>2022</span>--></span>
                        <span class="tpc_byline">By <span class="author">EVGENIA PERETZ</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_author">
                <h2 class="sbar_module_title">Vanessa Grigoriadis</h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2011/6/ol-mark-pincus-had-a-farm" title="View Article: OL' MARK PINCUS HAD A FARM..., June 2011 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20110601thumbnails/Spreads/0x420/70.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">OL' MARK PINCUS HAD A FARM...</h3>
                        <span class="tpc_date">June 2011 <!--<span>2011</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2012/9/riding-high" title="View Article: Riding High, September 2012 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20120901thumbnails/Spreads/0x420/102.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Fanfair</span>
                        <h3 class="tpc_title">Riding High</h3>
                        <span class="tpc_date">September 2012 <!--<span>2012</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2012/12/tory-burchs-ex-factor" title="View Article: TORY BURCH'S EX FACTOR, December 2012 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20121201thumbnails/Spreads/0x420/102.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">TORY BURCH'S EX FACTOR</h3>
                        <span class="tpc_date">December 2012 <!--<span>2012</span>--></span>
                        <span class="tpc_byline">By <span class="author">Vanessa Grigoriadis</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_illustrator">
                <h2 class="sbar_module_title">Philip Burke</h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2001/10/the-fox-factor" title="View Article: THE FOX FACTOR, October 2001 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20011001thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Letters</span>
                        <h3 class="tpc_title">THE FOX FACTOR</h3>
                        <span class="tpc_date">October 2001 <!--<span>2001</span>--></span>

                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1994/3/conversations-with-castro" title="View Article: Conversations with Castro, March 1994 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19940301thumbnails/Spreads/0x420/73.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Features</span>
                        <h3 class="tpc_title">Conversations with Castro</h3>
                        <span class="tpc_date">March 1994 <!--<span>1994</span>--></span>
                        <span class="tpc_byline">By <span class="author">Ann Louise Bardach</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1987/4/the-whole-robert-dole" title="View Article: The Whole ROBERT DOLE, April 1987 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19870401thumbnails/Spreads/0x420/59.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section"></span>
                        <h3 class="tpc_title">The Whole ROBERT DOLE</h3>
                        <span class="tpc_date">April 1987 <!--<span>1987</span>--></span>
                        <span class="tpc_byline">By <span class="author">Gail Sheehy</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>

            <div class="sbar_module mdtp_section">
                <h2 class="sbar_module_title"><a href="https://archive.vanityfair.com/sections/columns">Columns</a></h2>
                <ul class="storypage--sidebar_list sbar_section">

            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/2007/11/the-people-vs-the-profiteers" title="View Article: The People vs. the Profiteers, November 2007 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair20071101thumbnails/Spreads/0x420/114.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">The People vs. the Profiteers</h3>
                        <span class="tpc_date">November 2007 <!--<span>2007</span>--></span>
                        <span class="tpc_byline">By <span class="author">David Rose</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1987/7/being-and-somethingness" title="View Article: BEING AND SOMETHINGNESS, July 1987 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19870701thumbnails/Spreads/0x420/21.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">BEING AND SOMETHINGNESS</h3>
                        <span class="tpc_date">July 1987 <!--<span>1987</span>--></span>
                        <span class="tpc_byline">By <span class="author">James Atlas</span></span>
                    </div>
                </a>
            </li>
            <li class="bndwgt widget-spread bndwgt__pagefx">
                <a class="lndg_art_link" href="https://archive.vanityfair.com/article/1990/5/la-dolce-two-seater" title="View Article: LA DOLCE TWO-SEATER, May 1990 | Vanity Fair">
                    <div class="bndwgt__slide">
                        <span class="bndwgt__slide-link">
                            <img src="https://vanityfair.blob.core.windows.net/vanityfair19900501thumbnails/Spreads/0x420/85.jpg" alt="">
                            <span class="bndwgt__pgfx-top"></span><span class="bndwgt__pgfx-left"></span><span class="bndwgt__pgfx-right"></span><span class="bndwgt__pgfx-btm"></span><span class="bndwgt__pgfx-shine bndwgt__hilite"></span>
                        </span>
                    </div>
                    <div class="topFeatureText">
                        <span class="tpc_section">Columns</span>
                        <h3 class="tpc_title">LA DOLCE TWO-SEATER</h3>
                        <span class="tpc_date">May 1990 <!--<span>1990</span>--></span>
                        <span class="tpc_byline">By <span class="author">Mark Ginsburg</span></span>
                    </div>
                </a>
            </li>
                </ul>
            </div>



            </div>
        </div>

        </main>

                        <div role="contentinfo" class="bnd_page_footer ui inverted vertical footer segment">
        <div class="ui center aligned container">

            <div class="bnd_page_footer_billboard">
                <div class="">
                    <a class="footer_logo" href="/" tabindex="0" aria-label="Go to Vanity Fair Archive Homepage">Vanity Fair Archive</a>
                    <div class="footer_tagline"></div>
                </div>
            </div>

            <ul class="site_menu" role="menubar">
                <li class="menunav"><a class="nav_welcome" href="/" title="Welcome: Go to Vanity Fair Archive Homepage" tabindex="0" aria-label="Go to Homepage">Welcome</a></li>

                <li class="menunav"><a class="nav_issues bndwgt_decades_trigger" href="javascript:void(0)" tabindex="0" aria-haspopup="true" title="Browse Issues by Decade" aria-label="Browse Issues">Issues</a></li>

                                <li class="menunav"><a class="nav_topics bndwgt_topics_trigger" href="javascript:void(0)" tabindex="0" aria-haspopup="true" aria-label="Browse Collections">Collections</a></li>
                <li class="menunav"><a class="nav_authors bndwgt_authors_trigger" href="javascript:void(0)" tabindex="0" aria-haspopup="true" title="Browse Featured Contributors" aria-label="Browse Featured Contributors">Contributors</a></li>


                <li class="menunav"><a class="nav_search ui icon bnd_search_overlay_trigger" href="javascript:void(0)" tabindex="0" title="Search the Vanity Fair Archive" aria-label="Search" aria-haspopup="true">Search <i class="search icon"></i></a></li>
            </ul>
            <ul class="user_menu">
                <li class="menunav"><a href="https://www.vanityfair.com/">VF.com</a></li>



            <li class="user_menu_1 login"><a role="menuitem" class="" href="/login" tabindex="0" aria-label="Sign In">Sign In</a></li>
            <li class="user_menu_2"><a role="menuitem" href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_FOOTER_SUBSCRIBE_0" class="link-subscribe" target="_blank" tabindex="0" aria-label="Subscribe"><span data-alt="Subscribe Now"><span>Subscribe</span></span></a></li>

            </ul>
            <button id="fides-modal-link">Manage Preferences</button>
            <div class="footer_meta ui horizontal inverted small divided">
                <div class="bnd_footer_copyright">&copy;2025 Condé Nast. All rights reserved.
                    <span>Use of and/or registration on any portion of this site constitutes acceptance of our <a href="https://www.condenast.com/user-agreement/" target="_blank" rel="nofollow">User Agreement</a> (updated 1/1/20) and <a href="https://www.condenast.com/privacy-policy/" target="_blank" rel="nofollow">Privacy Policy and Cookie Statement</a> (updated 1/1/20). <a href="https://www.condenast.com/privacy-policy/#california" target="_blank" rel="nofollow">Your CA Privacy Rights</a> The material on this site may not be reproduced, distributed, transmitted, cached, or otherwise used, except with the prior written permission of Condé Nast.</span>
                </div>
            </div>
        </div>
    </div>

    <div id="bnd_subscribe_modaal" class="bnd_modaal">
    <div id="bnd_subscribe_popup" class="bnd_subscribe_popup" aria-modal="true">
        <div class="content">
            <div class="dual_modal_login">
                <div class="ui tab active" data-tab="login">
                    <div class="modal-image"></div>
                    <div class="bnd_login_content">
    <div class="form_wrapper">

                <span class="vflogo" title="Vanity Fair Archive" alt="Vanity Fair Logo"></span>
        <h1 id="LoginLabel" class="edge">Sign In to Your Account</h1>
        <p class="details">Subscribers have complete access to the archive.</p>
        <a class="ui button bnd_login" tab-index="0" aria-label="Sign In to view Content" href="/login">Sign In</a>


        <a class="bnd_login_join" href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_SIGN_IN_0" target="_blank"><span>Not a Subscriber?<span class="bnd_login_join_btn">Join Now</span></span></a>
    </div>
</div>
                </div>
            </div>
        </div>
    </div>
</div>


        <div class="bnd_modaal bnd_modal" data-trigger=".bndwgt_topics_trigger" data-title="Collections" data-slug="collections"></div>
    <div class="bnd_modaal bnd_modal" data-trigger=".bndwgt_authors_trigger" data-title="Contributors" data-slug="authors"></div>
                <div id="bnd_issues_modaal" class="bnd_modaal"></div>
                            <script src="https://cdn.jsdelivr.net/npm/modaal@0.4.4/dist/js/modaal.min.js"></script>

                        <script type="text/javascript">
                $(document).ready(function() {
                    $(window).on("scroll", function() {
                        if ($(window).scrollTop() > 1200) {
                            $('#backToTop').fadeIn(700);
                        }
                        if ($(window).scrollTop() < 1200) {
                            $('#backToTop').fadeOut(700);
                        }
                    });

                    $('#backToTop').on('click', function(e) {
                        e.preventDefault();
                        document.body.scrollTop = 0; // For Safari
                        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
                    });
                });
            </script>
            <button id="backToTop" class="bnd__backtotop circular ui icon button huge" title="Back to Top" type="button" aria-label="Back to Top of Page"><i class="icon angle up"></i></button>


            <div class="bndvwr viewer-display" tabindex="-1" role="dialog" aria-hidden="true" aria-label="Magazine Viewer for scanned image pages">
    <!-- <div tabindex="0" class="sentinelStart"></div> -->
    <div class="bndvwr__bg"></div>
    <div class="bndvwr__scroll-wrap">
        <div class="bndvwr__container">
            <div class="bndvwr__item"></div>
            <div class="bndvwr__item"></div>
            <div class="bndvwr__item"></div>
        </div>
        <div role="navigation" aria-label="Primary Viewer Menu" class="bndvwr__ui bndvwr__ui--hidden  ">

            <div role="menu" class="bndvwr__top-bar">
                <div id="sentinelStart" tabIndex="99"></div>


                <a id="" class="bndwvr__logo" role="menuitem" tabindex="99" href="/" title="Vanity Fair Archive Home" aria-label="Vanity Fair Archive Home" rel="home">
                    <h1>Vanity Fair</h1>
                </a>

                <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--close" title="Close (Esc)" aria-label="Close Viewer - or use Esc key"></button>
                <div class="bndwvr__partner_logo"></div>

                <div class="bndvwr__preloader">
                    <div class="bndvwr__preloader__icn">
                        <div class="bndvwr__preloader__cut">
                            <div class="bndvwr__preloader__donut"></div>
                        </div>
                    </div>
                </div>
            </div>





                        <div role="menu" class="bndvwr__jump_bar">
                <div class="jumpbar__top">
                                        <a role="menuitem" tabindex="99" href="https://archive.vanityfair.com/issue/20191001" class="jumpbar__issue" title="View the Full Issue" aria-label="View the Full Issue">October 2016</a>
                                    </div>
                <div class="jumpbar__btm">


                                                             <a href="javascript:void(0);" role="menuitem" tabindex="99" class="jumpbar__bkm_link bndvwr__button--jumpshare" title="View Article Permalink" aria-label="View article permalink on separate page"><i class="ui icon linkify bndvwr__button--jumpshare"></i></a>


                                                                                <a role="menuitem" tabindex="99" class="jumpbar__bkm_link bndvwr__button--print" title="Print this article" aria-label="Print this article"><i class="bkm_icon icon-printer bndvwr__button--print"></i></a>


                                    </div>
            </div>



                                        <div id="bndvwr__thumbstrip" class="bndvwr__thumbstrip bndvwr__mode_spread" aria-label="Secondary - Viewer Thumbnail Menu">



                    <ul class="bndvwr__flicker" data-flickity1='{ "cellAlign": "left", "contain": true, "groupCells": "80%", "pageDots": false, "imagesLoaded": true, "lazyLoad": true }'>
                                                                                    <li id="thumb_74" class="bndvwr__thumb thumb_even thumb_74">
           <a href="#" class="bndvwr__thumb" data-pagename="74" data-sequence="78" data-spread="1" style="">
               <span class="bndvwr__thumb_wrapper">
                   <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Pages/0x90/74.jpg" class="bndvwr__thumb" data-pagename="74" data-sequence="78" data-spread="1" alt="Page: - 74 | Vanity Fair">
               <span class="vwr_th_folio"></span></span>
               <span class="bndvwr__thumb_page">74</span>
           </a>
       </li>
                                                            <li id="thumb_74" class="bndvwr__thumb thumb_odd thumb_74">
           <a href="#" class="bndvwr__thumb" data-pagename="75" data-sequence="79" data-spread="1" style="">
               <span class="bndvwr__thumb_wrapper">
                   <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Pages/0x90/75.jpg" class="bndvwr__thumb" data-pagename="75" data-sequence="79" data-spread="1" alt="Page: - 75 | Vanity Fair">
               <span class="vwr_th_folio"></span></span>
               <span class="bndvwr__thumb_page">75</span>
           </a>
       </li>
                                                            <li id="thumb_76" class="bndvwr__thumb thumb_even thumb_76">
           <a href="#" class="bndvwr__thumb" data-pagename="76" data-sequence="80" data-spread="2" style="">
               <span class="bndvwr__thumb_wrapper">
                   <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Pages/0x90/76.jpg" class="bndvwr__thumb" data-pagename="76" data-sequence="80" data-spread="2" alt="Page: - 76 | Vanity Fair">
               <span class="vwr_th_folio"></span></span>
               <span class="bndvwr__thumb_page">76</span>
           </a>
       </li>
                                                            <li id="thumb_76" class="bndvwr__thumb thumb_odd thumb_76">
           <a href="#" class="bndvwr__thumb" data-pagename="77" data-sequence="81" data-spread="2" style="">
               <span class="bndvwr__thumb_wrapper">
                   <img src="https://vanityfair.blob.core.windows.net/vanityfair20191001thumbnails/Pages/0x90/77.jpg" class="bndvwr__thumb" data-pagename="77" data-sequence="81" data-spread="2" alt="Page: - 77 | Vanity Fair">
               <span class="vwr_th_folio"></span></span>
               <span class="bndvwr__thumb_page">77</span>
           </a>
       </li>
                                                                        </ul>
                </div>

                                <script type="text/javascript">
                    var $flicker = $('.bndvwr__flicker').flickity({
                        accessibility: false,
                        cellAlign: 'left',
                        contain: true,
                        groupCells: '80%',
                        pageDots: false,
                        imagesLoaded: true,
                        lazyLoad: true,
                        draggable: true,
                        freeScroll: true,
                        freeScrollFriction: 0.05
                    });
                </script>


            <div id="viewerArrows">
                <!-- <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--arrow--left" title="Previous Page" aria-label="View Previous Page"></button>
                <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--arrow--right" title="Next Page" aria-label="View Next Page"></button> -->
            </div>

            <div role="menu" class="bndvwr__btm-bar" aria-label="Secondary Viewer Menu">

                                <button role="menuitem" tabindex="99" id="bndwgt_pageinfo_trigger" class="bndvwr__button_custom bndvwr__button--info">Page Details</button>


                                <button role="menuitem" tabindex="99" id="thumbs_toggle" class="bndvwr__button--thumbs_toggle" title="View Page Thumbnails" aria-label="View Page Thumbnails">View Thumbnails</button>

                <div class="bndvwr__btm-innerRightBar">
                                        <button role="menuitem" tabindex="99" id="bndwgtViewText" class="bndwgt_article_trigger bndvwr__button_custom btn_text bndvwr__button--text" title="Read Article Text" aria-label="Read Plain Article Text">
                        <span class="bndvwr__btn_wide bndvwr__button--text">Read <strong class="bndvwr__button--text">Plain Text</strong></span>
                        <span class="bndvwr__btn_thin bndvwr__button--text">Read Text</span>
                    </button>

                                        <div role="menu" tabindex="99" id="bndwgtMultiViewText" class="ui dropdown bndvwr__button_custom bndwgt_multiarticle_trigger">
                        <div class="dropdown_fixed_text">
                            <span class="bndvwr__btn_wide">Read <strong>Plain Text</strong></span>
                            <span class="bndvwr__btn_thin">Read Text</span>
                        </div>
                        <i class="angle up icon"></i>
                        <div class="menu">
                            <a role="menuitem" class="item bndvwr__button--text" title="Read Article Text" aria-label="Read Plain Article Text">Article One</a>
                            <a role="menuitem" class="item bndvwr__button--text" title="Read Article Text" aria-label="Read Plain Article Text">Article Two</a>
                            <a role="menuitem" class="item bndvwr__button--text" title="Read Article Text" aria-label="Read Plain Article Text">Article Three</a>
                        </div>
                    </div>
                    <script> //Multi Article Dropdown
                        $('.ui.dropdown.bndwgt_multiarticle_trigger')
                            .dropdown()
                        ;
                    </script>

                    <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--outzoom" title="Zoom Out Gradually" aria-label="Zoom Out Gradually - or use DOWN arrow"></button>
                    <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--zoom" title="Maximum Zoom In/Out [SPACE BAR]" aria-label="Maximum Zoom in or out - or use SPACE bar"></button>
                    <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--inzoom" title="Zoom In Gradually" aria-label="Zoom In Gradually - or use UP arrow"></button>
                    <button role="menuitem" tabindex="99" class="bndvwr__button bndvwr__button--fs" title="Toggle fullscreen" aria-label="Toggle Fullscreen Image Viewer"></button>
                </div>            </div>
            <div class="bndvwr__counter" role="details" tabindex="-1"  title="Current Page" aria-label="Current Page Number"></div>
                        <div class="bndvwr__share-modal bndvwr__share-modal--hidden bndvwr__single-tap">
                <div class="bndvwr__share-tooltip"></div>
            </div>

            <div class="bndvwr__caption"><div class="bndvwr__caption__center"></div></div>
        </div>    </div></div>






<div id="" class="bndwgt__plain_text_outer_header">
    <button id="bndwgtViewPages" class="bndwgt__plain_text_closebutton bndvwr__button_custom btn_pages" title="View Article Pages" role="menuitem" tabindex="0" aria-label="Close plain text">
       <span class="bndvwr__btn_wide bndvwr__button--text">I'm <strong class="bndvwr__button--text">Done Reading</strong></span>
       <span class="bndvwr__btn_thin bndvwr__button--text">Done Reading</span>
    </button>
    <i id="" class="bndwgt__plain_text_closebutton close icon"></i>
</div>
<div class="bndwgt__plain_text_wrapper ui modal">
    <i id="closebutton" class="close icon" role="menuitem" tabindex="0" aria-label="Close plain text window"></i>


    <div class="content bndwgt__text"></div>


    <div class="actions">
        <div role="menuitem" tabindex="0" aria-label="Close plain text window" class="ui black deny button">Done Reading</div>
    </div>
    </div>






<div id="bndwgt__pageinfo_wrapper" class="bndwgt__pageinfo_wrapper ui modal"></div>
<script>
    // When closing the Page Info modal
    $('.bndwgt__pageinfo_wrapper').modal({
        onHidden: function() {
            $('body').removeClass('pageinfo_visible');
            $('.pageInfo_actions').insertAfter( "#bndwgt__pageinfo_wrapper" );
        }
    });
</script>


    <script src="https://archive.vanityfair.com/js/bondi.article.viewer.js?id=5fd314ee72be0e5c0f25"></script>

                            <div class="shared_footer_cta_basic">
    <div class="cta_inner">


                        <span class="bnd_meter_wrap">


                        <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_METER_ARTICLE_1 _0" target="_blank" class="hider">
                <span>The <em>Vanity Fair</em> Archive is a subscriber-only benefit.
                                        <strong>Enjoy one article on us.</strong>
                                    </span>
            </a>

        </span>




        <div class="cta_basic_content">
            <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_STICKY_FOOTER_0" target="_blank" class="link">Join Now</a>
            <span style="margin-left:10px">Already a Subscriber?</span>
            <a tab-index="0" aria-label="Sign In to view Content" href="/login" class="redlink">Sign In</a>
        </div>
    </div>
</div>




</style>
<div id="shared_cta1" class="shared_footer_cta_primary">
    <div class="cta_inner">



                <h3 class="promohead">
            Access everything <em>Vanity Fair</em> has ever published. <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_RISER_FOOTER_0" target="_blank" >Join Now</a>
            <span class="promodeck">Subscriber-Only Benefit — <strong>The Complete Vanity Fair Archive</strong> • <span class="">EVERY ISSUE. EVERY PAGE. 1913 TO TODAY.</span></span>
        </h3>

    </div>
</div>



                            <div class="shared_footer_cta_basic">
    <div class="cta_inner">


                        <span class="bnd_meter_wrap">


                        <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_METER_ARTICLE_1 _0" target="_blank" class="hider">
                <span>The <em>Vanity Fair</em> Archive is a subscriber-only benefit.
                                        <strong>Enjoy one article on us.</strong>
                                    </span>
            </a>

        </span>




        <div class="cta_basic_content">
            <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_STICKY_FOOTER_0" target="_blank" class="link">Join Now</a>
            <span style="margin-left:10px">Already a Subscriber?</span>
            <a tab-index="0" aria-label="Sign In to view Content" href="/login" class="redlink">Sign In</a>
        </div>
    </div>
</div>




</style>
<div id="shared_cta1" class="shared_footer_cta_primary">
    <div class="cta_inner">



                <h3 class="promohead">
            Access everything <em>Vanity Fair</em> has ever published. <a href="https://subscribe.vanityfair.com/subscribe/splits/vanityfair/VYF_ARCHIVES?source=HCL_VYF_ARCHIVES_RISER_FOOTER_0" target="_blank" >Join Now</a>
            <span class="promodeck">Subscriber-Only Benefit — <strong>The Complete Vanity Fair Archive</strong> • <span class="">EVERY ISSUE. EVERY PAGE. 1913 TO TODAY.</span></span>
        </h3>

    </div>
</div>



                <script type="text/javascript">
            $(document).ready(function() {
                $(window).on("scroll", function() {
                    if ($(window).scrollTop() > 2500) { $('#shared_cta1').slideDown(500); $('#shared_cta2').fadeIn(1000);
                    }
                    if ($(window).scrollTop() < 2500) { $('#shared_cta1').slideUp(500); $('#shared_cta2').fadeOut(1000);
                    }
                });
            });
        </script>


        <script src="https://archive.vanityfair.com/js/app-prod.js?id=527d078d0824bd1381b8"></script>
    </body>
</html>
