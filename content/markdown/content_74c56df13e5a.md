# Content from https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/

*Retrieved: 2025-09-15T04:28:11.754744*

---

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />


<meta name="description" content="Posted by Jason Wei and Yi Tay, Research Scientists, Google Research, Brain Team The field of natural language processing (NLP) has been revolution..."><meta name="keywords" content="NLP,Publications,Research"><link rel="canonical" href="https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" /><meta property="og:title" content="Characterizing Emergent Phenomena in Large Language Models"><meta property="og:url" content="https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/"><meta property="og:description" content="Posted by Jason Wei and Yi Tay, Research Scientists, Google Research, Brain Team The field of natural language processing (NLP) has been revolution..."><meta property="og:image" content="https://storage.googleapis.com/gweb-research2023-media/images/825fe036e00e3833b7bb7962fcd1ab05-i.width-800.format-jpeg.jpg"><meta property="og:image:secure_url" content="https://storage.googleapis.com/gweb-research2023-media/images/825fe036e00e3833b7bb7962fcd1ab05-i.width-800.format-jpeg.jpg"><meta property="og:type" content="Website">

<title>Characterizing Emergent Phenomena in Large Language Models</title>

    <meta name="description" content="Posted by Jason Wei and Yi Tay, Research Scientists, Google Research, Brain Team The field of natural language processing (NLP) has been revolution..." />

    <meta name="viewport" content="width=device-width, initial-scale=1 viewport-fit=cover"/>

<link rel="icon" type="image/png" href="https://www.gstatic.com/images/branding/googleg_gradient/1x/googleg_gradient_standard_20dp.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preload"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap"
        as="style">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Product+Sans&family=Google+Sans+Display:ital@0;1&family=Google+Sans:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&family=Google+Sans+Text:ital,wght@0,400;0,500;0,700;1,400;1,500;1,700&display=swap">
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet">

<link href="https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.css" rel="stylesheet" />
    <link href="https://www.gstatic.com/glue/v27_1/glue-material.min.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/gr/static/css/googleresearch.css?id=3bffee92b80ec0401925e5648f613e44">

<script id="analyticsScript" data-blog-publish-date="20221110"
          data-blog-word-count="1039">
        window.dataLayer = window.dataLayer || [];
        const blogData = document.querySelector('#analyticsScript')

dataLayer.push({
          publishDate: blogData?.dataset.blogPublishDate,
          wordCount: blogData?.dataset.blogWordCount,
        });
      </script>

<!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-K8QBZ7Q');
    </script>
    <!-- End Google Tag Manager -->
</head>

<body class=" js-google-tag-wrapper" data-gt-page-path="https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" data-env="production">
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-K8QBZ7Q"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

<header class="global-header glue-header glue-header--single not-glue">
  <a href="#page-content" class="glue-header__skip-content">Jump to Content</a>
  <div class="glue-header__bar glue-header__bar--mobile not-glue">
    <div class="glue-header__tier not-glue">
      <!-- mobile lockup component -->
      <div class="glue-header__container">
        <div class="glue-header__lock-up">
          <!-- Hamburger button component -->
          <div class="glue-header__hamburger">
            <button class="glue-header__drawer-toggle-btn" aria-label="Open the navigation drawer">
              <svg class="glue-icon glue-icon--24px" role="presentation" aria-hidden="true">
                <use href="/gr/static/assets/icons/glue-icons.svg#menu"></use>
              </svg>
            </button>
          </div>
          <div class="glue-header__logo">
            <a class="glue-header__logo-link" href="/" title="Google Research">
              <!-- Logo component -->
              <div class="glue-header__logo-container">

<svg role="presentation" aria-hidden="true" alt='Google' class="glue-icon  glue-icon glue-header__logo-svg">
  <use href="/gr/static/assets/icons/glue-icons.svg#google-color-logo"></use>
</svg>

</div>
              <span class="glue-header__logo--product">Research</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="glue-header__bar glue-header__bar--desktop glue-header__drawer">
    <div class="glue-header__tier">
      <!-- desktop lockup component -->
      <div class="glue-header__container">
        <div class="glue-header__lock-up">
          <div class="glue-header__logo">
            <a class="glue-header__logo-link" href="/" title="Google Research">
              <!-- Logo component -->
              <div class="glue-header__logo-container">

<svg role="presentation" aria-hidden="true" alt='Google' class="glue-icon  glue-icon glue-header__logo-svg not-glue --dark-logo">
  <use href="/gr/static/assets/icons/glue-icons.svg#google-solid-logo"></use>
</svg>

<svg role="presentation" aria-hidden="true" alt='Google' class="glue-icon  glue-icon glue-header__logo-svg --light-logo">
  <use href="/gr/static/assets/icons/glue-icons.svg#google-color-logo"></use>
</svg>

</div>
              <span class="glue-header__logo--product">Research</span>
            </a>
          </div>
        </div>
      </div>
      <!-- linkbar component -->
      <div class="glue-header__container glue-header__container--linkbar">
        <nav class="glue-header__link-bar navigation js-gt-global-nav-wrapper">
          <ul class="glue-header__list">

<li
    class="glue-header__item  js-sub-nav-parent --parent"
    data-gt-primary="Who we are"
  >

    <button
      class="glue-header__link js-sub-nav-target"
      aria-haspopup="true"
      aria-expanded="false"

    >

      <span class="">
        Who we are

          <span class="icon icon--caret"></span>

      </span>

    </button>


      <div class="navigation__sub js-sub-nav" role="menu">
        <div class="navigation__sub__container">
          <div class="navigation__sub__mobile-heading">
            <button class="glue-header__link js-sub-nav-close-mobile">
              <span class="sr-text">Back to</span>
              <span class="icon icon--caret"></span> Who we are
              <span class="sr-text">menu</span>
            </button>
            <hr/>
          </div>
          <div class="block-nav_drawer_columns_content">

<div class="navigation__sub--content" data-gt-secondary="Defining the technology of today and tomorrow.">
    <div class="navigation__sub__wrapper">

            <div class="navigation__sub__heading">
                <h2 class="headline-3">Defining the technology of today and tomorrow.</h2>

            </div>

<ul class="navigation__sub__columns">

<li data-gt-secondary="Philosophy">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Philosophy
            </h2>

        <p class="navigation__sub__columns__description caption">We strive to create an environment conducive to many different types of research across many different time scales and levels of risk.</p>

            <a
            href="https://research.google/philosophy/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Philosophy</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/philosophy/"

            >
                Philosophy
            </a>

    </div>
</li>

<li data-gt-secondary="People">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                People
            </h2>

        <p class="navigation__sub__columns__description caption">Our researchers drive advancements in computer science through both fundamental and applied research.</p>

            <a
            href="https://research.google/people/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our People</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/people/"

            >
                People
            </a>

    </div>
</li>

</ul>

</div>
</div>
</div>
        </div>
      </div>

  </li>

<li
    class="glue-header__item  js-sub-nav-parent --parent"
    data-gt-primary="Research areas"
  >

    <button
      class="glue-header__link js-sub-nav-target"
      aria-haspopup="true"
      aria-expanded="false"

    >

      <span class="">
        Research areas

          <span class="icon icon--caret"></span>

      </span>

    </button>


      <div class="navigation__sub js-sub-nav" role="menu">
        <div class="navigation__sub__container">
          <div class="navigation__sub__mobile-heading">
            <button class="glue-header__link js-sub-nav-close-mobile">
              <span class="sr-text">Back to</span>
              <span class="icon icon--caret"></span> Research areas
              <span class="sr-text">menu</span>
            </button>
            <hr/>
          </div>
          <div class="block-nav_drawer_columns_link_list">

<div class="navigation__sub--list">
    <div class="navigation__sub__wrapper">
        <ul class="navigation__sub__columns">

<li data-gt-secondary="Research areas">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">Research areas</h2>

<ul>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/"

                            >
                                Explore all research areas
                            </a>

                    </li>

            </ul>

    </div>
    <div class="navigation__sub__columns__mobile">
        <button class="glue-header__link js-sub-nav-target" data-panel="nested" role="menuitem" aria-haspopup="true">
            Research areas <span class="icon icon--caret"></span>
        </button>

<div class="navigation__nested-sub js-sub-nav-parent">

              <div class="navigation__sub__mobile-heading">
                <button class="glue-header__link js-sub-nav-close-mobile" role="menuitem" aria-haspopup="true">
                  <span class="sr-text">Back to</span>
                  <span class="icon icon--caret"></span> Research areas
                  <span class="sr-text">menu</span>
                </button>
                <hr/>
              </div>
              <ul>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Explore all research areas
                                    <span>

                                    </span>
                                </a>

                        </li>

                </ul>

        </div>
    </div>
</li>

<li data-gt-secondary="Foundational ML &amp; Algorithms">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">Foundational ML &amp; Algorithms</h2>

<ul>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/algorithms-and-theory/"

                            >
                                Algorithms &amp; Theory
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/data-management/"

                            >
                                Data Management
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/data-mining-and-modeling/"

                            >
                                Data Mining &amp; Modeling
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/information-retrieval-and-the-web/"

                            >
                                Information Retrieval &amp; the Web
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/machine-intelligence/"

                            >
                                Machine Intelligence
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/machine-perception/"

                            >
                                Machine Perception
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/machine-translation/"

                            >
                                Machine Translation
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/natural-language-processing/"

                            >
                                Natural Language Processing
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/speech-processing/"

                            >
                                Speech Processing
                            </a>

                    </li>

            </ul>

    </div>
    <div class="navigation__sub__columns__mobile">
        <button class="glue-header__link js-sub-nav-target" data-panel="nested" role="menuitem" aria-haspopup="true">
            Foundational ML &amp; Algorithms <span class="icon icon--caret"></span>
        </button>

<div class="navigation__nested-sub js-sub-nav-parent">

              <div class="navigation__sub__mobile-heading">
                <button class="glue-header__link js-sub-nav-close-mobile" role="menuitem" aria-haspopup="true">
                  <span class="sr-text">Back to</span>
                  <span class="icon icon--caret"></span> Foundational ML &amp; Algorithms
                  <span class="sr-text">menu</span>
                </button>
                <hr/>
              </div>
              <ul>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/algorithms-and-theory/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Algorithms &amp; Theory
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/data-management/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Data Management
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/data-mining-and-modeling/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Data Mining &amp; Modeling
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/information-retrieval-and-the-web/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Information Retrieval &amp; the Web
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/machine-intelligence/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Machine Intelligence
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/machine-perception/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Machine Perception
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/machine-translation/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Machine Translation
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/natural-language-processing/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Natural Language Processing
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/speech-processing/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Speech Processing
                                    <span>

                                    </span>
                                </a>

                        </li>

                </ul>

        </div>
    </div>
</li>

<li data-gt-secondary="Computing Systems &amp; Quantum AI">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">Computing Systems &amp; Quantum AI</h2>

<ul>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/distributed-systems-and-parallel-computing/"

                            >
                                Distributed Systems &amp; Parallel Computing
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/hardware-and-architecture/"

                            >
                                Hardware &amp; Architecture
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/mobile-systems/"

                            >
                                Mobile Systems
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/networking/"

                            >
                                Networking
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/quantum-computing/"

                            >
                                Quantum Computing
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/robotics/"

                            >
                                Robotics
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/security-privacy-and-abuse-prevention/"

                            >
                                Security, Privacy, &amp; Abuse Prevention
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/software-engineering/"

                            >
                                Software Engineering
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/software-systems/"

                            >
                                Software Systems
                            </a>

                    </li>

            </ul>

    </div>
    <div class="navigation__sub__columns__mobile">
        <button class="glue-header__link js-sub-nav-target" data-panel="nested" role="menuitem" aria-haspopup="true">
            Computing Systems &amp; Quantum AI <span class="icon icon--caret"></span>
        </button>

<div class="navigation__nested-sub js-sub-nav-parent">

              <div class="navigation__sub__mobile-heading">
                <button class="glue-header__link js-sub-nav-close-mobile" role="menuitem" aria-haspopup="true">
                  <span class="sr-text">Back to</span>
                  <span class="icon icon--caret"></span> Computing Systems &amp; Quantum AI
                  <span class="sr-text">menu</span>
                </button>
                <hr/>
              </div>
              <ul>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/distributed-systems-and-parallel-computing/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Distributed Systems &amp; Parallel Computing
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/hardware-and-architecture/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Hardware &amp; Architecture
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/mobile-systems/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Mobile Systems
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/networking/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Networking
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/quantum-computing/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Quantum Computing
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/robotics/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Robotics
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/security-privacy-and-abuse-prevention/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Security, Privacy, &amp; Abuse Prevention
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/software-engineering/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Software Engineering
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/software-systems/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Software Systems
                                    <span>

                                    </span>
                                </a>

                        </li>

                </ul>

        </div>
    </div>
</li>

<li data-gt-secondary="Science, AI &amp; Society">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">Science, AI &amp; Society</h2>

<ul>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/climate-and-sustainability/"

                            >
                                Climate &amp; Sustainability
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/economics-and-electronic-commerce/"

                            >
                                Economics &amp; Electronic Commerce
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/education-innovation/"

                            >
                                Education Innovation
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/general-science/"

                            >
                                General Science
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/health-bioscience/"

                            >
                                Health &amp; Bioscience
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/human-computer-interaction-and-visualization/"

                            >
                                Human-Computer Interaction and Visualization
                            </a>

                    </li>

                    <li>

                            <a
                                class="navigation__sub__columns__list-link caption js-drawer-link"
                                href="https://research.google/research-areas/responsible-ai/"

                            >
                                Responsible AI
                            </a>

                    </li>

            </ul>

    </div>
    <div class="navigation__sub__columns__mobile">
        <button class="glue-header__link js-sub-nav-target" data-panel="nested" role="menuitem" aria-haspopup="true">
            Science, AI &amp; Society <span class="icon icon--caret"></span>
        </button>

<div class="navigation__nested-sub js-sub-nav-parent">

              <div class="navigation__sub__mobile-heading">
                <button class="glue-header__link js-sub-nav-close-mobile" role="menuitem" aria-haspopup="true">
                  <span class="sr-text">Back to</span>
                  <span class="icon icon--caret"></span> Science, AI &amp; Society
                  <span class="sr-text">menu</span>
                </button>
                <hr/>
              </div>
              <ul>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/climate-and-sustainability/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Climate &amp; Sustainability
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/economics-and-electronic-commerce/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Economics &amp; Electronic Commerce
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/education-innovation/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Education Innovation
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/general-science/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    General Science
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/health-bioscience/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Health &amp; Bioscience
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/human-computer-interaction-and-visualization/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Human-Computer Interaction and Visualization
                                    <span>

                                    </span>
                                </a>

                        </li>

                        <li role="menuitem">

                            <a href="https://research.google/research-areas/responsible-ai/"
                            class="navigation__sub__columns__mobile__link"
                            >
                                    Responsible AI
                                    <span>

                                    </span>
                                </a>

                        </li>

                </ul>

        </div>
    </div>
</li>

</ul>

</div>
</div></div>
        </div>
      </div>

  </li>

<li
    class="glue-header__item  js-sub-nav-parent --parent"
    data-gt-primary="Our work"
  >

    <button
      class="glue-header__link js-sub-nav-target"
      aria-haspopup="true"
      aria-expanded="false"

    >

      <span class="">
        Our work

          <span class="icon icon--caret"></span>

      </span>

    </button>


      <div class="navigation__sub js-sub-nav" role="menu">
        <div class="navigation__sub__container">
          <div class="navigation__sub__mobile-heading">
            <button class="glue-header__link js-sub-nav-close-mobile">
              <span class="sr-text">Back to</span>
              <span class="icon icon--caret"></span> Our work
              <span class="sr-text">menu</span>
            </button>
            <hr/>
          </div>
          <div class="block-nav_drawer_columns_content">

<div class="navigation__sub--content" data-gt-secondary="">
    <div class="navigation__sub__wrapper">

<ul class="navigation__sub__columns">

<li data-gt-secondary="Projects">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Projects
            </h2>

        <p class="navigation__sub__columns__description caption">We regularly open-source projects with the broader research community and apply our developments to Google products.</p>

            <a
            href="https://research.google/resources/our-projects/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Projects</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/resources/our-projects/"

            >
                Projects
            </a>

    </div>
</li>

<li data-gt-secondary="Publications">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Publications
            </h2>

        <p class="navigation__sub__columns__description caption">Publishing our work allows us to share ideas and work collaboratively to advance the field of computer science.</p>

            <a
            href="https://research.google/pubs/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Publications</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/pubs/"

            >
                Publications
            </a>

    </div>
</li>

<li data-gt-secondary="Resources">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Resources
            </h2>

        <p class="navigation__sub__columns__description caption">We make products, tools, and datasets available to everyone with the goal of building a more collaborative ecosystem.</p>

            <a
            href="https://research.google/resources/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Resources</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/resources/"

            >
                Resources
            </a>

    </div>
</li>

</ul>

</div>
</div>
</div>
        </div>
      </div>

  </li>

<li
    class="glue-header__item  js-sub-nav-parent --parent"
    data-gt-primary="Programs &amp; events"
  >

    <button
      class="glue-header__link js-sub-nav-target"
      aria-haspopup="true"
      aria-expanded="false"

    >

      <span class="">
        Programs &amp; events

          <span class="icon icon--caret"></span>

      </span>

    </button>


      <div class="navigation__sub js-sub-nav" role="menu">
        <div class="navigation__sub__container">
          <div class="navigation__sub__mobile-heading">
            <button class="glue-header__link js-sub-nav-close-mobile">
              <span class="sr-text">Back to</span>
              <span class="icon icon--caret"></span> Programs &amp; events
              <span class="sr-text">menu</span>
            </button>
            <hr/>
          </div>
          <div class="block-nav_drawer_columns_content">

<div class="navigation__sub--content" data-gt-secondary="Shaping the future, together.">
    <div class="navigation__sub__wrapper">

            <div class="navigation__sub__heading">
                <h2 class="headline-3">Shaping the future, together.</h2>

                    <a
                        href="https://research.google/programs-and-events/"

                        class="js-drawer-link"
                        >
                        Collaborate with us
                    </a>

            </div>

<ul class="navigation__sub__columns">

<li data-gt-secondary="Student programs">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Student programs
            </h2>

        <p class="navigation__sub__columns__description caption">Supporting the next generation of researchers through a wide range of programming.</p>

            <a
            href="https://research.google/programs-and-events/student-engagement/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Student programs</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/programs-and-events/student-engagement/"

            >
                Student programs
            </a>

    </div>
</li>

<li data-gt-secondary="Faculty programs">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Faculty programs
            </h2>

        <p class="navigation__sub__columns__description caption">Participating in the academic research community through meaningful engagement with university faculty.</p>

            <a
            href="https://research.google/programs-and-events/faculty-engagement/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Faculty programs</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/programs-and-events/faculty-engagement/"

            >
                Faculty programs
            </a>

    </div>
</li>

<li data-gt-secondary="Conferences &amp; events">
    <div class="navigation__sub__columns__desktop">

            <h2 class="headline-6 navigation__sub__columns__heading">
                Conferences &amp; events
            </h2>

        <p class="navigation__sub__columns__description caption">Connecting with the broader research community through events is essential for creating progress in every aspect of our work.</p>

            <a
            href="https://research.google/conferences-and-events/"
            class="glue-inline-link js-drawer-link"
            >
                <span class="sr-text">Learn more about our Conferences &amp; events</span>
                <span aria-hidden="true">Learn more</span>
            </a>

    </div>
    <div class="navigation__sub__columns__mobile">

            <a
                class="glue-header__link"
                href="https://research.google/conferences-and-events/"

            >
                Conferences &amp; events
            </a>

    </div>
</li>

</ul>

<div class="navigation__sub__cta">
                <a  class="glue-button glue-button--high-emphasis js-drawer-link"
                href="https://research.google/programs-and-events/"
                target="_blank" rel="noreferrer noopener"
                >
                    Collaborate with us
                </a>
            </div>

    </div>
</div>
</div>
        </div>
      </div>

  </li>

<li
    class="glue-header__item  "
    data-gt-primary="Careers"
  >

    <a
      class="glue-header__link "
      href="https://research.google/careers/"


    >

      <span class="">
        Careers

      </span>

    </a>


  </li>

<li
    class="glue-header__item  "
    data-gt-primary="Blog"
  >

    <a
      class="glue-header__link "
      href="https://research.google/blog/"


    >

      <span class="">
        Blog

      </span>

    </a>


  </li>

</ul>
        </nav>
      </div>
      <!-- search (hide on search page) -->


      <div class="glue-header__search js-header-search">
        <div class="glue-header__search__input">

<div class="search-input " data-type="header">
  <input type="search" class="caption --empty-search js-search-bar js-gt-search-input"
    placeholder="Search">
  <button class="search-input__button --search js-gt-search-btn">

<svg role="presentation" aria-hidden="true"  class="glue-icon glue-icon--18px ">
  <use href="/gr/static/assets/icons/glue-icons.svg#search"></use>
</svg>

</button>
  <button class="search-input__button --clear">

<svg role="presentation" aria-hidden="true"  class="glue-icon glue-icon--18px ">
  <use href="/gr/static/assets/icons/glue-icons.svg#close"></use>
</svg>

</button>
</div>

</div>
        <button class="glue-header__search__btn js-header-search-btn">

<svg role="presentation" aria-hidden="true" aria-hidden="true" class="glue-icon glue-icon--24px search">
  <use href="/gr/static/assets/icons/glue-icons.svg#search"></use>
</svg>

<svg role="presentation" aria-hidden="true" aria-hidden="true" class="glue-icon glue-icon--24px close">
  <use href="/gr/static/assets/icons/glue-icons.svg#close"></use>
</svg>

<span class="sr-text js-header-search-sr-text">Search</span>
        </button>
      </div>

    </div>
  </div>
  <div class="glue-header__drawer-backdrop">
    <div class="glue-header__mobile_close">
      <button class="glue-header__drawer-toggle-btn js-mobile-nav-close" aria-label="Close the navigation drawer">
        <svg class="glue-icon glue-icon--24px" role="presentation" aria-hidden="true">
          <use href="/gr/static/assets/icons/glue-icons.svg#close"></use>
        </svg>
      </button>
    </div>
  </div>
</header>

<main id="page-content">

<div class="blog-detail-page --legacy " >

<section class="basic-hero bhoig --theme-dark  --large-image" data-gt-id="basic_hero" data-gt-component-name="">
  <div class="glue-page">
    <div class="glue-grid">
      <div class="bhoig__image-wrapper glue-grid__col--span-4 glue-grid__col--span-5-md glue-grid__col--span-4-lg">




            <div class="bhoig__image-bg" style="">

                <picture>
                  <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/825fe036e00e3833b7bb7962fcd1ab05-image1.png" alt="" class=""/>
                </picture>

            </div>


    </div>

<div class="bhoig__breadcrumb-wrapper glue-grid__col--span-10 glue-grid__col--span-9-md glue-grid__col--span-10-lg">

<nav class="glue-breadcrumbs" aria-label="Breadcrumbs">

    <ol class="glue-breadcrumbs__list">




        <li class="glue-breadcrumbs__item">
            <a class="glue-breadcrumbs__link attribution" href="/">Home</a>

<svg role="presentation" aria-hidden="true"  class="glue-icon  ">
  <use href="/gr/static/assets/icons/glue-icons.svg#chevron-right"></use>
</svg>

</li>



        <li class="glue-breadcrumbs__item">
            <a class="glue-breadcrumbs__link attribution" href="/blog/">Blog</a>

<svg role="presentation" aria-hidden="true"  class="glue-icon  ">
  <use href="/gr/static/assets/icons/glue-icons.svg#chevron-right"></use>
</svg>

</li>


    </ol>

</nav>
        </div>

<h1 class="headline-1 bhoig__headline glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">Characterizing Emergent Phenomena in Large Language Models</h1>

<div class="basic-hero__description bhoig__description glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">
            <div class="basic-hero--blog-detail__description"><p>November 10, 2022</p><span class="dot-separator"></span><p>Posted by Jason Wei and Yi Tay, Research Scientists, Google Research, Brain Team</p></div>
          </div>

<div class="bhoig__cta glue-grid__col--span-8 glue-grid__col--span-7-md glue-grid__col--span-8-lg">

        </div>
    </div>
  </div>
</section>

<div class="glue-page">
        <div class="glue-grid blog-detail-page__grid">
            <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md  glue-grid__col--span-9-lg">


                <div class="quicklinks-wrapper--mobile">
                    <div class="block-quick_links">

<section class="quicklinks">

        <h2 class="eyebrow">Quick links</h2>
        <ul class="quicklinks__list">


            <li class="quicklinks__item quicklinks__item--share js-quicklinks-share">
                <button
                    class="quicklinks__share-button js-quicklinks-share__button"
                    aria-expanded="false"
                    aria-controls="js-quicklinks-share__list">
                    <span class="icon icon--share"></span>
                    <span class="quicklinks__item__text">Share</span>
                </button>

<section class="glue-social glue-social--monochrome quicklinks__share-list js-quicklinks-share__list glue-elevation-level-1 js-gt-share-wrapper">
  <div class="glue-social__group">
    <ul class="glue-social__list" role="list">

<li class="glue-social__item">
        <a class="glue-social__link" href="https://twitter.com/intent/tweet?text=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/"
            title="Share on Twitter" target="_blank" rel="noopener" data-gt-method="x">
            <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--24px">
              <use href="/gr/static/assets/icons/twitter-x.svg#twitter-x"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/"
            title="Share on Facebook" target="_blank" rel="noopener" data-gt-method="facebook">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-facebook glue-icon--24px">
            <use href="/gr/static/assets/icons/facebook.svg#facebook"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.linkedin.com/shareArticle?url=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/&amp;mini=true" title="Share on LinkedIn" target="_blank" rel="noopener" data-gt-method="linkedin">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-linkedin glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#post-linkedin"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" title="Send via Email" data-gt-method="email">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-sharemail glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#email"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <div class="glue-social__popover">
          <div class="glue-social__icon-trigger" aria-label="Get shareable link" title="Get shareable link" id="share-static-popover-trigger">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
          </div>

<div class="glue-social__dialog" id="share-popover-dialog">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/public/icons/glue-icons.svg#link"></use>
            </svg>
            <div class="glue-social__copy" glue-copy-success="Copied to clipboard"
                glue-copy-fail="Press Ctrl+C or ⌘+C to copy">
              <input class="glue-social__copy-input" readonly="" type="text"
                  value="https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" aria-label="URL">
              <button class="glue-social__copy-btn" id="share-copy-btn" data-gt-method="link-copied">Copy link</button>
            </div>
            <div aria-label="Close" class="glue-social__close-btn">
              ×
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</section>
            </li>

        </ul>

</section>
</div>
                </div>

<div class="blog-detail-wrapper js-gt-blog-detail-wrapper" data-gt-publish-date="20221110">


    <div class="rich-text --theme- --mode-" data-gt-id="rich_text" data-gt-component-name="">

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJoQyQGqe67BekuWDn30rdtn9W1Lf7RvMeUKtoK2aoYziWIDOMAitiRYViKdyK-KYexgbDxExs3rxw2v306JK-tyZLNd5_6Y5LanpyDux6oiH7NhExBXwPUnJnUnrHUyjF5Y9k_ekMu6y0ZUPNbbn7tkQ7NVOXTMz2w2-3oDs_Pj-Ll64LyB4tkWLVqQ/s732/image1.png" style="display: none;" />

<p>
The field of natural language processing (NLP) has been revolutionized by language models trained on large amounts of text data. Scaling up the size of language models often leads to improved performance and sample efficiency on a range of downstream NLP tasks. In many cases, the performance of a large language model can be predicted by extrapolating the performance trend of smaller models. For instance, the effect of scale on language model <a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener noreferrer">perplexity</a> has been empirically shown to span more than <a href="https://arxiv.org/abs/2001.08361" target="_blank" rel="noopener noreferrer">seven orders of magnitude</a>.
</p>
<a name='more'></a>
<p>
On the other hand, performance for certain other tasks does not improve in a predictable fashion. For example, the <a href="https://arxiv.org/pdf/2005.14165.pdf" target="_blank" rel="noopener noreferrer">GPT-3 paper</a> showed that the ability of language models to perform multi-digit addition has a flat scaling curve (approximately random performance) for models from 100M to 13B parameters, at which point the performance jumped substantially. Given the growing use of language models in NLP research and applications, it is important to better understand abilities such as these that can arise unexpectedly.
</p>
<p>
In “<a href="https://openreview.net/forum?id=yzkSU5zdwD" target="_blank" rel="noopener noreferrer">Emergent Abilities of Large Language Models</a>,” recently published in the <em><a href="https://www.jmlr.org/tmlr/" target="_blank" rel="noopener noreferrer">Transactions on Machine Learning Research</a></em> (TMLR), we discuss the phenomena of <em>emergent abilities</em>, which we define as abilities that are not present in small models but are present in larger models. More specifically, we study emergence by analyzing the performance of language models as a function of language model scale, as measured by total <a href="https://en.wikipedia.org/wiki/Floating-point_arithmetic" target="_blank" rel="noopener noreferrer">floating point operations</a> (FLOPs), or how much compute was used to train the language model. However, we also explore emergence as a function of other variables, such as dataset size or number of model parameters (see the paper for full details). Overall, we present dozens of examples of emergent abilities that result from scaling up language models. The existence of such emergent abilities raises the question of whether additional scaling could potentially further expand the range of capabilities of language models.
</p>
<div style="line-height: 40%;">
    <br />
</div>
<h2>Emergent Prompted Tasks</h2>

<p>
First we discuss emergent abilities that may arise in prompted tasks. In such tasks, a pre-trained language model is given a prompt for a task framed as next word prediction, and it performs the task by completing the response. Without any further fine-tuning, language models can often perform tasks that were not seen during training.
</p>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigsk_RT3zBrzSTftNq6czTHYkv3izej5wCEhxNrjnoUrvIPt0aJLsV8s4zIgpnyoPysHobWFhHuzCU-B30AItGMAmYRMEWY_Pp--lLmQ6--oMMWrRciyDDv7qD1zf4Y--i7avr9EHv2nsz4Q7hHTY5-JeXFKHhbUttmVruMd8Py_fqCUtaAKCwHyOF_A/s1288/image2.png" target="_blank" rel="noopener noreferrer"><img border="0" data-original-height="341" data-original-width="1288" height="169" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigsk_RT3zBrzSTftNq6czTHYkv3izej5wCEhxNrjnoUrvIPt0aJLsV8s4zIgpnyoPysHobWFhHuzCU-B30AItGMAmYRMEWY_Pp--lLmQ6--oMMWrRciyDDv7qD1zf4Y--i7avr9EHv2nsz4Q7hHTY5-JeXFKHhbUttmVruMd8Py_fqCUtaAKCwHyOF_A/w640-h169/image2.png" width="640" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Example of few-shot prompting on movie review sentiment classification. The model is given one example of a task (classifying a movie review as positive or negative) and then performs the task on an unseen example.</td></tr></tbody></table>
<p>
We call a prompted task emergent when it unpredictably surges from random performance to above-random at a specific scale threshold. Below we show three examples of prompted tasks with emergent performance: <a href="https://github.com/google/BIG-bench/tree/main/bigbench/benchmark_tasks/modified_arithmetic" target="_blank" rel="noopener noreferrer">multi-step arithmetic</a>, taking <a href="https://arxiv.org/abs/2009.03300" target="_blank" rel="noopener noreferrer">college-level exams</a>, and <a href="https://pilehvar.github.io/wic/" target="_blank" rel="noopener noreferrer">identifying the intended meaning of a word</a>. In each case, language models perform poorly with very little dependence on model size up to a threshold at which point their performance suddenly begins to excel.
</p>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl5PSqGGHMWNxwav2cdB6GaoiHCrKESFwkRXQ6VJmJxVGCjcuQhqJsey9EiCQW6WUKaHDaMCmYj9LGxZaVuU5DpHTh9-Wl0pRzlTybDC2WES0_jSjmyGHcHKku9XZECXceG1TCtH5DNocVj-0PQHTztf_5Zzo7Ijrj8jlT_kClaW72fxzj4-3SQOwtNQ/s1013/image4.png" target="_blank" rel="noopener noreferrer"><img border="0" data-original-height="487" data-original-width="1013" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhl5PSqGGHMWNxwav2cdB6GaoiHCrKESFwkRXQ6VJmJxVGCjcuQhqJsey9EiCQW6WUKaHDaMCmYj9LGxZaVuU5DpHTh9-Wl0pRzlTybDC2WES0_jSjmyGHcHKku9XZECXceG1TCtH5DNocVj-0PQHTztf_5Zzo7Ijrj8jlT_kClaW72fxzj4-3SQOwtNQ/s16000/image4.png" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">The ability to perform multi-step arithmetic (<strong>left</strong>), succeed on college-level exams (<strong>middle</strong>), and identify the intended meaning of a word in context (<strong>right</strong>) all emerge only for models of sufficiently large scale. The models shown include <a href="https://arxiv.org/abs/2201.08239" target="_blank" rel="noopener noreferrer">LaMDA</a>, <a href="https://arxiv.org/abs/2005.14165" target="_blank" rel="noopener noreferrer">GPT-3</a>, <a href="https://arxiv.org/abs/2112.11446" target="_blank" rel="noopener noreferrer">Gopher</a>, <a href="https://arxiv.org/abs/2203.15556" target="_blank" rel="noopener noreferrer">Chinchilla</a>, and <a href="https://arxiv.org/abs/2204.02311" target="_blank" rel="noopener noreferrer">PaLM</a>.</td></tr></tbody></table>
<p>
Performance on these tasks only becomes non-random for models of sufficient scale — for instance, above 10<sup>22</sup> training FLOPs for the arithmetic and multi-task NLU tasks, and above 10<sup>24</sup> training FLOPs for the word in context tasks. Note that although the scale at which emergence occurs can be different for different tasks and models, no model showed smooth improvement in behavior on any of these tasks. Dozens of other emergent prompted tasks are listed <a href="https://openreview.net/forum?id=yzkSU5zdwD" target="_blank" rel="noopener noreferrer">in our paper</a>.
</p>
<div style="line-height: 40%;">
    <br />
</div>
<h2>Emergent Prompting Strategies</h2>

<p>
The second class of emergent abilities encompasses <em>prompting strategies</em> that augment the capabilities of language models. Prompting strategies are broad paradigms for prompting that can be applied to a range of different tasks. They are considered emergent when they fail for small models and can only be used by a sufficiently-large model.
</p>
<p>
One example of an emergent prompting strategy is called “<a href="https://twitter.com/Google/status/1525188695875366912" target="_blank" rel="noopener noreferrer">chain-of-thought prompting</a>”, for which the model is prompted to generate a series of intermediate steps before giving the final answer. Chain-of-thought prompting enables language models to perform tasks requiring complex reasoning, such as a multi-step math word problem. Notably, models acquire the ability to do chain-of-thought reasoning without being explicitly trained to do so. An example of chain-of-thought prompting is shown in the figure below.
</p>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjO6jryw6Oesg8YVxsa2hl2b5FSoBVfzuDou3U9LA9U6cBAIMbV1MZs5ZX5XLMHGg2jd29FPYpabC9hn7PgfC1qLDKMS7sWz6ay8XTKupyB0cB4EHu8ZpRkftQTMP5gFxyXiAPQ-dBscd6-QFEdp_P1qaUADthj0DOZ8zrZb1dBNd6nbzy4tFR-rtjkCw/s793/image3.png" target="_blank" rel="noopener noreferrer"><img border="0" data-original-height="370" data-original-width="793" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjO6jryw6Oesg8YVxsa2hl2b5FSoBVfzuDou3U9LA9U6cBAIMbV1MZs5ZX5XLMHGg2jd29FPYpabC9hn7PgfC1qLDKMS7sWz6ay8XTKupyB0cB4EHu8ZpRkftQTMP5gFxyXiAPQ-dBscd6-QFEdp_P1qaUADthj0DOZ8zrZb1dBNd6nbzy4tFR-rtjkCw/s16000/image3.png" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Chain of thought prompting enables sufficiently large models to solve multi-step reasoning problems.</td></tr></tbody></table>
<p>
The empirical results of chain-of-thought prompting are shown below. For smaller models, applying chain-of-thought prompting does not outperform standard prompting, for example, when applied to <a href="https://arxiv.org/abs/2110.14168" target="_blank" rel="noopener noreferrer">GSM8K</a>, a challenging benchmark of math word problems. However, for large models (10<sup>24</sup> FLOPs), chain-of-thought prompting substantially improves performance in our tests, reaching a 57% solve rate on GSM8K.
</p>

<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto;"><tbody><tr><td style="text-align: center;"><a href="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDr6dLlvyfWclgmTuqlzEQ0Ge-x2CUywoKXoozXO5wMJgw5ZERIzqRy59_aDr_P9YOC3XEZ1wFqoPWmGgP26-DvdJUMzHx9-i2Nc8fyDGIwu9s5kYyhDkadS8s4azusiper7nDPk7fgUe4dNM9KVgbQkZoO3AiXQ8-rIJ4CN3YY4US2g3Us-oMNr9gPQ/s732/image1.png" target="_blank" rel="noopener noreferrer"><img border="0" data-original-height="561" data-original-width="732" height="306" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDr6dLlvyfWclgmTuqlzEQ0Ge-x2CUywoKXoozXO5wMJgw5ZERIzqRy59_aDr_P9YOC3XEZ1wFqoPWmGgP26-DvdJUMzHx9-i2Nc8fyDGIwu9s5kYyhDkadS8s4azusiper7nDPk7fgUe4dNM9KVgbQkZoO3AiXQ8-rIJ4CN3YY4US2g3Us-oMNr9gPQ/w400-h306/image1.png" width="400" /></a></td></tr><tr><td class="tr-caption" style="text-align: center;">Chain-of-thought prompting is an emergent ability — it fails to improve performance for small language models, but substantially improves performance for large models. Here we illustrate the difference between standard and chain-of-thought prompting at different scales for two language models, <a href="https://ai.googleblog.com/2022/01/lamda-towards-safe-grounded-and-high.html" target="_blank" rel="noopener noreferrer">LaMDA</a> and <a href="https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html" target="_blank" rel="noopener noreferrer">PaLM</a>.</td></tr></tbody></table>

<div style="line-height: 40%;">
    <br />
</div>
<h2>Implications of Emergent Abilities</h2>

<p>
The existence of emergent abilities has a range of implications. For example, because emergent few-shot prompted abilities and strategies are not explicitly encoded in pre-training, researchers may not know the full scope of few-shot prompted abilities of current language models. Moreover, the emergence of new abilities as a function of model scale raises the question of whether further scaling will potentially endow even larger models with new emergent abilities.
</p>
<p>
Identifying emergent abilities in large language models is a first step in understanding such phenomena and their potential impact on future model capabilities. Why does scaling unlock emergent abilities? Because computational resources are expensive, can emergent abilities be unlocked via other methods without increased scaling (e.g., better model architectures or training techniques)? Will new real-world applications of language models become unlocked when certain abilities emerge? Analyzing and understanding the behaviors of language models, including emergent behaviors that arise from scaling, is an important research question as the field of NLP continues to grow.
</p>
<div style="line-height: 40%;">
    <br />
</div>
<h2>Acknowledgements</h2>

<p>
<em>It was an honor and privilege to work with Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, and William Fedus.</em>
</p>
</div>

</div>

<section aria-label="List of footnotes" data-gt-id="footnotes" data-gt-component-name="Footnotes">
  <ol class="js-footnotes footnotes">

  </ol>
</section>

<section class="blog-labels" data-gt-id="blog_labels" data-gt-component-name="Blog Labels">
    <ul class="blog-labels__list">
        <span class="caption">Labels:</span>

        <li class="caption">
            <a class="caption" href="/blog/label/conferences-events">Conferences &amp; Events</a>

        </li>

    </ul>
</section>

</div>

                <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-3-lg">
                    <div class="quicklinks-wrapper--desktop quicklinks-wrapper--sticky">
                        <div class="block-quick_links">

<section class="quicklinks">

        <h2 class="eyebrow">Quick links</h2>
        <ul class="quicklinks__list">


            <li class="quicklinks__item quicklinks__item--share js-quicklinks-share">
                <button
                    class="quicklinks__share-button js-quicklinks-share__button"
                    aria-expanded="false"
                    aria-controls="js-quicklinks-share__list">
                    <span class="icon icon--share"></span>
                    <span class="quicklinks__item__text">Share</span>
                </button>

<section class="glue-social glue-social--monochrome quicklinks__share-list js-quicklinks-share__list glue-elevation-level-1 js-gt-share-wrapper">
  <div class="glue-social__group">
    <ul class="glue-social__list" role="list">

<li class="glue-social__item">
        <a class="glue-social__link" href="https://twitter.com/intent/tweet?text=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/"
            title="Share on Twitter" target="_blank" rel="noopener" data-gt-method="x">
            <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--24px">
              <use href="/gr/static/assets/icons/twitter-x.svg#twitter-x"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.facebook.com/sharer/sharer.php?u=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/"
            title="Share on Facebook" target="_blank" rel="noopener" data-gt-method="facebook">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-facebook glue-icon--24px">
            <use href="/gr/static/assets/icons/facebook.svg#facebook"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="https://www.linkedin.com/shareArticle?url=https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/&amp;mini=true" title="Share on LinkedIn" target="_blank" rel="noopener" data-gt-method="linkedin">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-linkedin glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#post-linkedin"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <a class="glue-social__link" href="mailto:name@example.com?subject=Check%20out%20this%20site&body=Check%20out%20https%3A//research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" title="Send via Email" data-gt-method="email">
          <svg role="presentation" aria-hidden="true"
              class="glue-icon glue-icon--social glue-icon--color-sharemail glue-icon--24px">
            <use href="/gr/static/assets/icons/glue-icons.svg#email"></use>
          </svg>
        </a>
      </li>
      <li class="glue-social__item">
        <div class="glue-social__popover">
          <div class="glue-social__icon-trigger" aria-label="Get shareable link" title="Get shareable link" id="share-static-popover-trigger">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/gr/static/assets/icons/glue-icons.svg#link"></use>
            </svg>
          </div>

<div class="glue-social__dialog" id="share-popover-dialog">
            <svg role="presentation" aria-hidden="true"
                class="glue-icon glue-icon--social glue-icon--color-sharelink glue-icon--24px">
              <use href="/public/icons/glue-icons.svg#link"></use>
            </svg>
            <div class="glue-social__copy" glue-copy-success="Copied to clipboard"
                glue-copy-fail="Press Ctrl+C or ⌘+C to copy">
              <input class="glue-social__copy-input" readonly="" type="text"
                  value="https://research.google/blog/characterizing-emergent-phenomena-in-large-language-models/" aria-label="URL">
              <button class="glue-social__copy-btn" id="share-copy-btn" data-gt-method="link-copied">Copy link</button>
            </div>
            <div aria-label="Close" class="glue-social__close-btn">
              ×
            </div>
          </div>
        </div>
      </li>
    </ul>
  </div>
</section>
            </li>

        </ul>

</section>
</div>
                    </div>
                </div>

        </div>
    </div>

<section class="related-posts offset-two-up --theme-dark" data-gt-id="related_blog_posts" data-gt-component-name="Related Blog Posts">
    <div class="glue-page glue-grid">
        <div
            class="offset-two-up__left-col glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-3-lg">
            <h3 class="offset-two-up__headline headline-3">Other posts of interest</h3>
        </div>
        <div class="glue-grid__col glue-grid__col--span-4-sm glue-grid__col--span-12-md glue-grid__col--span-9-lg">
            <ul class="card-stack--basic nested-glue-grid-override">

                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">

<a class="glue-card not-glue " href="/blog/codeclm-aligning-language-models-with-tailored-synthetic-data/" aria-label="" >

<div class="glue-card__inner">

<div class="related-posts__image">



    <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/CodecLM1-Hero.png" alt="" />
</div>

<div class="glue-card__content --no-media">

    <p class="glue-label glue-spacer-1-bottom">May 30, 2024</p>

<span class="headline-5 js-gt-item-id">
      CodecLM: Aligning language models with tailored synthetic data
    </span>

</div>

<ul class="glue-card__link-list">

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Conferences &amp; Events

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Machine Intelligence

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Natural Language Processing

                </span>
            </li>

    </ul>

</div>

</a>

</li>

                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">

<a class="glue-card not-glue " href="/blog/google-research-at-google-io-2024/" aria-label="" >

<div class="glue-card__inner">

<div class="related-posts__image">



    <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/GRatIO2024-1-logo.png" alt="" />
</div>

<div class="glue-card__content --no-media">

    <p class="glue-label glue-spacer-1-bottom">May 24, 2024</p>

<span class="headline-5 js-gt-item-id">
      Google Research at Google I/O 2024
    </span>

</div>

<ul class="glue-card__link-list">

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Conferences &amp; Events

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Generative AI

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Health &amp; Bioscience

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Machine Intelligence

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Product

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Quantum

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Responsible AI

                </span>
            </li>

    </ul>

</div>

</a>

</li>

                <li class="glue-grid__col glue-grid__col--span-4-md glue-grid__col--span-4-sm">

<a class="glue-card not-glue " href="/blog/soar-new-algorithms-for-even-faster-vector-search-with-scann/" aria-label="" >

<div class="glue-card__inner">

<div class="related-posts__image">



    <img src="https://storage.googleapis.com/gweb-research2023-media/original_images/SOAR6-ResultsHero.png" alt="" />
</div>

<div class="glue-card__content --no-media">

    <p class="glue-label glue-spacer-1-bottom">April 10, 2024</p>

<span class="headline-5 js-gt-item-id">
      SOAR: New algorithms for even faster vector search with ScaNN
    </span>

</div>

<ul class="glue-card__link-list">

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Algorithms &amp; Theory

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Conferences &amp; Events

                    <span class="glue-card__link-list__spacer">&#183;</span>

                </span>
            </li>

            <li class="glue-card__link-list__item">
                <span class="not-glue caption">
                    Data Mining &amp; Modeling

                </span>
            </li>

    </ul>

</div>

</a>

</li>

            </ul>
        </div>
    </div>
</section>

</div>

</main>

<footer class="glue-footer">

    <div class="glue-page">
        <section class="glue-social">
            <div class="glue-social__group glue-social--monochrome">
                <p class="glue-social__title glue-social__title--inline">
                    Follow us
                </p>
                <nav class="js-gt-follow-us-wrapper" aria-label="Social media links">
                    <ul class="glue-social__list" role="list">

                        <li class="glue-social__item">
                            <a class="glue-social__link"
                                href="https://x.com/GoogleResearch"
                                title="Follow us on x"
                                target="_blank"
                                rel="noopener"
                                data-gt-method="x""
                            >
                                <svg role="presentation" aria-hidden="true"
                                    class="glue-icon glue-icon--social glue-icon--24px">

                                    <use href="/gr/static/assets/icons/twitter-x.svg#twitter-x"></use>

                                </svg>
                            </a>
                        </li>

                        <li class="glue-social__item">
                            <a class="glue-social__link"
                                href="https://www.linkedin.com/showcase/googleresearch/"
                                title="Follow us on linkedin"
                                target="_blank"
                                rel="noopener"
                                data-gt-method="linkedin""
                            >
                                <svg role="presentation" aria-hidden="true"
                                    class="glue-icon glue-icon--social glue-icon--24px">

                                    <use href="/gr/static/assets/icons/glue-icons.svg#post-linkedin"></use>

                                </svg>
                            </a>
                        </li>

                        <li class="glue-social__item">
                            <a class="glue-social__link"
                                href="https://www.youtube.com/c/GoogleResearch"
                                title="Follow us on youtube"
                                target="_blank"
                                rel="noopener"
                                data-gt-method="youtube""
                            >
                                <svg role="presentation" aria-hidden="true"
                                    class="glue-icon glue-icon--social glue-icon--24px">

                                    <use href="/gr/static/assets/icons/glue-icons.svg#video-youtube"></use>

                                </svg>
                            </a>
                        </li>

                        <li class="glue-social__item">
                            <a class="glue-social__link"
                                href="https://github.com/google-research"
                                title="Follow us on github"
                                target="_blank"
                                rel="noopener"
                                data-gt-method="github""
                            >
                                <svg role="presentation" aria-hidden="true"
                                    class="glue-icon glue-icon--social glue-icon--24px">

                                    <use href="/gr/static/assets/icons/github.svg#github"></use>

                                </svg>
                            </a>
                        </li>

                    </ul>
                </nav>
            </div>
        </section>
    </div>
    <div class="glue-fullbleed"></div>

    <section class="glue-page">
        <nav class="glue-footer__global" aria-label="Footer resource links">
            <div class="glue-footer__logo">
                <a href="https://www.google.com" title="Google" class="glue-footer__link">

<svg role="presentation" aria-hidden="true"  class="glue-icon  glue-footer__logo-img">
  <use href="/gr/static/assets/icons/glue-icons.svg#google-solid-logo"></use>
</svg>

</a>
            </div>
            <ul class="glue-footer__global-links glue-no-bullet js-gt-global-nav-wrapper" role="list">

                <li class="glue-footer__global-links-list-item" data-gt-primary="About Google">
                    <a class="glue-footer__link" href="https://about.google/" target="_blank" rel="noopener">
                        About Google
                    </a>
                </li>

                <li class="glue-footer__global-links-list-item" data-gt-primary="Google Products">
                    <a class="glue-footer__link" href="https://about.google/intl/en/products/" target="_blank" rel="noopener">
                        Google Products
                    </a>
                </li>

                <li class="glue-footer__global-links-list-item" data-gt-primary="Privacy">
                    <a class="glue-footer__link" href="https://policies.google.com/privacy" target="_blank" rel="noopener">
                        Privacy
                    </a>
                </li>

                <li class="glue-footer__global-links-list-item" data-gt-primary="Terms">
                    <a class="glue-footer__link" href="https://policies.google.com/terms" target="_blank" rel="noopener">
                        Terms
                    </a>
                </li>

            </ul>
            <ul class="glue-footer__global-links glue-footer__global-links--extra glue-no-bullet" role="list">
                <li class="glue-footer__global-links-list-item
            glue-footer__global-links-list-item--extra">
                    <a class="glue-footer__link" href="https://support.google.com/?hl=en">

<svg role="presentation" aria-hidden="true" aria-hidden="true" class="glue-icon glue-icon--24px glue-icon--footer-help">
  <use href="/gr/static/assets/icons/glue-icons.svg#help"></use>
</svg>

Help
                    </a>
                </li>
                <li class="glue-footer__global-links-list-item
            glue-footer__global-links-list-item--extra">

                        <button
                            class="glue-footer__link google-feedback js-feedback-button"
                            href=""
                            data-product-id="5137383"
                        >
                            Submit feedback
                        </button>

                </li>
            </ul>
        </nav>
    </section>
</footer>

<script>
        var scriptUrl = "https://www.gstatic.com/glue/v27_1/material-components-web.min.js";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "https://www.youtube.com/player_api";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "/gr/static/js/googleresearch.js?id=8e3aa9c2c986c2677a642446234e23b3";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>
    <script>
        var scriptUrl = "https://support.google.com/inapp/api.js";
        var scriptElement = document.createElement('script');
        scriptElement.async = false;
        scriptElement.src = scriptUrl;
        document.body.appendChild(scriptElement);
    </script>

<script>
        var scripts = [
            "https://www.gstatic.com/glue/cookienotificationbar/cookienotificationbar.min.js"
        ];

scripts.forEach(function(scriptUrl) {
            var scriptElement = document.createElement('script');
            scriptElement.async = false;
            scriptElement.src = scriptUrl;
            scriptElement.setAttribute("data-glue-cookie-notification-bar-category", "2B");
            document.body.appendChild(scriptElement);
        });
    </script>
</body>

</html>
