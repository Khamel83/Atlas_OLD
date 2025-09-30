# Content from http://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/

*Retrieved: 2025-09-15T01:53:25.691355*

---

<!DOCTYPE html>
<html lang="en-US" class="no-js">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<link rel='dns-prefetch' href='//dcf.espn.com' />

<script type="text/javascript">
			function setCountryCookie(value,days) {
				var expires = "";
				if (days) {
					var date = new Date();
					date.setTime(date.getTime() + (days*24*60*60*1000));
					expires = "; expires=" + date.toUTCString();
				}
				document.cookie = "country=" + (value || "") + expires + "; path=/";
			}

function getCountryCookie() {
				let value = decodeURIComponent(document.cookie);
				let parts = value.split(`; country=`);
  				if (parts.length === 2) {
					return parts.pop().split(';').shift();
				}
				return "";
			}

var countryCookie = getCountryCookie();
			if ( ! countryCookie || 'us' !== countryCookie ) {
				setCountryCookie('us',1);
			}
		</script>
				<script type="text/javascript">
			var dtciDataLayer = {"page":{"content_publish_date":"09\/25\/2014","content_publish_time":"13:54","content_last_update_date":"04\/21\/2017","content_last_update_time":"10:37","contentcategory":"2014 Midterms,Polling,Polls,Pollster Ratings,Senate Forecast","section_1":"politics","section_2":"politics:polling","story_title":"How FiveThirtyEight Calculates Pollster Ratings","story_id":54447,"author":"Nate Silver","page_name":"fivethirtyeight:politics:features","content_type":"features","app_version":"1.1.2","device_type":"Desktop","prev_page":false,"template":"standard_layout","editorial_other_subjects":["2014 Midterms","Polling","Polls","Pollster Ratings","Senate Forecast"],"word_count":7540},"site":{"edition":"en-us","language":"en","site":"fivethirtyeight"},"detailsEndpoint":"https:\/\/fivethirtyeight.com\/wp-json\/dtci_datalayer\/v1\/get_page_details\/","device":{"device_type":"Desktop"}};
		</script>

		<script src="https://dcf.espn.com/TWDC-DTCI/prod/Bootstrap.js"></script>
<title>How FiveThirtyEight Calculates Pollster Ratings | FiveThirtyEight</title>
<meta name='robots' content='max-image-preview:large' />
	<style>img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px }</style>
	<!-- Jetpack Site Verification Tags -->
<meta name="google-site-verification" content="-j2BzwWZ0QSsFphrQ_5sJtlT_ZF5B5qkZhCQHF2MRz8" />
<link rel='dns-prefetch' href='//cdn.registerdisney.go.com' />
<link rel='dns-prefetch' href='//platform.twitter.com' />
<link rel='dns-prefetch' href='//datawrapper.dwcdn.net' />
<link rel='dns-prefetch' href='//use.typekit.net' />
<link rel='stylesheet' id='wp-block-library-css' href='https://fivethirtyeight.com/wp-includes/css/dist/block-library/style.min.css?ver=6.8.2' media='all' />
<style id='classic-theme-styles-inline-css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='co-authors-plus-coauthors-style-inline-css'>
.wp-block-co-authors-plus-coauthors.is-layout-flow [class*=wp-block-co-authors-plus]{display:inline}

</style>
<style id='co-authors-plus-avatar-style-inline-css'>
.wp-block-co-authors-plus-avatar :where(img){height:auto;max-width:100%;vertical-align:bottom}.wp-block-co-authors-plus-coauthors.is-layout-flow .wp-block-co-authors-plus-avatar :where(img){vertical-align:middle}.wp-block-co-authors-plus-avatar:is(.alignleft,.alignright){display:table}.wp-block-co-authors-plus-avatar.aligncenter{display:table;margin-inline:auto}

</style>
<style id='co-authors-plus-image-style-inline-css'>
.wp-block-co-authors-plus-image{margin-bottom:0}.wp-block-co-authors-plus-image :where(img){height:auto;max-width:100%;vertical-align:bottom}.wp-block-co-authors-plus-coauthors.is-layout-flow .wp-block-co-authors-plus-image :where(img){vertical-align:middle}.wp-block-co-authors-plus-image:is(.alignfull,.alignwide) :where(img){width:100%}.wp-block-co-authors-plus-image:is(.alignleft,.alignright){display:table}.wp-block-co-authors-plus-image.aligncenter{display:table;margin-inline:auto}

</style>
<link rel='stylesheet' id='mediaelement-css' href='https://fivethirtyeight.com/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.17' media='all' />
<link rel='stylesheet' id='wp-mediaelement-css' href='https://fivethirtyeight.com/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=6.8.2' media='all' />
<style id='jetpack-sharing-buttons-style-inline-css'>
.jetpack-sharing-buttons__services-list{display:flex;flex-direction:row;flex-wrap:wrap;gap:0;list-style-type:none;margin:5px;padding:0}.jetpack-sharing-buttons__services-list.has-small-icon-size{font-size:12px}.jetpack-sharing-buttons__services-list.has-normal-icon-size{font-size:16px}.jetpack-sharing-buttons__services-list.has-large-icon-size{font-size:24px}.jetpack-sharing-buttons__services-list.has-huge-icon-size{font-size:36px}@media print{.jetpack-sharing-buttons__services-list{display:none!important}}.editor-styles-wrapper .wp-block-jetpack-sharing-buttons{gap:0;padding-inline-start:0}ul.jetpack-sharing-buttons__services-list.has-background{padding:1.25em 2.375em}
</style>
<style id='elasticpress-facet-style-inline-css'>
.widget_ep-facet input[type=search],.wp-block-elasticpress-facet input[type=search]{margin-bottom:1rem}.widget_ep-facet .searchable .inner,.wp-block-elasticpress-facet .searchable .inner{max-height:20em;overflow:scroll}.widget_ep-facet .term.hide,.wp-block-elasticpress-facet .term.hide{display:none}.widget_ep-facet .empty-term,.wp-block-elasticpress-facet .empty-term{opacity:.5;position:relative}.widget_ep-facet .empty-term:after,.wp-block-elasticpress-facet .empty-term:after{bottom:0;content:" ";display:block;left:0;position:absolute;right:0;top:0;width:100%;z-index:2}.widget_ep-facet .level-1,.wp-block-elasticpress-facet .level-1{padding-left:20px}.widget_ep-facet .level-2,.wp-block-elasticpress-facet .level-2{padding-left:40px}.widget_ep-facet .level-3,.wp-block-elasticpress-facet .level-3{padding-left:60px}.widget_ep-facet .level-4,.wp-block-elasticpress-facet .level-4{padding-left:5pc}.widget_ep-facet .level-5,.wp-block-elasticpress-facet .level-5{padding-left:75pt}.widget_ep-facet input[disabled],.wp-block-elasticpress-facet input[disabled]{cursor:pointer;opacity:1}.widget_ep-facet .term a,.wp-block-elasticpress-facet .term a{-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;position:relative}.widget_ep-facet .term a:hover .ep-checkbox,.wp-block-elasticpress-facet .term a:hover .ep-checkbox{background-color:#ccc}.ep-checkbox{-webkit-box-align:center;-ms-flex-align:center;-ms-flex-negative:0;-webkit-box-pack:center;-ms-flex-pack:center;align-items:center;background-color:#eee;display:-webkit-box;display:-ms-flexbox;display:flex;flex-shrink:0;height:1em;justify-content:center;margin-right:.25em;width:1em}.ep-checkbox:after{border:solid #fff;border-width:0 .125em .125em 0;content:"";display:none;height:.5em;-webkit-transform:rotate(45deg);transform:rotate(45deg);width:.25em}.ep-checkbox.checked{background-color:#5e5e5e}.ep-checkbox.checked:after{display:block}

</style>
<link rel='stylesheet' id='elasticpress-related-posts-block-css' href='https://fivethirtyeight.com/wp-content/mu-plugins/search/elasticpress/dist/css/related-posts-block-styles.min.css?ver=4.2.2' media='all' />
<style id='global-styles-inline-css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
:root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='gif-play-button-styles-css' href='https://fivethirtyeight.com/wp-content/plugins/gif-play-button/assets/css/gif-play-button.min.css?ver=1.1.2' media='all' />
<link rel='stylesheet' id='fte-css' href='https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/css/fiveThirtyEight.css?ver=1.1.2' media='' />
<link rel='stylesheet' id='fte-CCfonts-css' href='https://use.typekit.net/ktz4wdi.css?ver=1.1.2' media='' />
<style id='admin-announcements-inline-css'>
.st0, .st1 { fill: #fcdfc5; }
</style>
<script type="text/javascript" id="disney-oneid-js-extra">
/* <![CDATA[ */
var DisneyOneID = {"config":{"clientId":"DATG-FIVETHIRTYEIGHT.WEB","langPref":"en-US","debug":false,"responderPage":"https:\/\/fivethirtyeight.com\/oneid-responder","campaignName":"FiveThirtyEight"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://cdn.registerdisney.go.com/v4/OneID.js" id="disney-oneid-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/oneid.min.js?ver=1.1.2" id="disney-oneid-config-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/dtci-data-privacy/assets/js/adobe-datalayer.min.js?ver=1.1" id="dtci-datalayer-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/espn-social/assets/js/facebook.min.js?ver=1.1.2" id="facebook-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/espn-social/assets/js/twitter-prompt.min.js?ver=1.1.2" id="twitter-prompt-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/vendor/purify.min.js?ver=1.1.2" id="purify-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/underscore.min.js?ver=1.13.7" id="underscore-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/js/fivethirtyeightHeader.js?ver=1.1.2" id="fte-js"></script>
<script type="text/javascript" async="async" src="https://fivethirtyeight.com/wp-content/plugins/dtci-data-privacy/assets/js/twitter-platform.min.js" id="platform-twitter-js" defer></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/js/vendor/picturefill.min.js?ver=1.1.2" id="picturefill-js"></script>
<script type="text/javascript" id="abc-analytics-js-extra">
/* <![CDATA[ */
var ABCAnalytics = {"nielsen":{"asset_id":54447,"section":"politicspolling","seg_a":"","seg_b":"","seg_c":"","debug":""},"chartbeat":{"uid":"12240","domain":"fivethirtyeight.com","path":"\/features\/how-fivethirtyeight-calculates-pollster-ratings\/","sections":"politics,features","authors":"Nate Silver","title":"How FiveThirtyEight Calculates Pollster Ratings","loadPubJS":false,"loadVidJS":true},"gtm":{"id":"GTM-KLHT6T2"},"omniture":{"pageName":"politics:features:how-fivethirtyeight-calculates-pollster-ratings","prop1":"fivethirtyeight","prop2":"","prop5":"features","prop6":"Nate Silver","prop7":"politics","prop8":"politics:polling","prop12":"How FiveThirtyEight Calculates Pollster Ratings","prop13":"54447:How FiveThirtyEight Calculates Pollster Ratings","prop14":"","prop15":"https:\/\/fivethirtyeight.com\/features\/how-fivethirtyeight-calculates-pollster-ratings\/","prop16":"https:\/\/fivethirtyeight.com\/features\/how-fivethirtyeight-calculates-pollster-ratings\/","prop20":"Desktop","prop23":"2014 Midterms, Polling, Polls, Pollster Ratings, Senate Forecast","eVar5":"features","eVar6":"Nate Silver","eVar7":"politics","eVar8":"politics:polling","eVar9":"2014-09-25","eVar10":"13:54","eVar12":"How FiveThirtyEight Calculates Pollster Ratings","eVar13":"54447:How FiveThirtyEight Calculates Pollster Ratings","eVar14":"","eVar15":"https:\/\/fivethirtyeight.com\/features\/how-fivethirtyeight-calculates-pollster-ratings\/","eVar16":"https:\/\/fivethirtyeight.com\/features\/how-fivethirtyeight-calculates-pollster-ratings\/","eVar20":"Desktop","eVar21":null,"eVar22":null,"prop35":"2014-09-25"},"account":"wdgnewfivethirtyeight"};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-analytics/assets/js/analytics.min.js?ver=1.1.2" id="abc-analytics-js"></script>
<link rel="https://api.w.org/" href="https://fivethirtyeight.com/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://fivethirtyeight.com/wp-json/wp/v2/fte_features/54447" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://fivethirtyeight.com/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.8.2" />
<link rel='shortlink' href='http://53eig.ht/1pd8bmy' />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://fivethirtyeight.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffivethirtyeight.com%2Ffeatures%2Fhow-fivethirtyeight-calculates-pollster-ratings%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://fivethirtyeight.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffivethirtyeight.com%2Ffeatures%2Fhow-fivethirtyeight-calculates-pollster-ratings%2F&#038;format=xml" />
<meta name="color-scheme" content="only light" />
        <style>
        .getty.aligncenter {
            text-align: center;
        }
        .getty.alignleft {
            float: none;
            margin-right: 0;
        }
        .getty.alignleft > div {
            float: left;
            margin-right: 5px;
        }
        .getty.alignright {
            float: none;
            margin-left: 0;
        }
        .getty.alignright > div {
            float: right;
            margin-left: 5px;
        }
        </style>

<!-- Jetpack Open Graph Tags -->
<meta property="og:type" content="article" />
<meta property="og:title" content="How FiveThirtyEight Calculates Pollster Ratings" />
<meta property="og:url" content="https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/" />
<meta property="og:description" content="See FiveThirtyEight&#8217;s pollster ratings. Pollster ratings were one of the founding features of FiveThirtyEight. I was rating pollsters before I was building elec&#8230;" />
<meta property="article:published_time" content="2014-09-25T17:54:44+00:00" />
<meta property="article:modified_time" content="2014-09-25T17:54:44+00:00" />
<meta property="og:site_name" content="FiveThirtyEight" />
<meta property="og:image" content="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=712" />
<meta property="og:image:width" content="712" />
<meta property="og:image:height" content="532" />
<meta property="og:image:alt" content="" />
<meta property="og:locale" content="en_US" />
<meta property="article:author" content="https://facebook.com/natesilver" />
<meta name="twitter:text:title" content="How FiveThirtyEight Calculates Pollster Ratings" />
<meta name="twitter:image" content="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=640" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="article:publisher" content="https://www.facebook.com/fivethirtyeight" />
<meta property="fb:app_id" content="797620670264818" />
<meta property="fb:pages" content="687958677914631" />
<meta name="twitter:site" content="FiveThirtyEight" />
<meta name="twitter:site:id" content="2303751216" />
<meta name="twitter:widgets:csp" content="on" />
<meta name="twitter:maxage" content="300" />
<meta name="twitter:creator" content="natesilver538" />
<meta name="twitter:creator:id" content="16017475" />
<meta name="twitter:image:src" content="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=712" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="Nate Silver" />
<meta name="twitter:label2" content="Filed under" />
<meta name="twitter:data2" content="2014 Midterms, Polling, Polls, Pollster Ratings, Senate Forecast" />

<!-- End Jetpack Open Graph Tags -->
<meta name="DC.date.issued" content="2014-09-25T17:54:44+00:00" />
<meta name="description" content="See FiveThirtyEight&#8217;s pollster ratings. Pollster ratings were one of the founding features of FiveThirtyEight. I was rating pollsters before I was building elec&#8230;" />
<link rel='author' href='https://fivethirtyeight.com/contributors/nate-silver/' />
<link rel="alternate" type="application/rss+xml" title="Posts feed for Nate Silver" href="https://fivethirtyeight.com/contributors/nate-silver/feed/">
<link type="text/plain" rel="author" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/humans.txt" /><link rel='canonical' href='https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/' />
<script type='application/ld+json'>
{"@context":"http://schema.org","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/"},"headline":"How FiveThirtyEight Calculates Pollster Ratings","datePublished":"2014-09-25T13:54:44-04:00","dateModified":"2017-04-21T10:37:31-04:00","publisher":{"@type":"Organization","name":"FiveThirtyEight","logo":{"url":"https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/images/fivethirtyeight-logo-rich-snippets.png","height":60,"width":546,"@type":"ImageObject"}},"author":{"@type":"Person","name":"Nate Silver"},"articleSection":"Politics","image":{"@type":"ImageObject","url":"https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg","width":1000,"height":747}}
</script>
		<style type="text/css" id="wp-custom-css">
			section.viz {
background-color: #fff;
}
div.liveblog-entry-content>header.single-post-header{
display: none;
}		</style>
			<link rel="mask-icon" color="#ed713a" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/logo-fox-head-black.svg?v=1.1.2">
	<link rel="shortcut icon" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/favicon.ico?v=1.1.2">
	<link rel="apple-touch-icon" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/fivethirtyeight-logo-touch.png?v=1.1.2">
</head>
<body class="wp-singular fte_features-template-default single single-fte_features postid-54447 wp-theme-espn-fivethirtyeight vertical-politics slug-how-fivethirtyeight-calculates-pollster-ratings topic-slug-polling no-ads">

<a href="#content" class="skip-to-content-link visually-hidden">Skip to main content</a>
<i class="header-global-bground"></i>
<header class="header-global" id="header-global">
	<div class="site-wrapper header-global-top">
							<h2 class="header-global-logo">
							<a href="/" name="&amp;lpos=fivethirtyeight&amp;lid=Header Home" class="header-global-logo-link">
					<span class="visually-hidden">FiveThirtyEight</span>
					<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="163.451" viewBox="0 318.275 1280 163.451" class="site-logo" role="presentation"><path d="M0 318.275h76.009v24.323H27.363v30.403h45.606v24.323H27.363v51.687H0zm94.252 109.453h15.202v-54.727H94.252v-24.323h39.525v79.05h12.162v21.283H94.252v-21.283zm15.202-109.453h24.323v24.323h-24.323v-24.323zm434.774 109.453h15.202v-54.727h-15.202v-24.323h39.525v79.05h12.162v21.283h-51.686v-21.283zm15.202-109.453h24.323v24.323H559.43v-24.323zm401.33 109.453h15.202v-54.727H960.76v-24.323h39.525v79.05h12.161v21.283H960.76v-21.283zm15.202-109.453h24.323v24.323h-24.323v-24.323zm-811.781 82.09v-51.687h24.323v45.606l12.161 30.343h3.04l12.162-30.343v-45.606h24.323v51.687l-21.283 48.646h-33.444zm173.301 48.646h-41.288c-24.901 0-37.762-11.584-37.762-35.968v-27.88c0-23.016 13.074-39.525 39.525-39.525 28.367 0 39.525 15.415 39.525 42.565v21.283h-51.686v5.29c0 7.966 3.04 12.952 10.398 12.952h41.288v21.283zm-51.686-60.808h24.323v-4.713c0-7.966-3.223-16.57-12.557-16.57-8.483 0-11.766 6.689-11.766 16.57v4.713zm94.251-45.605h-30.403v-24.323h88.171v24.323h-30.404v106.413h-27.364zm234.11 106.413V348.678h24.323v12.161c3.466-7.449 11.401-12.161 21.952-12.161h8.452v24.323h-18.242c-8.635 0-12.161 2.858-12.161 11.857v64.152h-24.324zm130.736 0h-14.715c-21.617 0-30.89-11.219-30.89-33.9v-42.109h-18.242v-24.323h18.242v-21.283h24.323v21.283h21.283v24.323H723.61l-.213 42.353c0 6.75 2.828 12.374 11.128 12.374h10.368v21.282zm535.107 0h-14.715c-21.617 0-30.89-11.219-30.89-33.9v-42.109h-18.242v-24.323h18.242v-21.283h24.323v21.283H1280v24.323h-21.283l-.213 42.353c0 6.75 2.828 12.374 11.128 12.374H1280v21.282zm-506.953 32.714l14.016-28.883-23.928-52.477v-51.687h24.323v45.606l12.162 30.404h3.04l12.162-30.404v-45.606h24.323v51.687l-37.397 81.36zm90.421-163.45h76.009v24.323h-48.646v27.363h45.606v24.323h-45.606v30.404h48.646v24.323h-76.009zm161.14 145.938v-6.081h48.95c6.081 0 8.817-.547 8.817-3.861v-1.034c0-3.284-2.767-4.226-8.817-4.226h-39.829v-15.202l15.202-15.202c-16.084-4.5-24.323-16.509-24.323-33.444v-3.04c0-22.985 13.499-36.485 42.565-36.485a66.672 66.672 0 0 1 18.09 3.04l12.313-18.242 15.202 9.121-12.161 18.242c4.165 5.868 9.121 14.989 9.121 24.323v3.04c0 21.283-10.033 32.41-36.484 33.444l-9.121 12.161h18.242c17.999 0 27.363 7.966 27.363 23.35v.334c0 15.384-8.239 24.962-26.208 24.962h-39.525c-13.043.002-19.397-5.593-19.397-15.2zm57.767-76.01v-9.121c0-10.033-4.044-12.161-15.202-12.161-11.158 0-15.202 2.128-15.202 12.161v9.121c0 10.033 4.226 12.162 15.202 12.162s15.202-2.128 15.202-12.162zm72.969 60.808h-24.323V318.275h24.323v42.565c3.466-8.118 10.337-12.161 21.283-12.161 19.033 0 27.363 9.364 27.363 32.714v67.618h-24.323v-63.848c0-9.516-3.253-15.202-12.162-15.202-8.908 0-12.161 5.686-12.161 15.202v63.848zm-678.004 0h-24.323V318.275h24.323v42.565c3.466-8.118 11.888-12.161 22.772-12.161 19.033 0 25.874 9.516 25.874 32.867v67.466h-24.323v-66.888c0-9.516-3.253-13.499-12.161-13.499s-12.162 6.871-12.162 16.388v63.998z"/></svg>
					<img src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/logo-fox-head-color.svg" alt="FiveThirtyEight" width="57" height="55" class="site-logo-small" id="site-logo-small" />
				</a>
							</h2>

			<form action="https://fivethirtyeight.com/" method="get" id="searchform" class="search-form">
				<label for="search-field" class="search-form-label">Search</label>
				<div class="search-form-input-wrapper"><input type="search" name="s" id="search-field" class="search-form-input" placeholder="Search" tabindex="-1"></div>
				<input type="submit" value="Search" class="search-form-submit" tabindex="-1">
				<button aria-label="Search" class="search-button" id="search-button" aria-expanded="false">
					<span class="visually-hidden">Search</span>
				</button>
			</form>

<a href="https://abcnews.go.com/" rel="noopener" title="ABC News" target="_blank" class="header-espn-link" name="&amp;lpos=fivethirtyeightHeader&amp;lid=Header ABC News">
				<svg width="65" height="23" xmlns="http://www.w3.org/2000/svg" role="presentation"><path d="M25.089 6.709c-.47-.496-.974-.798-1.322-.798h-.313v-.275h.261c.121 0 1.548.058 1.687.058.227 0 .886-.058 1.026-.058h.278l6.618 7.345V7.187c0-.921-.4-1.276-1.407-1.276h-.296v-.275h.313c.035 0 1.529.058 1.65.058.173 0 1.164-.058 1.355-.058h.192l.017.275c-.922.071-1.165.32-1.165 1.135v9.16h-.312l-7.904-8.77v6.6c0 1.384.314 1.756 1.46 1.756h.295v.296h-.331c-.243 0-1.441-.06-1.72-.06-.156 0-1.269.06-1.512.06h-.279v-.296c1.166-.107 1.41-.302 1.41-1.153v-7.93h-.001zm11.98.106c0-.691-.261-.904-1.079-.904h-.26v-.275h.678c.47 0 3.008.058 3.026.058.364 0 2.777-.058 3.296-.058h.695l.035 2.277h-.27c-.053-1.188-.58-1.667-1.795-1.667h-2.43v4.026h2.1c.816 0 1.268-.39 1.389-1.225l.31.018v3.178h-.293c-.138-.993-.642-1.383-1.857-1.383h-1.666v3.672c0 .603.296.905.885.905h1.736c1.126 0 1.944-.515 2.43-1.58h.314l-.731 2.23c-.505 0-2.898-.058-3.696-.058-.539 0-3.13.04-3.722.058h-.452v-.295h.278c.818-.017 1.08-.23 1.08-.923V6.815zm16.701 9.41h-.487l-1.984-5.511-2.035 5.512h-.47L45.4 6.975c-.26-.71-.505-.993-.957-1.08v-.26h.296c.191 0 1.149.059 1.375.059.191 0 1.182-.058 1.391-.058h.314v.275c-.505.019-.714.16-.714.443 0 .16.052.39.14.639l2.383 6.557 1.357-3.74-.887-2.516c-.383-1.081-.714-1.364-1.55-1.383v-.275h.28c.243 0 1.496.058 1.793.058.242 0 1.495-.058 1.773-.058h.417v.275h-.417c-.574 0-.852.142-.852.443 0 .16.07.444.174.727l2.314 6.522 1.827-5.53c.226-.709.33-1.17.33-1.453 0-.496-.243-.71-.782-.71h-.313v-.274h.087c.243 0 .851.058 1.217.058.173 0 .851-.058 1.18-.058h.123v.275c-.436.125-.66.443-1.007 1.525l-2.923 8.79zm4.01-2.563c.278.688.52 1.008.988 1.361.59.46 1.37.69 2.237.69 1.491 0 2.497-.796 2.497-1.946 0-.85-.486-1.31-2.282-2.175-1.74-.85-2.174-1.274-2.538-1.628-.537-.584-.762-1.114-.762-1.822 0-1.627 1.3-2.704 3.265-2.704.592 0 1.236.088 1.933.264.278.07.557.106.714.106.138 0 .209-.035.26-.153h.3l.034 2.229h-.247c-.156-.531-.26-.76-.487-1.05-.488-.585-1.254-.903-2.237-.903-1.248 0-2.064.601-2.064 1.504 0 .778.47 1.22 2.134 1.998 2.134 1.008 3.426 1.911 3.426 3.573 0 1.91-1.537 3.2-3.807 3.2a8.04 8.04 0 0 1-1.838-.229 3.676 3.676 0 0 0-.624-.089c-.209 0-.277.036-.415.2h-.295l-.035-.248c-.118-.7-.258-1.398-.418-2.09l.261-.089zM3.97 9.732c-.262 0-.51.06-.73.168-.587.291-.957.89-.955 1.546 0 .946.755 1.714 1.684 1.714.931 0 1.684-.768 1.684-1.714 0-.947-.753-1.715-1.684-1.715zm7.259 0c-.93 0-1.685.767-1.685 1.714 0 .946.754 1.714 1.685 1.714.93 0 1.684-.768 1.684-1.714 0-.947-.755-1.715-1.684-1.715z"/><path d="M18.47 14.875c-1.862 0-3.37-1.535-3.37-3.43 0-1.893 1.508-3.428 3.37-3.428 1.596 0 2.932 1.132 3.28 2.65h-1.78a1.68 1.68 0 0 0-1.5-.936c-.932 0-1.686.768-1.686 1.715 0 .946.754 1.714 1.685 1.714a1.68 1.68 0 0 0 1.502-.94l1.783-.017c-.339 1.53-1.68 2.672-3.285 2.672zm-7.241 0c-1.853 0-3.356-1.522-3.369-3.405l-.04-6.016h1.704l.01 3.228c.499-.396 1.077-.665 1.695-.665 1.86 0 3.368 1.535 3.368 3.429s-1.509 3.429-3.368 3.429zm-5.546 0l-.007-.859c-.382.389-1.043.859-1.824.859-1.86 0-3.251-1.535-3.251-3.43 0-1.893 1.508-3.428 3.368-3.428.29 0 .573.037.843.108 1.453.38 2.526 1.723 2.526 3.32v.01l.02 3.42H5.682zM11.229.017C5.027.017 0 5.134 0 11.446s5.027 11.43 11.229 11.43c6.2 0 11.228-5.118 11.228-11.43 0-6.312-5.028-11.429-11.228-11.429z"/></svg>
				<span class="visually-hidden">ABC News</span>
			</a>

<button class="nav-global-toggle" id="nav-global-toggle" aria-expanded="false">Menu</button>

</div>
			<div class="single-sticky">

							<div class="single-sticky-vertical"></div>
				<div class="single-sticky-title">
											How FiveThirtyEight Calculates Pollster Ratings									</div>
				<a href="https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/?share=facebook" class="button share-sticky sticky-facebook">Share on Facebook</a>
				<a href="https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/?share=twitter"  class="button share-sticky sticky-twitter">Share on Twitter</a>

			</div>
			<div class="site-wrapper header-global-bottom" role="dialog" aria-label="Main menu">
		<nav class="nav-global" id="nav-global">
			<ul class="nav-global-menu">
				<li class="nav-global-menu-item menu-politics -current-vertical">
					<a
						href="https://fivethirtyeight.com/politics/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Politics"
						aria-current=page					>
						Politics					</a>
				</li>
				<li class="nav-global-menu-item menu-sports">
					<a
						href="https://fivethirtyeight.com/sports/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Sports"
											>
						Sports					</a>
				</li>
				<li class="nav-global-menu-item menu-science">
					<a
						href="https://fivethirtyeight.com/science/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Science"
											>
						Science					</a>
				</li>
				<li class="nav-global-menu-item menu-podcast">
					<a
						href="https://fivethirtyeight.com/podcasts/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Podcasts"
											>
						Podcasts					</a>
				</li>
				<li class="nav-global-menu-item menu-video">
					<a
						href="https://fivethirtyeight.com/videos/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Video"
											>
						Video					</a>
				</li>
				<li class="nav-global-menu-item menu-interactive">
					<a
						href="https://projects.fivethirtyeight.com/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Interactives"
					>
						Interactives					</a>
				</li>
				<li class="nav-global-menu-item menu-abcn -mobile-only">
					<a href="https://abcnews.go.com/" rel="noopener" name="&amp;lpos=fivethirtyeightHeader&amp;lid=Header ABC News">
						ABC News					</a>
				</li>
			</ul>

</nav><!-- #nav-global -->
		</div><!-- .site-wrapper -->
</header><!-- #header-global -->

<div class="site-main">
	<div id="wrapper" class="site-wrapper">
<div class="espn-announcement-banner"
			style="background-color: #dd9933;"
		>

<a href="http://abcnews.com/538" class="banner-content">

		<div class="banner-icon lightning">
			<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 100 100"><path class="st0" d="M78.8 26.6c-.5-.5-1.3-.9-2-.9-.2 0-.5.1-.7.1l-23.7 5.9L62.6 3.9c.2-.4.3-.7.3-1.1 0-1.4-1.2-2.5-2.7-2.5H40.6c-1.3 0-2.3.8-2.6 1.9L26 51.6c-.2.8.1 1.7.8 2.3.5.4 1.2.7 1.9.7.2 0 .5 0 .7-.1l24.3-6.1-11.9 48.5c-.3 1.3.5 2.5 1.8 2.9.3.1.6.1.8.1 1.1 0 2-.6 2.5-1.5l32.3-69.3c.5-.8.3-1.8-.4-2.5"/></svg>		</div>

<div class="banner-content-text">This is an archived site and is no longer being updated. New 538 articles can be found at www.abcnews.com/538.</div>

<div class="banner-icon chevron">
			<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 100 100"><path class="st1" d="M83.5 50c0-.8-.4-1.7-1-2.3L36.1 1.3c-.6-.6-1.5-1-2.3-1-.8 0-1.7.4-2.3 1l-5 5c-.6.6-1 1.5-1 2.3 0 .8.4 1.7 1 2.3L65.6 50 26.5 89.1c-.6.6-1 1.5-1 2.3 0 .9.4 1.7 1 2.3l5 5c.6.6 1.5 1 2.3 1 .8 0 1.7-.4 2.3-1l46.4-46.4c.6-.6 1-1.5 1-2.3"/></svg>		</div>
		</a>

</div>

<div id="content" class="single single-feature" data-col="2">

<div class="single-feature__row">
			<div id="primary" class="single-feature__col">
				<div id="article-main">
					<article id="post-54447" class="post-54447 fte_features type-fte_features status-publish has-post-thumbnail hentry tag-2014-midterms tag-polling tag-polls tag-pollster-ratings tag-senate-forecast espn_verticals-politics vertical-politics topic-slug-polling">

<header class="post-info single-post-header">
														<p class="topic single-topic">
								<time class="datetime">Sep. 25, 2014</time>,
								at
								<time class="datetime updated" title="2014-09-25T17:54:44+00:00">1:54 PM</time>

</p>

							<div class="single-header">
								<h1 class="article-title article-title-single entry-title">
									How FiveThirtyEight Calculates Pollster Ratings								</h1>

</div>

<div class="single-header-metadata-and-share-wrap">
								<div class="single-header-metadata-wrap">
																			<p class="single-metadata single-byline vcard">By <a href="https://fivethirtyeight.com/contributors/nate-silver/" title="" class="author url fn" rel="author">Nate Silver</a></p>

																		<p class="single-metadata single-topic">Filed under <a href="https://fivethirtyeight.com/tag/polling/" class="term " name="">Polling</a></p>

											<p class="single-metadata single-data-source">
					<span class='gh-a'>Get the data on <a target="_blank" href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings">GitHub</a></span>
			<span class='gh-b'>GitHub data at <a target="_blank" href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings">data/pollster-ratings</a></span>
			</p>

</div>
								<div class="share">
																	</div> <!-- .share -->
							</div>

</header><!-- .post-info -->

<figure id="single-featured-image" class="single-featured-image banner">
	<span class="has-bugs post-thumbnail">
					<div class="bug-container">
				<picture class="featured-picture">
											<source media="(min-width: 768px)" srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/lede_poll.jpg">

											<source srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=575 1x, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=1150 2x">
						<img width="575" height="430" src="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?w=575" class="attachment-lede size-lede" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg 1000w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=768,574 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=683,510 683w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=575,430 575w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=600,448 600w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=348,260 348w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=214,160 214w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=771,576 771w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2014/09/banner_poll.jpg?resize=920,687 920w" sizes="(max-width: 575px) 100vw, 575px" />									</picture>

</div>

</span><!-- .has-bugs -->

<figcaption class="caption banner-caption">
										<p class="credits">Illustration by Matt Chase</p>
					</figcaption>

				<figcaption class="caption featured-image-caption">
													<p class="credits">Illustration by Matt Chase</p>
							</figcaption>

</figure><!-- .single-featured-image -->

						<div class="entry-content single-post-content">
							<p><em>See <a href="https://fivethirtyeight.com/interactives/pollster-ratings/" target="_blank" rel="noopener noreferrer">FiveThirtyEight’s pollster ratings</a>.</em></p>
<p>Pollster ratings were one of the founding features of FiveThirtyEight. I was <a href="https://fivethirtyeight.com/features/pollster-ratings-updated/">rating pollsters</a> before I was building election models. I was <a href="https://fivethirtyeight.com/features/pollster-ratings-v31/">eagerly updating the ratings</a> after every major batch of election results. I rated pollsters while walking two miles uphill … barefoot … in the snow. And then I got a little burned out on them. We last issued a <a href="https://fivethirtyeight.com/features/pollster-ratings-v40-methodology/">major set of pollster ratings in June 2010</a> and made only a cursory update before the 2012 elections.</p>
<p>What happened? Well, when you publish a set of pollster ratings, people are understandably fixated upon how you’ve rated the individual polling firms: Is Pollster XYZ better than Pollster PDQ?</p>
<p>Naturally, we hope the pollster ratings can give you a better basis for understanding the polls as a news consumer. However, discussions about individual polling firms — there are now more than 300 of them in our database — can sometimes miss the point. I’m more interested in the big-picture questions. Are some pollsters consistently better than others, as measured by how accurately they predict election results? In other words, is pollster performance predictable? And if so, are a pollster’s past results the better predictor — or are its methodological standards more telling?</p>
<p>The short answer is that pollster performance is predictable — to some extent. Polling data is noisy and bad pollsters can get lucky. But pollster performance is predictable on the scale of something like the batting averages of Major League Baseball players.</p>
<p>Let me take that analogy a bit further. In baseball, there isn’t much difference in an absolute sense between a .300 hitter and a .260 hitter — it amounts to getting about one extra hit during each week of the baseball season. Likewise, the differences in poll accuracy aren’t that large. We estimate that the very best pollsters might be about 1 percentage point more accurate than the average pollster over the long run. However, the average poll in our database missed the final election outcome by 5.3 percentage points. That means even the best poll would still be off by 4.3 points. It’s almost always better to take an average of polls rather than hoping for any one of them to “<a href="http://www.huffingtonpost.com/mark-blumenthal/hitting_a_bullet_with_a_bullet_b_725707.html">hit a bullet with a bullet</a>.”</p>
<p>What about the very worst pollsters? Well, we estimate that the absolute worst ones might introduce 2 to 3 points of error, as compared with average polls, based on poor methodology. That means that the worst polls are worse (further below average) than the best polls are good (above average). While there are intrinsic limits to how accurate any poll can be (because of <a href="http://en.wikipedia.org/wiki/Sampling_error">sampling error</a> and other factors), there is no shortage of ways to screw up.</p>
<p>But just as most baseball players hit somewhere around .260, most pollsters tend to be about average. Or at least, that’s the best guess we can make based on examining their past results. Poll accuracy statistics, like batting averages, take a long time to converge to the mean. You shouldn’t assume a polling firm is awesome just because it nailed the most recent election any more than you should mistake a shortstop who went 2-for-5 one day for a .400 hitter.</p>
<p>Nonetheless, when you aggregate results over a number of elections and the sample sizes become larger, you’ll find that there is some consistency in pollster performance.</p>
<p>Before we go any further, I’d encourage you to <a href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings" target="_blank" rel="noopener noreferrer">download the database of polls that we’ve used to construct the pollster ratings</a>. We’re making it public for the first time. The database includes (with just a few minor exceptions that I’ll describe below) every poll conducted in the last three weeks of a presidential, U.S. Senate, U.S. House or gubernatorial campaign since 1998, along with polls in the final three weeks of presidential primaries and caucuses since 2000. Test everything out for yourself — probably you’ll agree with some elements of our approach and disagree with others. Better yet, maybe you’ll discover a bunch of cool things that we hadn’t thought to look for. We think <a href="https://fivethirtyeight.com/features/why-arent-there-more-pollster-ratings/">there should be more pollster ratings</a> — FiveThirtyEight shouldn’t have the last word on them.</p>
<p>Perhaps the simplest measure of poll accuracy is how far the poll’s margin was from the actual election result. For instance, if a poll had the Democrat ahead by 10 percentage points and she actually won by 3 points, that would represent a 7-point error. In the table below, I’ve listed polling firms’ average error for elections from 1998 through 2007, and again for the same polling firms for elections from 2008 onward. (About half the polls in our database are from 2008 or later, so this is a logical dividing point.) I’ve restricted the list to the 28 firms with at least 10 polls in both halves of the sample.</p>
<p><img decoding="async" class="size-full wp-image-54593" src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png" alt="silver-pollster-ratings-table-1" width="610" height="967" srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=47,75 47w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=189,300 189w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=768,1217 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=646,1024 646w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=969,1536 969w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=323,512 323w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=273,432 273w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=222,352 222w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=142,225 142w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=284,450 284w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=164,260 164w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=101,160 101w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=363,576 363w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=98,155 98w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=63,100 63w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=38,60 38w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=433,687 433w" sizes="(max-width: 610px) 100vw, 610px" data-sizes="(max-width: 610px) 100vw, 610px" data-src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png" data-srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=47,75 47w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=189,300 189w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=768,1217 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=646,1024 646w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=969,1536 969w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=323,512 323w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=273,432 273w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=222,352 222w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=142,225 142w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=284,450 284w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=164,260 164w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=101,160 101w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=363,576 363w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=98,155 98w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=63,100 63w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=38,60 38w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-12.png?resize=433,687 433w"></p>
<p>As you can see, there’s a fair amount of consistency in these results; the <a href="http://mathworld.wolfram.com/CorrelationCoefficient.html">correlation coefficient</a> (where 1 is a perfect correlation and 0 is no correlation) is about 0.6. InsiderAdvantage and American Research Group were among the least accurate pollsters in both halves of the sample; polls from ABC News and The Washington Post (who usually conduct polls jointly) were among the most accurate in both cases. (ABC News, like ESPN and FiveThirtyEight, is owned by the Walt Disney Company.)</p>
<p>But there are a number of other things we’ll want to account for. In particular, we’ll want to know how much of the error had to do with circumstantial factors. For instance, <a href="https://fivethirtyeight.com/features/is-the-polling-industry-in-stasis-or-in-crisis/">polls of presidential primaries are associated with much more error</a> than polls of general elections. This is a consequence of factors intrinsic to primaries (for instance, turnout is far lower) and mostly isn’t the pollsters’ fault. One more baseball analogy: Polling primaries is like hitting in Dodger Stadium against Clayton Kershaw, whereas polling general elections is like hitting in Coors Field.</p>
<p>How do we account for factors like these? It takes some work — the balance of this article will be devoted to describing our process. This year, we’re publishing <a href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings" target="_blank" rel="noopener noreferrer">a variety of different versions of the pollster ratings</a> that range from simple to more complex. If at any point you think we’ve made one assumption too many, you can take the exit ramp and use one of the simpler versions. Or you can download the raw data and construct your own.</p>
<p>Our overall method is <a href="https://fivethirtyeight.com/features/pollster-ratings-v40-methodology/">largely the same as in 2010</a>. That year, for the first time, we introduced a consideration of a poll’s methodological standards in addition to its past accuracy. We think the case for doing so has probably grown stronger since then, but you can find a number of versions of the pollster ratings based on past accuracy alone if you prefer them.</p>
<p>There are also a few things I’ve come to think about differently since 2010.</p>
<p><b>First, the case against Internet-based polls has grown much weaker in the last four years.</b> At that time, the <a href="https://fivethirtyeight.com/features/zogby-broke-internet-but-it-can-be/">most prominent Internet pollster was Zogby Interactive</a> (it has since been re-branded as JZ Analytics), which used a poor methodology and got <a href="https://fivethirtyeight.com/features/worst-pollster-in-world-strikes-again/">equally poor results</a>. But Internet penetration has increased considerably since then (<a href="http://massnumbers.blogspot.com/2014/09/the-rise-of-internet-pollingmore-adults.html">it now exceeds landline telephone penetration</a>) and a number of Internet-based polling firms with more thoughtful methodologies have come along. In 2012, the Internet-based polls <a href="https://fivethirtyeight.com/features/which-polls-fared-best-and-worst-in-the-2012-presidential-race/">did a little better than the telephone polls as a group</a> (especially compared to telephone polls that did not call cellphones). There are still some reasons to be skeptical of Internet polls — especially those that do not use <a href="http://www.people-press.org/methodology/sampling/why-probability-sampling/">probability sampling</a>. But the FiveThirtyEight pollster ratings no longer include an explicit penalty for Internet polls<span class="espn-footnote-link" data-footnote-id="1" data-footnote-url="#fn-1" data-footnote-content="&lt;p&gt;The pollster ratings do include a consideration of whether a polling firm calls cellphones, which Internet polls (since they don’t place phone calls at all) do not. However, they are treated the same as other polls that do not place calls to cellphones.&lt;/p&gt;
"><sup id="ss-1">1</sup></span> as they did in 2010.</p>
<p><b>Second, it has become harder to distinguish a “partisan” poll.</b> As I <a href="https://fivethirtyeight.com/features/senate-update-alaska-a-frontier-for-bad-polling/">described earlier this month</a>, FiveThirtyEight has been applying a more relaxed standard for what we define as “partisan” polls since 2012. The challenge in trying to use a more restrictive standard had been that there were too many borderline cases — and we didn’t like having to make a lot of ad hoc decisions about which polls to include. Some polling firms, like Public Policy Polling, conduct polls on behalf of interest groups and campaigns but pay for others themselves. Blogs like <a href="http://www.dailykos.com/">Daily Kos</a> and <a href="http://www.redracinghorses.com/">Red Racing Horses</a> now sponsor polls. And in some cases, it isn’t clear who’s paying for a poll. Only the most unambiguously partisan polls — those sponsored by candidates or by party groups like the Republican National Committee — are excluded from the FiveThirtyEight forecast models.</p>
<p>But we still keep track of polls even when we don’t use them in our forecast models — and their results are reflected in the pollster ratings. These polls are labeled with a partisan “flag” in the database.<span class="espn-footnote-link" data-footnote-id="2" data-footnote-url="#fn-2" data-footnote-content="&lt;p&gt;Be careful about coming to too many conclusions based on the way we have these polls labeled. They reflect the standard applied by FiveThirtyEight at the time the poll was added to the database — we haven’t gone back and reclassified older polls according to our current standard.&lt;/p&gt;
"><sup id="ss-2">2</sup></span> The idea is that a polling firm ought to be held accountable for any poll it puts out for public consumption. If a polling firm releases biased and inaccurate polls on behalf of candidates, that will be reflected in its pollster rating — even if it does better work when conducting polls on behalf of a media organization.</p>
<p>Our pollster ratings database also includes a couple of ways for you to track potential bias in the polls. The term<b> bias</b> itself refers to how much a polling firm’s results have erred toward one party or the other as compared against actual election results. <b>House effect</b>, by contrast, refers to how a firm’s results compare against other polls. If Pollster PDQ had the Democrat ahead by 5 points in an election where every other pollster had the race tied, it would have a Democratic house effect. But if the Democrat turned out to win by 10 points, PDQ would have a Republican bias as compared against the actual election results. As is the case for measures of poll accuracy, measures of bias and house effects can sometimes reflect statistical noise rather than anything systematic. But if they occur over dozens or hundreds of surveys, they should be a concern.</p>
<p><b>Third, we’re seeing clearer evidence of pollster “herding.” </b>Herding is the tendency of some polling firms to be influenced by others when issuing poll results. A pollster might want to avoid publishing a poll if it perceives that poll to be an outlier. Or it might have a poor methodology and make ad hoc adjustments so that its poll is more in line with a stronger one.</p>
<p>The problem with herding is that it reduces polls’ independence. One benefit of aggregating different polls is that you can account for any number of different methods and perspectives. But take the extreme case where there’s only one honest pollster in the field and a dozen herders who look at the honest polling firm’s results to calibrate their own. (For instance, if the honest poll has the Democrat up by 6 points, perhaps all the herders will list the Democrat as being ahead by somewhere between 4 and 8 points.) In this case, you really have just one poll that provides any information — everything else is just a reflection of its results. And if the honest poll happens to go wrong, so will everyone else’s results.<span class="espn-footnote-link" data-footnote-id="3" data-footnote-url="#fn-3" data-footnote-content='&lt;p&gt;Furthermore, many common statistical measurements like the normal distribution are &lt;a href="http://en.wikipedia.org/wiki/Central_limit_theorem"&gt;predicated on the notion of independent or random trials&lt;/a&gt;. These assumptions may be violated if pollsters are not behaving independently from one another.&lt;/p&gt;
'><sup id="ss-3">3</sup></span></p>
<p>There’s reasonably persuasive evidence that herding has occurred in <a href="https://fivethirtyeight.com/features/are-bad-pollsters-copying-good-pollsters/">polls of Senate elections</a>, <a href="http://www.vanderbilt.edu/csdi/research/CSDI_WP_04-2012.pdf">presidential primaries</a> and the <a href="http://votamatic.org/pollsters-may-be-herding/">most recent presidential general election</a>. It <a href="https://fivethirtyeight.com/features/are-bad-pollsters-copying-good-pollsters/">seems to be more common</a> among pollsters that take methodological shortcuts.</p>
<p>Paradoxically, while herding may make an individual polling firm’s results more accurate, it can make polling averages worse. There’s some tentative evidence that this is already happening. From our polling database, I compared two quantities: First, how accurate the average individual poll was; and second, how accurate the polling average was.<span class="espn-footnote-link" data-footnote-id="4" data-footnote-url="#fn-4" data-footnote-content="&lt;p&gt;To be clear about the difference: Imagine in a race where the Republican won by 10 points, one poll had the Republican ahead by 5 points and another had her ahead by 15. The average poll was off by 5 percentage points. But the polling average, which showed a 10-point lead for the Republican, was exactly right.&lt;/p&gt;
"><sup id="ss-4">4</sup></span> I limited the analysis to general election races where at least three polls had been conducted.</p>
<p>From 1998 through 2007, the average poll in these races missed the final margin by 4.7 percentage points. The average error has been somewhat lower — 4.3 percentage points — in races from 2008 onward.</p>
<p>But the polling average hasn’t gotten any better — if anything it’s gotten slightly worse. From 1998 through 2007, the polling average missed the final margin in an election by an average of 3.7 percentage points. Since 2008, the error has been 3.9 percentage points instead.</p>
<p>So this is something we’re concerned about — the benefit of aggregating polls together will decline if herding behavior continues to increase. This year’s pollster ratings introduce a couple of attempts to account for such behavior.</p>
<p>Now let’s get into the details — what follows is a reasonably comprehensive description of how we calculate the pollster ratings.</p>
<h2>Step 1: Collect and classify polls</h2>
<p>Almost all of the work is in this step; we’ve spent hundreds of hours over the years collecting polls. The ones represented in the <a href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings" target="_blank" rel="noopener noreferrer">pollster ratings database</a> meet three simple criteria:</p>
<ul>
<li>They were conducted in 1998 or later;</li>
<li>They were conducted in the final three weeks of the campaign;</li>
<li>They were conducted in one of the following types of elections:
<ul>
<li>Presidential general elections;</li>
<li>Presidential primaries;</li>
<li>Senate elections;</li>
<li>Gubernatorial elections;</li>
<li>U.S. House elections.</li>
</ul>
</li>
</ul>
<p>Of course, it’s not quite <i>that</i> simple; a number of other considerations come up from time to time:</p>
<ul>
<li>Sample sizes are sometimes missing from older polls. In these cases, we’ve estimated a poll’s sample size from its reported margin of error or from how many people a polling firm surveyed in other polls where the sample size was listed.<span class="espn-footnote-link" data-footnote-id="5" data-footnote-url="#fn-5" data-footnote-content="&lt;p&gt;For example, if a certain polling firm usually conducts 800-person polls, we’d list that as the sample size in a case where it was unreported.&lt;/p&gt;
"><sup id="ss-5">5</sup></span> As a last resort, we use 600 as a default sample size.</li>
<li>If a pollster listed results among likely voters and registered voters (or all adults), we list only the likely voter version in the database. Because the database covers the final three weeks of the campaign and almost all polling firms publish likely voter polls by that time, almost all polls in the database should be likely voter surveys.</li>
<li>When a pollster publishes multiple versions of the same survey (for example, versions of the poll with and without a third-party candidate included), FiveThirtyEight’s policy is to average the versions together. However, some of the polls in our database were taken from sources that may have followed different rules, so the treatment of these cases may be inconsistent.</li>
<li>Polls of special elections are included.</li>
<li>Polls of <a href="http://en.wikipedia.org/wiki/Nonpartisan_blanket_primary">nonpartisan primaries</a> (such as in Louisiana) are included.<span class="espn-footnote-link" data-footnote-id="6" data-footnote-url="#fn-6" data-footnote-content="&lt;p&gt;Polls of single-party primaries are not included except in the case of presidential primaries and caucuses.&lt;/p&gt;
"><sup id="ss-6">6</sup></span></li>
<li>National polls for the presidential popular vote and the generic congressional ballot are included.<span class="espn-footnote-link" data-footnote-id="7" data-footnote-url="#fn-7" data-footnote-content="&lt;p&gt;The accuracy of generic congressional ballot polls is evaluated in comparison to the aggregate popular vote for the U.S. House.&lt;/p&gt;
"><sup id="ss-7">7</sup></span></li>
<li>The use of tracking polls is restricted to non-overlapping dates. For instance, if a firm’s final tracking poll was conducted on the Friday through the Sunday before an election, we wouldn’t also list the version that covered Thursday through Saturday.</li>
<li>Polls are included in the database even if they were not used in the FiveThirtyEight forecasts.<span class="espn-footnote-link" data-footnote-id="8" data-footnote-url="#fn-8" data-footnote-content='&lt;p&gt;For example, polls from Strategic Vision are not used in FiveThirtyEight’s forecasts because there is &lt;a href="https://fivethirtyeight.com/features/strategic-vision-polls-exhibit-unusual/"&gt;strong evidence that the firm’s results were fabricated&lt;/a&gt;.&lt;/p&gt;
'><sup id="ss-8">8</sup></span></li>
<li>A poll’s date as listed in the database reflects the median date the poll was in the field — not the date the poll was released. For example, a poll conducted from Oct. 20 to Oct. 22 and released on Oct. 25 would have its date listed as Oct. 21.</li>
<li>Although in general all polls within the final three weeks of a campaign are included, there are minor exceptions in the case of the presidential primaries. No polls of the New Hampshire primary are included until after the Iowa caucus has been completed, and no polls of states beyond New Hampshire are included until New Hampshire has voted.<span class="espn-footnote-link" data-footnote-id="9" data-footnote-url="#fn-9" data-footnote-content="&lt;p&gt;For primaries, we also exclude polls if one of the leading candidates dropped out between the date of the poll and the date of the election.&lt;/p&gt;
"><sup id="ss-9">9</sup></span></li>
</ul>
<p>Sources for the data include previous iterations of FiveThirtyEight, along with <a href="http://elections.huffingtonpost.com/pollster">HuffPost Pollster</a>, <a href="http://www.realclearpolitics.com/">Real Clear Politics</a>, <a href="http://www.pollingreport.com/">PollingReport.com</a>, the <a href="https://archive.org/index.php">Internet Archive</a>, and searches of Google News and other newspaper archives. They also include data sent to us by various polling firms — however, we have sought to verify that such polls were in fact released to the public in advance of each election<span class="espn-footnote-link" data-footnote-id="10" data-footnote-url="#fn-10" data-footnote-content="&lt;p&gt;There are no private, internal polls in the database.&lt;/p&gt;
"><sup id="ss-10">10</sup></span> and that the pollster did not cherry-pick the results sent to us.</p>
<p>We’ve chosen 1998 as the cutoff point because there are multiple sources covering that election onward, meaning that the data ought to be reasonably comprehensive. Nevertheless, we’re certain that there are omissions from the database. We’re equally certain that there are any number of errors — some that were included in the original sources, and some that we’ve introduced ourselves. We’re hoping that releasing the data publicly will allow people to check for potential errors and omissions.<span class="espn-footnote-link" data-footnote-id="11" data-footnote-url="#fn-11" data-footnote-content="&lt;p&gt;However, we are not likely to release another major version of the database until the 2014 elections are complete. Minor errors and omissions should not make much difference to the overall pollster ratings. For firms with dozens or hundreds of polls in the database, a couple of missing (or incorrect) polls should make little difference in the average results. For firms with fewer polls, the pollster ratings are regressed heavily to the mean, so one or two polls likewise won’t have much impact.&lt;/p&gt;
"><sup id="ss-11">11</sup></span></p>
<p>A big challenge comes in how to identify the pollster we associate with each survey. For instance, Marist College has recently begun to conduct polls for NBC News. Are these classified as Marist College polls, NBC News polls, NBC/Marist polls, or something else?</p>
<p>The answer is that they’re Marist College polls. Our policy is to classify the poll with the pollster itself rather than the media sponsor.</p>
<p>However, a few media companies like CBS News and The New York Times have in-house polling operations.<span class="espn-footnote-link" data-footnote-id="12" data-footnote-url="#fn-12" data-footnote-content="&lt;p&gt;If you see a poll listed with a media organization in the database, it’s because it has an in-house polling operation or because we were unable to identify the polling firm responsible for the underlying work.&lt;/p&gt;
"><sup id="ss-12">12</sup></span> Confusingly, media companies sometimes also act as the sponsors of polls conducted by other firms. Our goal is to associate the poll with the company that, in our estimation, contributed the most intellectual property to the survey’s methodology. For instance, the <a href="http://www.nytimes.com/2014/07/28/upshot/explaining-online-panels-and-the-2014-midterms.html">set of polls</a> conducted earlier this year by YouGov for CBS News and The New York Times are classified as YouGov polls, not CBS News/New York Times polls.<span class="espn-footnote-link" data-footnote-id="13" data-footnote-url="#fn-13" data-footnote-content="&lt;p&gt;Media organizations with longstanding polling partnerships — like CBS News and The New York Times or ABC News and The Washington Post — sometimes release polls that are sponsored by just one of the partners. For instance, The Washington Post sometimes conducts polls of Maryland and Virginia that are not co-branded with ABC News. We still classify these together with other ABC News/Washington Post polls. On the other hand, news organizations sometimes switch polling partners. For instance, most Fox News polls were conducted by Opinion Dynamics Corp. through early 2011; since then, they’ve been conducted jointly by Anderson Robbins Research and Shaw &amp;amp; Company Research. Those polls are treated as distinct series.&lt;/p&gt;
"><sup id="ss-13">13</sup></span></p>
<p>Polling firms sometimes operate under multiple brand names and add or subtract partners. Some cases are reasonably clear — for instance, Rasmussen Reports is a subsidiary of <a href="http://www.pulseopinionresearch.com/">Pulse Opinion Research</a>, so polls marketed under each name are classified together. Other cases are more ambiguous; we’ve simply had to apply our best judgment about where one polling firm ends and another begins.</p>
<p>In previous versions of the pollster ratings, we included separate entries for telephone and Internet polls from the same company — for instance, <a href="http://www.ipsos.com/">Ipsos</a> conducts both types of polls and they’re listed separately in the database. This is becoming increasingly impractical as polling firms adopt mixed-mode samples (polls with Internet and telephone responses combined together) or otherwise fail to clearly differentiate one mode from the other. For now, we have grandfathered in preexisting cases like Ipsos and continued to list their Internet and telephone polls as separate entries. However, this will very likely change with the next major release of the pollster ratings database after the 2014 election.</p>
<h2>Step 2: Calculate simple average error</h2>
<p>This part’s really simple: We compare the margin in the poll against the election result and see how far apart they were. If the poll projected the Republican to win by 4 points and he won by 9 instead, that reflects a 5-point error. (Our preferred source for election results is <a href="http://uselectionatlas.org/">Dave Leip’s Atlas of U.S. Presidential Elections</a>.)</p>
<p>The error is calculated based on the margin separating the top two finishers in the election — and not the top two candidates in the poll. For instance, if a certain poll had the 2008 Iowa Democratic caucus with Hillary Clinton at 32 percent, Barack Obama with 30 percent and John Edwards with 28 percent, we’d look at how much it projected Obama to win over Edwards since they were the top two finishers (Clinton narrowly finished third).</p>
<p>The database also includes a column indicating whether a poll “called” the winner of the race correctly. But we think this is generally a poor measure of poll accuracy. In a race that the Democrat won by 1 percentage point, a poll that had the Republican winning by 1 point did a pretty good job, whereas one that had the Democrat winning by 13 was wildly off the mark.</p>
<h2>Step 3: Calculate Simple Plus-Minus</h2>
<p>As I mentioned, some elections are more conducive to accurate polling. In particular, presidential general elections are associated with accurate polling while presidential primaries are much more challenging to poll.<span class="espn-footnote-link" data-footnote-id="14" data-footnote-url="#fn-14" data-footnote-content="&lt;p&gt;Polls of primaries for lower offices like the U.S. House would undoubtedly be worse still, but these aren’t included in the pollster ratings.&lt;/p&gt;
"><sup id="ss-14">14</sup></span> Polls of general elections for Congress and for governor are somewhere in between.</p>
<p>This step seeks to account for that consideration along with a couple of other factors. We run a regression analysis that predicts polling error based on the type of election surveyed,<span class="espn-footnote-link" data-footnote-id="15" data-footnote-url="#fn-15" data-footnote-content="&lt;p&gt;In the regression, we use the dummy variables for the five major election types in the database: presidential general elections, presidential primaries, U.S. Senate general elections, U.S. House general elections and gubernatorial general elections.&lt;/p&gt;
"><sup id="ss-15">15</sup></span> a poll’s sample size,<span class="espn-footnote-link" data-footnote-id="16" data-footnote-url="#fn-16" data-footnote-content='&lt;p&gt;In the regression, this is specified as 1 divided by the square root of a poll’s sample size, as this calculation is proportional to a poll’s &lt;a href="http://en.wikipedia.org/wiki/Margin_of_error"&gt;sampling error&lt;/a&gt;.&lt;/p&gt;
'><sup id="ss-16">16</sup></span> and the number of days<span class="espn-footnote-link" data-footnote-id="17" data-footnote-url="#fn-17" data-footnote-content="&lt;p&gt;In the regression, this is specified as the square root of the number of days between the poll’s median field date and the election; the relationship between the time the poll was conducted and its accuracy is slightly nonlinear.&lt;/p&gt;
"><sup id="ss-17">17</sup></span> separating the poll from the election.<span class="espn-footnote-link" data-footnote-id="18" data-footnote-url="#fn-18" data-footnote-content="&lt;p&gt;As a control, the regression also includes a dummy variable for each polling firm. The purpose of this is to check whether differences in polling accuracy between different types of elections are the result of the mix of polling firms that happen to survey those races rather than factors intrinsic to the races themselves. This doesn’t make much difference — however, the modest exception is polls for the U.S. House, which have historically been less accurate than polls of Senate and gubernatorial races. The regression analysis suggests most of this difference is the result of worse pollsters tending to survey House races — in particular, the proportion of partisan polls is much higher in House races.&lt;/p&gt;
"><sup id="ss-18">18</sup></span></p>
<p>We then calculate a plus-minus score by comparing a poll’s average error against the error one would expect from these factors. For instance, Quinnipiac University polls have an average error of 4.6 percentage points. By comparison, the average pollster, surveying the same types of races on the same dates and with the same sample sizes, would have an error of 5.3 points according to the regression. Quinnipiac therefore gets a Simple Plus-Minus score of -0.7. This is a good score: As in golf, negative scores indicate better-than-average performance. Specifically, it means Quinnipiac polls have been 0.7 percentage points more accurate than other polls under similar circumstances.</p>
<p>A few words about the other factors Simple Plus-Minus considers: In the <a href="https://fivethirtyeight.com/features/pollster-ratings-v30/">past</a>, we’ve described the error in polls as resulting from three major components: sampling error, temporal error and pollster-induced error. They are related by a sum of squares formula:</p>
<p>\[Total\ Error=\sqrt{Sampling\ Error + Temporal\ Error + Pollster\text{-}Induced\ Error}\]</p>
<p><b>Sampling error</b> reflects the fact that a poll surveys only some portion of the electorate rather than everybody. This matters less than you might expect; a poll of 1,000 voters will miss the final margin in the race by an average of only about 2.5 percentage points because of sampling error alone — even in a state with 10 million voters.<span class="espn-footnote-link" data-footnote-id="19" data-footnote-url="#fn-19" data-footnote-content='&lt;p&gt;The reason to decompose this factor from other sources of polling error is that pollsters sometimes vary their sample sizes. If a certain polling firm had been getting inaccurate results because it conducted only 300-voter samples but it shifted to using 1,500-voter samples instead, you’d expect its results to get better. FiveThirtyEight’s forecast models &lt;a href="https://fivethirtyeight.com/features/how-the-fivethirtyeight-senate-forecast-model-works/"&gt;account for a pollster’s sample size&lt;/a&gt;, so it’s helpful to know how much this contributed to a poll’s accuracy (or lack thereof) compared with other factors. I’ve previously &lt;a href="https://fivethirtyeight.com/features/how-the-fivethirtyeight-senate-forecast-model-works/"&gt;insinuated&lt;/a&gt; that a poll’s sample size makes less difference in practice than it’s supposed to in theory, but after checking my own work more carefully, I no longer believe this to be the case; taking a larger sample helps about as much as you’d expect it to. However, the previous version of the pollster ratings gave too much credit for a larger sample size. The problem is that I’d been assuming that the different error components should be added together linearly, when instead their relationship is governed by a sum-of-squares formula.&lt;/p&gt;
'><sup id="ss-19">19</sup></span> Unfortunately, sampling error isn’t the only problem pollsters have to worry about.</p>
<p>Another concern is that polls are (almost) never conducted on Election Day itself. I refer to this property as <b>temporal (or time-dependent) error</b>. There have been elections when important news events occurred in the 48 to 72 hours that separated the final polls from the election, such as the New Hampshire Democratic primary debate in 2008, or the revelation of George W. Bush’s 1976 DUI arrest before the 2000 presidential election.</p>
<p>If late-breaking news can sometimes affect the outcome of elections, why go back three weeks in evaluating pollster accuracy? Well, there are a number of considerations we need to balance against the possibility of last-minute shifts in the polls:</p>
<ul>
<li>The overwhelming majority of elections do not feature important late-breaking developments. There will often be head-fakes and media-hyped “game changers,” but <a href="http://www.centerforpolitics.org/crystalball/articles/why-campaign-game-changers-rarely-change-the-game/">they rarely make much difference</a> upon careful analysis.</li>
<li>Herding (see above) becomes more prominent in the final few days before an election. It’s fairly common for a pollster to publish some wild-seeming results — which can affect media coverage of the campaign — only to “fall in line” with its final poll.</li>
<li>Some of the apparent movement in the polls in the late days of the election is <a href="http://www.ropercenter.uconn.edu/public-perspective/ppscan/43/43022.pdf">probably artificial</a>, reflecting response bias (voters for a certain candidate might be more likely to respond to polls after the candidate has a strong news cycle) and badly designed turnout models rather than genuine changes in public opinion.</li>
<li>“Election Day” is something of a misnomer. Many states accept ballots by mail or provide for early voting; in the 2012 presidential election, about <a href="http://elections.gmu.edu/early_vote_2012.html">one-quarter of the votes nationwide</a> were cast before Nov. 6.</li>
<li>Accounting for all polls in the final three weeks of the campaign increases the sample size.</li>
</ul>
<p>Three weeks is an arbitrary cutoff point; I’d have no profound objection to expanding the interval to a month or narrowing it to two weeks, or to using a slightly different standard for primaries and general elections. But we feel strongly that evaluating a polling firm’s accuracy based only on its very last poll is a mistake.</p>
<p>Nonetheless, the pollster ratings account for the fact that polling on the eve of the election is slightly easier than doing so a couple of weeks out. So a firm shouldn’t be at any advantage or disadvantage because of when it surveys a race.</p>
<p>The final component is what we’ve referred to in the past as <b>pollster-induced error</b>; it’s the residual error component that can’t be explained by sampling error or temporal error. I’ve grown to dislike the term “pollster-induced error”; it sounds more accusatory than it should. Certain things (like projecting turnout) are inherently pretty hard and it may not be the pollster’s fault when it fails to do them perfectly. Our research suggests that even if all polls were conducted on Election Day itself (no temporal error) and took an infinite sample size (no sampling error) the average one would still miss the final margin in the race by about 2 percentage points.</p>
<p>However, some polling firms are associated with more of this type of error. That’s what our plus-minus scores seek to evaluate.</p>
<h2>Step 4: Calculate Advanced Plus-Minus</h2>
<p>Earlier this year, House majority leader Eric Cantor <a href="https://fivethirtyeight.com/features/eric-cantors-loss-was-like-an-earthquake/">lost his Republican primary to David Brat</a>, a college professor, in Virginia’s 7th congressional district. It was a stunning upset, at least according to the polls. For instance, a <a href="http://dailycaller.com/2014/06/06/shock-poll-shows-eric-cantor-struggling-in-primary/">Vox Populi poll</a> had put Cantor ahead by 12 points. Instead, <a href="http://hosted.ap.org/dynamic/files/elections/2014/by_state/VA_Page_0610.html?SITE=AP&amp;SECTION=POLITICS">Brat won by 12 points</a>. The Vox Populi poll missed by 24 points.</p>
<p>According to Simple Plus-Minus, that poll would score very poorly. We don’t have a comprehensive database of House primary polls and don’t include them in the pollster ratings, but I’d guess that such polls are off by something like 10 percentage points on average. Vox Populi’s poll missed by 24, so it would get a Simple Plus-Minus score of +14.</p>
<p>That seems pretty terrible — until you compare it to the only other poll of the race, an <a href="http://www.washingtonpost.com/blogs/post-politics/wp/2014/06/06/cantor-internal-poll-claims-34-point-lead-over-primary-opponent-brat/">internal poll released by McLaughlin &amp; Associates on behalf of Cantor’s campaign</a>. That poll had Cantor up by 34 points — a 46-point error! If we calculated something called Relative Plus-Minus (how the poll compares against others of the same race) the Vox Populi poll would get a score of -22, since it was 22 points more accurate than the McLaughlin survey.</p>
<p>Advanced Plus-Minus, the next step in the calculation, seeks to balance these considerations. It weights Relative Plus-Minus based on the number of distinct polling firms<span class="espn-footnote-link" data-footnote-id="20" data-footnote-url="#fn-20" data-footnote-content="&lt;p&gt;Polling firms as opposed to polls — if one pollster surveyed the same race 10 times, it counts as just one poll for the purposes of this calculation.&lt;/p&gt;
"><sup id="ss-20">20</sup></span> that surveyed the same race, then treats Simple Plus-Minus as equivalent to three polls. For example, if six other polling firms surveyed a certain race, Relative Plus-Minus would get two-thirds of the weight and Simple Plus-Minus would get one-third.</p>
<p>The short version: When there are a lot of polls in the field, Advanced Plus-Minus is mostly based on how well a poll did in comparison to others of the same election. But when there is scant polling, it’s mostly based on a comparison to polls of the same <i>type</i> of election (for example, other presidential primaries).</p>
<p>Meticulous readers might wonder about another problem. If we’re comparing a poll against its competitors, shouldn’t we account for the strength of the competition? If a pollster misses every election by 40 points, it’s easy to look good by comparison if you happen to poll the same races. The problem is similar to the one you’ll encounter if you try to design college football or basketball rankings: Ideally, you’ll want to account for strength of schedule in addition to wins and losses and margin of victory. Advanced Plus-Minus addresses this by means of iteration (see a good explanation <a href="http://www.colleyrankings.com/matrate.pdf">here</a>), a technique commonly applied in sports power ratings.</p>
<p>Advanced Plus-Minus also addresses another problem. As I’ve mentioned, polls tend to be more accurate when there are more of them in the field. This may reflect herding, selection bias (pollsters may be more inclined to survey easier races; consider <a href="https://fivethirtyeight.com/features/senate-update-the-races-most-sensitive-to-new-polling/">how many of them are avoiding</a> the challenging Senate races in Kansas and Alaska this year), or some combination thereof. So Advanced-Plus Minus also adjusts scores based on how many other polling firms surveyed the same election. This has the effect of rewarding polling firms that survey races few other pollsters do and penalizing those that swoop in only after there are already a dozen polls in the field.</p>
<p>Two final wrinkles. Advanced Plus-Minus puts slightly more weight on more recent polls.<span class="espn-footnote-link" data-footnote-id="21" data-footnote-url="#fn-21" data-footnote-content="&lt;p&gt;The weights are a linear function of the year in which the poll was conducted and are calculated as: (&lt;em&gt;year&lt;/em&gt;-1988)/20.&lt;/p&gt;
"><sup id="ss-21">21</sup></span> It also contains a subtle adjustment to account for the higher volatility of certain election types, especially presidential primaries.<span class="espn-footnote-link" data-footnote-id="22" data-footnote-url="#fn-22" data-footnote-content='&lt;p&gt;Polls of presidential primaries are associated not only with a higher average error, but also with a higher standard deviation in the error term. Advanced Plus-Minus &lt;a href="http://en.wikipedia.org/wiki/Standard_score"&gt;normalizes&lt;/a&gt; the error term such that it’s equal across different types of races.&lt;/p&gt;
'><sup id="ss-22">22</sup></span></p>
<p>Before we proceed to the final step, let’s pause to re-examine the results for the 28 polling firms we listed before, but this time using Advanced Plus-Minus rather than Simple Average Error.</p>
<p><img decoding="async" class="size-full wp-image-54595" src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png" alt="silver-pollster-ratings-table-2" width="610" height="967" srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=47,75 47w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=189,300 189w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=768,1217 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=646,1024 646w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=969,1536 969w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=323,512 323w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=273,432 273w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=222,352 222w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=142,225 142w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=284,450 284w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=164,260 164w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=101,160 101w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=363,576 363w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=98,155 98w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=63,100 63w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=38,60 38w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=433,687 433w" sizes="(max-width: 610px) 100vw, 610px" data-sizes="(max-width: 610px) 100vw, 610px" data-src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png" data-srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=47,75 47w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=189,300 189w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=768,1217 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=646,1024 646w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=969,1536 969w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=323,512 323w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=273,432 273w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=222,352 222w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=142,225 142w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=284,450 284w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=164,260 164w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=101,160 101w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=363,576 363w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=98,155 98w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=63,100 63w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=38,60 38w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-table-21.png?resize=433,687 433w"></p>
<p>There’s still a correlation — although it’s somewhat weaker than before (the correlation coefficient is roughly 0.45 instead of 0.60). Accounting for the fact that American Research Group polls a lot of primaries makes the firm look somewhat less bad, for instance.</p>
<p>But pollster performance still looks to be predictable to some extent. As I’ll describe next, it’s more predictable if you look at a poll’s methodological standards in addition to its past performance.</p>
<h2>Step 5: Calculate Predictive Plus-Minus</h2>
<p>When we last updated the pollster ratings in 2010, I failed to be explicit enough about our goal: to predict which polling firms would be most accurate going forward. This is useful to know if <a href="https://fivethirtyeight.com/features/how-the-fivethirtyeight-senate-forecast-model-works/">you’re using polls to forecast election results</a>, for example.</p>
<p>But that may not be your purpose. If you’re interested in a purely retrospective analysis of poll accuracy, there are a number of measures of it <a href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings" target="_blank" rel="noopener noreferrer">in our pollster ratings spreadsheet</a>. For instance, you’ll find each pollster’s Simple Plus-Minus and Advanced Plus-Minus scores. The version I’d personally recommend is called “Mean-Reverted Advanced Plus-Minus,” which is retrospective but discounts the results for pollsters with a small number of polls in the database.<span class="espn-footnote-link" data-footnote-id="23" data-footnote-url="#fn-23" data-footnote-content="&lt;p&gt;This works by adding the equivalent of 30 average polls (that is, polls with a zero plus-minus score) to each firm’s record. For instance, say that a polling firm had an Advanced Plus-Minus score of +0.9 after 60 polls. Adding 30 average polls to this would bring its Mean-Reverted Advanced Plus-Minus score to +0.6.&lt;/p&gt;
"><sup id="ss-23">23</sup></span></p>
<p>The difference with Predictive Plus-Minus is that it also accounts for a polling firm’s methodological standards — albeit in a slightly roundabout way. In 2010, we looked at whether a polling firm was a member of the <a href="http://www.ncpp.org/">National Council on Public Polls</a> (NCPP) or a supporter of the <a href="http://www.aapor.org/List_of_Supporters.htm#.VCDhBitdW18">American Association for Public Opinion Research (AAPOR) Transparency Initiative</a>.<span class="espn-footnote-link" data-footnote-id="24" data-footnote-url="#fn-24" data-footnote-content="&lt;p&gt;Neither AAPOR nor NCPP are participants in the FiveThirtyEight pollster ratings or endorse them in any way.&lt;/p&gt;
"><sup id="ss-24">24</sup></span></p>
<p>One other thing I was probably not clear enough about in 2010 was that participation in these organizations was intended as a <a href="http://en.wikipedia.org/wiki/Proxy_(statistics)">proxy variable</a> for methodological quality. That is, it’s a correlate of methodological quality rather than a direct measure of it.<span class="espn-footnote-link" data-footnote-id="25" data-footnote-url="#fn-25" data-footnote-content="&lt;p&gt;AAPOR and NCPP do some vetting of applicants and require them to meet certain disclosure and professional standards before joining. This vetting process, along with self-selection in which firms choose to participate in these groups, tends to screen out firms with poorer methodological standards.&lt;/p&gt;
"><sup id="ss-25">25</sup></span> Nevertheless, polling firms that participated in one of these initiatives tended to have more accurate polls prior to 2010. Have they also been more accurate since?</p>
<p>Yes they have — and by a wide margin. The chart below tracks the performance of polling firms based on whether they were members of NCPP or the AAPOR Transparency Initiative as of <a href="https://web.archive.org/web/20100608231653/http://www.fivethirtyeight.com/2010/06/pollster-ratings-v40-results.html">June 6, 2010</a>, when FiveThirtyEight last released a full set of pollster ratings.<span class="espn-footnote-link" data-footnote-id="26" data-footnote-url="#fn-26" data-footnote-content="&lt;p&gt;The chart is based on Simple Average Error for each group of polls, although you’d come to the same conclusions if you used a more advanced error measure instead.&lt;/p&gt;
"><sup id="ss-26">26</sup></span></p>
<p><img loading="lazy" decoding="async" class="size-full wp-image-54506" src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png" alt="silver-pollster-ratings-chart-1" width="610" height="474" srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=97,75 97w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=300,233 300w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=768,597 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=1024,796 1024w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=659,512 659w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=556,432 556w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=453,352 453w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=290,225 290w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=579,450 579w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=335,260 335w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=206,160 206w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=741,576 741w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=199,155 199w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=100,78 100w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=60,47 60w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=884,687 884w" sizes="auto, (max-width: 610px) 100vw, 610px" data-sizes="auto, (max-width: 610px) 100vw, 610px" data-src="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png" data-srcset="https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png 1220w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=97,75 97w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=300,233 300w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=768,597 768w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=1024,796 1024w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=659,512 659w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=556,432 556w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=453,352 453w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=290,225 290w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=579,450 579w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=335,260 335w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=206,160 206w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=741,576 741w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=199,155 199w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=100,78 100w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=60,47 60w, https://fivethirtyeight.com/wp-content/uploads/2014/09/silver-pollster-ratings-chart-1.png?resize=884,687 884w"></p>
<p>From 1998 through 2009, the average poll from an AAPOR/NCPP polling firm had an error of 4.6 percentage points, compared with an average error of 5.5 percentage points for firms that did not participate in one of these groups. While this difference is highly statistically significant, it isn’t that impressive. The reason is that we evaluated participation in AAPOR/NCPP only after the fact. Perhaps polling firms with terrible track records <a href="http://en.wikipedia.org/wiki/Survivorship_bias">didn’t survive long enough</a> to participate in AAPOR/NCPP as of June 2010, or perhaps AAPOR/NCPP didn’t admit them.</p>
<p>What <i>is</i> impressive is that the difference has continued to be just as substantial since June 2010. In the general election in November 2010, polls from firms that had participated in AAPOR/NCPP as of that June were associated with an average error of 4.7 percentage points, compared with 5.7 percentage points for those that hadn’t. And throughout 2012 (including both the presidential primaries and the general election), the AAPOR/NCPP polls were associated with an average error of 4.0 percentage points, versus 5.2 points for nonparticipants.</p>
<p>For clarity: The 2010 and 2012 results are true <a href="http://www.investopedia.com/articles/trading/10/backtesting-walkforward-important-correlation.asp">out-of-sample tests</a>. In the chart above, the polling firms are classified based on the way FiveThirtyEight had them in June 2010 — before these elections occurred. In my view, this is reasonably persuasive evidence that methodology matters, at least to the extent we can infer something about it from AAPOR/NCPP participation.</p>
<p>This year, we’ve introduced a two-pronged test for methodological quality. The first test is similar to before: Is a polling firm a member of NCPP, a participant in the AAPOR Transparency Initiative, or does it release its raw data to the <a href="http://www.ropercenter.uconn.edu/data_access/data/data_providers.html">Roper Center Archive</a>?<span class="espn-footnote-link" data-footnote-id="27" data-footnote-url="#fn-27" data-footnote-content="&lt;p&gt;A firm needs to do only one of these things to pass this test; there is no bonus for doing two or three of them.&lt;/p&gt;
"><sup id="ss-27">27</sup></span> And second, does the firm regularly call cellphones in addition to landlines? Each firm gets a methodological score between 0 and 2 based on the answers to these questions.</p>
<p>Tracking which firms call cellphones is tricky. We’ve done a reasonably extensive search through recent polls to see whether they document calling cellphones. However, we do not list a polling firm as calling cellphones until we have some evidence that it does. There are undoubtedly some false negatives on our list; we encourage polling firms to contact us with documentation that they’ve been calling cellphones.<span class="espn-footnote-link" data-footnote-id="28" data-footnote-url="#fn-28" data-footnote-content="&lt;p&gt;There are also some end-arounds that don’t meet our standards. Some pollsters communicate with cellphone respondents by means other than a phone call, such as through a website that can be accessed on a mobile phone, or by including an “opt-in” sample of cellphone voters rather than calling them at random. We don’t consider such polls to have passed the cellphone standard. Other firms call cellphones for some but not all their polls; these firms score a half-point in this category.&lt;/p&gt;
"><sup id="ss-28">28</sup></span></p>
<p>So let’s say you have one polling firm that passes our methodological tests but hasn’t been so accurate, and another that doesn’t meet the methodological standards but has a reasonably good track record. Which one should you expect to be more accurate going forward?</p>
<p>That’s the question Predictive Plus-Minus ratings are intended to address. But the answer isn’t straightforward; it depends on how large a sample of polls you have from each firm. Our finding is that past performance reflects more noise than signal until you have about 30 polls to evaluate, so you should probably go with the firm with the higher methodological standards up to that point. If you have 100 polls from each pollster, however, you should tend to value past performance over methodology.<span class="espn-footnote-link" data-footnote-id="29" data-footnote-url="#fn-29" data-footnote-content="&lt;p&gt;A baseball analogy may once again be helpful here: When scouting pitchers, should you prefer the one with the better fastball or the better stats? It depends on how many stats you have. If the junkballer has posted a better ERA over 10 innings, that doesn’t mean very much. But if he’s done so over a full season, he might well be the better prospect.&lt;/p&gt;
"><sup id="ss-29">29</sup></span></p>
<p>One further complication is herding. The methodologically inferior pollster may be posting superficially good results by manipulating its polls to match those of the stronger polling firms. If left to its own devices — without stronger polls to guide it — it might not do so well.</p>
<p>My colleague Harry Enten looked at Senate polls since 2006 and found that methodologically poor pollsters improve their accuracy by roughly 2 percentage points <a href="https://fivethirtyeight.com/features/are-bad-pollsters-copying-good-pollsters/" target="_blank" rel="noopener noreferrer">when there are also strong polls in the field</a>. My own research on the broader polling database did not find quite so large an effect; instead it was closer to 0.6 percentage points. Still, the effect was highly statistically significant. As a result, Predictive Plus-Minus includes a “herding penalty” for pollsters with low methodology ratings.<span class="espn-footnote-link" data-footnote-id="30" data-footnote-url="#fn-30" data-footnote-content="&lt;p&gt;Although we estimate that methodologically inferior pollsters benefit by about 0.6 percentage points when there are high-quality polls in the field, only about two-thirds of races they surveyed also had “gold standard” polls. Therefore, the herding penalty is equal to about 0.4 percentage points instead of 0.6. If the pollster passes one methodological test but not the other, it gets half the herding penalty, or about 0.2 percentage points.&lt;/p&gt;
"><sup id="ss-30">30</sup></span></p>
<p>The formula for how to calculate Predictive Plus-Minus is included in the footnotes.<span class="espn-footnote-link" data-footnote-id="31" data-footnote-url="#fn-31" data-footnote-content="&lt;p&gt;To calculate Predictive Plus-Minus, start with the following quantities:&lt;/p&gt;
&lt;p&gt;&lt;i&gt;q&lt;/i&gt; = methodological quality score (from 0 to 2 based on AAPOR/NCPP/Roper participation and inclusion of cellphones)&lt;/p&gt;
&lt;p&gt;&lt;i&gt;a&lt;/i&gt; = Advanced Plus-Minus&lt;/p&gt;
&lt;p&gt;&lt;i&gt;n&lt;/i&gt; = sample size (number of polls in the database).&lt;/p&gt;
&lt;p&gt;Then, calculate &lt;i&gt;m&lt;/i&gt;, the mean that Predictive Plus-Minus is reverted toward. It is calculated as follows:&lt;/p&gt;
&lt;p&gt;\[m=0.36-0.59q+0.36q\cdot \left(1- \frac{n}{n+30}\right) \]&lt;/p&gt;
&lt;p&gt;Finally, revert &lt;i&gt;a&lt;/i&gt; toward &lt;i&gt;m &lt;/i&gt;based on the number of polls you have — and add the herding penalty for polls with low &lt;i&gt;q&lt;/i&gt; scores.&lt;/p&gt;
&lt;p&gt;\[m + (a-m) \cdot\left(\frac{n}{n+30}\right) + 0.19\cdot(2-q) \]&lt;/p&gt;
"><sup id="ss-31">31</sup></span> Basically, it’s a version of Advanced Plus-Minus where scores are reverted toward a mean, where the mean depends on whether the poll passed one or both methodological standards.<span class="espn-footnote-link" data-footnote-id="32" data-footnote-url="#fn-32" data-footnote-content="&lt;p&gt;The mean also depends on sample size; firms with very few polls are treated as being below-average in most cases.&lt;/p&gt;
"><sup id="ss-32">32</sup></span> The fewer polls a firm has, the more its score is reverted toward this mean. So Predictive Plus-Minus is mostly about a poll’s methodological standards for firms with only a few surveys in the database, and mostly about its past results for those with many.<span class="espn-footnote-link" data-footnote-id="33" data-footnote-url="#fn-33" data-footnote-content="&lt;p&gt;Note, however, that the herding penalty is not phased out even for polling firms with large samples.&lt;/p&gt;
"><sup id="ss-33">33</sup></span></p>
<p>As a final step, we’ve translated each firm’s Predictive Plus-Minus rating into a letter grade, from A+ to F. One purpose of this is to make clear that the vast majority of polling firms cluster somewhere in the middle of the spectrum; about 84 percent of polling firms receive grades in the B or C range.</p>
<p>There are a whole bunch of other goodies in the <a href="https://github.com/fivethirtyeight/data/tree/master/pollster-ratings" target="_blank" rel="noopener noreferrer">pollster ratings spreadsheet</a>, including various measures of bias and house effects. We think the pollster ratings are a valuable tool, so we wanted to make sure you had a few more options for how to use them.</p>
<p><strong>CORRECTION (May 21, 2016, 4 p.m.)</strong>: An earlier version of this article included an incorrect date in the formula in Footnote 21. The date should be 1988, not 1998.</p>
						</div><!-- .entry-content -->
					</article>
				</div>
				<div id="article-additional">
											<div class="entry-footnotes print-only">
	<h2>Footnotes</h2>
	<div class="entry-footnotes-content">
		<ol class="footnotes"><li data-wrap="false" data-footnote-id="1" id="fn-1"><span><p>The pollster ratings do include a consideration of whether a polling firm calls cellphones, which Internet polls (since they don’t place phone calls at all) do not. However, they are treated the same as other polls that do not place calls to cellphones.</p>
</span></li><li data-wrap="false" data-footnote-id="2" id="fn-2"><span><p>Be careful about coming to too many conclusions based on the way we have these polls labeled. They reflect the standard applied by FiveThirtyEight at the time the poll was added to the database &#8212; we haven’t gone back and reclassified older polls according to our current standard.</p>
</span></li><li data-wrap="false" data-footnote-id="3" id="fn-3"><span><p>Furthermore, many common statistical measurements like the normal distribution are <a href="http://en.wikipedia.org/wiki/Central_limit_theorem">predicated on the notion of independent or random trials</a>. These assumptions may be violated if pollsters are not behaving independently from one another.</p>
</span></li><li data-wrap="false" data-footnote-id="4" id="fn-4"><span><p>To be clear about the difference: Imagine in a race where the Republican won by 10 points, one poll had the Republican ahead by 5 points and another had her ahead by 15. The average poll was off by 5 percentage points. But the polling average, which showed a 10-point lead for the Republican, was exactly right.</p>
</span></li><li data-wrap="false" data-footnote-id="5" id="fn-5"><span><p>For example, if a certain polling firm usually conducts 800-person polls, we’d list that as the sample size in a case where it was unreported.</p>
</span></li><li data-wrap="false" data-footnote-id="6" id="fn-6"><span><p>Polls of single-party primaries are not included except in the case of presidential primaries and caucuses.</p>
</span></li><li data-wrap="false" data-footnote-id="7" id="fn-7"><span><p>The accuracy of generic congressional ballot polls is evaluated in comparison to the aggregate popular vote for the U.S. House.</p>
</span></li><li data-wrap="false" data-footnote-id="8" id="fn-8"><span><p>For example, polls from Strategic Vision are not used in FiveThirtyEight’s forecasts because there is <a href="https://fivethirtyeight.com/features/strategic-vision-polls-exhibit-unusual/">strong evidence that the firm&#8217;s results were fabricated</a>.</p>
</span></li><li data-wrap="false" data-footnote-id="9" id="fn-9"><span><p>For primaries, we also exclude polls if one of the leading candidates dropped out between the date of the poll and the date of the election.</p>
</span></li><li data-wrap="false" data-footnote-id="10" id="fn-10"><span><p>There are no private, internal polls in the database.</p>
</span></li><li data-wrap="false" data-footnote-id="11" id="fn-11"><span><p>However, we are not likely to release another major version of the database until the 2014 elections are complete. Minor errors and omissions should not make much difference to the overall pollster ratings. For firms with dozens or hundreds of polls in the database, a couple of missing (or incorrect) polls should make little difference in the average results. For firms with fewer polls, the pollster ratings are regressed heavily to the mean, so one or two polls likewise won’t have much impact.</p>
</span></li><li data-wrap="false" data-footnote-id="12" id="fn-12"><span><p>If you see a poll listed with a media organization in the database, it’s because it has an in-house polling operation or because we were unable to identify the polling firm responsible for the underlying work.</p>
</span></li><li data-wrap="false" data-footnote-id="13" id="fn-13"><span><p>Media organizations with longstanding polling partnerships &#8212; like CBS News and The New York Times or ABC News and The Washington Post &#8212; sometimes release polls that are sponsored by just one of the partners. For instance, The Washington Post sometimes conducts polls of Maryland and Virginia that are not co-branded with ABC News. We still classify these together with other ABC News/Washington Post polls. On the other hand, news organizations sometimes switch polling partners. For instance, most Fox News polls were conducted by Opinion Dynamics Corp. through early 2011; since then, they’ve been conducted jointly by Anderson Robbins Research and Shaw &amp; Company Research. Those polls are treated as distinct series.</p>
</span></li><li data-wrap="false" data-footnote-id="14" id="fn-14"><span><p>Polls of primaries for lower offices like the U.S. House would undoubtedly be worse still, but these aren’t included in the pollster ratings.</p>
</span></li><li data-wrap="false" data-footnote-id="15" id="fn-15"><span><p>In the regression, we use the dummy variables for the five major election types in the database: presidential general elections, presidential primaries, U.S. Senate general elections, U.S. House general elections and gubernatorial general elections.</p>
</span></li><li data-wrap="false" data-footnote-id="16" id="fn-16"><span><p>In the regression, this is specified as 1 divided by the square root of a poll’s sample size, as this calculation is proportional to a poll’s <a href="http://en.wikipedia.org/wiki/Margin_of_error">sampling error</a>.</p>
</span></li><li data-wrap="false" data-footnote-id="17" id="fn-17"><span><p>In the regression, this is specified as the square root of the number of days between the poll’s median field date and the election; the relationship between the time the poll was conducted and its accuracy is slightly nonlinear.</p>
</span></li><li data-wrap="false" data-footnote-id="18" id="fn-18"><span><p>As a control, the regression also includes a dummy variable for each polling firm. The purpose of this is to check whether differences in polling accuracy between different types of elections are the result of the mix of polling firms that happen to survey those races rather than factors intrinsic to the races themselves. This doesn’t make much difference &#8212; however, the modest exception is polls for the U.S. House, which have historically been less accurate than polls of Senate and gubernatorial races. The regression analysis suggests most of this difference is the result of worse pollsters tending to survey House races &#8212; in particular, the proportion of partisan polls is much higher in House races.</p>
</span></li><li data-wrap="false" data-footnote-id="19" id="fn-19"><span><p>The reason to decompose this factor from other sources of polling error is that pollsters sometimes vary their sample sizes. If a certain polling firm had been getting inaccurate results because it conducted only 300-voter samples but it shifted to using 1,500-voter samples instead, you’d expect its results to get better. FiveThirtyEight’s forecast models <a href="https://fivethirtyeight.com/features/how-the-fivethirtyeight-senate-forecast-model-works/">account for a pollster’s sample size</a>, so it’s helpful to know how much this contributed to a poll’s accuracy (or lack thereof) compared with other factors. I’ve previously <a href="https://fivethirtyeight.com/features/how-the-fivethirtyeight-senate-forecast-model-works/">insinuated</a> that a poll’s sample size makes less difference in practice than it’s supposed to in theory, but after checking my own work more carefully, I no longer believe this to be the case; taking a larger sample helps about as much as you’d expect it to. However, the previous version of the pollster ratings gave too much credit for a larger sample size. The problem is that I’d been assuming that the different error components should be added together linearly, when instead their relationship is governed by a sum-of-squares formula.</p>
</span></li><li data-wrap="false" data-footnote-id="20" id="fn-20"><span><p>Polling firms as opposed to polls &#8212; if one pollster surveyed the same race 10 times, it counts as just one poll for the purposes of this calculation.</p>
</span></li><li data-wrap="false" data-footnote-id="21" id="fn-21"><span><p>The weights are a linear function of the year in which the poll was conducted and are calculated as: (<em>year</em>-1988)/20.</p>
</span></li><li data-wrap="false" data-footnote-id="22" id="fn-22"><span><p>Polls of presidential primaries are associated not only with a higher average error, but also with a higher standard deviation in the error term. Advanced Plus-Minus <a href="http://en.wikipedia.org/wiki/Standard_score">normalizes</a> the error term such that it’s equal across different types of races.</p>
</span></li><li data-wrap="false" data-footnote-id="23" id="fn-23"><span><p>This works by adding the equivalent of 30 average polls (that is, polls with a zero plus-minus score) to each firm’s record. For instance, say that a polling firm had an Advanced Plus-Minus score of +0.9 after 60 polls. Adding 30 average polls to this would bring its Mean-Reverted Advanced Plus-Minus score to +0.6.</p>
</span></li><li data-wrap="false" data-footnote-id="24" id="fn-24"><span><p>Neither AAPOR nor NCPP are participants in the FiveThirtyEight pollster ratings or endorse them in any way.</p>
</span></li><li data-wrap="false" data-footnote-id="25" id="fn-25"><span><p>AAPOR and NCPP do some vetting of applicants and require them to meet certain disclosure and professional standards before joining. This vetting process, along with self-selection in which firms choose to participate in these groups, tends to screen out firms with poorer methodological standards.</p>
</span></li><li data-wrap="false" data-footnote-id="26" id="fn-26"><span><p>The chart is based on Simple Average Error for each group of polls, although you’d come to the same conclusions if you used a more advanced error measure instead.</p>
</span></li><li data-wrap="false" data-footnote-id="27" id="fn-27"><span><p>A firm needs to do only one of these things to pass this test; there is no bonus for doing two or three of them.</p>
</span></li><li data-wrap="false" data-footnote-id="28" id="fn-28"><span><p>There are also some end-arounds that don’t meet our standards. Some pollsters communicate with cellphone respondents by means other than a phone call, such as through a website that can be accessed on a mobile phone, or by including an “opt-in” sample of cellphone voters rather than calling them at random. We don’t consider such polls to have passed the cellphone standard. Other firms call cellphones for some but not all their polls; these firms score a half-point in this category.</p>
</span></li><li data-wrap="false" data-footnote-id="29" id="fn-29"><span><p>A baseball analogy may once again be helpful here: When scouting pitchers, should you prefer the one with the better fastball or the better stats? It depends on how many stats you have. If the junkballer has posted a better ERA over 10 innings, that doesn’t mean very much. But if he’s done so over a full season, he might well be the better prospect.</p>
</span></li><li data-wrap="false" data-footnote-id="30" id="fn-30"><span><p>Although we estimate that methodologically inferior pollsters benefit by about 0.6 percentage points when there are high-quality polls in the field, only about two-thirds of races they surveyed also had “gold standard” polls. Therefore, the herding penalty is equal to about 0.4 percentage points instead of 0.6. If the pollster passes one methodological test but not the other, it gets half the herding penalty, or about 0.2 percentage points.</p>
</span></li><li data-wrap="false" data-footnote-id="31" id="fn-31"><span><p>To calculate Predictive Plus-Minus, start with the following quantities:</p>
<p><i>q</i> = methodological quality score (from 0 to 2 based on AAPOR/NCPP/Roper participation and inclusion of cellphones)</p>
<p><i>a</i> = Advanced Plus-Minus</p>
<p><i>n</i> = sample size (number of polls in the database).</p>
<p>Then, calculate <i>m</i>, the mean that Predictive Plus-Minus is reverted toward. It is calculated as follows:</p>
<p>\[m=0.36-0.59q+0.36q\cdot \left(1- \frac{n}{n+30}\right) \]</p>
<p>Finally, revert <i>a</i> toward <i>m </i>based on the number of polls you have &#8212; and add the herding penalty for polls with low <i>q</i> scores.</p>
<p>\[m + (a-m) \cdot\left(\frac{n}{n+30}\right) + 0.19\cdot(2-q) \]</p>
</span></li><li data-wrap="false" data-footnote-id="32" id="fn-32"><span><p>The mean also depends on sample size; firms with very few polls are treated as being below-average in most cases.</p>
</span></li><li data-wrap="false" data-footnote-id="33" id="fn-33"><span><p>Note, however, that the herding penalty is not phased out even for polling firms with large samples.</p>
</span></li></ol>	</div><!-- .entry-footnotes-content -->
</div><!-- .entry-footnotes -->
<div class="mini-bio">
		<p>Nate Silver founded and was the editor in chief of FiveThirtyEight. <span class="mail"><a aria-label="Email Nate Silver" href="mailto:nrsilver@fivethirtyeight.com"><i class="icon icon-mail"></i></a></span> <span class="twitter"><a href="https://twitter.com/natesilver538" target="_blank"><i class="icon icon-twitter"></i> <span class="twitter-username">@natesilver538</span></a></span></p>
</div>
<!-- .post-author -->
<div id="entry-comments" class="fte-expandable">
	<h3 class="fte-expandable-title">Comments</h3>

<div class="entry-comments-content fte-expandable-content">
		<div class="fb-comments" data-href="http://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/" data-numposts="5" data-colorscheme="light"
														></div>
	</div>
	<!-- .entry-comments-content -->
</div>
<!-- .entry-comments -->
<div class="tags">
	<p class="filed-under">Filed under</p>
	<p class="tag-links"><a class="tag" href="https://fivethirtyeight.com/tag/polling/">Polling <span class="count">(553 posts)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/polls/">Polls <span class="count">(511)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/2014-midterms/">2014 Midterms <span class="count">(167)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/pollster-ratings/">Pollster Ratings <span class="count">(40)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/senate-forecast/">Senate Forecast <span class="count">(39)</span></a>
</p>
</div>
									</div>
			</div>
						<div class="single-feature__col">
				<div id="secondary" class="single-col vertical-col blog-col">

<div class="sidebar-feature visually-hidden"><aside id="fivethirtyeight-embed-490" class="widget flexible interactives embed "><h2 class="widget-title">Interactives</h2>
					<iframe id="pym-fivethirtyeight_embed_490" title="Interactives" src="https://projects.fivethirtyeight.com/polls/president-primary-r/2024/national/" width="300" height="250" scrolling="no"></iframe>
			</aside>

<aside class="widget fivethirtyeight-featured-video-widget">
		<h2 class="widget-title">Latest Videos</h2>
					<ul>
										<li>
							<article id="post-54447" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/why-biden-is-losing-support-among-voters-of-color/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="1" data-content_title="Why Biden Is Losing Support Among Voters Of Color" data-content_id="362896" data-content_select_type="fte_videos">
											Why Biden Is Losing Support Among Voters Of Color										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/why-biden-is-losing-support-among-voters-of-color/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="1" data-content_title="Why Biden Is Losing Support Among Voters Of Color" data-content_id="362896" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-54447" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/should-we-trust-polls-campaigns-leak-to-the-press/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="2" data-content_title="Should We Trust Polls Campaigns Leak To The Press?" data-content_id="362859" data-content_select_type="fte_videos">
											Should We Trust Polls Campaigns Leak To The Press?										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/should-we-trust-polls-campaigns-leak-to-the-press/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="2" data-content_title="Should We Trust Polls Campaigns Leak To The Press?" data-content_id="362859" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-54447" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/how-well-can-you-tell-the-2024-gop-candidates-apart/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="3" data-content_title="How Well Can You Tell The 2024 GOP Candidates Apart?" data-content_id="362601" data-content_select_type="fte_videos">
											How Well Can You Tell The 2024 GOP Candidates Apart?										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/how-well-can-you-tell-the-2024-gop-candidates-apart/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="3" data-content_title="How Well Can You Tell The 2024 GOP Candidates Apart?" data-content_id="362601" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-54447" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/what-the-gop-primary-looks-like-in-the-early-states/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="4" data-content_title="What The GOP Primary Looks Like In The Early States" data-content_id="362590" data-content_select_type="fte_videos">
											What The GOP Primary Looks Like In The Early States										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/what-the-gop-primary-looks-like-in-the-early-states/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="4" data-content_title="What The GOP Primary Looks Like In The Early States" data-content_id="362590" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
									</ul>
			</aside>
			<!-- end widget -->
		</div></div><!-- #secondary -->
			</div>
					</div>

</div><!-- .single -->

</div><!-- #wrapper .site-wrapper -->
	</div><!-- .site-main -->

<footer id="colophon" class="site-footer">

<div class="site-wrapper footer-main-content">

<div class="footer-section-get-more">
			Get more FiveThirtyEight		</div>

<div class="footer-section-primary-links">
			<ul class="footer-menu">
				<li class="footer-menu-item">
					<a href="https://cottonbureau.com/stores/fivethirtyeight#/shop" name="&amp;lpos=fivethirtyeightFooter&amp;lid=store">Store</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://twitter.com/fivethirtyeight" name="&amp;lpos=fivethirtyeightFooter&amp;lid=twitter">Twitter</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://www.facebook.com/fivethirtyeight" name="&amp;lpos=fivethirtyeightFooter&amp;lid=facebook">Facebook</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://data.fivethirtyeight.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=data">Data</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/features/fear-not-readers-we-have-rss-feeds/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=rss">RSS</a>
				</li>
			</ul>
		</div><!-- .footer-primary-links -->

<div class="footer-section-social-follow">
			<ul class="footer-menu">
				<li class="footer-menu-item social-share-item">
					<div class="fb-like" data-href="https://www.facebook.com/fivethirtyeight" data-layout="button_count"></div>
				</li>
				<li class="footer-menu-item social-share-item">
					<a href="https://twitter.com/FiveThirtyEight" class="twitter-follow-button" data-show-count="true">Follow @FiveThirtyEight</a>
				</li>
			</ul>
		</div>

<div class="footer-section-secondary-links">
			<ul class="footer-menu">
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/about-us/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=about-us">About Us</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/jobs/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=jobs">Jobs</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/masthead/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=masthead">Masthead</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/how-to-pitch-fivethirtyeight/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=pitch">Pitch FiveThirtyEight</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://disneyadsales.com/our-brands/abc-news/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=advertise">Advertise With Us</a>
				</li>
				<li class="footer-menu-item">
					<a href="http://priv-policy.imrworldwide.com/priv/browser/us/en/optout.html" name="&amp;lpos=fivethirtyeightFooter&amp;lid=nielsen">About Nielsen Measurement</a>
				</li>
			</ul>
		</div><!-- .footer-secondary-links -->

<div class="footer-section-powered-by">
			Powered by <a href="https://wpvip.com/?utm_source=vip_powered_wpcom&#038;utm_medium=web&#038;utm_campaign=VIP%20Footer%20Credit&#038;utm_term=fivethirtyeight.com" rel="generator nofollow" class="powered-by-wpcom">WordPress VIP</a>		</div><!-- .powered-by -->

<div class="footer-section-tertiary-links">
			<ul class="footer-menu">
				<li class="menu-item">
					<a href="https://disneytermsofuse.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyTOS" target="_blank" rel="noopener noreferrer">Terms of Use</a>
				</li>
				<li class="menu-item">
					<a href="https://disneyprivacycenter.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyPrivacy" target="_blank" rel="noopener noreferrer">Privacy Policy</a>
				</li>

<li class="menu-item"><a href="https://privacy.thewaltdisneycompany.com/en/dnssmpi/" class="ot-cmp-link">Do Not Sell or Share My Personal Information</a></li>
				<li class="menu-item">
					<a href="https://privacy.thewaltdisneycompany.com/en/current-privacy-policy/your-us-state-privacy-rights/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=californiaPrivacyRights" target="_blank" rel="noopener noreferrer">Your US State Privacy Rights</a>
				</li>
				<li class="menu-item">
					<a href="https://disneyprivacycenter.com/kids-privacy-policy/english/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=childrensPrivacy" target="_blank" rel="noopener noreferrer">Children's Online Privacy Policy</a>
				</li>
				<li class="menu-item">
					<a href="https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=adPreferences" target="_blank" rel="noopener noreferrer">Interest-Based Ads</a>
				</li>
			</ul>
			<p>
				&copy; 2025 ABC News Internet Ventures. All rights reserved.
			</p>
		</div>
		<!-- / .footer-section-tertiary-links -->
	</div><!-- .site-wrapper -->

<div class="footer-section-additional-info" id="footer-additional-info">
		<div class="site-wrapper">
			<button class="close-additional-info" id="close-additional-info" aria-label="Close"><span class="visually-hidden">Close Additional Information</span></button>
			<a href="https://disneytermsofuse.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyTOS">Terms of Use</a> and <a href="https://disneyprivacycenter.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyPrivacy">Privacy Policy</a> and Safety Information/<a href="https://disneyprivacycenter.com/notice-to-california-residents/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=californiaPrivacyRights">Your California Privacy Rights</a>/<a href="https://disneyprivacycenter.com/kids-privacy-policy/english/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=childrensPrivacy">Children's Online Privacy Policy</a> are applicable to you. © 2025 ABC News Internet Ventures. All rights reserved. <a href="https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=adPreferences">Interest-Based Ads</a>. <a href="https://disneyprivacycenter.com/cookies-policy-translations/cookies-policy/">Cookie Policy</a>.
		</div><!-- .site-wrapper -->
	</div><!-- .footer-section-additional-info -->
</footer><!-- .site-footer -->
<script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\/*"},{"not":{"href_matches":["\/wp-*.php","\/wp-admin\/*","\/wp-content\/uploads\/*","\/wp-content\/*","\/wp-content\/plugins\/*","\/wp-content\/themes\/espn-fivethirtyeight\/*","\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-blocks/assets/js/pym.min.js" id="abc-ai2html-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-audio-features/assets/js/blocks.min.js?ver=1.2.2" id="abc-audio-features-blocks-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-blocks/assets/js/blocks.min.js?ver=1.1.2" id="abc-blocks-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/gif-play-button/assets/js/gif-play-button.min.js?ver=1.1.2" id="gif-play-button-scripts-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/utilities/assets/js/video.min.js?ver=1.1.2" id="video-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/newsletter.min.js?ver=1.1.2" id="newsletter-oneid-js"></script>
<script type="text/javascript" id="wp-util-js-extra">
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/wp-util.min.js?ver=6.8.2" id="wp-util-js"></script>
<script type="text/javascript" id="fte-main-js-extra">
/* <![CDATA[ */
var ESPNSocial = {"fbVersion":"6.0","fbAppId":"797620670264818"};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/js/frontend.js?ver=1.1.2" id="fte-main-js"></script>
<script type="text/javascript" src="//datawrapper.dwcdn.net/lib/embed.js?ver=1.1.2" id="datawrapper-js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=Accessible&amp;ver=1.3.13" id="mathjax-js"></script>
<script type="text/javascript" id="mathjax-js-after">
/* <![CDATA[ */
MathJax.Hub.Config({"messageStyle":"none","TeX":{"equationNumbers":{"autoNumber":"all"}},"CommonHTML":{"linebreaks":{"automatic":true}},"HTML-CSS":{"linebreaks":{"automatic":true}},"SVG":{"linebreaks":{"automatic":true}}});
/* ]]> */
</script>
</body>
</html>
