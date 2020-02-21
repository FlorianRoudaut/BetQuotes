"""Test to read a web page from PMU"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/home/florian/Documents/Dev/BetQuotes/')

import unittest
from WebScrapping.html_builder import build_html_tree

TEST_PAGE = r"""<!DOCTYPE html>
<html lang="fr" dir="ltr"
  xmlns:fb="http://ogp.me/ns/fb#">
<head>
  <link rel="profile" href="http://www.w3.org/1999/xhtml/vocab" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="alternate" media="only screen and (max-width: 640px)" href="https://mobile.parier.pmu.fr/PMU-Webkit/page/sportif/match?matchId=666562" />
<link rel="shortcut icon" href="https://paris-sportifs.pmu.fr/profiles/core/themes/pmu_theme/favicon.ico" type="image/vnd.microsoft.icon" />
<meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:15" />
<script type="application/ld+json">{
    "@context": "http://schema.org",
    "@type": "SportsEvent",
    "startDate": "2020-02-16T15:50:00",
    "location": {
        "@type": "Place",
        "name": "TOP 14",
        "address": {
            "@type": "PostalAddress",
            "name": ""
        }
    },
    "name": "Racing 92 // Toulouse",
    "url": "https://paris-sportifs.pmu.fr/event/666562",
    "homeTeam": {
        "@context": "http://schema.org",
        "@type": "SportsTeam",
        "name": "Racing 92 ",
        "sport": "Rugby"
    },
    "awayTeam": {
        "@context": "http://schema.org",
        "@type": "SportsTeam",
        "name": " Toulouse",
        "sport": "Rugby"
    },
    "description": "Paris sportifs sur PMU.FR avec les cotes du match de Rugby Racing 92 // Toulouse. Pariez sur ce match de TOP 14 du dimanche 16 février 2020."
}</script>
<meta name="description" content="Paris sportifs sur PMU.fr. avec les cotes pour pimenter le match Racing 92 // Toulouse de Rugby de TOP 14 Promotions, et offres de bienvenue du PMU : jusqu’à 100 euros offerts." />
<meta property="fb:pages" content="125532387462663" />
  <title>Racing 92 // Toulouse - TOP 14 - Rugby: cotes et paris en ligne sur PMU.fr</title>
  <link type="text/css" rel="stylesheet" href="https://paris-sportifs.pmu.fr/sites/default/files/css/css_lQaZfjVpwP_oGNqdtWCSpJT1EMqXdMiU84ekLLxQnc4.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://paris-sportifs.pmu.fr/sites/default/files/css/css_6zemUaNACzZ5sPLowbJJP0jVAcgeofg1dmXJdb1dfGY.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://paris-sportifs.pmu.fr/sites/default/files/css/css_6kkpI4h4QNswBE6c3MU19aH-V7_oWRgqkyIFywcjKM0.css" media="all" />
<style>.node-type-landing-page.live,.page-event.live-event{background-image:url(https://paris-sportifs.pmu.fr/sites/default/files/Live_Page_image_1711x1041_Football_3.jpg)}
</style>
<link type="text/css" rel="stylesheet" href="https://paris-sportifs.pmu.fr/sites/default/files/css/css_LJunFicg1BtnOKeqixf9ICvofIujWHYWHSCHNw7eI0U.css" media="all" />
<link type="text/css" rel="stylesheet" href="https://paris-sportifs.pmu.fr/sites/default/files/css/css_OmVveoTuqhStmQAnU9EacT94e6xiYttwdqboR40rToE.css" media="all" />
  <!-- HTML5 element support for IE6-8 -->
  <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->

  <script>
    var page_build_time = 1581623591
</script>
</head>
<body class="html not-front not-logged-in no-sidebars page-event page-event-666562 fantasy-league-page jackpot-page tc-track-page-loads i18n-fr-ob"  data-name="sportif.parier.sports.competition.match" data-sport_id="rugby" data-compet_id="top_14" data-event_id="racing_92__toulouse">
  <div id="skip-link">
    <a href="#main-content" class="element-invisible element-focusable">Skip to main content</a>
  </div>
  <div id="cookie-compliance" class="cookie-compliance clearfix">
  <div class="cookie-compliance__inner">
    <div class="cookie-compliance__text">
          <p>En poursuivant votre navigation, vous acceptez l'utilisation des cookies pour vous proposer des services et des offres adaptés à vos centres d'intérêts Pour en savoir plus, <a href="https://www.pmu.fr/turf/#!/informations-legales/3" target="_blank" class="cnil-link">Cliquez ici</a>.</p>
        </div>
          <form action="/event/666562" method="post" id="simple-cookie-compliance-dismiss-form" accept-charset="UTF-8"><div><button class="cookie-compliance__button btn form-submit" type="submit" id="edit-submit" name="op" value=""></button>
<input type="hidden" name="form_build_id" value="form-nXoL_9yQOXVapuL1K7YjXjJsHXgBWwMcISmSnZI3RTE" />
<input type="hidden" name="form_id" value="simple_cookie_compliance_dismiss_form" />
</div></form>      </div>
</div>

<noscript>
  <div class="cookie-compliance clearfix">
    <div class="cookie-compliance__inner">
      <div class="cookie-compliance__text">
              <p>En poursuivant votre navigation, vous acceptez l'utilisation des cookies pour vous proposer des services et des offres adaptés à vos centres d'intérêts Pour en savoir plus, <a href="https://www.pmu.fr/turf/#!/informations-legales/3" target="_blank" class="cnil-link">Cliquez ici</a>.</p>
            </div>
              <form action="/event/666562" method="post" id="simple-cookie-compliance-dismiss-form" accept-charset="UTF-8"><div></div></form>          </div>
  </div>
</noscript>
      <div class="region region-header">
    
<div class="alert-msg-wrapper">
  <section id="block-bean-arjel-banner" class="block block-bean clearfix">

            
    
<div  class="pmu-ds-image-banner entity entity-bean bean-image-banner view-mode-default">
  
      <a href="http://www.joueurs-info-service.fr/"
       data-attr-title="arjel_banner_-_header_-_ne_jamais_enlever"       class="pmu-ds-image-link ">

              <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/jeu-responsable-blanc.gif?time=1463150891" width="579" height="60" alt="" />      
    </a>
  
</div>



  </section>
</div>
  </div>
<div id="header-wrapper">
  <div class="container container-fluidable" data-fluid="1200">
    <div class="row">
      <div class="col-sm-12 col-md-9 col-lg-12">
        <!-- Header -->
        <header id="header">
          <div class="header-wrapper">
            <div class="row">
              <div class="col-sm-12 col-lg-7">
                <div class="row">
                  <div class="col-sm-3">
                    <a href="#" class="header--burger overlay-trigger" data-target-name="#sidebar-left" data-action="open">
                      <span class="glyphicon glyphicon-menu-hamburger"></span>
                    </a>
                                          <a class="header--logo" href="/" title="Domicile">
                        <img class="logo-pmu" src="https://paris-sportifs.pmu.fr/profiles/core/themes/pmu_theme/logo.png" alt="Domicile"/>
                      </a>
                                      </div>
                  <div class="col-sm-9">
                    <nav id="header-menu-pmu" class="header-menu-pmu" role="navigation">
                                              <ul><li class="first expanded header-menu-pmu--hippique dropdown"><a href="https://www.pmu.fr/" class="tc-header-hippiques dropdown-toggle" data-target="#dropdown" data-toggle="dropdown">Paris hippiques<span class="glyphicon glyphicon-triangle-bottom"></span></a><ul class="dropdown-menu"><li class="first leaf"><a href="https://www.pmu.fr/turf/">En ligne</a></li>
<li class="last leaf header-menu-pmu--last-element"><a href="https://info.pmu.fr/" target="_blank">En point de vente</a></li>
</ul></li>
<li class="leaf header-menu-pmu--sportif menu-current-active"><a href="/">Paris sportifs</a></li>
<li class="leaf header-menu-pmu--poker"><a href="https://poker.pmu.fr/">Poker</a></li>
<li class="last leaf header-menu-pmu--icon header-menu-pmu--last-element"><a href="https://communaute-aide.pmu.fr/">Communauté</a></li>
<li class="header--login-btn pull-right hidden-lg"><a href="#" class="overlay-trigger" data-target-name=".popin-login" data-action="open"><span class="glyphicon glyphicon-pmu-buddy"></span></a></li><li class="header--basket-btn pull-right hidden-md hidden-lg"><a href="#" class="overlay-trigger" data-target-name="#betslip" data-action="open"><span class="glyphicon glyphicon-pmu-basket"></span></a></li></ul>                                            <div class="header--user header--user--tablet">
                                              </div>
                    </nav>
                  </div>
                </div>
              </div>
              <div class="hidden-sm col-lg-5">
                <div class="header--user">
                  <section id="block-pmu-connect-pmu-connect-main" class="block block-pmu-connect clearfix">

      
  <div class="block-content">
    
<!-- HEADER LOGIN CONTAINER STARTS HERE -->
<div class="header--login">
    <!-- LOGIN FORM STARTS HERE -->
    <form autocomplete="off" class="header--login-form" action="#" method="post" id="header-login-form">
        <span class="glyphicon glyphicon-pmu-buddy"></span>
        <input type="text" class="form-control input-login" placeholder="N° Client"
               name="numeroExterne" id="login-username" autocomplete="off">
        <input type="password" class="form-control input-login" placeholder="CODE"
               id="input-login-password" autocomplete="off" style="display: none;">
        <input type="submit" value="OK" class="btn btn-cta btn-green" id="input-login-submit">
        <!-- START OF: Hidden values to send when the submit form is pressed -->
        <input type="hidden" name="pinpadKey" value="" id="pinpad-key"/>
        <input type="hidden" name="codeConf" value="" id="secret-code"/>
        <input type="hidden" name="dateNaissance" value="" id="hidden-date" />
        <!-- END OF: Hidden values to send when the submit form is pressed -->
    </form>
    <!-- LOGIN FORM ENDS HERE -->

    <!-- FORGOT PASSWORD/REGISTER STARTS HERE -->
    <div class="header--login-option">
        <a href="https://inscription.pmu.fr/?clientApi=2&typeCompte=2010&codePromo=SPORT&redirectionUrl=https%3A%2F%2Fparis-sportifs.pmu.fr%2F" class="btn btn-cta btn-red">
            <span class="glyphicon glyphicon-pencil"></span>
            <span>Ouvrir un compte</span>
        </a>
    </div>
    <!-- FORGOT PASSWORD/REGISTER ENDS HERE -->
</div>
<!-- HEADER LOGIN CONTAINER ENDS HERE -->

<!-- LOGIN PASSWORD PINPAD STARTS HERE -->
<div id="popinPinPad" class="popinPinPad">
    <div class="pinpadHeader">
        <p>Identification</p>
        <a class="closeBtn" id="btnClose" href="#">Fermer X</a>
    </div>
    <div class="pinpadBody">
        <div class="pinpadBodyIsd">

            <div style="background:white;padding:8px;">
                <h5 style="color:#009933; font-size:15px; padding: 0; margin:0px;">1. Saisir votre date de naissance :</h5>
                <div style="margin-left:80px;margin:11px 0 17px 87px">
                    <input type="text" name="day" id="pinpad_day"  maxlength="2"  style="width:25px;" tabindex="25" />
                    <input type="text" name="month" id="pinpad_month"  maxlength="2"  style="width:25px;" tabindex="26" />
                    <input type="text" name="year" id="pinpad_year" maxlength="4" style="width:50px;" tabindex="27" />
                    <span class="PinPadHelpIcon" title="Vous devez avoir au moins 18 ans pour parier"></span>
                </div>
            </div>
            <div style="padding:8px;">
                <h5 style="color:black; font-size:15px; padding: 0; margin:0px;">2. Saisir votre Code Confidentiel :</h5>
                <p style="font-style:italic; font-size:13px;">
                    Pour des raisons de sécurité, vous devez cliquer sur les chiffres de la grille pour saisir votre Code Confidentiel :
                </p>
                <div class="cx">
                    <div id="pinpadGrid" class="grid">
                        <a href="#" id="n0" class="num">0</a>
                        <a href="#" id="n1" class="num">1</a>
                        <a href="#" id="n2" class="num">2</a>
                        <a href="#" id="n3" class="num">3</a>
                        <a href="#" id="n4" class="num">4</a>
                        <a href="#" id="n5" class="num">5</a>
                        <a href="#" id="n6" class="num">6</a>
                        <a href="#" id="n7" class="num">7</a>
                        <a href="#" id="n8" class="num">8</a>
                        <a href="#" id="n9" class="num">9</a>
                    </div>
                    <div class="btnLeft">
                        <p>
                            <a href="#" id="btnCorrect" class="btn btnCorrect">Corriger</a>
                            <a href="#" id="btnCancel" class="btn btnCancel">Annuler</a>
                        </p>
                    </div>
                </div>
                <div class="cx">
                    <form action="#" method="post">
                        <p style="padding: 0; margin:0px;">
                            <input type="password" id="codePinPad" name="codePinPad" disabled="disabled" maxlength="6" style="width:160px;"/>
                            <strong>(4 ou 6 chiffres)</strong>
                        </p>
                        <p style="padding: 0; margin:0px;">
                            <a href="#" id="btnConfirm" class="btn btnConfirm">Confirmer</a>
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- LOGIN PASSWORD PINPAD STARTS HERE -->

<div id="maskPinPad" class="layoutMaskPinPad"></div>

<!-- ORANGE PINPAD STARTS HERE -->
<aside class="popin-login" id="orange-pinpad-container">

    <div class="popin--header popin--header-grey">
        <div class="row">
            <div class="col-sm-10">
                <span class="glyphicon glyphicon-pmu-buddy"></span>
                <h6>Connexion</h6>
            </div>
            <div class="col-sm-2">
                <a href="#" class="overlay-trigger" data-target-name=".popin-login" data-action="close"><span class="glyphicon glyphicon-pmu-close"></span></a>
            </div>
        </div>
    </div>

    <div class="popin--content">
        <form action="#" class="clearfix mb-40">
            <div class="form-error--resume hidden">
                <p>Votre N° client, votre date de naissance <br> ou votre code confidentiel sont incorrects.</p>
                <strong>Veuillez renouveler votre saisie, merci. (code 200)</strong>
            </div>
            <fieldset class="mt-30">
                <label for="popin-login--client-id" class="form-label-bold">N° client</label>
                <input type="text" class="form-control input form-error--field" id="popin-login--client-id" placeholder="10 chiffres">
                <div class="form-error--icon hidden" id="error-icon-for-id"><span class="glyphicon glyphicon-remove"></span></div>
                <div class="form-error--msg hidden" id="error-message-for-id">Veuillez renseigner un n° client valide</div>
                <div class="mt-10">
                    <input type="checkbox" class="checkbox checkbox-green checkbox-big" id="popin-login--remember-me">
                    <label for="popin-login--remember-me">Retenir mon n° client</label>
                </div>
            </fieldset>
            <fieldset class="mt-10">
                <label for="popin-login--birthday-input" class="form-label-bold">Date de naissance</label>
                <ul class="form-birthdate form-error--field">
                    <li><input type="text" class="form-control input text-center pinpad_date_input" id="popin-login--birthday-input" maxlength="2" placeholder="Jour (jj)"></li><!--
                    --><li><input type="text" class="form-control input text-center pinpad_date_input" id="popin-login--birthmonth-input" maxlength="2" placeholder="Mois (mm)"></li><!--
                    --><li><input type="text" class="form-control input text-center pinpad_date_input" id="popin-login--birthyear-input" maxlength="4"
                    placeholder="Année (aaaa)">
                    </li>
                </ul>
                <div class="form-error--icon hidden" id="error-icon-for-date"><span class="glyphicon glyphicon-remove"></span></div>
                <div class="form-error--msg hidden" id="error-message-for-date">Veuillez renseigner une date de naissance valide</div>
            </fieldset>
            <fieldset class="mt-10">
                <label for="popin-login--client-pin" class="form-label">Code confidentiel</label>
                <input type="password" class="pinpad" id="popin-login--client-pin" placeholder="4 ou 6 chiffres">
                <div class="form-error--icon hidden" id="error-icon-for-code"><span class="glyphicon glyphicon-remove"></span></div>
                <div class="form-error--msg hidden" id="error-message-for-code">Veuillez renseigner un code confidentiel valide</div>
                <p class="mt-10 text-underline"><a class="link-grey-dark" href="https://compte.pmu.fr/code-confidentiel-oublie?clientApi=2&typeCompte=2010">Code confidentiel oublié ?</a></p>
            </fieldset>

            <button role="button" class="btn btn-cta btn-orange btn-centered mt-30" id="orange-submit-button">Se connecter</button>
            <p class="mt-10 text-center text-underline">
                <a href="https://inscription.pmu.fr/?clientApi=2&typeCompte=2010&codePromo=SPORT&redirectionUrl=https%3A%2F%2Fparis-sportifs.pmu.fr%2F" class="link-grey-dark">Ouvrir un compte</a>
            </p>
        </form>
    </div>
</aside>
<!-- ORANGE PINPAD ENDS HERE -->
  </div>

</section> <!-- /.block -->
                </div>
              </div>
            </div>
            <div class="row">
              <div class="hidden-sm col-md-11 col-md-offset-1">
                                  <nav id="header-menu-sports-betting">
                    <ul class="row"><li class="col-sm-2 obet-event-list-grid-formatter-col secondary-menu-en-direct"><a href="/en-direct">En Direct</a></li>
<li class="col-sm-2 obet-event-list-grid-formatter-col"><a href="/cash-out">Cash Out</a></li>
<li class="col-sm-2 obet-event-list-grid-formatter-col secondary-menu-multibonus"><a href="/combimax">CombiMax</a></li>
<li class="col-sm-2 obet-event-list-grid-formatter-col secondary-menu-jackpot"><a href="https://paris-sportifs.pmu.fr/1n2-jackpot">1N2 Jackpot</a></li>
<li class="col-sm-2 obet-event-list-grid-formatter-col"><a href="/fantasy-league">Fantasy League</a></li>
<li class="col-sm-2 obet-event-list-grid-formatter-col secondary-menu-promotions"><span class="glyphicon glyphicon-pmu-price-tag-black "></span><a href="/promotions/all">Promotions</a></li>
</ul>                  </nav>
                              </div>
            </div>
          </div>
        </header>
      </div>
      <div id="betslip-md" class="basket-landscape-wrapper hidden-lg col-md-3">
        <!-- Betslip tablet wrapper -->
      </div>
    </div>
  </div>
</div>
<aside id="breadcrumb">
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <div class="breadcrumb-wrapper"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"> <a href="/"> <span itemprop="title">Paris sportifs </span> </a> </span><span class="breadcrumb-sep">&gt;</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"> <a href="/pari/sport/8/rugby"> <span itemprop="title">Rugby </span> </a> </span><span class="breadcrumb-sep">&gt;</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"> <a href="/pari/competition/1366/rugby/top-14"> <span itemprop="title">TOP 14 </span> </a> </span></div>      </div>
          <div class="col-sm-2">
            <div class="date-wrapper">
              <time datetime="2020-02-13 20:53">13 février 2020 - 20h53</time>
            </div>
          </div>
        </div>
      </div>
</aside>


<section>
  <div class="container">
    <a id="main-content"></a>
                                  <div class="messages"></div>  </div>
    <div class="region region-content">
    <section id="block-system-main" class="block block-system clearfix">

      
  <div class="block-content">
    
<div class="panelizer-view-mode node node-full node-landing-page node-15">
        


<div class="template-main container container-fluidable" data-fluid="1200">
  <div class="row">
      </div>

  <div class="row">
        
<div class="col-md-2 visible-lg-block">
  <div class="row">
                                      <div class="three-rows-region--first-left">
          <div class="panel-pane pane-block pane-obet-search-search-form-compact col-xs-12 pane--cols mb-20"  >
  
      
  
  <div class="pane-content">
    
<div class="sb-l-wrap">
    <div class="sb-search">
        <form class="main-search--form" action="https://paris-sportifs.pmu.fr/recherche" method="get" id="obet-search-form-compact-callback" accept-charset="UTF-8"><div><label class="glyphicon glyphicon-pmu-magnifiying main-search--trigger"></label><div class="form-item form-item-token form-type-textfield form-group"><input placeholder="Trouver un pari ..." class="tokenInput form-control form-text" type="text" id="edit-token" name="token" value="" size="60" maxlength="128" /></div><a role="button" class="glyphicon glyphicon-pmu-close main-search--close"></a></div></form>    </div>
</div>
  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-menu-quick-links col-xs-12 pane--cols mb-20"  >
  
        <h2 class="pane-title sb-l-title">
      À LA UNE    </h2>
    
  
  <div class="pane-content">
    <div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/en-direct" class="quick-links-en-direct sb-list-item"><figure class="sb-list-item--live-icon"><img src="https://paris-sportifs.pmu.fr/sites/default/files/anim-live-black-orange.gif" alt="En Direct" /></figure><em class="sb-list-item--label"><em class="sb-list-item--label"><strong class="sb-list-item--counter">17</strong> En Direct</em></em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/promotions/all" class="quick-links-promotions sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-price-tag-black glyphicon-orange"></span></span><em class="sb-list-item--label">Promotions</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2900" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-gift glyphicon-green "></span></span><em class="sb-list-item--label">10 € offerts sur le Foot Français</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2963" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-gift glyphicon-green "></span></span><em class="sb-list-item--label">5 000€ sur la Coupe de France</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/663625" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.epinal__st_etienne" data-sport_id="football" data-compet_id="coupe_de_france" data-event_id="epinal__st_etienne"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Epinal // St-Etienne</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/662844" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.ac_milan__juventus" data-sport_id="football" data-compet_id="coupe_ditalie" data-event_id="ac_milan__juventus"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">AC Milan // Juventus</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/665753" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.sociedad__mirandes" data-sport_id="football" data-compet_id="coupe_du_roi" data-event_id="sociedad__mirandes"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Sociedad // Mirandés</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/pari/competition/169/football/ligue-1-conforama" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Ligue 1 Conforama</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/170/football/dominos-%C2%AE-ligue-2" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Domino's Ligue 2</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/sport/9/tennis" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-tennis glyphicon-light-yellow"></span></span><em class="sb-list-item--label">ATP / WTA</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/3502/basket-us/nba-matchs" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball glyphicon-dark-red"></span></span><em class="sb-list-item--label">NBA</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/1366/rugby/top-14" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby glyphicon-dark-green "></span></span><em class="sb-list-item--label">TOP 14</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/reseaux-sociaux" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-thumb-up glyphicon-cyan"></span></span><em class="sb-list-item--label">Réseaux Sociaux</em></a></div></div></div>
  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-menu-quick-betting-links col-xs-12 pane--cols mb-20"  >
  
        <h2 class="pane-title sb-l-title">
      PARIER AUTREMENT    </h2>
    
  
  <div class="pane-content">
    <div class="row"><div class="col-sm-12"><a href="/cash-out" class="paris-rapides-cashout sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-cash-out glyphicon-orange"></span></span><em class="sb-list-item--label">Cash Out<span class="sb-list-item--details"><p>Soyez maître de vos paris</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/combimax" class="paris-rapides-multibonus sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bomb glyphicon-orange"></span></span><em class="sb-list-item--label">CombiMax<span class="sb-list-item--details"><p>Plus votre grille est ambitieuse, plus le bonus s'envole !</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/1n2-jackpot" class="paris-rapides-jackpot sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon pmu-custom-glyphicon-jackpot  glyphicon-orange"></span></span><em class="sb-list-item--label">1N2 Jackpot<span class="sb-list-item--details"><p>Multipliez jusqu'à 100x votre gain</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/fantasy-league" class="paris-rapides-fantasy-league sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-fantasy-league  glyphicon-orange"></span></span><em class="sb-list-item--label">Fantasy League<span class="sb-list-item--details"><p>Entrez dans la peau d'un manager</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/bet-machine" class="paris-rapides-bet-machine sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-draggable glyphicon-orange"></span></span><em class="sb-list-item--label">Bet Machine<span class="sb-list-item--details">Décider ce que vous pourriez gagner</span></em></a></div></div>
  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-menu-sports-menu col-xs-12 pane--cols mb-20"  >
  
        <h2 class="pane-title sb-l-title">
      TOUS LES SPORTS    </h2>
    
  
  <div class="pane-content">
    <ul class="menu nav"><li class="first collapsed row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/25/football" data-hierarchy-level-events-counter="550" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="football"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football "></span></span><em class="sb-list-item--label">Football</em><strong class="sb-list-item--counter_pmu">550</strong></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/9/tennis" data-hierarchy-level-events-counter="38" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tennis"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-tennis "></span></span><em class="sb-list-item--label">Tennis</em><strong class="sb-list-item--counter_pmu">38</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/7755/tennis/wta-saint-p%C3%A9tersbourg" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wta_saint-petersbourg">WTA Saint-Pétersbourg</a></li>
<li class="leaf"><a href="/pari/competition/447/tennis/atp-rotterdam" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_rotterdam">ATP Rotterdam</a></li>
<li class="leaf"><a href="/pari/competition/8796/tennis/atp-new-york" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_new_york">ATP New York</a></li>
<li class="leaf"><a href="/pari/competition/7024/tennis/atp-buenos-aires" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_buenos_aires">ATP Buenos Aires</a></li>
<li class="leaf"><a href="/pari/competition/441/tennis/open-daustralie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="open_daustralie_h">Open d'Australie (H)</a></li>
<li class="leaf"><a href="/pari/competition/440/tennis/open-daustralie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="open_daustralie_f">Open d'Australie (F)</a></li>
<li class="leaf"><a href="/pari/competition/759/tennis/roland-garros-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="roland_garros_h">Roland Garros (H)</a></li>
<li class="leaf"><a href="/pari/competition/400/tennis/roland-garros-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="roland_garros_f">Roland Garros (F)</a></li>
<li class="leaf"><a href="/pari/competition/744/tennis/wimbledon-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wimbledon_h">Wimbledon (H)</a></li>
<li class="leaf"><a href="/pari/competition/745/tennis/wimbledon-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wimbledon_f">Wimbledon (F)</a></li>
<li class="leaf"><a href="/pari/competition/785/tennis/jo" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="jo">JO</a></li>
<li class="leaf"><a href="/pari/competition/673/tennis/us-open-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="us_open_h">US Open (H)</a></li>
<li class="leaf"><a href="/pari/competition/416/tennis/us-open-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="us_open_f">US Open (F)</a></li>
<li class="leaf"><a href="/pari/competition/666/tennis/paris-sur-les-joueurs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="paris_sur_les_joueurs">Paris sur les joueurs</a></li>
<li class="leaf"><a href="/pari/competition/7590/tennis/wta-hua-hin" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wta_hua_hin">WTA Hua Hin</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/59/basket-euro" data-hierarchy-level-events-counter="36" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="basketball_euro"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball "></span></span><em class="sb-list-item--label">Basketball Euro</em><strong class="sb-list-item--counter_pmu">36</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1415/basket-euro/france-pro" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="france_-_pro_a">France - Pro A</a></li>
<li class="leaf"><a href="/pari/competition/2189/basket-euro/france-pro-b" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="france_-_pro_b">France - Pro B</a></li>
<li class="leaf"><a href="/pari/competition/1402/basket-euro/euroligue-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="euroligue_h">Euroligue (H)</a></li>
<li class="leaf"><a href="/pari/competition/1417/basket-euro/allemagne-bundesliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="allemagne_-_bundesliga">Allemagne - Bundesliga</a></li>
<li class="leaf"><a href="/pari/competition/5021/basket-euro/australie-nbl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="australie_-_nbl">Australie - NBL</a></li>
<li class="leaf"><a href="/pari/competition/1425/basket-euro/espagne-ligue-acb" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="espagne_-_ligue_acb">Espagne - Ligue ACB</a></li>
<li class="leaf"><a href="/pari/competition/1493/basket-euro/espagne-ligue-leb-oro" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="espagne_-_ligue_leb_oro">Espagne - Ligue LEB Oro</a></li>
<li class="leaf"><a href="/pari/competition/1423/basket-euro/italie-s%C3%A9rie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="italie_-_serie_a">Italie - Série A</a></li>
<li class="leaf"><a href="/pari/competition/4495/basket-euro/leaders-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="leaders_cup">Leaders Cup</a></li>
<li class="leaf"><a href="/pari/competition/1422/basket-euro/coupe-ditalie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="coupe_ditalie">Coupe d'Italie</a></li>
<li class="leaf"><a href="/pari/competition/1426/basket-euro/coupe-du-roi" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="coupe_du_roi">Coupe du Roi</a></li>
<li class="leaf"><a href="/pari/competition/1491/basket-euro/ligue-aba" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="ligue_aba">Ligue ABA</a></li>
<li class="leaf"><a href="/pari/competition/8630/basket-euro/belgique-1%C3%A8re-division" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="belgique_-_1ere_division">Belgique - 1ère division</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/12/basket-us" data-hierarchy-level-events-counter="81" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="basketball_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball "></span></span><em class="sb-list-item--label">Basketball US</em><strong class="sb-list-item--counter_pmu">81</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/3502/basket-us/nba-matchs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_matchs">NBA - Matchs</a></li>
<li class="leaf"><a href="/pari/competition/1395/basket-us/nba-vainqueur" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_vainqueur">NBA - Vainqueur</a></li>
<li class="leaf"><a href="/pari/competition/1393/basket-us/nba-conf-est" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_conf._est">NBA - Conf. Est</a></li>
<li class="leaf"><a href="/pari/competition/1394/basket-us/nba-conf-ouest" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_conf._ouest">NBA - Conf. Ouest</a></li>
<li class="leaf"><a href="/pari/competition/7393/basket-us/nba-divisions" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_divisions">NBA - Divisions</a></li>
<li class="leaf"><a href="/pari/competition/9969/basket-us/ncaa-matchs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_matchs">NCAA - Matchs</a></li>
<li class="leaf"><a href="/pari/competition/1392/basket-us/ncaa-divers" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_divers">NCAA - Divers</a></li>
<li class="leaf"><a href="/pari/competition/9138/basket-us/ncaa-vainqueur" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_vainqueur">NCAA - Vainqueur</a></li>
</ul></div></div></div></li>
<li class="expanded active-trail active row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/8/rugby" data-hierarchy-level-events-counter="81" data-target="#" class="sb-list-item-small has-children 0 active tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="rugby"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby "></span></span><em class="sb-list-item--label">Rugby</em><strong class="sb-list-item--counter_pmu">81</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1380/rugby/tournoi-des-6-nations" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="tournoi_des_6_nations">Tournoi des 6 Nations</a></li>
<li class="leaf active-trail active"><a href="/pari/competition/1366/rugby/top-14" class="sb-sublist-item 0 link-grey-dark active tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="top_14">TOP 14</a></li>
<li class="leaf"><a href="/pari/competition/1450/rugby/pro-d2" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="pro_d2">PRO D2</a></li>
<li class="leaf"><a href="/pari/competition/1375/rugby/champions-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="champions_cup">Champions Cup</a></li>
<li class="leaf"><a href="/pari/competition/1378/rugby/challenge-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="challenge_cup">Challenge Cup</a></li>
<li class="leaf"><a href="/pari/competition/9064/rugby/gallagher-premiership" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="gallagher_premiership">Gallagher Premiership</a></li>
<li class="leaf"><a href="/pari/competition/7324/rugby/super-rugby" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="super_rugby">Super Rugby</a></li>
<li class="leaf"><a href="/pari/competition/7575/rugby/world-rugby-sevens-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="world_rugby_sevens_series">World Rugby Sevens Series</a></li>
<li class="leaf"><a href="/pari/competition/8504/rugby/pro-14" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="pro_14">Pro 14</a></li>
<li class="leaf"><a href="/pari/competition/9992/rugby/coupe-du-monde-2023" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="coupe_du_monde_2023">Coupe du Monde 2023</a></li>
<li class="leaf"><a href="/pari/competition/2475/rugby/tournoi-6-nations-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="tournoi_6_nations_f">Tournoi 6 Nations (F)</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/45/aviron" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="aviron"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rowing "></span></span><em class="sb-list-item--label">Aviron</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/217/bobsleigh" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="bobsleigh"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bobsleigh "></span></span><em class="sb-list-item--label">Bobsleigh</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/213/luge" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="luge"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-skeleton "></span></span><em class="sb-list-item--label">Luge</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/114/jo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="medailles_jo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-medale "></span></span><em class="sb-list-item--label">Médailles JO</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/215/patinage-de-vitesse" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="patinage_de_vitesse"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-ice-skating "></span></span><em class="sb-list-item--label">Patinage de Vitesse</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/220/patinage-de-vitesse-sur-piste-courte" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="short_track"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-ice-skating "></span></span><em class="sb-list-item--label">Short Track</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/214/skeleton" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="skeleton"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-skeleton "></span></span><em class="sb-list-item--label">Skeleton</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/218/freestyle" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_freestyle"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-alpine-skiing "></span></span><em class="sb-list-item--label">Ski Freestyle</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/219/snowboard" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="snowboard"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snowboard "></span></span><em class="sb-list-item--label">Snowboard</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/15/athl%C3%A9tisme" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="athletisme"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-athletism "></span></span><em class="sb-list-item--label">Athlétisme</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/62/badminton" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="badminton"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-badminton "></span></span><em class="sb-list-item--label">Badminton</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/14/baseball" data-hierarchy-level-events-counter="3" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="baseball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-baseball "></span></span><em class="sb-list-item--label">Baseball</em><strong class="sb-list-item--counter_pmu">3</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1436/baseball/world-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="world_series">World Series</a></li>
<li class="leaf"><a href="/pari/competition/1458/baseball/american-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="american_league">American League</a></li>
<li class="leaf"><a href="/pari/competition/1459/baseball/national-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="national_league">National League</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/151/beach-volley" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="beach_volley"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-beach-volley "></span></span><em class="sb-list-item--label">Beach Volley</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/84/biathlon" data-hierarchy-level-events-counter="1" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="biathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-biathlon "></span></span><em class="sb-list-item--label">Biathlon</em><strong class="sb-list-item--counter_pmu">1</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2128/biathlon/antholz-anterselva" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="biathlon" data-compet_id="antholz-anterselva">Antholz-Anterselva</a></li>
</ul></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/166/" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="billard_americain"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snooker "></span></span><em class="sb-list-item--label">Billard américain</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/11/boxe" data-hierarchy-level-events-counter="4" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="boxe"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-boxe "></span></span><em class="sb-list-item--label">Boxe</em><strong class="sb-list-item--counter_pmu">4</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/994/boxe/combats-de-boxe-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="boxe" data-compet_id="combats_de_boxe_-_monde">Combats de boxe - Monde</a></li>
</ul></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/184/cano%C3%AB-kayak" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="canoe-kayak"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-kayak "></span></span><em class="sb-list-item--label">Canoë-Kayak</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/144/curling" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="curling"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-curling "></span></span><em class="sb-list-item--label">Curling</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/36/cyclisme" data-hierarchy-level-events-counter="4" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="cyclisme"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-road-cycling "></span></span><em class="sb-list-item--label">Cyclisme</em><strong class="sb-list-item--counter_pmu">4</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1024/cyclisme/tour-de-france" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_de_france">Tour de France</a></li>
<li class="leaf"><a href="/pari/competition/1032/cyclisme/paris-roubaix" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="paris_-_roubaix">Paris - Roubaix</a></li>
<li class="leaf"><a href="/pari/competition/1027/cyclisme/tour-ditalie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_ditalie">Tour d'Italie</a></li>
<li class="leaf"><a href="/pari/competition/1035/cyclisme/tour-des-flandres" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_des_flandres">Tour des Flandres</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/152/escrime" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="escrime"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-fencing "></span></span><em class="sb-list-item--label">Escrime</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/164/football-am%C3%A9ricain" data-hierarchy-level-events-counter="3" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="football_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-us "></span></span><em class="sb-list-item--label">Football US</em><strong class="sb-list-item--counter_pmu">3</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1956/football-am%C3%A9ricain/nfl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="football_us" data-compet_id="nfl">NFL</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/4/golf" data-hierarchy-level-events-counter="9" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="golf"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-golf "></span></span><em class="sb-list-item--label">Golf</em><strong class="sb-list-item--counter_pmu">9</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1336/golf/us-masters" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="us_masters">US Masters</a></li>
<li class="leaf"><a href="/pari/competition/1324/golf/ryder-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="ryder_cup">Ryder Cup</a></li>
<li class="leaf"><a href="/pari/competition/1277/golf/open-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="open_championship">Open Championship</a></li>
<li class="leaf"><a href="/pari/competition/1343/golf/uspga-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="uspga_championship">USPGA Championship</a></li>
<li class="leaf"><a href="/pari/competition/1323/golf/players-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="the_players_championship">The Players Championship</a></li>
<li class="leaf"><a href="/pari/competition/1274/golf/genesis-open" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="genesis_open">Genesis Open</a></li>
<li class="leaf"><a href="/pari/competition/1265/golf/open-daustralie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="open_daustralie_f">Open d'Australie (F)</a></li>
<li class="leaf"><a href="/pari/competition/7657/golf/jo-h-2020" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="jo_h_2020">JO (H) 2020</a></li>
<li class="leaf"><a href="/pari/competition/1339/golf/us-open" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="us_open">US Open</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/197/halt%C3%A9rophilie" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="halterophilie"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-weightlifting "></span></span><em class="sb-list-item--label">Haltérophilie </em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/54/handball" data-hierarchy-level-events-counter="20" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="handball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-handball "></span></span><em class="sb-list-item--label">Handball</em><strong class="sb-list-item--counter_pmu">20</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1092/handball/ligue-des-champions-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="ligue_des_champions_h">Ligue des Champions (H)</a></li>
<li class="leaf"><a href="/pari/competition/1089/handball/bundesliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="bundesliga">Bundesliga</a></li>
<li class="leaf"><a href="/pari/competition/1088/handball/espagne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="espagne_h">Espagne (H)</a></li>
<li class="leaf"><a href="/pari/competition/3976/handball/coupe-ehf-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="coupe_ehf_h.">Coupe EHF (H).</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/160/hockey-sur-glace-eu" data-hierarchy-level-events-counter="66" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_euro"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey Euro</em><strong class="sb-list-item--counter_pmu">66</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1881/hockey-sur-glace-eu/ligue-magnus" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="ligue_magnus">Ligue Magnus</a></li>
<li class="leaf"><a href="/pari/competition/4258/hockey-sur-glace-eu/russie-khl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="russie_-_khl">Russie - KHL</a></li>
<li class="leaf"><a href="/pari/competition/1887/hockey-sur-glace-eu/allemagne-del" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="allemagne_-_del">Allemagne - DEL</a></li>
<li class="leaf"><a href="/pari/competition/1883/hockey-sur-glace-eu/autriche-ehl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="autriche_-_ehl">Autriche - EHL</a></li>
<li class="leaf"><a href="/pari/competition/1884/hockey-sur-glace-eu/finlande-sm-liiga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="finlande_-_sm-liiga">Finlande - SM-Liiga</a></li>
<li class="leaf"><a href="/pari/competition/7272/hockey-sur-glace-eu/norv%C3%A8ge-get-ligaen" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="norvege_get_ligaen">Norvège Get Ligaen</a></li>
<li class="leaf"><a href="/pari/competition/1888/hockey-sur-glace-eu/r%C3%A9p-tch%C3%A8que-extraliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="rep._tcheque_-_extraliga">Rép. Tchèque - Extraliga</a></li>
<li class="leaf"><a href="/pari/competition/7376/hockey-sur-glace-eu/slovaquie-extraliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="slovaquie_-_extraliga">Slovaquie - Extraliga</a></li>
<li class="leaf"><a href="/pari/competition/1885/hockey-sur-glace-eu/su%C3%A8de-shl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="suede_-_shl">Suède - SHL</a></li>
<li class="leaf"><a href="/pari/competition/7377/hockey-sur-glace-eu/suisse-nla" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="suisse_-_nla">Suisse - NLA</a></li>
<li class="leaf"><a href="/pari/competition/2420/hockey-sur-glace-eu/championnats-du-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="championnats_du_monde">Championnats du Monde</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/161/hockey-sur-glace-us" data-hierarchy-level-events-counter="14" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey US</em><strong class="sb-list-item--counter_pmu">14</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1970/hockey-sur-glace-us/nhl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="nhl">NHL</a></li>
<li class="leaf"><a href="/pari/competition/1927/hockey-sur-glace-us/stanley-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="stanley_cup">Stanley Cup</a></li>
<li class="leaf"><a href="/pari/competition/1973/hockey-sur-glace-us/conf%C3%A9rence-est" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="conference_est.">Conférence Est.</a></li>
<li class="leaf"><a href="/pari/competition/1972/hockey-sur-glace-us/conf%C3%A9rence-ouest" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="conference_ouest">Conférence Ouest</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/195/hockey-sur-gazon" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_sur_gazon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey sur gazon</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/203/judo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="judo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-judo "></span></span><em class="sb-list-item--label">Judo</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/192/lutte" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="lutte"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-judo "></span></span><em class="sb-list-item--label">Lutte</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/72/natation" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="natation"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-swimming "></span></span><em class="sb-list-item--label">Natation</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/246/petanque" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="petanque"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-petanque "></span></span><em class="sb-list-item--label">Pétanque</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/187/pentathlon-moderne" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="pentathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-horse-riding "></span></span><em class="sb-list-item--label">Pentathlon</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/100/rugby-%C3%A0-xiii" data-hierarchy-level-events-counter="19" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="rugby_a_xiii"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby "></span></span><em class="sb-list-item--label">Rugby à XIII</em><strong class="sb-list-item--counter_pmu">19</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2327/rugby-%C3%A0-xiii/nrl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby_a_xiii" data-compet_id="nrl">NRL</a></li>
<li class="leaf"><a href="/pari/competition/2328/rugby-%C3%A0-xiii/super-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby_a_xiii" data-compet_id="super_league">Super League</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/82/ski-alpin" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_alpin"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-cross-country-skiing "></span></span><em class="sb-list-item--label">Ski Alpin</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/146/ski-de-fond" data-hierarchy-level-events-counter="2" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_de_fond"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-alpine-skiing "></span></span><em class="sb-list-item--label">Ski de Fond</em><strong class="sb-list-item--counter_pmu">2</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/7016/ski-de-fond/ostersund" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="ski_de_fond" data-compet_id="ostersund">Ostersund</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/159/snooker" data-hierarchy-level-events-counter="5" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="snooker"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snooker "></span></span><em class="sb-list-item--label">Snooker</em><strong class="sb-list-item--counter_pmu">5</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2422/snooker/open-du-pays-de-galles" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="snooker" data-compet_id="open_du_pays_de_galles">Open du Pays de Galles</a></li>
<li class="leaf"><a href="/pari/competition/3873/snooker/championnats-du-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="snooker" data-compet_id="championnats_du_monde">Championnats du Monde</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/5/sports-m%C3%A9caniques" data-hierarchy-level-events-counter="7" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="sports_mecaniques"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-auto-moto "></span></span><em class="sb-list-item--label">Sports mécaniques</em><strong class="sb-list-item--counter_pmu">7</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/8953/sports-m%C3%A9caniques/f1-championnat-des-pilotes" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="f1_championnat_des_pilotes">F1 Championnat des pilotes</a></li>
<li class="leaf"><a href="/pari/competition/9446/sports-m%C3%A9caniques/f1-championnat-des-constructeurs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="f1_championnat_des_constructeurs">F1 Championnat des constructeurs</a></li>
<li class="leaf"><a href="/pari/competition/9486/sports-m%C3%A9caniques/nascar-daytona-500" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar_-_daytona_500">NASCAR - Daytona 500</a></li>
<li class="leaf"><a href="/pari/competition/1645/sports-m%C3%A9caniques/rallye-wrc-de-su%C3%A8de" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="rallye_wrc_de_suede">Rallye WRC de Suède</a></li>
<li class="leaf"><a href="/pari/competition/8347/sports-m%C3%A9caniques/nascar-cup-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar_cup_series">NASCAR Cup Series</a></li>
<li class="leaf"><a href="/pari/competition/1002/sports-m%C3%A9caniques/championnats-du-monde-des-rallyes-wrc" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="championnats_du_monde_des_rallyes_wrc">Championnats du Monde des Rallyes (WRC)</a></li>
<li class="leaf"><a href="/pari/competition/1581/sports-m%C3%A9caniques/nascar" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar">Nascar</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/155/taekwondo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="taekwondo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-taekwondo "></span></span><em class="sb-list-item--label">Taekwondo</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/77/tennis-de-table" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tennis_de_table"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-table-tennis "></span></span><em class="sb-list-item--label">Tennis de Table</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/183/tir-%C3%A0-larc" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tir_a_larc"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-archery "></span></span><em class="sb-list-item--label">Tir à l'Arc</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/190/triathlon" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="triathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-road-cycling "></span></span><em class="sb-list-item--label">Triathlon</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/124/voile" data-hierarchy-level-events-counter="1" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="voile"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-sailing "></span></span><em class="sb-list-item--label">Voile</em><strong class="sb-list-item--counter_pmu">1</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/4932/voile/coupe-de-lam%C3%A9rica" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="voile" data-compet_id="coupe_de_lamerica">Coupe de l'América</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/57/volley-ball" data-hierarchy-level-events-counter="23" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="volley-ball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-volley-ball "></span></span><em class="sb-list-item--label">Volley-Ball</em><strong class="sb-list-item--counter_pmu">23</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1081/volley-ball/ligue-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_a_h">Ligue A (H)</a></li>
<li class="leaf"><a href="/pari/competition/2278/volley-ball/ligue-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_a_f">Ligue A (F)</a></li>
<li class="leaf"><a href="/pari/competition/1076/volley-ball/ligue-des-champions-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_des_champions_h">Ligue des Champions (H)</a></li>
<li class="leaf"><a href="/pari/competition/1084/volley-ball/allemagne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="allemagne_h">Allemagne (H)</a></li>
<li class="leaf"><a href="/pari/competition/8637/volley-ball/belgique-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="belgique._h">Belgique. (H)</a></li>
<li class="leaf"><a href="/pari/competition/8639/volley-ball/italie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="italie_h">Italie (H)</a></li>
<li class="leaf"><a href="/pari/competition/2235/volley-ball/italie-s%C3%A9rie-a1-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="italie_-_serie_a1_f">Italie - Série A1 (F)</a></li>
<li class="leaf"><a href="/pari/competition/2399/volley-ball/pologne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="pologne_h">Pologne (H)</a></li>
<li class="leaf"><a href="/pari/competition/2230/volley-ball/russie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="russie_h">Russie (H)</a></li>
<li class="leaf"><a href="/pari/competition/5074/volley-ball/russie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="russie_f">Russie (F)</a></li>
<li class="leaf"><a href="/pari/competition/1500/volley-ball/turquie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="turquie_h">Turquie (H)</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/168/water-polo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="water-polo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-waterpolo "></span></span><em class="sb-list-item--label">Water-polo</em></a></div></div></div></li>
<li class="leaf row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="https://www.pmu.fr/turf/" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="turf"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-horse-riding "></span></span><em class="sb-list-item--label">Turf</em></a></div></div></div></li>
<li class="last leaf row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="https://poker.pmu.fr/" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="poker"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-star "></span></span><em class="sb-list-item--label">Poker</em></a></div></div></div></li>
</ul>  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-menu-services col-xs-12 pane--cols mb-20"  >
  
        <h2 class="pane-title sb-l-title">
      PMU Services    </h2>
    
  
  <div class="pane-content">
    <div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="javascript:void(0);" class="pmu-services-statistiques sb-list-item-small" onclick="javascript:popWin = window.open(&quot;https://s5.sir.sportradar.com/pmu/fr&quot;, &quot;Statistiques&quot;, &quot;left=10, top=10, width=1000, height=730, scrollbars=1, titlebar=0, status=0, toolbar=0, menubar=0, location=0&quot;); popWin.focus();"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bar-chart "></span></span><em class="sb-list-item--label">Statistiques</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/aide/regles-paris" class="pmu-services-regles-paris sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-note "></span></span><em class="sb-list-item--label">Règles des paris</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/info/calendrier" class="pmu-services-calendar sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-calendar "></span></span><em class="sb-list-item--label">Calendrier</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/results" class="pmu-services-resultats sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-goal "></span></span><em class="sb-list-item--label">Résultats</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="https://communaute-forum.pmu.fr/categories/3395-sport" class="pmu-services-aide sb-list-item-small" target="_blank"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-help "></span></span><em class="sb-list-item--label">Aide - Communauté</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/pservices/simulator" class="overlay-trigger pmu-services-simulateur sb-list-item-small" data-target-name=".popin" data-action="open"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-calc "></span></span><em class="sb-list-item--label">Simulateur</em></a></div></div></div>
  </div>

  
  </div>
        </div>
                                                                                                                                                                                                </div>
</div>

<div class="col-sm-12 col-md-9 col-lg-7">
  <div class="row">
    <div class="twelve-rows-region twelve-rows-region--second row">
      <div class="twelve-rows--rows twelve-rows">
                                                                                                                        <div class="twelve-rows-region twelve-rows-region--first-center">
              <div class="panel-pane pane-block pane-pmu-hierarchy-metadata-pmu-contextual-event-page-banner col-xs-12 pane--cols"  >
  
      
  
  <div class="pane-content">
    <div class="cover-page cover-page--event" style="background-image:url(https://paris-sportifs.pmu.fr/sites/default/files/682x235_Event-Banner_Rugby.jpg);">
  <div class="row">
    <div class="col-sm-12">
      <div class="pt-50">
              </div>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
      <p class="text-center text-xsmall mt-10">
        Dimanche 16 février 2020 - 16h50      </p>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
      <p class="text-center text-large mt-10">
        Rugby - TOP 14      </p>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-12">
      <p class="text-center text-xxlarge text-uppercase mt-5">
        Racing 92 // Toulouse      </p>
    </div>
  </div>
</div>
  </div>

  
  </div>
            </div>
                                                          <div class="twelve-rows-region twelve-rows-region--third-center">
              <div class="panel-pane pane-block pane-obet-events-event-collections-context col-xs-12 pane--cols"  >
  
      
  
  <div class="pane-content">
    <div class="event-markets-container"  data-ev_id="666562" data-ev_status="A">
      <div class="market-sorts select-a-bet">
      <h5>Choisissez un pari</h5>
      <select class="tc-track-element-events" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.menu_deroulant">
          <option class="show-all-markets">Tous</option>
                              <option class="filter-market" data-market-id="23765369">Vainqueur avec handicap</option>
                                        <option class="filter-market" data-market-id="23765370">Vainqueur du match</option>
                                        <option class="filter-market" data-market-id="23765367">1 2</option>
                                        <option class="filter-market" data-market-id="23765368">1 2 avec handicap.</option>
                        </select>
    </div>
  

            

  <div class="table table-event shadow " data-market_sort="
  MH"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A">

    <div class="row">
              <div class="table--header-orange table--header-full table--market-sort">
                      <div class="col-sm-9 pr-0">
              <div class="table--header">
                <a href="#table-content-23765369" role="button" data-toggle="collapse" aria-expanded="true" aria-controls="table-content-23765369"
                   class="table--header--inner ">
                  <span class="glyphicon glyphicon-chevron-down"></span>
                  <h3 class="table--header-title">
                    Vainqueur avec handicap
                    
                    
                  </h3>
                </a>
              </div>
            </div>
          
                    <div class="col-sm-3 pl-0">
            <div class="table--header">
              <a class="table--header-rules overlay-trigger tc-track-element-events"
                 data-action="open" data-target-name=".popin"
                 href="/pservices/bet_rules"
                 data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.regles_du_pari">
                Règles du pari              </a>
            </div>
          </div>
        </div>
          </div>

    <div class="table--main
       in"
         id="table-content-23765369" role="group" aria-expanded="true" >
              <table class="table table-bordered table--fixed mb-0">
          <tbody>
          

  <tr >
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465309" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="850" data-lp_den="1000" data-price_type="LP" data-hcap="-7.0" data-minor-sort = "H">
  <span class="outcome-name">
     Racing 92  </span>
  <span class="handicap-value" data-ev_mkt_id="23765369" data-sort="H">
            ( -7.0 )       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465309" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="850" data-lp_den="1000" data-price_type="LP" data-hcap="-7.0" data-minor-sort = "H" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,85</a>
        </div>
        </div>      </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465310" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="21000" data-lp_den="1000" data-price_type="LP" data-hcap="-7.0" data-minor-sort = "L">
  <span class="outcome-name">
     Egalité  </span>
  <span class="handicap-value" data-ev_mkt_id="23765369" data-sort="L">
            ( -7.0 )       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465310" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="21000" data-lp_den="1000" data-price_type="LP" data-hcap="-7.0" data-minor-sort = "L" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">22,0</a>
        </div>
        </div>      </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465311" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="850" data-lp_den="1000" data-price_type="LP" data-hcap="7.0" data-minor-sort = "A">
  <span class="outcome-name">
     Toulouse  </span>
  <span class="handicap-value" data-ev_mkt_id="23765369" data-sort="A">
            ( +7.0 )       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765369" data-ev_mkt_status="A" data-ev_oc_id="156465311" data-ev_oc_status="A" data-sort="MH" data-bir_index="0" data-lp_num="850" data-lp_den="1000" data-price_type="LP" data-hcap="7.0" data-minor-sort = "A" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,85</a>
        </div>
        </div>      </td>
      </tr>

          </tbody>
        </table>
          </div>
  </div>
                

  <div class="table table-event shadow " data-market_sort="
  MR"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A">

    <div class="row">
              <div class="table--header-orange table--header-full table--market-sort">
                      <div class="col-sm-9 pr-0">
              <div class="table--header">
                <a href="#table-content-23765370" role="button" data-toggle="collapse" aria-expanded="true" aria-controls="table-content-23765370"
                   class="table--header--inner ">
                  <span class="glyphicon glyphicon-chevron-down"></span>
                  <h3 class="table--header-title">
                    Vainqueur du match
                    
                                          <span class="trow--icon circled-icon bet-cashout-event">
                        <span class="glyphicon glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction bet-cashout-event-span" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
                      </span>
                    
                  </h3>
                </a>
              </div>
            </div>
          
                    <div class="col-sm-3 pl-0">
            <div class="table--header">
              <a class="table--header-rules overlay-trigger tc-track-element-events"
                 data-action="open" data-target-name=".popin"
                 href="/pservices/bet_rules"
                 data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.regles_du_pari">
                Règles du pari              </a>
            </div>
          </div>
        </div>
          </div>

    <div class="table--main
       in"
         id="table-content-23765370" role="group" aria-expanded="true" >
              <table class="table table-bordered table--fixed mb-0">
          <tbody>
          

  <tr >
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465312" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="300" data-lp_den="1000" data-price_type="LP" data-hcap="0">
  <span class="outcome-name">
     Racing 92  </span>
  <span class="handicap-value" data-ev_mkt_id="23765370" data-sort="H">
       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465312" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="300" data-lp_den="1000" data-price_type="LP" data-hcap="0" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,30</a>
        </div>
        </div>      </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465313" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="19000" data-lp_den="1000" data-price_type="LP" data-hcap="0">
  <span class="outcome-name">
     Egalité  </span>
  <span class="handicap-value" data-ev_mkt_id="23765370" data-sort="D">
       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465313" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="19000" data-lp_den="1000" data-price_type="LP" data-hcap="0" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">20,0</a>
        </div>
        </div>      </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465314" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="2200" data-lp_den="1000" data-price_type="LP" data-hcap="0">
  <span class="outcome-name">
     Toulouse  </span>
  <span class="handicap-value" data-ev_mkt_id="23765370" data-sort="A">
       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765370" data-ev_mkt_status="A" data-ev_oc_id="156465314" data-ev_oc_status="A" data-sort="MR" data-bir_index="0" data-lp_num="2200" data-lp_den="1000" data-price_type="LP" data-hcap="0" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">3,20</a>
        </div>
        </div>      </td>
      </tr>

          </tbody>
        </table>
          </div>
  </div>
                

  <div class="table table-event shadow " data-market_sort="
  HH"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765367" data-ev_mkt_status="A">

    <div class="row">
              <div class="table--header-orange table--header-full table--market-sort">
                      <div class="col-sm-9 pr-0">
              <div class="table--header">
                <a href="#table-content-23765367" role="button" data-toggle="collapse" aria-expanded="true" aria-controls="table-content-23765367"
                   class="table--header--inner ">
                  <span class="glyphicon glyphicon-chevron-down"></span>
                  <h3 class="table--header-title">
                    1 2
                    
                                          <span class="trow--icon circled-icon bet-cashout-event">
                        <span class="glyphicon glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction bet-cashout-event-span" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
                      </span>
                    
                  </h3>
                </a>
              </div>
            </div>
          
                    <div class="col-sm-3 pl-0">
            <div class="table--header">
              <a class="table--header-rules overlay-trigger tc-track-element-events"
                 data-action="open" data-target-name=".popin"
                 href="/pservices/bet_rules"
                 data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.regles_du_pari">
                Règles du pari              </a>
            </div>
          </div>
        </div>
          </div>

    <div class="table--main
       in"
         id="table-content-23765367" role="group" aria-expanded="true" >
              <table class="table table-bordered table--fixed mb-0">
          <tbody>
          

  <tr >
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765367" data-ev_mkt_status="A" data-ev_oc_id="156465305" data-ev_oc_status="A" data-sort="HH" data-bir_index="0" data-lp_num="190" data-lp_den="1000" data-price_type="LP" data-hcap="0">
  <span class="outcome-name">
     Racing 92  </span>
  <span class="handicap-value" data-ev_mkt_id="23765367" data-sort="H">
       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765367" data-ev_mkt_status="A" data-ev_oc_id="156465305" data-ev_oc_status="A" data-sort="HH" data-bir_index="0" data-lp_num="190" data-lp_den="1000" data-price_type="LP" data-hcap="0" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,19</a>
        </div>
        </div>      </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765367" data-ev_mkt_status="A" data-ev_oc_id="156465306" data-ev_oc_status="A" data-sort="HH" data-bir_index="0" data-lp_num="1800" data-lp_den="1000" data-price_type="LP" data-hcap="0">
  <span class="outcome-name">
     Toulouse  </span>
  <span class="handicap-value" data-ev_mkt_id="23765367" data-sort="A">
       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765367" data-ev_mkt_status="A" data-ev_oc_id="156465306" data-ev_oc_status="A" data-sort="HH" data-bir_index="0" data-lp_num="1800" data-lp_den="1000" data-price_type="LP" data-hcap="0" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">2,80</a>
        </div>
        </div>      </td>
      </tr>

          </tbody>
        </table>
          </div>
  </div>
                

  <div class="table table-event shadow " data-market_sort="
  WH"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765368" data-ev_mkt_status="A">

    <div class="row">
              <div class="table--header-orange table--header-full table--market-sort">
                      <div class="col-sm-9 pr-0">
              <div class="table--header">
                <a href="#table-content-23765368" role="button" data-toggle="collapse" aria-expanded="true" aria-controls="table-content-23765368"
                   class="table--header--inner ">
                  <span class="glyphicon glyphicon-chevron-down"></span>
                  <h3 class="table--header-title">
                    1 2 avec handicap.
                    
                    
                  </h3>
                </a>
              </div>
            </div>
          
                    <div class="col-sm-3 pl-0">
            <div class="table--header">
              <a class="table--header-rules overlay-trigger tc-track-element-events"
                 data-action="open" data-target-name=".popin"
                 href="/pservices/bet_rules"
                 data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.regles_du_pari">
                Règles du pari              </a>
            </div>
          </div>
        </div>
          </div>

    <div class="table--main
       in"
         id="table-content-23765368" role="group" aria-expanded="true" >
              <table class="table table-bordered table--fixed mb-0">
          <tbody>
          

  <tr >
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765368" data-ev_mkt_status="A" data-ev_oc_id="156465307" data-ev_oc_status="A" data-sort="WH" data-bir_index="0" data-lp_num="700" data-lp_den="1000" data-price_type="LP" data-hcap="-7.5" data-minor-sort = "H">
  <span class="outcome-name">
     Racing 92  </span>
  <span class="handicap-value" data-ev_mkt_id="23765368" data-sort="H">
            ( -7.5 )       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765368" data-ev_mkt_status="A" data-ev_oc_id="156465307" data-ev_oc_status="A" data-sort="WH" data-bir_index="0" data-lp_num="700" data-lp_den="1000" data-price_type="LP" data-hcap="-7.5" data-minor-sort = "H" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,70</a>
        </div>
        </div>      </td>
          <td>
              </td>
          <td>
        <div  class="table--wrapper-align-middle clearfix">
<div  class="table--element-align-middle hierarchy-outcome-name"  data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765368" data-ev_mkt_status="A" data-ev_oc_id="156465308" data-ev_oc_status="A" data-sort="WH" data-bir_index="0" data-lp_num="620" data-lp_den="1000" data-price_type="LP" data-hcap="7.5" data-minor-sort = "A">
  <span class="outcome-name">
     Toulouse  </span>
  <span class="handicap-value" data-ev_mkt_id="23765368" data-sort="A">
            ( +7.5 )       </span>
</div>

              <div class="pull-right">
        <a href="#"  class="hierarchy-outcome-price btn btn-odds tc-track-element-events"           data-ev_id="666562" data-ev_status="A" data-ev_mkt_id="23765368" data-ev_mkt_status="A" data-ev_oc_id="156465308" data-ev_oc_status="A" data-sort="WH" data-bir_index="0" data-lp_num="620" data-lp_den="1000" data-price_type="LP" data-hcap="7.5" data-minor-sort = "A" data-event_id="racing_92__egalite__toulouse" data-compet_id="top_14" data-sport_id="rugby" data-name="sportif.clic.parier.sports.competition.match.cote">1,62</a>
        </div>
        </div>      </td>
      </tr>

          </tbody>
        </table>
          </div>
  </div>
      </div>
  </div>

  
  </div>
            </div>
                                                                                                                                                                                                                                                                  </div>
    </div>
  </div>
</div>

<div class="col-md-3 hidden-sm">
  <div class="row">
                                                                                                                                                                                            <div class="three-rows-region--first-right">
          <div class="panel-pane pane-block pane-obet-betslip-core-betslip col-xs-12 pane--cols visible-lg-block"  >
  
      
  
  <div class="pane-content">
    
<div id="betslip" class="betslip bets">
  <div class="bets--inner">
    <div class="bets-wrapper">

      <header class="bets-header" id="bets-trigger--collapse">
        <div class="bets-header--infos">
          <span class="glyphicon glyphicon-pmu-basket desktop-only bets-header--icon"></span>
          <div class="bets-header--titleAndSelection">
            <div class="bets-header--title">
              <a href="#" class="bets-header--icon-collapse">
                <span class="glyphicon glyphicon-chevron-down"></span>
              </a>
              <span class="betslip-blue-header--title">Mes paris</span>
            </div>
            
<script type="text/template" id="betslip-icon-template">
     <%= betCountText %> <span class="num-selections">(<%= betCount %>)</span>
</script>
            <span class="bets-header--selection"></span>
          </div>
        </div>
        <a class="bets-header--clearbasket visible-lg"  title="Supprimer toutes les sélections du panier" id="betslip-clear">
          <span class="glyphicon glyphicon-pmu-trash"></span>
        </a>
        <a href="#" class="overlay-trigger bets-header--icon-basket" data-target-name="#basket" data-action="close">
          <span class="glyphicon glyphicon-pmu-basket"></span>
        </a>

        <a class="bets-header--icon-info hidden" target="_blank" href="#">
          <span class="glyphicon glyphicon-pmu-info" data-toggle="tooltip" data-placement="bottom" title="Aide" style="height: auto;"></span>
        </a>
      </header>

      <img id="betslip-loader" class="center-block" style="display: none;" src="/misc/progress.gif" alt="Chargement" />
      <div id="betslip-body" class="bets-content">
        <div class="tabs-wrapper">
            <header class="tabs-header" id="bet-types">
              <ul class="nav nav-tabs" role="tablist">
                <li role="presentation" class="simple-tab active non-persistent">
                    <a href="#bets-simple" aria-controls="bets-simple" role="tab" data-toggle="tab" aria-expanded="true"><span>Simple</span></a>
                </li>
                <li role="presentation" class="combine-tab">
                  <a href="#bets-combine" aria-controls="bets-combine" role="tab" data-toggle="tab" aria-expanded="false"><span>Combiné</span></a>
                </li>
                <li role="presentation" class="system-tab">
                  <a href="#bets-system1462" aria-controls="bets-system1462" role="tab" data-toggle="tab" aria-expanded="false"><span>Système</span></a>
                </li>
              </ul>
              <a class="bets-header--clearbasket hidden-lg" id="betslip-clear">
                <span class="glyphicon glyphicon-pmu-trash"></span>
              </a>
            </header>

            <div id="betslip-pre-place-bets" class="tab-content">
              <section role="tabpanel" class="tab-pane active" id="bets-simple" data-scope="singles">
                <div id="betslip-singles-body" class="betslip-singles-body tab-pane--content collapse in "></div>
                <footer class="tab-pane--footer">
                  <div  id="betslip-totals" class="bets-total">
                    <div class="trow--inline">
                      <div class="total-bet">
                        Mise simple : <span class="total-bet--value betslip-numeric betslip-singles-stake">0,00€</span>
                      </div>
                    </div>
                    <div class="trow--inline">
                      <div class="potential-gain">
                        Gains potentiels : <span class="potential-gain--value betslip-singles-returns">0,00€</span>
                      </div>
                      <div class="potential-bonus singles invisible">
                        Dont Bonus potentiel : <span class="potential-bonus--value singles-bonus">0,00€</span>
                      </div>
                    </div>
                  </div>
                  <div class="approvisionning_link hidden">
                    <a href="https://compte.pmu.fr/approvisionnement?clientApi=2&typeCompte=2010&redirectAuto=true&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2Fhttps%3A%2F%2Fparis-sportifs.pmu.fr%2Fevent%2F666562"><em>Approvisionner mon compte</em></a>
                  </div>
                  <div class="bets-submit">
                    <button id="betslip-place-singles" type="button" disabled class="btn btn-cta btn-orange btn-block bet-place place-singles">
                      Valider mes paris</button>
                  </div>
                </footer>
              </section>
              <section role="tabpanel" class="tab-pane" id="bets-combine" data-scope="multiples">
                <div class="tab-pane--content">
                  <div id="betslip-multiples-body" class="tab-pane--content collapse in"></div>
                </div>
                <footer class="tab-pane--footer">
                  <div id="acc-bet"></div>
                  <div  id="betslip-totals" class="bets-total trow">
                    <div class="trow--inline">
                      <div class="potential-gain">
                        Gains potentiels : <span class="potential-gain--value betslip-multiples-returns">0,00€</span>
                      </div>
                      <div class="potential-bonus combine invisible">
                        dont CombiMax (<span class="combiMax-bonus"></span> %) : <span class="potential-bonus--value multiples-bonus">0,00€</span>
                      </div>
                    </div>
                  </div>

                  <div id="combiMax_upselling" class="combiMax hide">
                    <div class="combiMax--block col-sm-4">
                      <img src="/profiles/core/themes/pmu_theme/resources/public/combimax.png" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au CombiMax" alt="combimax">
                    </div>
                    <div class="combiMax--block combiMax--table col-sm-8">
                      <div id="combiMax_upselling_msg">
                        <div class="combiMax-message">Combinez au moins 4 sélections et gagnez 5 % de bonus!</div>
                        <div class="combiMax-upselling hide">Ajoutez encore une sélection et gagnez <span class="combiMax-reward"></span> % de bonus!</div>
                      </div>
                    </div>
                    <div class="clearfix"></div>
                  </div>

                  <div class="approvisionning_link hidden">
                    <a href="https://compte.pmu.fr/approvisionnement?clientApi=2&typeCompte=2010&redirectAuto=true&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2Fhttps%3A%2F%2Fparis-sportifs.pmu.fr%2Fevent%2F666562"><em>Approvisionner mon compte</em></a>
                  </div>
                  <div class="bets-submit">
                    <button id="betslip-place-multiples" type="button" disabled class="btn btn-cta btn-orange btn-block bet-place place-multiples">
                      Valider mes paris</button>
                  </div>
                </footer>
              </section>
              <section role="tabpanel" class="tab-pane" id="bets-system1462" data-scope="systems">
                <div class="panel-wrapper">
                  <div class="tab-pane--content">
                    <div class="panel-wrapper-inner">
                      <div class="betslip-systems-legs"></div>
                    </div>
                  </div>
                  <div class="tab-pane--content bets-type--system-container">
                    <div class="bets-type--system trow"></div>
                  </div>
                </div>

                <footer class="tab-pane--footer">
                  <div  id="betslip-totals" class="bets-total trow">
                    <div class="trow--inline">
                      <div class="total-bet">
                        Pari : <span class="total-bet--value betslip-numeric betslip-systems-stake">0,00€</span>
                      </div>
                    </div>
                    <div class="trow--inline">
                      <div class="potential-gain">
                        Gains potentiels : <span class="potential-gain--value betslip-systems-returns">0,00€</span>
                      </div>
                      <div class="potential-bonus systems invisible">
                        Dont Bonus potentiel : <span class="potential-bonus--value systems-bonus">0,00€</span>
                      </div>
                    </div>
                  </div>
                  <div class="approvisionning_link hidden">
                    <a href="https://compte.pmu.fr/approvisionnement?clientApi=2&typeCompte=2010&redirectAuto=true&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2Fhttps%3A%2F%2Fparis-sportifs.pmu.fr%2Fevent%2F666562"><em>Approvisionner mon compte</em></a>
                  </div>
                  <div class="bets-submit">
                    <button id="betslip-place-systems" type="button" disabled class="btn btn-cta btn-orange btn-block bet-place place-systems">
                      Valider mes paris</button>
                  </div>
                </footer>
              </section>
            </div><!-- End of .tab-content -->

          <div id="betslip-post-place-bets" style="display: none; height: 100%;">
                          <div id="betslip-receipt" class="tab-content" style="height: 100%;"></div>
                      </div>
          <div id="betslip-async-waiting" class="text-center">
            <div class="betslip-loader">
              <h3>Chargement.....</h3>
              <br/>
              <img src="/profiles/core/themes/pmu_theme/resources/public/loader_big.gif" alt="Chargement" />
            </div>
          </div>
        </div><!-- End of .tab-wrapper -->
      </div> <!-- End of .bets-content -->

      <!-- Popup Errors wrappers - helpers -->
      <a id="trigger-betslip-modal" class="overlay-bets-trigger" data-target-name=".popin-bets-error" data-action="open" href="#"></a>
      <a id="trigger-betslip-confirm-modal" class="overlay-trigger" data-target-name=".popin" data-action="open" href="#"></a>
      <aside class="overlay-bets"></aside>
      <aside class="popin-bets-validate"></aside>
      <aside class="popin-bets-error"></aside>
      <!-- End of .Popup Errors -->

      <!-- Errors template-->
      <script type="text/template" id="betslip-errors-template">
        <% errors.forEach(function(error) { %>
        <header class="popin-bets-error--header">
          <h6><%= error.title %></h6>
        </header>

        <div class="popin-bets-error--content">
          <p><%= error.error %></p>
          <% if (error.code == 'WEEKLY_LIMIT_REACHED'){ %>
          <a href="https://compte.pmu.fr/autolimitations?clientApi=2&typeCompte=2010&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2F" target="_blank" class="btn btn-cta btn-dark-grey btn-block">Modifier</a>
          <% } %>
                    <% if (error.code == Drupal.t('REMAINING_BETS')) { %>
          <button id="remaining-bets-preserve-selections" class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">Conserver mes sélections et rejouer</button>
          <% } %>
          <br/>
          <button id="<% if (error.code == Drupal.t('REMAINING_BETS')) { %>remaining-bets-clear<% } %>" class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">Annuler</button>
        </div>
        <% }); %>
      </script>
      <script type="text/template" id="betslip-single-leg-template">
        <div class="betslip-single" data-ev_id="<%= eventId %>" data-ev_mkt_id="<%= marketId %>" data-ev_status="A" data-ev_mkt_status="A" data-ev_oc_id="<%= selectionId %>" data-ev_oc_status="A">
          <div class="trow--event">

            <span class="trow--icon glyphicon glyphicon-pmu-<%= className %>"></span>
            <span class="trow--event-name" data-typename="<%= typeName %>" data-eventname="<%= eventName %>" data-eventstarttime="<%= eventStartTime %>" data-marketname="<%= marketName %>" data-selectionname="<%= selectionName %>"><%= eventName %></span>
          </div>

          <div class="trow--bet">
            <div class="trow--bet-inline inline-table">
              <div class="trow--bet-title"><%= marketName %></div>

              <% if (specialOffer == 'MBS' && eventIsLiveNow != true) { %>
                <span class="trow--icon glyphicon glyphicon-pmu-price-tag-black icon-orange"></span>
              <% } %>

              <% if (cashoutAvail == 'Y' || cashoutAvail == 'S') { %>
              <span class="trow--icon circled-icon glyphicon-pmu-cashOut-icon">
                <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
              </span>
              <% } %>

              <% if (isCombimax == true) { %>
              <div class="trow--bet-iconsContainer">
                <div class="trow--bet-inline trow--bet-icons">
                    <span class="trow--bet-max">
                      <img src="/profiles/core/themes/pmu_theme/resources/public/combimax_max.png" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au CombiMax" alt="combinax" />
                    </span>
                </div>
              </div>
              <% }%>
            </div>

            <div class="trow--bet-inline selection" data-ev_oc_id="<%= selectionId %>" data-ev_oc_status="A">
              <span class="trow--bet-choice">
                <span><%= selectionName %></span>
                <% if (parseFloat(hcap) !== 0) { %>
                  <span class="handicap-value" data-ev_mkt_id="<%= marketId %>" data-sort="<%= selectionMeaningMinorCode %>">
                    (<%= (parseFloat(hcap) > 0) ? "+" + hcap : hcap %>)
                  </span>
                <% }%>
              </span>
              <span class="trow--bet-odd betslip-single-price betslip-numeric odds" data-ev_oc_id="<%= selectionId %>" data-lp_num="<%= priceNum %>" data-lp_den="<%= priceDen %>"><%= priceOutput.replace('.', ',') %></span>
            </div>
          </div>

          <div class="trow--info">
            <a
              href="#"
              tabindex="1"
              class="betslip-single-info"
              data-toggle="popover"
              data-trigger="hover focus"
              data-placement="left"
              title="Plus d'infos"
              data-content="<%= eventName %><br /><%= eventStartTime %><br /><%= marketName %><br /><%= selectionName %>"
              >
              <span class="glyphicon glyphicon-pmu-info icon-orange"></span>
            </a>
          </div>
          <div class="trow--delete">
            <button class="betslip-remove" data-selection="<%= selectionId %>">
              <span class="glyphicon glyphicon-pmu-close icon-grey" title="Supprimer cette sélection"></span>
            </button>
          </div>
          <div class="singlebet">
          </div>
      </script>
      <!-- Bet Errors template-->
      <script type="text/template" id="betslip-bet-errors-template">
        <% groupedErrors.forEach(function(group) { %>
          <header class="popin-bets-error--header">
            <h6>Information</h6>
          </header>

          <div class="popin-bets-error--content">
            <% if (group.key == 'OUTCOME_SUSPENDED') { %>
              <% group.errors.forEach(function(error) { %>
                <% if (error.code == 'OUTCOME_SUSPENDED') { %>
                <p> Erreur sur la sélection ajoutée au panier. <br /><br />
                  Avertissement <br /><br />
                  Problème sur une sélection                </p>
                  <p><%= error.selectionName %>: Sélection est suspendu.</p>
                  <p>Vous ne pouvez pas la valider.</p>
                <% } %>
              <% }); %>
              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>
            <% } else if (group.key == 'MIN_MAX_BET_ERROR') { %>
              Pari impossible sur cette sélection              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>
            <% } else if (group.key == 'HANDICAP_CHANGED') { %>
              <% group.errors.forEach(function(error) { %>
                <p> Erreur sur la sélection ajoutée au panier. <br /><br />
                  Avertissement <br /><br />
                  Problème sur une sélection</p>
                <p><%= error.selectionName %>: Le pari handicap a changé (<%= (parseFloat(error.outcomeHandicap) > 0) ? "+" + error.outcomeHandicap : error.outcomeHandicap %>)</p>
                <br/>
            <% }); %>

                <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>
                <br/>
                <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss <% if (group.inBet) { %> accept-place <% } else { %> accept-modification <% } %>"
                        data-action="close" data-target-name=".popin-bets-error" <% if (group.scope){ %> data-scope="<%= group.scope %>" <% } %> data-leg-ref="<% group.errors.forEach(function(error) { %><%= error.legRef %>,<% }); %>">
                <% if (group.inBet) { %>
                  Accepter les modifications et placer un pari                <% } else { %>
                  Accepter les modifications                <% } %>
                </button>
            <% } else if (group.key == 'PRICE_CHANGED') { %>
              <% group.errors.forEach(function(error) { %>
                <p>Erreur avec une sélection</p>
                <p>Avertissement</p>
                <p>Problème sur une sélection</p>
                <p><%= error.selectionName %>: Prix modifié pour  <%= error.price %></p>
              <% }); %>

              <br/>
              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>
              <br/>
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss <% if (group.inBet) { %> accept-place <% } else { %> accept-modification <% } %>"
                      data-action="close" data-target-name=".popin-bets-error" <% if (group.scope){ %> data-scope="<%= group.scope %>" <% } %> data-leg-ref="<% group.errors.forEach(function(error) { %><%= error.legRef %>,<% }); %>">
              <% if (group.inBet) { %>
                Accepter les modifications et placer un pari              <% } else { %>
                Accepter les modifications              <% } %>
              </button>

            <% } else if (group.key == 'BIR_INDEX_CHANGED') { %>
              <% group.errors.forEach(function(error) { %>
              <p> Erreur sur la sélection ajoutée au panier. <br /><br />
                Avertissement <br /><br />
                Problème sur une sélection              </p>
              <p><%= error.selectionName %>: Ce pari n'est plus disponible <%= error.marketName %></p>
              <% }); %>

              <br/>
              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>

            <% } else if (group.key == 'WEEKLY_LIMIT_REACHED') { %>
              <p class="weekly-limit-reached"><%= group.errors[0].error  %></p>
              <a href="https://compte.pmu.fr/autolimitations?clientApi=2&typeCompte=2010&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2F" target="_blank" class="btn btn-cta btn-dark-grey btn-block">Modifier</a><br/>
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
                Plus Tard              </button>
            <% } else if (group.key == 'WEEKLY_LIMIT_EXCEEDED') { %>
              <p>Votre plafond sportif hebdomadaire est dépassé</p>
              <br />
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
                Annuler              </button>
            <% } else if (group.key == 'WEEKLY_BET_LIMIT_ALERT') { %>
              <p><%= group.errors[0].error  %></p><br />
                            <a href="https://compte.pmu.fr/autolimitations?clientApi=2&typeCompte=2010&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2F" target="_blank" class="btn btn-cta btn-dark-grey btn-block">Modifier</a><br/>
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger" data-action="close" data-target-name=".popin-bets-error">
                Plus Tard              </button>

            <% } else if (group.key == 'STAKE_TOO_HIGH') { %>
            <p><%= group.title  %>: </p>
            <% group.errors.forEach(function(error) { %>
              <p class="stake-too-high"><%= error.error  %></p>
              <br />
            <% }); %>
            <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
              Annuler            </button>

            <% } else if (group.key == 'STAKE_TOO_LOW') { %>
            <p><%= group.title  %>: </p>
            <% group.errors.forEach(function(error) { %>
            <p class="stake-too-high"><%= error.error  %></p>
            <br />
            <% }); %>
            <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
              Annuler            </button>

            <% } else if (group.key == 'LIVE_PRICE_NOT_AVAILABLE') { %>
              <% group.errors.forEach(function(error) { %>
                <p>Erreur avec une sélection</p>
                <p>Avertissement</p>
                <p>Problème sur une sélection</p>
                <p class="mb-15"><%= error.selectionName %>: Pas de cote disponible</p>
              <% }); %>
              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>

            <% } else if (group.key == 'EVENT_STARTED') { %>
              <% group.errors.forEach(function(error) { %>
                <p>Erreur avec une sélection</p>
                <p>Avertissement</p>
                <p>Problème sur une sélection</p>
                <p class="mb-15"><%= error.selectionName %>: L'évènement a déja commencé</p>
              <% }); %>
              <button class="btn btn-cta btn-dark-grey btn-block error-remove" data-selection="<% group.errors.forEach(function(error) { %><%= error.selectionId %>,<% }); %>"><% if (group.errors.length > 1) { %>Supprimer les sélections<% } else { %>Supprimez la sélection<% } %></button>
            <% } else if (group.key == 'MAX_PAYOUT') { %>
              <% group.errors.forEach(function(error) { %>
              <p class="stake-too-high"><%= error.error  %></p>
              <br />
              <% }); %>
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error" data-max-stake-value="1">
                OK              </button>
            <% } else if (group.key == 'INSUFFICIENT_FUNDS') { %>
            <p>Le solde de votre compte est insuffisant</p>
            <a href="https://compte.pmu.fr/approvisionnement?clientApi=2&typeCompte=2010&redirectAuto=true&redirectionUrl=https%3A%2F%2Fparis-sportifs%2Epmu%2Efr%2Fhttps%3A%2F%2Fparis-sportifs.pmu.fr%2Fevent%2F666562<%= group.current_path  %>" class="mt-10 btn-cta btn-dark-grey btn-block">
              Approvisionner mon compte            </a>
            <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
              Annuler            </button>
            <% } else { %>
              <p class="mb-15"><%= group.title  %></p>
              <button class="btn btn-cta btn-dark-grey btn-block overlay-bets-trigger bet-modal-dismiss" data-action="close" data-target-name=".popin-bets-error">
                Annuler              </button>
            <% } %>
          </div>
          <% }); %>
      </script>
    
<script type="text/template" id="betslip-single-template">
  <% if (status == 'active') { %>
      <div class="trow--bet-inline stake-returns">
        <div class="trow--bet-sum" data-min-bet="<%= minBet %>" data-max-bet="<%= maxBet %>">
          Pari          <input class="form-control input-bet stake" type="text" value="<%= stake.toFixed(2).replace('.', ',') %>" maxlength="15" size="7"/>
        </div>
        <span class="trow--bet-gain betslip-estimated-returns">Gains <strong class="trow--bet-gain--value"><%= estimatedReturns.toFixed(2).replace('.', ',') %>€</strong></span>
        <% if (potentialBonus > 0) { %>
        <div class="col-md-12"><span class="badge">Bonus potentiel: </span> <%= potentialBonus.toFixed(2).replace('.', ',') %></div>
        <% } %>
      </div>

    <% if (eachWayAvailable) { %>
      <div class="trow--checkbox checkbox">
        <fieldset>
          <input type="checkbox" class="checkbox each-way-avail" id="sb-<%= selectionId %>" <% if (type == 'E')%> checked="checked" <% ; %> />
          <label for="sb-<%= selectionId %>">Gagnant / Place</label>
        </fieldset>
      </div>
      <div class="trow--inline">
        <span class="text-xxxsmall"><%= eachWayPlaces %> places payées <%= eachWayFractionNum %>/<%= eachWayFractionDen %> de la cote</span>
      </div>
    <% } %>
  <% } %>

  <% errors.forEach(function(error) { %>
  <div class="bet-label text-center"><%= error %></div>
  <% }); %>
  <div class="free"></div>
</script>

<script type="text/template" id="betslip-multiple-template">
  <div class="betslip-multiple">
    <% legs.models.forEach(function(leg) { %>
    <div class="betslip-single trow" data-ev_id="<%= leg.attributes.eventId %>" data-ev_mkt_id="<%= leg.attributes.marketId %>" data-ev_status="A" data-ev_mkt_status="A" data-ev_oc_status="A" data-ev_oc_id="<%=leg.attributes.selectionId %>">

      <div class="trow--event">
        <span class="trow--icon glyphicon glyphicon-pmu-<%= leg.attributes.className %>"></span>
        <span class="trow--event-name" data-typename="<%= leg.attributes.typeName %>" data-eventname="<%= leg.attributes.eventName %>" data-eventstarttime="<%= leg.attributes.eventStartTime %>" data-marketname="<%= leg.attributes.marketName %>" data-selectionname="<%= leg.attributes.selectionName %>"><%= leg.attributes.eventName %></span>
      </div>
      <div class="trow--bet">
        <div class="trow--bet-inline inline-table">
          <div class="trow--bet-title"><%= leg.attributes.marketName %></div>

          <% if (leg.attributes.specialOffer == 'MBS' && leg.attributes.eventIsLiveNow != true) { %>
            <span class="trow--icon glyphicon glyphicon-pmu-price-tag-black icon-orange"></span>
          <% }%>

          <% if (leg.attributes.cashoutAvail == 'Y' || leg.attributes.cashoutAvail == 'S') { %>
            <span class="trow--icon circled-icon glyphicon-pmu-cashOut-icon">
              <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
            </span>
          <% }%>

          <% if (leg.attributes.isCombimax == true) { %>
            <div class="trow--bet-iconsContainer">
              <div class="trow--bet-inline trow--bet-icons">
                    <span class="trow--bet-max">
                      <img src="/profiles/core/themes/pmu_theme/resources/public/combimax_max.png" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au CombiMax" alt="combinax" />
                    </span>
              </div>
            </div>
          <% }%>
        </div>
        <div class="trow--bet-inline selection" data-ev_oc_id="<%= leg.attributes.selectionId %>" data-ev_oc_status="A">
          <div class="col-xs-1 hidden">
            <label class="">
              <input class="include-in-multiples" type="checkbox" <% if (leg.attributes.includeInMultiples)%> checked="checked" <% ; %>/>
              <span></span>
            </label>
          </div>
          <span class="trow--bet-choice">
            <span><%= leg.attributes.selectionName %></span>
            <% if (leg.attributes.hcap !== 0) { %>
              <span class="handicap-value" data-ev_mkt_id="<%= leg.attributes.marketId %>" data-sort="<%= leg.attributes.selectionMeaningMinorCode %>">
                <% if (parseFloat(leg.attributes.hcap) > 0) {%> (+<%= leg.attributes.hcap %>) <% } else if (parseFloat(leg.attributes.hcap) < 0) {%> (<%= leg.attributes.hcap %>) <% } %>
              </span>
            <% }%>
          </span>
          <span class="trow--bet-odd betslip-single-price betslip-numeric odds" data-ev_oc_id="<%= leg.attributes.selectionId %>" data-lp_num="<%= leg.attributes.priceNum %>" data-lp_den="<%= leg.attributes.priceDen %>">
            <%= OpenBet.Price.convertToCurrentPricePreference(leg.attributes.priceNum, leg.attributes.priceDen).replace('.', ',')  %>
          </span>
        </div>
      </div>
      <div class="trow--info">
        <a
          href="#"
          tabindex="0"
          class="betslip-single-info"
          data-toggle="popover"
          data-trigger="hover focus"
          title="Plus d'infos"
          data-content="<%= leg.attributes.eventName %><br /><%= leg.attributes.eventStartTime %><br /><%= leg.attributes.marketName %><br /><%= leg.attributes.selectionName %>"
          >
          <span class="glyphicon glyphicon-pmu-info icon-orange"></span>
        </a>
      </div>
      <div class="trow--delete">
        <button class="betslip-remove" data-selection="<%= leg.id %>">
          <span class="glyphicon glyphicon-pmu-close icon-grey" title="Supprimer cette sélection"></span>
        </button>
      </div>

    </div>
    <% }); %>
</script>


<script type="text/template" id="betslip-acc-footer-template">
  <div class="bets-type--triple trow" id="acc-totals-stake">
    <% if (type == 'DBL' || type == 'TBL') { %>
    <p class="trow--title"><%= Drupal.t('bet') + ' ' + typeName %>
      <% if (cashoutAvail) { %>
        <span class="trow--icon circled-icon glyphicon-pmu-cash-out--inline glyphicon-pmu-cash-out--bet">
          <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
        </span>
      <% }  %>
    </p>
    <% } else { %>
    <p class="trow--title"><%= typeName %>
      <!-- TODO: remove the following comments -->
      <% if (cashoutAvail) { %>
        <span class="trow--icon circled-icon glyphicon-pmu-cash-out--inline glyphicon-pmu-cash-out--bet">
          <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny"  data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
        </span>
      <% }  %>
    </p>
    <% } %>
    <div class="free"></div>
    <% if (eachWayAvailable) { %>
    <div class="trow--checkbox checkbox">
      <fieldset>
        <input type="checkbox" class="checkbox each-way-avail" id="sb-acc-ew" <% if (legType == 'E')%> checked="checked" <% ; %> />
        <label for="sb-acc-ew">Gagnant / Placé</label>
      </fieldset>
    </div>
    <% } %>
  </div>
  <div class="trow--inline acc-totals-stake bets-total trow">
    <div class="total-bet-sum betslip-stake betslip-numeric trow--inline">
      Pari :
      <span class="trow--currency"> € </span>
      <input class="form-control stake input-total-bet" value="<%= parseFloat(stake).toFixed(2).replace('.', ',') %>"/>
    </div>
    <% errors.forEach(function(error) { %>
      <div class="bet-label text-center"><%= error %></div>
    <% }); %>
  </div>
  <div class="trow--inline acc-totals-returns bets-total trow">
    <div class="total-odd trow--inline">
      Cote cumulée : <span class="total-odd--value betslip-estimated-returns betslip-numeric"><%= payoutPotential.toFixed(2).replace('.', ',') %></span>
    </div>
  </div>
</script>
<script type="text/template" id="betslip-freebet-select-template">
  <div class="col-md-12 col-sm-12 col-xs-5">
    <select class="form-control form-select"></select>
  </div>
</script>
<script type="text/template" id="betslip-freebet-template">
  <%= freebetValue %> -- <%= freebetId %>
</script>

<script type="text/template" id="betslip-freebet-option-template">
  <option class="unselected-freebet">Choisir</option>
  <% _.forEach(bets, function(bet) { %>
    <% if (bet.betTypeName) { %>
      <option data-bet-ref="<%= bet.betRef %>" <% if (bet.selected) %> selected <%; %> class="freebet-option"><%= bet.betTypeName %></option>
    <% } else { %>
      <option data-bet-ref="<%= bet.betRef %>" <% if (bet.selected) %> selected <%; %> class="freebet-option"><%= bet.eventName %> - <%= bet.selectionName %></option>
    <% } %>
  <% }); %>
</script>

<script type="text/template" id="betslip-freebet-value-message-template">
  <!--  We have to keep the template script tag here cause its already
   registered as underscore template. -->
</script>

<script type="text/template" id="betslip-free-option-template">
  <%= freebetValue %> € -- <%= freebetName %>
</script>


<script type="text/template" id="betslip-errors-template">
  <% errors.forEach(function(error) { %>
    <hr>
    <div class="alert alert-danger"><%= error %></div>
  <% }); %>
</script>

<script type="text/template" id="betslip-success-template">
      <div class="alert alert-success"><%= message %></div>
  </script>

<script type="text/template" id="betslip-title-template">
  <%= count %> bets in your betslip</script>

<script type="text/template" id="betslip-receipt-template">
  <div class="bets-content">

    <div class="tabs-wrapper">
      <header class="tabs-header">
        <h5>Vos sélections (<%= selectionsNumber %>)</h5>
      </header>

      <div class="tab-content">

          <section role="tabpanel" class="tab-pane active" id="bets-system3f24">
            <div class="panel-wrapper" style="max-height: calc(100% - 228px);">
              <div class="tab-pane--content" style="min-height: 40%;">
                <div class="panel-wrapper-inner">
                  <div class="betslip-systems-legs">
                    <% selections.forEach(function(selection) { %>
                    <div class="trow">
                      <div class="trow--event">
                        <span class="trow--icon glyphicon glyphicon-pmu-<%=  selection.className %>"></span>
                        <span class="trow--event-name"> <%= selection.eventName %> </span>
                      </div>
                      <div class="trow--bet">
                        <div class="trow--bet-inline">
                          <div class="trow--bet-title"><%= selection.typeName %></div>
                        </div>
                        <div class="trow--bet-inline inline-table">
                          <div class="trow--bet-title"><%= selection.marketName %></div>

                          <% if (selection.cashoutAvail == 'Y' || selection.cashoutAvail == 'S') { %>
                          <span class="trow--icon circled-icon glyphicon-pmu-cashOut-icon">
                            <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
                          </span>
                          <% }%>

                          <% if (selection.isCombimax == true) { %>
                            <div class="trow--bet-iconsContainer">
                              <div class="trow--bet-inline trow--bet-icons">
                                <span class="trow--bet-max">
                                  <img src="/profiles/core/themes/pmu_theme/resources/public/combimax_max.png" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au CombiMax" alt="combinax" />
                                </span>
                              </div>
                            </div>
                          <% }%>
                        </div>
                        <div class="trow--bet-inline">
                          <div class="trow--bet-title"><%= selection.eventStartTime %></div>
                        </div>
                        <div class="trow--bet-inline">
                          <span class="trow--bet-choice"><%= selection.selectionName %> <% if (selection.hcap !== '0'){ %>(<%= selection.hcap %>)<% } %></span>
                    <span class="trow--bet-odd"><%= selection.odds.replace('.', ',') %><% if (selection.type == 'E') %>
                  <%= selection.ewText %> @ <%= selection.ewFraction %>,
                  <%= selection.eachWayPlaces %> <%=selection.ewPlaceText%>
                  <% ; %></span>
                        </div>
                      </div>
                    </div>
                    <% }); %>
                  </div>
                </div>
              </div>

              <div class="tab-pane--content" style="margin-top: auto; bottom: 0;">
                <div class="bets-type--system bets-total trow">
                  <% bets.forEach(function(bet) { %>
                  <div class="trow--inline">
                    <div>
                      <span style="display:inline-table"><%= bet.typeName %></span>
                      <% if (bet.cashoutAvail == 1 && bet.systeme_cashout_allowed) { %>
                        <span class="trow--icon circled-icon glyphicon-pmu-cash-out--inline glyphicon-pmu-cash-out--bet">
                          <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny"  data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
                        </span>
                      <% } %>
                    </div>
                    <div>
                      <%= bet.numLines %> ligne(s) <%= bet.betStake.toFixed(2).replace('.', ',') %>€ par ligne                    </div>
                    <div>
                      Mise totale pour ce pari:
                      <span class="trow--sum"> <%= bet.betStakeTotal.toFixed(2).replace('.', ',') %>€</span>
                    </div>
                    <div class="potential-gain">
                      Gains potentiels:
                      <span class="potential-gain--value"> <%= bet.betReturns.toFixed(2).replace('.', ',') %>€</span>
                    </div>

                    <% if (bet.potentialBonus != '0'){ %>
                    <div class="potential-bonus">
                      <% if (isCombimax == 1) { %>
                        dont CombiMax <%= combimaxPercent %>:
                      <% } else { %>
                        Dont Bonus potentiel:
                      <% } %>

                      <span class="potential-bonus--value"><%= bet.potentialBonus.toFixed(2).replace('.', ',') %>€</span>
                    </div>
                    <% } %>

                    <div class="trow--ref mt-20">
                      N° de référence: <%= bet.receipt %>
                    </div>
                  </div>
                  <% }); %>
                </div>
              </div>
            </div>


            <footer class="tab-pane--footer">
              <div id="betslip-totals" class="bets-total trow">
                <div class="trow--inline">
                  <div class="mt-5">
                    Mise totale : <span class="total-odd--value betslip-total-stake"><%= receiptStake.toFixed(2).replace('.', ',') %>€</span>
                  </div>

                  <div class="mt-5">
                    Paris gratuits : <span class="total-free-odd--value"><%= totalFreeBetValue.toFixed(2).replace('.', ',') %>€</span>
                  </div>

                  <div class="mt-5">
                    Coût Total : <span class="total-price--value"><%= totalPaid.toFixed(2).replace('.', ',') %>€</span>
                  </div>
                </div>
              </div>

              <div id="receipt-buttons" class="bets-summary">
                <p class="bets-summary--valid">vos paris ont bien été enregistrés <span class="glyphicon glyphicon-ok"></span></p>

                <div class="trow--checkbox checkbox text-center">
                  <fieldset>
                    <input type="checkbox" class="checkbox" id="betslip-retain-selections">
                    <label for="betslip-retain-selections" class="text-orange text-xxsmall">Conserver mes sélections et rejouer</label>
                  </fieldset>
                </div>
                <div class="row">
                  <div class="col-sm-6">
                    <button type="button" id="betslip-print" class="btn btn-cta btn-orange btn-full-width" data-toggle="tooltip" data-placement="top" title="Imprimer">Imprimer</button>
                  </div>
                  <div class="col-sm-6">
                    <button type="button" id="betslip-ok" class="btn btn-cta btn-orange btn-full-width" data-toggle="tooltip" data-placement="top" title="Fermer">Fermer</button>
                  </div>
                </div>
              </div>
            </footer>

          </section><!-- Enf od #bets-system -->
        </div><!-- End of .tab-content -->
    </div><!-- End of .tab-wrapper -->
  </div>
</script>

<script type="text/template" id="betslip-singles-confirm">
  <div class="popin-bets-confirm-cash-out active">
    <header class="popin--header popin--header-blue">
      <div class="row">
        <div class="col-sm-10">
          <h6 class="text-center-correction">Confirmation prise de pari</h6>
        </div>
        <div class="col-sm-2">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close"><span class="glyphicon glyphicon-pmu-close"></span></a>
        </div>
      </div>
    </header>

    <div class="popin--content mt-20">
      <% if (priceChangeMsg != '') { %>
      <div class="row">
        <div class="col-sm-12">
          <p class="mb-15"><%= priceChangeMsg %></p>
        </div>
      </div>
      <% } %>

      <div class="row confirmation-popup-bet-details">
        <div class="col-sm-12">
          <% singles.forEach(function(bet) { %>
          <p class="mb-5">Mise de <%= bet.stake.toFixed(2).replace('.', ',') %> € sur <%= bet.selection %> <% if (bet.hcap !== '0'){ %> (<%= bet.hcap %>)<% } %> <% if (bet.legType == 'E'){ %> GP à <% }else { %> gagnant à  <% } %> <%= bet.odds.toString().replace('.', ',') %>.
            <% if (bet.legType == 'E'){ %>
            <%= bet.ewPlaces %> payées <%= bet.ewFraction %> de la cote. Mise totale pour ce pari: <%= bet.totalStake.toFixed(2).replace('.', ',') %>
            <% } %>
            <% if (bet.cashoutAvail == 'Y' || bet.cashoutAvail == 'S'){ %>
              <span class="trow--icon circled-icon popin--icon-cash-out glyphicon-pmu-cash-out--inline glyphicon-pmu-cashOut-icon">
                <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--tiny-medium"></span>
              </span>
            <% } %>
          </p>
          <% if (bet.cashoutAvail == 'F') { %>
          <p class="mt-15 mb-10">Warning: The Cashout is not available for bets using freebets.</p>
          <% } %>

          <% }); %>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <p class="mt-10 pixel-fix"><em>Êtes-vous sûr de vouloir placer ce panier ?</em></p>
        </div>
      </div>
      <div class="row popin--background-brown">
        <div class="col-sm-6">
          <p class="text-center">Mise totale :</p>
          <p class="text-center bet-value"><%= totalSinglesStake.toFixed(2).replace('.', ',') %> €</p>
        </div>
        <div class="col-sm-6">
          <p class="text-center">Gains potentiels pour ce panier :</p>
          <p class="text-center bet-value"> <%= totalSinglesPotential.toFixed(2).replace('.', ',') %> €</p>
        </div>
      </div>

      <% if (totalFreeBetValue > 0) { %>
        <div class="row">
          <div class="col-sm-12">
            <p><em>Total pari gratuit: <%= totalFreeBetValue.toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10"><em>Coût Total: <%= (totalSinglesStake - totalFreeBetValue).toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10 mb-5">Les gains issus d'un pari gratuit ne comprennent pas la mise.</p>
          </div>
        </div>
      <% } %>

      <% if (totalCashoutAbleBets > 0) { %>
      <div class="row">
        <div class="col-sm-12">
          <p class="message-alert">A noter : Ce pari sera éligible au Cash Out.</p>
        </div>
      </div>
      <% } %>

      <div class="row">
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <!--                <a>-->
          <div class="btn btn-cta btn-small btn-centered-block btn-orange confirm-singles">Confirmer</div>
          <!--                </a>-->
        </div>
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close">
            <div class="btn btn-cta btn-small btn-centered-block btn-grey">Annuler</div>
          </a>
        </div>
      </div>

    </div>
  </div>
</script>

<script type="text/template" id="betslip-systems-confirm">
  <div class="popin-bets-confirm-cash-out active">
    <header class="popin--header popin--header-blue">
      <div class="row">
        <div class="col-sm-10">
          <h6 class="text-center-correction">Confirmation prise de pari</h6>
        </div>
        <div class="col-sm-2">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close"><span class="glyphicon glyphicon-pmu-close"></span></a>
        </div>
      </div>
    </header>

    <div class="popin--content mt-20">

      <% if (priceChangeMsgs.length > 0) { %>
        <div class="row">
          <div class="col-sm-12">
            <% priceChangeMsgs.forEach(function(priceChangeMsg) { %>
              <p class="mb-15"><%= priceChangeMsg %></p>
            <% }); %>
          </div>
        </div>
      <% } %>

      <div class="confirmation-popup-bet-details">
        <% systems.forEach(function(bet) { %>
          <div class="row">
            <div class="col-sm-12">
              <p><%= bet.typeName %> (<%= bet.numLines %> paris).<% if (bet.legType == 'E'){ %> Gagnant / Placé <% } %>
                <% if (bet.cashoutAvailSystems == 'Y' && bet.systeme_cashout_allowed) { %>
                  <span class="trow--icon circled-icon popin--icon-cash-out glyphicon-pmu-cashOut-icon" style="display: inline">
                    <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--tiny-medium"></span>
                  </span>
                <% } %>
                <br/> <%= bet.numLines %> ligne(s) à <%= bet.stake.toFixed(2).replace('.', ',') %>€ par ligne.
              </p>
              <% if (bet.cashoutAvailSystems == 'F' && bet.systeme_cashout_allowed) { %>
                <p class="mt-15 mb-10">Warning: The Cashout is not available for bets using freebets.</p>
              <% } %>
            </div>
          </div>
          <div class="row">
            <div class="col-sm-12">
              <p class="mt-15 mb-15">Mise totale pour ce pari: <%= (bet.numLines * bet.stake).toFixed(2).replace('.', ',') %>€.</p>
            </div>
          </div>
        <% }); %>
      </div>

      <div class="row">
        <div class="col-sm-12">
          <p class="mt-10 pixel-fix"><em>Êtes-vous sûr de vouloir placer ce panier ?</em></p>
        </div>
      </div>
      <div class="row popin--background-brown">
        <div class="col-sm-6">
          <p class="text-center">Mise totale :</p>
          <p class="text-center bet-value"><%= totalSystemsStake.toFixed(2).replace('.', ',') %> €</p>
        </div>
        <div class="col-sm-6">
          <p class="text-center">Gains potentiels pour ce panier :</p>
          <p class="text-center bet-value"><%= totalSystemsPotential.toFixed(2).replace('.', ',') %> €</p>
          <% if (bonusPotential > 0) { %>
          <p class="text-center bet-bonus">Dont Bonus potentiel : <%= bonusPotential.toFixed(2).replace('.', ',') %> €</p>
          <% } %>
        </div>
      </div>

      <% if (totalFreeBetValue > 0) { %>
        <div class="row">
          <div class="col-sm-12">
            <p><em>Total pari gratuit: <%= totalFreeBetValue.toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10"><em>Coût Total: <%= (totalSystemsStake - totalFreeBetValue).toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10 mb-5">Les gains issus d'un pari gratuit ne comprennent pas la mise.</p>
          </div>
        </div>
      <% } %>

      <div class="row">
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <!--                <a href="#" class="overlay-trigger" data-target-name=".popin" data-action="close">-->
          <div class="btn btn-cta btn-small btn-centered-block btn-orange confirm-systems">Confirmer</div>
          <!--                </a>-->
        </div>
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close">
            <div class="btn btn-cta btn-small btn-centered-block btn-grey">Annuler</div>
          </a>
        </div>
      </div>
    </div>
  </div>
</script>
<script type="text/template" id="betslip-multiples-confirm">
  <div class="popin-bets-confirm-cash-out active">
    <header class="popin--header popin--header-blue">
      <div class="row">
        <div class="col-sm-10">
          <h6 class="text-center-correction">Confirmation prise de pari</h6>
        </div>
        <div class="col-sm-2">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close"><span class="glyphicon glyphicon-pmu-close"></span></a>
        </div>
      </div>
    </header>
    <div class="popin--content mt-20">

      <% if (priceChangeMsgs.length > 0) { %>
        <div class="row">
          <div class="col-sm-12">
            <% priceChangeMsgs.forEach(function(priceChangeMsg) { %>
              <p class="mb-15"><%= priceChangeMsg %></p>
            <% }); %>
          </div>
        </div>
      <% } %>

      <div class="row">
        <div class="col-sm-12">
          <p><%= multiple.typeName %>(<%= multiple.numLines %> pari).<% if (multiple.legType == 'E'){ %> Gagnant / Placé <% } %>
            <% if (multiple.cashoutAvailMultiple == 'Y' && totalFreeBetValue == 0) { %>
              <span class="trow--icon circled-icon popin--icon-cash-out glyphicon-pmu-cashOut-icon" style="display: inline">
                <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--tiny-medium"></span>
              </span>
            <% } %>
            <br/> <%= multiple.numLines %> ligne(s) à <%= parseFloat(multiple.stake).toFixed(2).replace('.', ',') %> € par ligne.
          </p>
          <% if (multiple.cashoutAvailMultiple == 'Y' && totalFreeBetValue > 0) { %>
            <p class="mt-15">Warning: The Cashout is not available for bets using freebets.</p>
          <% } %>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <p class="mt-15">Mise totale pour ce pari: <%= parseFloat(totalMultiplesStake).toFixed(2).replace('.', ',') %>€.</p>
        </div>
      </div>
      <div class="row">
        <div class="col-sm-12">
          <p class="mt-10 pixel-fix"><em>Êtes-vous sûr de vouloir placer ce panier ?</em></p>
        </div>
      </div>
      <div class="row popin--background-brown">
        <div class="col-sm-6">
          <p class="text-center">Mise totale :</p>
          <p class="text-center bet-value"><%= parseFloat(totalMultiplesStake).toFixed(2).replace('.', ',') %> €</p>
        </div>
        <div class="col-sm-6">
          <p class="text-center">Gains potentiels pour ce panier :</p>
          <p class="text-center bet-value"><%= multiple.potentialWin.toFixed(2).replace('.', ',') %> €</p>
          <% if (multiple.potentialBonus > 0) { %>
            <p class="text-center bet-bonus">Dont Bonus potentiel : <%= multiple.potentialBonus.toFixed(2).replace('.', ',') %> €</p>
          <% } %>
        </div>
      </div>
      <% if (totalFreeBetValue > 0) { %>
        <div class="row">
          <div class="col-sm-12">
            <p><em>Total pari gratuit: <%= parseFloat(totalFreeBetValue).toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10"><em>Coût Total: <%= (totalMultiplesStake - totalFreeBetValue).toFixed(2).replace('.', ',') %>€.</em></p>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-12">
            <p class="mt-10 mb-5">Les gains issus d'un pari gratuit ne comprennent pas la mise.</p>
          </div>
        </div>
      <% } %>

      <div class="row">
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <div class="btn btn-cta btn-small btn-centered-block btn-orange confirm-multiples">Confirmer</div>
        </div>
        <div class="col-sm-6 mb-20 mt-25 pixel-fix">
          <a href="#" class="overlay-trigger confirm-cancel" data-target-name=".popin" data-action="close">
            <div class="btn btn-cta btn-small btn-centered-block  btn-grey">Annuler</div>
          </a>
        </div>
      </div>
    </div>
  </div>
</script>
<script type="text/template" id="betslip-ew-template">
  <div class="trow--checkbox checkbox">
    <fieldset>
      <input type="checkbox" class="checkbox" id="sb-<%= selectionId %>" <% if (type == 'E')%> checked="checked" <% ; %> />
      <label for="sb-<%= selectionId %>">Gagnant / Place</label>
    </fieldset>
  </div>
  <div class="trow--inline">
    <span class="text-xxxsmall"><%= eachWayPlaces %> places payées <%= eachWayFractionNum %>/<%= eachWayFractionDen %> de la cote</span>
  </div>
</script><script type="text/template" id="betslip-multiplesystems-template">
  <div class="betslip-multiple system">
    <div class="system-bet--sum">
      <span style="display:inline-table"><%= typeName %> (<%= numLines %> paris)</span>
      <a href="#"
         class="system-bet--sum-desc"
         title="<%= multiBetTypeDesc %>"
      >
        <span class="glyphicon glyphicon-pmu-info icon-orange"></span>
      </a>
      <% if (cashoutAvail && systeme_cashout_allowed) { %>
        <span class="trow--icon circled-icon glyphicon-pmu-cash-out--inline glyphicon-pmu-cash-out--bet">
          <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny"  data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
        </span>
      <% }  %>
      <span class="trow--currency"> € </span>
      <input class="form-control input-bet stake" value="<%= parseFloat(stake).toFixed(2).replace('.', ',') %>">
    </div>
    <div class="free"></div>
    <% if (eachWayAvailable) { %>
    <div class="trow--checkbox checkbox">
      <fieldset>
        <input type="checkbox" class="checkbox each-way-avail" id="sb-system-<%= ref %>" <% if (legType == 'E')%> checked="checked" <% ; %> />
        <label for="sb-system-<%= ref %>">Gagnant / Placé</label>
      </fieldset>
    </div>
    <% } %>
  </div>
</script>
<script type="text/template" id="betslip-system-template">
  <div class="betslip-single system" data-ev_id="<%= eventId %>" data-ev_mkt_id="<%= marketId %>" data-ev_status="A" data-ev-mkt-status="A" data-ev_oc_id="<%= selectionId %>">
    <div class="trow--event">

      <span class="trow--icon glyphicon glyphicon-pmu-<%= className %>"></span>
      <span class="trow--event-name" data-typename="<%= typeName %>" data-eventname="<%= eventName %>" data-eventstarttime="<%= eventStartTime %>" data-marketname="<%= marketName %>" data-selectionname="<%= selectionName %>"><%= eventName %></span>
    </div>

    <div class="trow--bet">
      <div class="trow--bet-inline inline-table">
        <div class="trow--bet-title"><%= marketName %></div>

        <% if (specialOffer == 'MBS' && eventIsLiveNow != true) { %>
          <span class="trow--icon glyphicon glyphicon-pmu-price-tag-black icon-orange"></span>
        <% }%>
        <% if (cashoutAvail == 'Y' || cashoutAvail == 'S') { %>
          <span class="trow--icon circled-icon glyphicon-pmu-cashOut-icon">
            <span class="glyphicon glyphicon-orange glyphicon-pmu-cash-out glyphicon-pmu-cash-out--correction-orange glyphicon-pmu-cash-out--tiny" data-toggle="tooltip" data-placement="bottom" title="Pari éligible au Cash Out"></span>
          </span>
        <% }%>
      </div>

      <div class="trow--bet-inline selection" data-ev_oc_id="<%= selectionId %>" data-ev_oc_status="A">

        <span class="trow--bet-choice">
          <span><%= selectionName %></span>
          <% if (hcap !== 0) { %>
            <span class="handicap-value" data-ev_mkt_id="<%= marketId %>" data-sort="<%= selectionMeaningMinorCode %>">
              <% if (parseFloat(hcap) > 0) {%> (+<%= hcap %>) <% } else if (parseFloat(hcap) < 0) {%> (<%= hcap %>) <% } %>
            </span>
          <% }%>
        </span>
        <span class="trow--bet-odd betslip-single-price betslip-numeric odds" data-ev_oc_id="<%= selectionId %>" data-lp_num="<%= priceNum %>" data-lp_den="<%= priceDen %>"><%= priceOutput.replace('.', ',') %></span>
      </div>

    </div>

    <div class="trow--info">
      <a
        href="#"
        tabindex="0"
        class="betslip-single-info"
        data-toggle="popover"
        data-trigger="hover focus"
        title="Plus d'infos"
        data-content="<%= eventName %><br /><%= eventStartTime %><br /><%= marketName %><br /><%= selectionName %>"
        >
        <span class="glyphicon glyphicon-pmu-info icon-orange"></span>
      </a>
    </div>
    <div class="trow--delete">
      <button class="betslip-remove">
        <span class="glyphicon glyphicon-pmu-close icon-grey" title="Supprimer cette sélection"></span>
      </button>
    </div>

  </div>
</script>

    </div><!-- End of .bets-wrapper -->
  </div><!-- End of .bets-inner -->
</div>
<div class="header-sticky--placeholder"></div>
  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-pmu-register-banner-pmu-register-banner-block col-xs-12 pane--cols"  >
  
      
  
  <div class="pane-content">
    <div class="sb-push" id="sb-push-create-account">
  <a class="push-link" href="https://inscription.pmu.fr/?clientApi=2&typeCompte=2010&codePromo=SPORT&redirectionUrl=https%3A%2F%2Fparis-sportifs.pmu.fr%2F">
    <div class="push-create-account">
      <p class="push-create-account--title">J'ouvre un compte</p>
      <span class="glyphicon glyphicon-pmu-arrow-down"></span>
      <span class="push-sep"></span>
      <div class="push-create-account--text">
        <p>jusqu'à</p>
        <p class="push-create-account--highlight text-xxxlarge text-bold">100€</p>
        <p>offerts*</p>
      </div>
    </div>
  </a>
</div>
  </div>

  
  </div>
<div class="panel-separator"></div><div class="panel-pane pane-block pane-views-push-banners-block col-xs-12 pane--cols"  >
  
      
  
  <div class="pane-content">
    



    <div class="views-row views-row-1 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2963"
        data-attr-title="push_banner_-_decrochez_la_coupe__5_000__en_jeu"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-DLC.png?time=1577697677" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Du 10 au 13 février, faites 15 € de paris sur les quarts de finale de Coupe de France</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-2 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2900"
        data-attr-title="push_banner_-_direction_le_titre__10__offerts"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-LCAT_2.png?time=1576236018" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Du 13 au 17 février, 1 pari Ligue 1 Conforama®  + 1 pari Domino’s</strong><strong>® Ligue 2 = 10 € offerts</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-3 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/4#pmu-promotion-2416"
        data-attr-title="push_banner_-_combimax"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380%20-%20CombiMax.png?time=1556274759" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Avec CombiMax, pariez en combiné et remportez un bonus CASH en plus de vos gains !</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-4 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/reseaux-sociaux"
        data-attr-title="push_banner_-_reseaux_sociaux_2019"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496%20x%20380_r%C3%A9seaux%20sociaux_0.png?time=1556555374" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Suivez-nous sur les Réseaux Sociaux</strong>. Chaque semaine des cadeaux à gagner !</p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-5 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/4#pmu-promotion-1356"
        data-attr-title="push_banner_-_appli_mobile_sport"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380%20-%20AppMob.png?time=1556209187" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Pariez où et quand vous voulez grâce à notre appli mobile !</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-6 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2091"
        data-attr-title="push_banner_-_parrainage__jusqua_50_offerts_"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-bis.png?time=1562151518" width="496" height="380" alt="" />                    <figcaption>
                          <p>Parrainez jusqu’à 5 amis et profitez d’un bonus de 50€ + 5€ de bonus !</p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>






  </div>

  
  </div>
        </div>
                                          </div>
</div>
  </div>
</div>

</div>
  </div>

</section> <!-- /.block -->
  </div>
</section>

<div id="sidebar-left" class="hidden-lg" data-responsive-below="1200">
  <section>
    <header class="sb-l-header">
      <a href="#" class="sb-header--burger overlay-trigger" data-target-name="#sidebar-left" data-action="close">
        <span class="glyphicon glyphicon-menu-hamburger"></span>
      </a>
              <a href="/" class="sb-header--logo">
          <img class="logo-pmu" src="https://paris-sportifs.pmu.fr/profiles/core/themes/pmu_theme/logo.png" alt="Domicile">
        </a>
            <a href="#" class="sb-header--close overlay-trigger" data-target-name="#sidebar-left" data-action="close">
        <span class="glyphicon glyphicon-pmu-close"></span>
      </a>
    </header>
      <div class="region region-tablet-menubar">
    <section id="block-obet-search-search-form-compact" class="block block-obet-search clearfix mb-20">
      
  <div class="block-content mb-20">
    
<div class="sb-l-wrap">
    <div class="sb-search">
        <form class="main-search--form" action="https://paris-sportifs.pmu.fr/recherche" method="get" id="obet-search-form-compact-callback--2" accept-charset="UTF-8"><div><label class="glyphicon glyphicon-pmu-magnifiying main-search--trigger"></label><div class="form-item form-item-token form-type-textfield form-group"><input placeholder="Trouver un pari ..." class="tokenInput form-control form-text" type="text" id="edit-token--2" name="token" value="" size="60" maxlength="128" /></div><a role="button" class="glyphicon glyphicon-pmu-close main-search--close"></a></div></form>    </div>
</div>
  </div>

</section> <!-- /.block -->
<section id="block-menu-quick-links" class="block block-menu clearfix mb-20">
        <div class="row">
      <div class="col-sm-12">
        <div class="sb-l-wrap">
          <h4 class="sb-l-title">ACCÈS DIRECTS</h4>
        </div>
      </div>
    </div>
    
  <div class="block-content mb-20">
    <div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/en-direct" class="quick-links-en-direct sb-list-item"><figure class="sb-list-item--live-icon"><img src="https://paris-sportifs.pmu.fr/sites/default/files/anim-live-black-orange.gif" alt="En Direct" /></figure><em class="sb-list-item--label"><em class="sb-list-item--label"><strong class="sb-list-item--counter">17</strong> En Direct</em></em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/promotions/all" class="quick-links-promotions sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-price-tag-black glyphicon-orange"></span></span><em class="sb-list-item--label">Promotions</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2900" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-gift glyphicon-green "></span></span><em class="sb-list-item--label">10 € offerts sur le Foot Français</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2963" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-gift glyphicon-green "></span></span><em class="sb-list-item--label">5 000€ sur la Coupe de France</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/663625" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.epinal__st_etienne" data-sport_id="football" data-compet_id="coupe_de_france" data-event_id="epinal__st_etienne"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Epinal // St-Etienne</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/662844" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.ac_milan__juventus" data-sport_id="football" data-compet_id="coupe_ditalie" data-event_id="ac_milan__juventus"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">AC Milan // Juventus</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/event/665753" class="sb-list-item tc-track-element-events" data-name="sportif.clic.acces_direct.sociedad__mirandes" data-sport_id="football" data-compet_id="coupe_du_roi" data-event_id="sociedad__mirandes"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Sociedad // Mirandés</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/pari/competition/169/football/ligue-1-conforama" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Ligue 1 Conforama</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/170/football/dominos-%C2%AE-ligue-2" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-black glyphicon-dark-blue "></span></span><em class="sb-list-item--label">Domino's Ligue 2</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/sport/9/tennis" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-tennis glyphicon-light-yellow"></span></span><em class="sb-list-item--label">ATP / WTA</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/3502/basket-us/nba-matchs" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball glyphicon-dark-red"></span></span><em class="sb-list-item--label">NBA</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="/pari/competition/1366/rugby/top-14" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby glyphicon-dark-green "></span></span><em class="sb-list-item--label">TOP 14</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-direct sb-l-wrap shadow"><a href="https://paris-sportifs.pmu.fr/reseaux-sociaux" class="sb-list-item"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-thumb-up glyphicon-cyan"></span></span><em class="sb-list-item--label">Réseaux Sociaux</em></a></div></div></div>
  </div>

</section> <!-- /.block -->
<section id="block-menu-quick-betting-links" class="block block-menu clearfix mb-20">
        <div class="row">
      <div class="col-sm-12">
        <div class="sb-l-wrap">
          <h4 class="sb-l-title">PARIER AUTREMENT</h4>
        </div>
      </div>
    </div>
    
  <div class="block-content mb-20">
    <div class="row"><div class="col-sm-12"><a href="/cash-out" class="paris-rapides-cashout sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-cash-out glyphicon-orange"></span></span><em class="sb-list-item--label">Cash Out<span class="sb-list-item--details"><p>Soyez maître de vos paris</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/combimax" class="paris-rapides-multibonus sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bomb glyphicon-orange"></span></span><em class="sb-list-item--label">CombiMax<span class="sb-list-item--details"><p>Plus votre grille est ambitieuse, plus le bonus s'envole !</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/1n2-jackpot" class="paris-rapides-jackpot sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon pmu-custom-glyphicon-jackpot  glyphicon-orange"></span></span><em class="sb-list-item--label">1N2 Jackpot<span class="sb-list-item--details"><p>Multipliez jusqu'à 100x votre gain</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/fantasy-league" class="paris-rapides-fantasy-league sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-fantasy-league  glyphicon-orange"></span></span><em class="sb-list-item--label">Fantasy League<span class="sb-list-item--details"><p>Entrez dans la peau d'un manager</p>
</span></em></a></div></div>
<div class="row"><div class="col-sm-12"><a href="/bet-machine" class="paris-rapides-bet-machine sb-list-item-multiline shadow"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-draggable glyphicon-orange"></span></span><em class="sb-list-item--label">Bet Machine<span class="sb-list-item--details">Décider ce que vous pourriez gagner</span></em></a></div></div>
  </div>

</section> <!-- /.block -->
<section id="block-menu-sports-menu" class="block block-menu clearfix mb-20">
        <div class="row">
      <div class="col-sm-12">
        <div class="sb-l-wrap">
          <h4 class="sb-l-title">TOUS LES SPORTS</h4>
        </div>
      </div>
    </div>
    
  <div class="block-content mb-20">
    <ul class="menu nav"><li class="first collapsed row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/25/football" data-hierarchy-level-events-counter="550" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="football"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football "></span></span><em class="sb-list-item--label">Football</em><strong class="sb-list-item--counter_pmu">550</strong></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/9/tennis" data-hierarchy-level-events-counter="38" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tennis"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-tennis "></span></span><em class="sb-list-item--label">Tennis</em><strong class="sb-list-item--counter_pmu">38</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/7755/tennis/wta-saint-p%C3%A9tersbourg" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wta_saint-petersbourg">WTA Saint-Pétersbourg</a></li>
<li class="leaf"><a href="/pari/competition/447/tennis/atp-rotterdam" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_rotterdam">ATP Rotterdam</a></li>
<li class="leaf"><a href="/pari/competition/8796/tennis/atp-new-york" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_new_york">ATP New York</a></li>
<li class="leaf"><a href="/pari/competition/7024/tennis/atp-buenos-aires" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="atp_buenos_aires">ATP Buenos Aires</a></li>
<li class="leaf"><a href="/pari/competition/441/tennis/open-daustralie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="open_daustralie_h">Open d'Australie (H)</a></li>
<li class="leaf"><a href="/pari/competition/440/tennis/open-daustralie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="open_daustralie_f">Open d'Australie (F)</a></li>
<li class="leaf"><a href="/pari/competition/759/tennis/roland-garros-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="roland_garros_h">Roland Garros (H)</a></li>
<li class="leaf"><a href="/pari/competition/400/tennis/roland-garros-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="roland_garros_f">Roland Garros (F)</a></li>
<li class="leaf"><a href="/pari/competition/744/tennis/wimbledon-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wimbledon_h">Wimbledon (H)</a></li>
<li class="leaf"><a href="/pari/competition/745/tennis/wimbledon-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wimbledon_f">Wimbledon (F)</a></li>
<li class="leaf"><a href="/pari/competition/785/tennis/jo" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="jo">JO</a></li>
<li class="leaf"><a href="/pari/competition/673/tennis/us-open-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="us_open_h">US Open (H)</a></li>
<li class="leaf"><a href="/pari/competition/416/tennis/us-open-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="us_open_f">US Open (F)</a></li>
<li class="leaf"><a href="/pari/competition/666/tennis/paris-sur-les-joueurs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="paris_sur_les_joueurs">Paris sur les joueurs</a></li>
<li class="leaf"><a href="/pari/competition/7590/tennis/wta-hua-hin" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="tennis" data-compet_id="wta_hua_hin">WTA Hua Hin</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/59/basket-euro" data-hierarchy-level-events-counter="36" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="basketball_euro"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball "></span></span><em class="sb-list-item--label">Basketball Euro</em><strong class="sb-list-item--counter_pmu">36</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1415/basket-euro/france-pro" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="france_-_pro_a">France - Pro A</a></li>
<li class="leaf"><a href="/pari/competition/2189/basket-euro/france-pro-b" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="france_-_pro_b">France - Pro B</a></li>
<li class="leaf"><a href="/pari/competition/1402/basket-euro/euroligue-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="euroligue_h">Euroligue (H)</a></li>
<li class="leaf"><a href="/pari/competition/1417/basket-euro/allemagne-bundesliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="allemagne_-_bundesliga">Allemagne - Bundesliga</a></li>
<li class="leaf"><a href="/pari/competition/5021/basket-euro/australie-nbl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="australie_-_nbl">Australie - NBL</a></li>
<li class="leaf"><a href="/pari/competition/1425/basket-euro/espagne-ligue-acb" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="espagne_-_ligue_acb">Espagne - Ligue ACB</a></li>
<li class="leaf"><a href="/pari/competition/1493/basket-euro/espagne-ligue-leb-oro" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="espagne_-_ligue_leb_oro">Espagne - Ligue LEB Oro</a></li>
<li class="leaf"><a href="/pari/competition/1423/basket-euro/italie-s%C3%A9rie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="italie_-_serie_a">Italie - Série A</a></li>
<li class="leaf"><a href="/pari/competition/4495/basket-euro/leaders-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="leaders_cup">Leaders Cup</a></li>
<li class="leaf"><a href="/pari/competition/1422/basket-euro/coupe-ditalie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="coupe_ditalie">Coupe d'Italie</a></li>
<li class="leaf"><a href="/pari/competition/1426/basket-euro/coupe-du-roi" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="coupe_du_roi">Coupe du Roi</a></li>
<li class="leaf"><a href="/pari/competition/1491/basket-euro/ligue-aba" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="ligue_aba">Ligue ABA</a></li>
<li class="leaf"><a href="/pari/competition/8630/basket-euro/belgique-1%C3%A8re-division" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_euro" data-compet_id="belgique_-_1ere_division">Belgique - 1ère division</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/12/basket-us" data-hierarchy-level-events-counter="81" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="basketball_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-basketball "></span></span><em class="sb-list-item--label">Basketball US</em><strong class="sb-list-item--counter_pmu">81</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/3502/basket-us/nba-matchs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_matchs">NBA - Matchs</a></li>
<li class="leaf"><a href="/pari/competition/1395/basket-us/nba-vainqueur" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_vainqueur">NBA - Vainqueur</a></li>
<li class="leaf"><a href="/pari/competition/1393/basket-us/nba-conf-est" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_conf._est">NBA - Conf. Est</a></li>
<li class="leaf"><a href="/pari/competition/1394/basket-us/nba-conf-ouest" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_conf._ouest">NBA - Conf. Ouest</a></li>
<li class="leaf"><a href="/pari/competition/7393/basket-us/nba-divisions" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="nba_-_divisions">NBA - Divisions</a></li>
<li class="leaf"><a href="/pari/competition/9969/basket-us/ncaa-matchs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_matchs">NCAA - Matchs</a></li>
<li class="leaf"><a href="/pari/competition/1392/basket-us/ncaa-divers" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_divers">NCAA - Divers</a></li>
<li class="leaf"><a href="/pari/competition/9138/basket-us/ncaa-vainqueur" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="basketball_us" data-compet_id="ncaa_-_vainqueur">NCAA - Vainqueur</a></li>
</ul></div></div></div></li>
<li class="expanded active-trail active row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/8/rugby" data-hierarchy-level-events-counter="81" data-target="#" class="sb-list-item-small has-children 0 active tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="rugby"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby "></span></span><em class="sb-list-item--label">Rugby</em><strong class="sb-list-item--counter_pmu">81</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1380/rugby/tournoi-des-6-nations" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="tournoi_des_6_nations">Tournoi des 6 Nations</a></li>
<li class="leaf active-trail active"><a href="/pari/competition/1366/rugby/top-14" class="sb-sublist-item 0 link-grey-dark active tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="top_14">TOP 14</a></li>
<li class="leaf"><a href="/pari/competition/1450/rugby/pro-d2" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="pro_d2">PRO D2</a></li>
<li class="leaf"><a href="/pari/competition/1375/rugby/champions-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="champions_cup">Champions Cup</a></li>
<li class="leaf"><a href="/pari/competition/1378/rugby/challenge-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="challenge_cup">Challenge Cup</a></li>
<li class="leaf"><a href="/pari/competition/9064/rugby/gallagher-premiership" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="gallagher_premiership">Gallagher Premiership</a></li>
<li class="leaf"><a href="/pari/competition/7324/rugby/super-rugby" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="super_rugby">Super Rugby</a></li>
<li class="leaf"><a href="/pari/competition/7575/rugby/world-rugby-sevens-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="world_rugby_sevens_series">World Rugby Sevens Series</a></li>
<li class="leaf"><a href="/pari/competition/8504/rugby/pro-14" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="pro_14">Pro 14</a></li>
<li class="leaf"><a href="/pari/competition/9992/rugby/coupe-du-monde-2023" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="coupe_du_monde_2023">Coupe du Monde 2023</a></li>
<li class="leaf"><a href="/pari/competition/2475/rugby/tournoi-6-nations-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby" data-compet_id="tournoi_6_nations_f">Tournoi 6 Nations (F)</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/45/aviron" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="aviron"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rowing "></span></span><em class="sb-list-item--label">Aviron</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/217/bobsleigh" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="bobsleigh"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bobsleigh "></span></span><em class="sb-list-item--label">Bobsleigh</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/213/luge" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="luge"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-skeleton "></span></span><em class="sb-list-item--label">Luge</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/114/jo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="medailles_jo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-medale "></span></span><em class="sb-list-item--label">Médailles JO</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/215/patinage-de-vitesse" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="patinage_de_vitesse"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-ice-skating "></span></span><em class="sb-list-item--label">Patinage de Vitesse</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/220/patinage-de-vitesse-sur-piste-courte" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="short_track"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-ice-skating "></span></span><em class="sb-list-item--label">Short Track</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/214/skeleton" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="skeleton"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-skeleton "></span></span><em class="sb-list-item--label">Skeleton</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/218/freestyle" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_freestyle"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-alpine-skiing "></span></span><em class="sb-list-item--label">Ski Freestyle</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/219/snowboard" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="snowboard"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snowboard "></span></span><em class="sb-list-item--label">Snowboard</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/15/athl%C3%A9tisme" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="athletisme"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-athletism "></span></span><em class="sb-list-item--label">Athlétisme</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/62/badminton" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="badminton"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-badminton "></span></span><em class="sb-list-item--label">Badminton</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/14/baseball" data-hierarchy-level-events-counter="3" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="baseball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-baseball "></span></span><em class="sb-list-item--label">Baseball</em><strong class="sb-list-item--counter_pmu">3</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1436/baseball/world-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="world_series">World Series</a></li>
<li class="leaf"><a href="/pari/competition/1458/baseball/american-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="american_league">American League</a></li>
<li class="leaf"><a href="/pari/competition/1459/baseball/national-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="baseball" data-compet_id="national_league">National League</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/151/beach-volley" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="beach_volley"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-beach-volley "></span></span><em class="sb-list-item--label">Beach Volley</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/84/biathlon" data-hierarchy-level-events-counter="1" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="biathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-biathlon "></span></span><em class="sb-list-item--label">Biathlon</em><strong class="sb-list-item--counter_pmu">1</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2128/biathlon/antholz-anterselva" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="biathlon" data-compet_id="antholz-anterselva">Antholz-Anterselva</a></li>
</ul></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/166/" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="billard_americain"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snooker "></span></span><em class="sb-list-item--label">Billard américain</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/11/boxe" data-hierarchy-level-events-counter="4" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="boxe"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-boxe "></span></span><em class="sb-list-item--label">Boxe</em><strong class="sb-list-item--counter_pmu">4</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/994/boxe/combats-de-boxe-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="boxe" data-compet_id="combats_de_boxe_-_monde">Combats de boxe - Monde</a></li>
</ul></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/184/cano%C3%AB-kayak" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="canoe-kayak"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-kayak "></span></span><em class="sb-list-item--label">Canoë-Kayak</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/144/curling" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="curling"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-curling "></span></span><em class="sb-list-item--label">Curling</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/36/cyclisme" data-hierarchy-level-events-counter="4" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="cyclisme"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-road-cycling "></span></span><em class="sb-list-item--label">Cyclisme</em><strong class="sb-list-item--counter_pmu">4</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1024/cyclisme/tour-de-france" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_de_france">Tour de France</a></li>
<li class="leaf"><a href="/pari/competition/1032/cyclisme/paris-roubaix" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="paris_-_roubaix">Paris - Roubaix</a></li>
<li class="leaf"><a href="/pari/competition/1027/cyclisme/tour-ditalie" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_ditalie">Tour d'Italie</a></li>
<li class="leaf"><a href="/pari/competition/1035/cyclisme/tour-des-flandres" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="cyclisme" data-compet_id="tour_des_flandres">Tour des Flandres</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/152/escrime" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="escrime"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-fencing "></span></span><em class="sb-list-item--label">Escrime</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/164/football-am%C3%A9ricain" data-hierarchy-level-events-counter="3" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="football_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-football-us "></span></span><em class="sb-list-item--label">Football US</em><strong class="sb-list-item--counter_pmu">3</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1956/football-am%C3%A9ricain/nfl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="football_us" data-compet_id="nfl">NFL</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/4/golf" data-hierarchy-level-events-counter="9" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="golf"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-golf "></span></span><em class="sb-list-item--label">Golf</em><strong class="sb-list-item--counter_pmu">9</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1336/golf/us-masters" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="us_masters">US Masters</a></li>
<li class="leaf"><a href="/pari/competition/1324/golf/ryder-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="ryder_cup">Ryder Cup</a></li>
<li class="leaf"><a href="/pari/competition/1277/golf/open-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="open_championship">Open Championship</a></li>
<li class="leaf"><a href="/pari/competition/1343/golf/uspga-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="uspga_championship">USPGA Championship</a></li>
<li class="leaf"><a href="/pari/competition/1323/golf/players-championship" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="the_players_championship">The Players Championship</a></li>
<li class="leaf"><a href="/pari/competition/1274/golf/genesis-open" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="genesis_open">Genesis Open</a></li>
<li class="leaf"><a href="/pari/competition/1265/golf/open-daustralie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="open_daustralie_f">Open d'Australie (F)</a></li>
<li class="leaf"><a href="/pari/competition/7657/golf/jo-h-2020" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="jo_h_2020">JO (H) 2020</a></li>
<li class="leaf"><a href="/pari/competition/1339/golf/us-open" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="golf" data-compet_id="us_open">US Open</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/197/halt%C3%A9rophilie" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="halterophilie"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-weightlifting "></span></span><em class="sb-list-item--label">Haltérophilie </em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/54/handball" data-hierarchy-level-events-counter="20" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="handball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-handball "></span></span><em class="sb-list-item--label">Handball</em><strong class="sb-list-item--counter_pmu">20</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1092/handball/ligue-des-champions-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="ligue_des_champions_h">Ligue des Champions (H)</a></li>
<li class="leaf"><a href="/pari/competition/1089/handball/bundesliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="bundesliga">Bundesliga</a></li>
<li class="leaf"><a href="/pari/competition/1088/handball/espagne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="espagne_h">Espagne (H)</a></li>
<li class="leaf"><a href="/pari/competition/3976/handball/coupe-ehf-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="handball" data-compet_id="coupe_ehf_h.">Coupe EHF (H).</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/160/hockey-sur-glace-eu" data-hierarchy-level-events-counter="66" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_euro"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey Euro</em><strong class="sb-list-item--counter_pmu">66</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1881/hockey-sur-glace-eu/ligue-magnus" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="ligue_magnus">Ligue Magnus</a></li>
<li class="leaf"><a href="/pari/competition/4258/hockey-sur-glace-eu/russie-khl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="russie_-_khl">Russie - KHL</a></li>
<li class="leaf"><a href="/pari/competition/1887/hockey-sur-glace-eu/allemagne-del" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="allemagne_-_del">Allemagne - DEL</a></li>
<li class="leaf"><a href="/pari/competition/1883/hockey-sur-glace-eu/autriche-ehl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="autriche_-_ehl">Autriche - EHL</a></li>
<li class="leaf"><a href="/pari/competition/1884/hockey-sur-glace-eu/finlande-sm-liiga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="finlande_-_sm-liiga">Finlande - SM-Liiga</a></li>
<li class="leaf"><a href="/pari/competition/7272/hockey-sur-glace-eu/norv%C3%A8ge-get-ligaen" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="norvege_get_ligaen">Norvège Get Ligaen</a></li>
<li class="leaf"><a href="/pari/competition/1888/hockey-sur-glace-eu/r%C3%A9p-tch%C3%A8que-extraliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="rep._tcheque_-_extraliga">Rép. Tchèque - Extraliga</a></li>
<li class="leaf"><a href="/pari/competition/7376/hockey-sur-glace-eu/slovaquie-extraliga" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="slovaquie_-_extraliga">Slovaquie - Extraliga</a></li>
<li class="leaf"><a href="/pari/competition/1885/hockey-sur-glace-eu/su%C3%A8de-shl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="suede_-_shl">Suède - SHL</a></li>
<li class="leaf"><a href="/pari/competition/7377/hockey-sur-glace-eu/suisse-nla" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="suisse_-_nla">Suisse - NLA</a></li>
<li class="leaf"><a href="/pari/competition/2420/hockey-sur-glace-eu/championnats-du-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_euro" data-compet_id="championnats_du_monde">Championnats du Monde</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/161/hockey-sur-glace-us" data-hierarchy-level-events-counter="14" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_us"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey US</em><strong class="sb-list-item--counter_pmu">14</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1970/hockey-sur-glace-us/nhl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="nhl">NHL</a></li>
<li class="leaf"><a href="/pari/competition/1927/hockey-sur-glace-us/stanley-cup" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="stanley_cup">Stanley Cup</a></li>
<li class="leaf"><a href="/pari/competition/1973/hockey-sur-glace-us/conf%C3%A9rence-est" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="conference_est.">Conférence Est.</a></li>
<li class="leaf"><a href="/pari/competition/1972/hockey-sur-glace-us/conf%C3%A9rence-ouest" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="hockey_us" data-compet_id="conference_ouest">Conférence Ouest</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/195/hockey-sur-gazon" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="hockey_sur_gazon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-hockey "></span></span><em class="sb-list-item--label">Hockey sur gazon</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/203/judo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="judo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-judo "></span></span><em class="sb-list-item--label">Judo</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/192/lutte" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="lutte"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-judo "></span></span><em class="sb-list-item--label">Lutte</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/72/natation" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="natation"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-swimming "></span></span><em class="sb-list-item--label">Natation</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/246/petanque" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="petanque"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-petanque "></span></span><em class="sb-list-item--label">Pétanque</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/187/pentathlon-moderne" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="pentathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-horse-riding "></span></span><em class="sb-list-item--label">Pentathlon</em></a></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/100/rugby-%C3%A0-xiii" data-hierarchy-level-events-counter="19" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="rugby_a_xiii"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-rugby "></span></span><em class="sb-list-item--label">Rugby à XIII</em><strong class="sb-list-item--counter_pmu">19</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2327/rugby-%C3%A0-xiii/nrl" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby_a_xiii" data-compet_id="nrl">NRL</a></li>
<li class="leaf"><a href="/pari/competition/2328/rugby-%C3%A0-xiii/super-league" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="rugby_a_xiii" data-compet_id="super_league">Super League</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/82/ski-alpin" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_alpin"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-cross-country-skiing "></span></span><em class="sb-list-item--label">Ski Alpin</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/146/ski-de-fond" data-hierarchy-level-events-counter="2" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="ski_de_fond"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-alpine-skiing "></span></span><em class="sb-list-item--label">Ski de Fond</em><strong class="sb-list-item--counter_pmu">2</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/7016/ski-de-fond/ostersund" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="ski_de_fond" data-compet_id="ostersund">Ostersund</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/159/snooker" data-hierarchy-level-events-counter="5" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="snooker"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-snooker "></span></span><em class="sb-list-item--label">Snooker</em><strong class="sb-list-item--counter_pmu">5</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/2422/snooker/open-du-pays-de-galles" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="snooker" data-compet_id="open_du_pays_de_galles">Open du Pays de Galles</a></li>
<li class="leaf"><a href="/pari/competition/3873/snooker/championnats-du-monde" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="snooker" data-compet_id="championnats_du_monde">Championnats du Monde</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/5/sports-m%C3%A9caniques" data-hierarchy-level-events-counter="7" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="sports_mecaniques"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-auto-moto "></span></span><em class="sb-list-item--label">Sports mécaniques</em><strong class="sb-list-item--counter_pmu">7</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/8953/sports-m%C3%A9caniques/f1-championnat-des-pilotes" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="f1_championnat_des_pilotes">F1 Championnat des pilotes</a></li>
<li class="leaf"><a href="/pari/competition/9446/sports-m%C3%A9caniques/f1-championnat-des-constructeurs" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="f1_championnat_des_constructeurs">F1 Championnat des constructeurs</a></li>
<li class="leaf"><a href="/pari/competition/9486/sports-m%C3%A9caniques/nascar-daytona-500" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar_-_daytona_500">NASCAR - Daytona 500</a></li>
<li class="leaf"><a href="/pari/competition/1645/sports-m%C3%A9caniques/rallye-wrc-de-su%C3%A8de" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="rallye_wrc_de_suede">Rallye WRC de Suède</a></li>
<li class="leaf"><a href="/pari/competition/8347/sports-m%C3%A9caniques/nascar-cup-series" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar_cup_series">NASCAR Cup Series</a></li>
<li class="leaf"><a href="/pari/competition/1002/sports-m%C3%A9caniques/championnats-du-monde-des-rallyes-wrc" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="championnats_du_monde_des_rallyes_wrc">Championnats du Monde des Rallyes (WRC)</a></li>
<li class="leaf"><a href="/pari/competition/1581/sports-m%C3%A9caniques/nascar" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="sports_mecaniques" data-compet_id="nascar">Nascar</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/155/taekwondo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="taekwondo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-taekwondo "></span></span><em class="sb-list-item--label">Taekwondo</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/77/tennis-de-table" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tennis_de_table"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-table-tennis "></span></span><em class="sb-list-item--label">Tennis de Table</em></a></div></div></div></li>
<li class="leaf hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/183/tir-%C3%A0-larc" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="tir_a_larc"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-archery "></span></span><em class="sb-list-item--label">Tir à l'Arc</em></a></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/190/triathlon" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="triathlon"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-road-cycling "></span></span><em class="sb-list-item--label">Triathlon</em></a></div></div></div></li>
<li class="leaf expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/124/voile" data-hierarchy-level-events-counter="1" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="voile"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-sailing "></span></span><em class="sb-list-item--label">Voile</em><strong class="sb-list-item--counter_pmu">1</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/4932/voile/coupe-de-lam%C3%A9rica" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="voile" data-compet_id="coupe_de_lamerica">Coupe de l'América</a></li>
</ul></div></div></div></li>
<li class="expanded row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/57/volley-ball" data-hierarchy-level-events-counter="23" data-target="#" class="sb-list-item-small has-children tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="volley-ball"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-volley-ball "></span></span><em class="sb-list-item--label">Volley-Ball</em><strong class="sb-list-item--counter_pmu">23</strong></a><ul class="sb-sport--events--wrapper"><li class="leaf"><a href="/pari/competition/1081/volley-ball/ligue-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_a_h">Ligue A (H)</a></li>
<li class="leaf"><a href="/pari/competition/2278/volley-ball/ligue-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_a_f">Ligue A (F)</a></li>
<li class="leaf"><a href="/pari/competition/1076/volley-ball/ligue-des-champions-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="ligue_des_champions_h">Ligue des Champions (H)</a></li>
<li class="leaf"><a href="/pari/competition/1084/volley-ball/allemagne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="allemagne_h">Allemagne (H)</a></li>
<li class="leaf"><a href="/pari/competition/8637/volley-ball/belgique-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="belgique._h">Belgique. (H)</a></li>
<li class="leaf"><a href="/pari/competition/8639/volley-ball/italie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="italie_h">Italie (H)</a></li>
<li class="leaf"><a href="/pari/competition/2235/volley-ball/italie-s%C3%A9rie-a1-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="italie_-_serie_a1_f">Italie - Série A1 (F)</a></li>
<li class="leaf"><a href="/pari/competition/2399/volley-ball/pologne-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="pologne_h">Pologne (H)</a></li>
<li class="leaf"><a href="/pari/competition/2230/volley-ball/russie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="russie_h">Russie (H)</a></li>
<li class="leaf"><a href="/pari/competition/5074/volley-ball/russie-f" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="russie_f">Russie (F)</a></li>
<li class="leaf"><a href="/pari/competition/1500/volley-ball/turquie-h" class="sb-sublist-item link-grey-dark tc-track-element-events" data-name="sportif.clic.tous_sports.competition" data-sport_id="volley-ball" data-compet_id="turquie_h">Turquie (H)</a></li>
</ul></div></div></div></li>
<li class="leaf element-hidden hidden hide row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="/pari/sport/168/water-polo" data-hierarchy-level-events-counter="0" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="water-polo"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-waterpolo "></span></span><em class="sb-list-item--label">Water-polo</em></a></div></div></div></li>
<li class="leaf row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="https://www.pmu.fr/turf/" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="turf"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-horse-riding "></span></span><em class="sb-list-item--label">Turf</em></a></div></div></div></li>
<li class="last leaf row"><div class="col-sm-12"><div class="sb-sport shadow" role="tablist"><div class="sb-sport--item"><a href="https://poker.pmu.fr/" class="sb-list-item-small tc-track-element-events" data-name="sportif.clic.tous_sports.sport" data-sport_id="poker"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-star "></span></span><em class="sb-list-item--label">Poker</em></a></div></div></div></li>
</ul>  </div>

</section> <!-- /.block -->
<section id="block-menu-services" class="block block-menu clearfix mb-20">
        <div class="row">
      <div class="col-sm-12">
        <div class="sb-l-wrap">
          <h4 class="sb-l-title">PMU Services</h4>
        </div>
      </div>
    </div>
    
  <div class="block-content mb-20">
    <div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="javascript:void(0);" class="pmu-services-statistiques sb-list-item-small" onclick="javascript:popWin = window.open(&quot;https://s5.sir.sportradar.com/pmu/fr&quot;, &quot;Statistiques&quot;, &quot;left=10, top=10, width=1000, height=730, scrollbars=1, titlebar=0, status=0, toolbar=0, menubar=0, location=0&quot;); popWin.focus();"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-bar-chart "></span></span><em class="sb-list-item--label">Statistiques</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/aide/regles-paris" class="pmu-services-regles-paris sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-note "></span></span><em class="sb-list-item--label">Règles des paris</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/info/calendrier" class="pmu-services-calendar sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-calendar "></span></span><em class="sb-list-item--label">Calendrier</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/results" class="pmu-services-resultats sb-list-item-small"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-goal "></span></span><em class="sb-list-item--label">Résultats</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="https://communaute-forum.pmu.fr/categories/3395-sport" class="pmu-services-aide sb-list-item-small" target="_blank"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-help "></span></span><em class="sb-list-item--label">Aide - Communauté</em></a></div></div></div>
<div class="row"><div class="col-sm-12"><div class="sb-service shadow"><a href="/pservices/simulator" class="overlay-trigger pmu-services-simulateur sb-list-item-small" data-target-name=".popin" data-action="open"><span class="circled-icon"><span class="glyphicon glyphicon-pmu-calc "></span></span><em class="sb-list-item--label">Simulateur</em></a></div></div></div>
  </div>

</section> <!-- /.block -->
  </div>
  </section>
</div>

<div class="sb-wrapper-tablet hidden-lg hidden-md">
  <div class="sb-title" role="button" data-toggle="collapse" data-target="#sb-push-live-push-banners-bottom" aria-expanded="true"
       aria-controls="sb-push-live-push-banners-bottom">
    En ce moment
    <span class="glyphicon glyphicon-chevron-up invisible"></span>
  </div>

  <div class="collapse in" id="sb-push-live-push-banners-bottom">
              



    <div class="views-row views-row-1 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2963"
        data-attr-title="push_banner_-_decrochez_la_coupe__5_000__en_jeu"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-DLC.png?time=1577697677" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Du 10 au 13 février, faites 15 € de paris sur les quarts de finale de Coupe de France</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-2 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2900"
        data-attr-title="push_banner_-_direction_le_titre__10__offerts"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-LCAT_2.png?time=1576236018" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Du 13 au 17 février, 1 pari Ligue 1 Conforama®  + 1 pari Domino’s</strong><strong>® Ligue 2 = 10 € offerts</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-3 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/4#pmu-promotion-2416"
        data-attr-title="push_banner_-_combimax"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380%20-%20CombiMax.png?time=1556274759" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Avec CombiMax, pariez en combiné et remportez un bonus CASH en plus de vos gains !</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-4 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/reseaux-sociaux"
        data-attr-title="push_banner_-_reseaux_sociaux_2019"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496%20x%20380_r%C3%A9seaux%20sociaux_0.png?time=1556555374" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Suivez-nous sur les Réseaux Sociaux</strong>. Chaque semaine des cadeaux à gagner !</p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-5 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/4#pmu-promotion-1356"
        data-attr-title="push_banner_-_appli_mobile_sport"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380%20-%20AppMob.png?time=1556209187" width="496" height="380" alt="" />                    <figcaption>
                          <p><strong>Pariez où et quand vous voulez grâce à notre appli mobile !</strong></p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>
  <div class="views-row views-row-6 row">
    
<div class="col-sm-12">
  <div  class="pmu-ds-push-banner sb-push shadow node node-push-banners node-teaser view-mode-teaser">
    
          <a href="https://paris-sportifs.pmu.fr/promotions/3#pmu-promotion-2091"
        data-attr-title="push_banner_-_parrainage__jusqua_50_offerts_"         class="pmu-ds-banner-link push-link ">

        <figure class="push-image">
                      <img class="img-responsive" src="https://paris-sportifs.pmu.fr/sites/default/files/push_banners/2019/496x380-bis.png?time=1562151518" width="496" height="380" alt="" />                    <figcaption>
                          <p>Parrainez jusqu’à 5 amis et profitez d’un bonus de 50€ + 5€ de bonus !</p>
                      </figcaption>
        </figure>

      </a>
    
  </div>


    </div>
  </div>






      </div>
</div>

<!-- Footer -->
<div class="footer-wrapper clearfix">
    <div class="region region-footer">
    <footer id="footer-primary" class="container clearfix">

              <div class="footer--title">
        <h4>Nous Contacter</h4>
      </div>
        
  <div class="block-content">
    <ul class="footer--list clearfix"><li class="first leaf footer-nous-contacter-aide"><a href="https://communaute-aide.pmu.fr/"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_aideetcommunaute_v4.png" alt="AIDE et Communauté PMU" /></a></li>
<li class="leaf footer-nous-contacter-tel"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_telephone_v4.png" alt="TÉLÉPHONE 09 77 40 39 71" /></li>
<li class="leaf footer-nous-contacter-courrier"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_courrier_v0.png" alt="COURRIER" /></li>
<li class="leaf footer-nous-contacter-email"><a href="https://info.pmu.fr/contact"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_Email_v0.png" alt="E-MAIL" /></a></li>
<li class="leaf footer-nous-contacter-live-chat"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_LiveChat_v1.png" alt="LIVE CHAT" /></li>
<li class="last leaf footer-nous-contacter-sourd"><a href="https://pmu.elioz.fr/index.php?hash=d10a37700d9fb6a22bf8cc92c56af77a"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/pmu_SourdetMalentendant_v0.png" alt="SOURDS ET MALENTENDANTS" /></a></li>
</ul>  </div>

</footer> <!-- /.block -->
<footer id="footer-secondary-social" class="container clearfix">

      
  <div class="block-content">
    <ul class="footer-secondary--row-1"><li class="first leaf"><a href="https://www.facebook.com/PMU.Sport/" title="Facebook" target="_blank"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/facebook-40x40.png" alt="Facebook" /></a></li>
<li class="leaf"><a href="https://twitter.com/PMU_Sport" title="Twitter" target="_blank"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/twitter-40x40.png" alt="Twitter" /></a></li>
<li class="last leaf"><a href="https://www.instagram.com/pmu_sport/?hl=fr" title="Instagram" target="_blank"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/instagram-40x40.png" alt="Instagram" /></a></li>
</ul>  </div>

</footer> <!-- /.block -->
<footer id="footer-secondary-nav" class="container clearfix">

      
  <div class="block-content">
    <ul class="footer-secondary--row-2"><li class="first leaf"><a href="https://www.pmu.fr/" target="_blank">Accueil PMU.FR</a></li>
<li class="leaf"><a href="https://www.pmu.fr/ouverture-compte/programme-affiliation-pmu/" target="_blank">Affiliation</a></li>
<li class="leaf footer-entreprise"><a href="http://entreprise.pmu.fr/" target="_blank">L'entreprise</a></li>
<li class="leaf footer-carrieres"><a href="http://pmu-recrute.talent-soft.com/accueil.aspx" target="_blank">Carrières</a></li>
<li class="leaf"><a href="http://www.arjel.fr/-Bonnes-pratiques-.html" target="_blank">Bonnes Pratiques</a></li>
<li class="leaf footer-infos-legales"><a href="https://www.pmu.fr/turf/informations-legales" target="_blank">Infos légales</a></li>
<li class="leaf footer-contact"><a href="https://www.pmu.fr/turf/contact" target="_blank">Contact</a></li>
<li class="leaf footer-aide"><a href="http://entraide-sport.pmu.fr/" target="_blank">Aide</a></li>
<li class="last leaf"><a href="https://inscription.pmu.fr?clientApi=2&amp;typeCompte=2010&amp;codePromo=SPORT&amp;redirectionUrl=https%3A%2F%2Fparis-sportifs.pmu.fr%2F" class="footer_ouverture_compte" target="_blank">Ouvrir un compte</a></li>
</ul>  </div>

</footer> <!-- /.block -->
<footer id="footer-secondary-logo" class="container clearfix">

      
  <div class="block-content">
    <ul class="footer-secondary--row-3"><li class="first leaf"><a href="https://entreprise.pmu.fr/nos-6-engagements/" title="jouons responsable"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/Jouons%20responsable%20petit_0.png" alt="jouons responsable" /></a></li>
<li class="leaf"><a href="http://entreprise.pmu.fr/nos-6-engagements/" title="Les jeux de hasard et d&#039;argent sont interdits aux moins de 18 ans"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/18%20ans%20petit.png" alt="Les jeux de hasard et d&#039;argent sont interdits aux moins de 18 ans" /></a></li>
<li class="leaf"><a href="https://www.demarches.interieur.gouv.fr/particuliers/interdiction-jeux" title="Toute personne souhaitant faire l’objet d’une interdiction de jeux doit le faire elle-même auprès du ministère de l’intérieur. Cette interdiction est valable dans les casinos, les cercles de jeux et sur les sites de jeux en ligne autorisés en vertu de la loi no 2010-476 du 12 mai 2010. Elle est prononcée pour une durée de trois ans non réductible."><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/iconIVJ.png" alt="Toute personne souhaitant faire l’objet d’une interdiction de jeux doit le faire elle-même auprès du ministère de l’intérieur. Cette interdiction est valable dans les casinos, les cercles de jeux et sur les sites de jeux en ligne autorisés en vertu de la loi no 2010-476 du 12 mai 2010. Elle est prononcée pour une durée de trois ans non réductible." /></a></li>
<li class="leaf"><a href="http://www.arjel.fr/" title="Numéro d&#039;agrément : 0002-PS-2010-06-07"><img src="https://paris-sportifs.pmu.fr/sites/default/files/logo-arjel.png" alt="Numéro d&#039;agrément : 0002-PS-2010-06-07" /></a></li>
<li class="leaf"><a href="http://www.escda.fr/" title="*Catégorie Jeux – Étude BVA Group – Viséo CI – mai à juillet 2019 – Plus d’infos sur escda.fr"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/logo_escda_2020_v1.jpg" alt="*Catégorie Jeux – Étude BVA Group – Viséo CI – mai à juillet 2019 – Plus d’infos sur escda.fr" /></a></li>
<li class="last leaf"><a href="https://mediateurdesjeuxenligne.fr/"><img src="https://paris-sportifs.pmu.fr/sites/default/files/menuimage/mediateur-des-jeux-en-ligne.jpg" alt="Médiateur des Jeux en Ligne" /></a></li>
</ul>  </div>

</footer> <!-- /.block -->
<footer id="footer-secondary" class="container clearfix">

      
  <div class="block-content">
    <ul class="footer-secondary--row-4"><li class="first leaf">N° d'agrément</li>
<li class="leaf">Hippique : 0002-PH-2015-06-07</li>
<li class="leaf">Sportif : 0002-PS-2010-06-07</li>
<li class="last leaf">Poker : 0002-PO-2010-06-07</li>
</ul>  </div>

</footer> <!-- /.block -->
  </div>
</div>

<aside class="turn-horizontal hidden">
  <div class="pmu-app--wrapper">
    <div class="text-center text-xsmall text-white">Pour profiter au mieux de votre expérience de paris avec le PMU, veuillez tourner votre tablette en mode paysage.</div>
  </div>
</aside>

<aside class="pmu-app visible-xs-block">
  <div class="pmu-app--wrapper">
    <a href="https://mobile.parier.pmu.fr/PMU-Webkit/page/sportif/home">
      <h4 class="text-center text-medium text-orange text-uppercase text-bold">Téléchargez l'application PMU SPORT !</h4>
      <img alt="PMU Sport on the App Store" src="/profiles/core/themes/pmu_theme/resources/public/logo-app-pmu.jpeg">
      <h5 class="text-center text-small mt-15">Disponible pour iPhone, iPad et Android</h5>
      <p class="text-center text-xxsmall mt-10">Ou bien pariez sur le site mobile</p>
    </a>
  </div>
</aside>

<!--Output wrappers needed for the pop-ups.-->
<aside class="overlay"></aside>
<div id="popin_container" class="popin popin-gain-simulator popin-gain-simulator-simple-bet">
    <img class="loader" src="/profiles/core/themes/pmu_theme/resources/public/loader.gif" alt="Loading"/></div>  <script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_qb8r7Jsd0M2aKgHzaSw8_D1E8clqGt428RMCuD32X5E.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_mtbwbHrJ5vCPTUi9UUVLqpw7bHUN4qKlpmM_y32RhqA.js"></script>
<script>
var LiveServOptions = {
  is_shorter_odds_increase: "false",
  page_start_liveserv_time: 2000,
  recheck_subscriptions_time: 2000
};
var push_www_url          = window.location.protocol + "//paris-sportifs-live.pmu.fr";
var push_instances        = [ "paris-sportifs-live.pmu.fr", 443, "AJAX",];
var push_common_subdomain = "pmu.fr";
if (push_common_subdomain != "") {
  document.domain = push_common_subdomain;
}
</script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_jy3FHUlrRbujuyO-DXJ7fGGB9KVKQ90jzlAPjOiETqA.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_1ZR5-4ceqlE1xAzKdESNtFnYu3Oo2vfXlRauOpaMMdE.js"></script>
<script src="https://cs.betradar.com/ls/widgets/?/pmu/fr/Europe:Paris/widgetloader/widgets"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_gXBSKqNma33WsuA3p-X9oiLK2V4wlmdQr3hZ9Zvsdvc.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_4mAWJoZIcPz0ZdZM9jhGHAYiS0YMiQstd9B4fXUU2G8.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_8_iXqfWhCPP8rjq9DMmIhvqYOXIS1I4qhYh2HM-EXxU.js"></script>
<script>jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"pmu_theme","theme_token":"NXWP_6ws-9fhY8dg6RVXNEOvQI7duPDxDPi0xcwg3CA","jquery_version":"1.10","js":{"profiles\/core\/modules\/openbet\/pmu\/pmu_config\/js\/pmu_config_betslip_locale.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_event_list\/js\/pmu_event_list.js":1,"profiles\/core\/themes\/bootstrap\/js\/bootstrap.js":1,"profiles\/core\/modules\/contrib\/jquery_update\/replace\/jquery\/1.10\/jquery.min.js":1,"misc\/jquery-extend-3.4.0.js":1,"misc\/jquery.once.js":1,"profiles\/core\/libraries\/underscore\/underscore-min.js":1,"profiles\/core\/modules\/openbet\/obet_core\/js\/obet_core.js":1,"profiles\/core\/libraries\/backbone\/backbone.min.js":1,"misc\/drupal.js":1,"profiles\/core\/modules\/openbet\/obet_simple_array_codec\/js\/obet_simple_array_codec.js":1,"profiles\/core\/modules\/contrib\/jquery_update\/replace\/ui\/external\/jquery.cookie.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/obet_live_serv_interface.classes.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/helper.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/LiveServ.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/subjects\/sEVENT.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/subjects\/sPRICE.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/subjects\/sSELCN.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/subjects\/sEVMKT.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/js\/subjects\/sMHCAP.js":1,"profiles\/core\/modules\/contrib\/jquery_update\/replace\/misc\/jquery.form.min.js":1,"misc\/ajax.js":1,"profiles\/core\/modules\/contrib\/jquery_update\/js\/jquery_update.js":1,"0":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/obet_betslip_core.classes.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_sports_legs\/js\/obet_betslip_sports_legs.classes.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_freebets\/js\/obet_betslip_freebets.classes.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_sports_bets\/js\/obet_betslip_sports_bets.classes.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/obet_betslip_core.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_sports_legs\/js\/obet_betslip_sports_legs.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_freebets\/js\/obet_betslip_freebets.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_sports_bets\/js\/obet_betslip_sports_bets.js":1,"profiles\/core\/modules\/contrib\/simple_cookie_compliance\/js\/simple_cookie_compliance.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/Betslip.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/BetError.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/BetslipError.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/Freebet.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/SportsBet.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/MultipleBet.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/SingleBet.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/models\/SportsLeg.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/views\/BetslipView.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/views\/SportsBetView.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/views\/MultipleBetView.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/views\/SingleBetView.js":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/js\/views\/FreebetView.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_account\/modules\/pmu_connect\/js\/PMUConnectMessages.js":1,"public:\/\/languages\/fr-ob_2yD_GpDMtEq0RolUD-lAEEe6_aHakRMKbf_4zBQqFTQ.js":1,"profiles\/core\/modules\/openbet\/obet_client_storage_handler\/obet_client_storage_handler.api.js":1,"profiles\/core\/modules\/openbet\/obet_favourites\/js\/favourites-front.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/live_serv_web_client_api\/push_cfg.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/modules\/obet_live_serv_interface\/live_serv_web_client_api\/push_connect.js":1,"profiles\/core\/modules\/openbet\/obet_price\/js\/obet_price.js":1,"profiles\/core\/modules\/openbet\/obet_push_interface\/js\/obet_push_interface.classes.js":1,"profiles\/core\/modules\/openbet\/obet_user_preference\/js\/obet_user_preference.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_account\/js\/pmu_account.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_account\/modules\/pmu_connect\/js\/pmu_connect.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_gauge\/js\/pmu_gauge.js":1,"profiles\/core\/modules\/contrib\/ctools\/js\/modal.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_market_sorts\/js\/pmu_market_sorts.toggle.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_market_sorts\/js\/pmu_market_sorts.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_multibonus_grid\/js\/pmu_multibonus_grid.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_promotion\/js\/pmu_promotion.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_account\/modules\/pmu_connect\/js\/pinpad.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_simulator\/js\/simulator_main.js":1,"public:\/\/tag_commander\/tc_PMUonlineSport_2.15_0.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_tag_commander\/js\/pmu_tag_commander_functions.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_tag_commander\/js\/pmu_tag_commander_custom.js":1,"public:\/\/pmu_tag_commander_public.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_video_streaming\/js\/pmu_video_streaming.js":1,"profiles\/core\/themes\/bootstrap\/js\/misc\/_progress.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_commentary\/js\/pmu_commentary_betradar.js":1,"https:\/\/cs.betradar.com\/ls\/widgets\/?\/pmu\/fr\/Europe:Paris\/widgetloader\/widgets":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_fantasy_league\/js\/pmu_fantasy_league.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_jackpot\/js\/pmu_jackpot.js":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_deploy\/features\/pmu_notifications\/pmu_notifications.js":1,"profiles\/core\/themes\/pmu_theme\/bootstrap\/js\/bootstrap.min.js":1,"profiles\/core\/themes\/pmu_theme\/js\/pmu_theme.js":1,"profiles\/core\/themes\/pmu_theme\/js\/pmu_countdown.js":1,"profiles\/core\/themes\/pmu_theme\/js\/jQuery.print.js":1,"profiles\/core\/themes\/pmu_theme\/js\/betslip\/betslip_theme.js":1,"profiles\/core\/themes\/pmu_theme\/js\/betslip\/betslip.js":1,"profiles\/core\/themes\/pmu_theme\/js\/betslip\/betslip_errors.js":1,"profiles\/core\/themes\/pmu_theme\/js\/mustache.js":1,"profiles\/core\/themes\/pmu_theme\/js\/nouislider.js":1,"profiles\/core\/themes\/pmu_theme\/js\/wNumb.js":1,"profiles\/core\/themes\/pmu_theme\/js\/moment.js":1,"profiles\/core\/themes\/pmu_theme\/js\/moment-locale-fr.js":1,"profiles\/core\/themes\/pmu_theme\/js\/hammer.js":1,"profiles\/core\/themes\/pmu_theme\/js\/select2.js":1,"profiles\/core\/themes\/pmu_theme\/js\/jquery.selectBox.js":1,"profiles\/core\/themes\/pmu_theme\/js\/dropdowns.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/bets.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/calendar.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/cashout-info.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/focus-toggle.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/gauge.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/sticky-header.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/filter-content.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/slider-content.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/gluey.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/idle-timer.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/overlay.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/pinpad.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/resizer.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/placeholder.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/responsive-helper.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/search-toggle.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/select.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/team.plugins.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/bonus-bomb.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/integer-inc.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/jackpot.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/scroll-more.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/slider.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/swipe.plugin.js":1,"profiles\/core\/themes\/pmu_theme\/js\/plugins\/loading_overlay.js":1,"profiles\/core\/themes\/pmu_theme\/js\/main.js":1,"profiles\/core\/themes\/pmu_theme\/js\/idle-timer-popup.js":1,"profiles\/core\/themes\/pmu_theme\/js\/liveserv\/subjects\/sSBINC.js":1,"profiles\/core\/themes\/pmu_theme\/js\/liveserv\/subjects\/sSBINM.js":1,"profiles\/core\/themes\/pmu_theme\/js\/liveserv\/helpers\/generic.js":1,"profiles\/core\/themes\/pmu_theme\/js\/liveserv\/helpers\/commentary.js":1,"profiles\/core\/themes\/bootstrap\/js\/modules\/ctools\/js\/modal.js":1,"profiles\/core\/themes\/bootstrap\/js\/misc\/ajax.js":1,"profiles\/core\/themes\/pmu_theme\/js\/ie.js":1,"profiles\/core\/themes\/pmu_theme\/js\/liveserv\/liveserv.js":1},"css":{"modules\/system\/system.base.css":1,"profiles\/core\/modules\/contrib\/date\/date_api\/date.css":1,"profiles\/core\/modules\/contrib\/date\/date_popup\/themes\/datepicker.1.7.css":1,"modules\/field\/theme\/field.css":1,"modules\/node\/node.css":1,"profiles\/core\/modules\/contrib\/views\/css\/views.css":1,"profiles\/core\/modules\/contrib\/ckeditor\/css\/ckeditor.css":1,"profiles\/core\/modules\/contrib\/ctools\/css\/ctools.css":1,"profiles\/core\/modules\/contrib\/panels\/css\/panels.css":1,"profiles\/core\/modules\/openbet\/obet_betslip_core\/css\/obet_betslip_core.css":1,"profiles\/core\/modules\/openbet\/pmu\/pmu_account\/modules\/pmu_connect\/css\/pmu_connect.css":1,"profiles\/core\/modules\/contrib\/ctools\/css\/modal.css":1,"0":1,"profiles\/core\/modules\/contrib\/simple_cookie_compliance\/css\/simple_cookie_compliance.css":1,"profiles\/core\/themes\/pmu_theme\/bootstrap\/css\/bootstrap.min.css":1,"profiles\/core\/themes\/pmu_theme\/css\/jquery.selectBox.css":1,"profiles\/core\/themes\/pmu_theme\/css\/nouislider.css":1,"profiles\/core\/themes\/pmu_theme\/css\/nouislider.tooltips.css":1,"profiles\/core\/themes\/pmu_theme\/css\/style.css":1,"profiles\/core\/themes\/pmu_theme\/css\/pmu_style.css":1}},"hierarchyIDS":{"categoryID":"1","classID":"8","typeID":"1366","eventID":"666562"},"urlIsAjaxTrusted":{"https:\/\/paris-sportifs.pmu.fr\/recherche":true,"\/system\/ajax":true,"\/event\/666562":true},"obet_client_storage_handler":{"CLIENT_STORAGE_SPORTS_LEGS":"sports_legs","CLIENT_STORAGE_BET_TYPES":"bet_types","CLIENT_STORAGE_MISC":"misc","CLIENT_STORAGE_FREEBETS_SELECTIONS":"freebets_selections","CLIENT_STORAGE_JOURNEY_HISTORY":"journey_history","CLIENT_STORAGE_JOURNEY_STAKE":"journey_stake","sports_legs_format":["leg_ref","ev_oc_ids","lp_num","lp_den","leg_sort","leg_type","price_type","hcap_value","bir_index","ew_places","ew_fac_num","ew_fac_den","banker"],"bet_types_format":["bet_ref","bet_type","leg_ref","num_lines","stake_per_line","potential_win","min_stake","max_stake","leg_type"],"misc_format":["bs_single_expansion","bs_multi_expansion"],"freebets_selections_format":["freebet_ref","bet_type"],"journey_history_format":["back_url"],"journey_stake_format":["stake"],"CLIENT_STORAGE_ACTIVE_STORAGES":["cookies"],"CLIENT_STORAGE_COOKIE_DELIMITERS":{"sports_legs":{"values_delimiter":"|","rows_delimiter":"@"},"bet_types":{"values_delimiter":"|","rows_delimiter":"@"},"misc":{"values_delimiter":"|","rows_delimiter":"@"},"freebets_selections":{"values_delimiter":"|","rows_delimiter":"@"},"journey_history":{"values_delimiter":"|","rows_delimiter":"@"}},"CLIENT_STORAGE_COOKIE_DELIMITERS_DEFAULT":{"values_delimiter":"|","rows_delimiter":"@"}},"obet_betslip_core":{"multiples_enabled":1,"success_message_enabled":1,"bet_receipt_enabled":1,"bet_validate_enabled":1,"maximum_number_of_legs":15,"betslip_build_option":"page_load"},"obet_betslip_freebets":{"schema_version":2},"obet_betslip_sports_bets":{"schema_version":2},"obet_betslip_sports_legs":{"schema_version":2},"favourites":{"modalSize":{"type":"scale","width":0.7,"height":0.6},"modalOptions":{"opacity":0.5,"background-color":"#000"},"animation":"fadeIn","modalTheme":"CtoolsFavourites"},"obet_push_interface":{"services":["obet_live_serv_interface"]},"cashout":{"systeme_array":["TRX","PAT","YAN","L15","CAN","L31","HNZ","L63","SHNZ","GOL"]},"loading_animated_gif":"profiles\/core\/themes\/pmu_theme\/resources\/public\/loader.gif","pmu_config":{"sports_mapping":{"default":"default","soccer":"football","football":"football","foot-uk---comp\u00e9tition":"football","foot-europe---comp\u00e9tition":"football","football-specials":"football","virtual-football":"football","rugby":"rugby","rugby-\u00e0-xiii":"rugby","tennis":"tennis","tennis de table":"table-tennis","tennis_de_table":"table-tennis","tennis-de-table":"table-tennis","basket-us":"basketball","basket-europe":"basketball","basket europe":"basketball","basket euro":"basketball","basket-euro":"basketball","basket us":"basketball","football-am\u00e9ricain":"football-us","baseball":"baseball","hockey-eu":"hockey","hockey-us":"hockey","billard":"snooker","billard-am\u00e9ricain":"snooker","volley-ball":"volley-ball","boxe":"boxe","jo":"jo","golf":"golf","judo":"judo","cano\u00eb-kayak":"kayak","cano\u00e9-kayak":"kayak","canoeing":"kayak","badminton":"badminton","cross-country":"cross-country-skiing","taekwondo":"taekwondo","water-polo":"waterpolo","waterpolo":"waterpolo","rink-hockey":"hockey","hockey-sur-glace-us":"hockey","hockey-sur-glace-eu":"hockey","hockey-euro":"hockey","hockey-sur-glace-am\u00e9ricain":"hockey","hockey-sur-gazon":"hockey","hockey-sur-patins":"hockey","snooker":"snooker","handball":"handball","patinage-artistique":"ice-skating","patinage-de-vitesse":"ice-skating","patinage-de-vitesse-sur-piste-courte":"ice-skating","luge":"luge","natation":"swimming","pool":"swimming","aviron":"rowing","beach-volley":"beach-volley","tir-\u00e0-l\u0027arc":"archery","voile":"sailing","halt\u00e9rophilie":"weightlifting","weightlifting":"Weightlifting","snowboard":"snowboard","biathlon":"biathlon","skeleton":"skeleton","equitation":"horse-riding","curling":"curling","escrime":"fencing","bobsleigh":"bobsleigh","athl\u00e9tisme":"athletism","bowls":"petanque","boules":"petanque","saut-d\u0027obstacle":"horse-riding","ski-de-fond":"alpine-skiing","ski-alpin":"alpine-skiing","saut-\u00e0-ski":"cross-country-skiing","lutte":"judo","itf-salisbury-doubles":"tennis","retail-racing":"auto-moto","university-boat-race":"rowing","cyclisme":"road-cycling"}},"betslipStringOverrides":{"OBET_BET_ERROR_PRICE_CHANGED":"La cote a chang\u00e9","PRICE_CHANGED":"Le price a chang\u00e9","OBET_BET_ERROR_EVENT_STARTED":"Le event a commenc\u00e9","EVENT_STARTED":"Le event a commenc\u00e9","OBET_BET_ERROR_OUTCOME_SUSPENDED":"Le outcome est suspondu","OBET_BET_ERROR_GENERIC_ERROR":"L\u0027erreur g\u00e9n\u00e9rique","OBET_BETSLIP_ERROR_ACCOUNT_BETTING_DISABLED":"Le account betting disabled","OBET_BET_ERROR_INSUFFICIENT_FUNDS":"Solde insuffisant","INSUFFICIENT_FUNDS":"Solde insuffisant \/ Limitation atteinte","WEEKLY_LIMIT_EXCEEDED":"Votre plafond sportif hebdomadaire est d\u00e9pass\u00e9","OUTCOME_SUSPENDED":"Le outcome est suspondu","STAKE_TOO_LOW":"Mise invalide","STAKE_TOO_HIGH":"Mise invalide","SERVICE_UNAVAILABLE":"Service indisponible","OTHER_BETS_FAILED":"Autres paris ont \u00e9chou\u00e9","ACCOUNT_BETTING_DISBALED":"Paris est d\u00e9sactiv\u00e9 pour ce compte","HANDICAP_CHANGED":"Handicap a chang\u00e9","MIN_MAX_BET_ERROR":"Pari impossible sur cette s\u00e9lection","GENERIC_ERROR":"L\u0027erreur g\u00e9n\u00e9rique","OBET_BETSLIP_MULTI_DESC_AC10":"1 Combin\u00e9 10 issu de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_AC11":"1 Combin\u00e9 11 issu de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_AC12":"1 Combin\u00e9 12 issu de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_AC13":"1 Combin\u00e9 13 issu de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_AC14":"1 Combin\u00e9 14 issu de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_AC15":"1 Combin\u00e9 15 issu de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC4":"1 Quadruple issu de 4 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC5":"1 Combin\u00e9 5 issu de 5 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC6":"1 Combin\u00e9 6 issu de 6 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC7":"1 Combin\u00e9 7 issu de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC8":"1 Combin\u00e9 8 issu de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_ACC9":"1 Combin\u00e9 9 issu de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_CAN":"1 Canadian contient 26 paris bas\u00e9s sur 5 s\u00e9lections : 10 Doubles, 10 Triples, 5 Quadruples et 1 Combin\u00e9 5","OBET_BETSLIP_MULTI_DESC_DBL":"1 Double issu de 2 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_GOL":"1 Goliath contient 247 paris bas\u00e9s sur 8 s\u00e9lections : 28 Doubles, 56 Triples, 70 Quadruples, 56 Combin\u00e9s 5, 28 Combin\u00e9s 6, 8 Combin\u00e9s 7, 1 Combin\u00e9 8","OBET_BETSLIP_MULTI_DESC_HNZ":"1 Heinz contient 57 paris bas\u00e9s sur 6 s\u00e9lections : 15 Doubles, 20 Triples, 15 Quadruples, 6 Combin\u00e9s 5, 1 Combin\u00e9s 6","OBET_BETSLIP_MULTI_DESC_L15":"1 Lucky 15 contient 15 paris bas\u00e9s sur 4 s\u00e9lections : 4 Simples, 6 Doubles, 4 Triples et 1 Quadruple","OBET_BETSLIP_MULTI_DESC_L31":"1 Lucky 31 contient 31 paris bas\u00e9s sur 5 s\u00e9lections : 5 Simples, 10 Doubles, 10 Triples, 5 Quadruples et 1 Combin\u00e9 5","OBET_BETSLIP_MULTI_DESC_L63":"1 Lucky 63 contient 63 paris bas\u00e9s sur 6 s\u00e9lections : 6 Simples, 15 Doubles, 20 Triples, 15 Quadruples, 6 Combin\u00e9s 5, 1 Combin\u00e9 6","OBET_BETSLIP_MULTI_DESC_P-23":"3 Doubles issus de 3 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-24":"6 Doubles issus de 4 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-25":"10 Doubles issus de 5 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-26":"15 Doubles issus de 6 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-27":"21 Doubles issus de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-28":"28 Doubles issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-29":"36 Doubles issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-34":"4 Triples issus de 4 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-35":"10 Triples issus de 5 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-36":"20 Triples issus de 6 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-37":"35 Triples issus de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-38":"56 Triples issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-39":"84 Triples issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-45":"5 Quadruples issus de 5 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-46":"15 Quadruples issus de 6 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-47":"35 Quadruples issus de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-48":"70 Quadruples issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-49":"126 Quadruples issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-56":"6 Combin\u00e9s 5 issus de 6 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-57":"21 Combin\u00e9s 5 issus de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-58":"56 Combin\u00e9s 5 issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-59":"126 Combin\u00e9s 5 issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-67":"7 Combin\u00e9s 6 issus de 7 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-68":"28 Combin\u00e9s 6 issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-69":"84 Combin\u00e9s 6 issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-78":"8 Combin\u00e9s 7 issus de 8 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-79":"36 Combin\u00e9s 7 issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P-89":"9 Combin\u00e9s 8 issus de 9 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1011":"11 Combin\u00e9s 10 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1012":"66 Combin\u00e9s 10 issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1013":"286 Combin\u00e9s 10 issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1112":"12 Combin\u00e9s 11 issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1113":"78 Combin\u00e9s 11 issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1114":"364 Combin\u00e9s 11 issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1213":"13 Combin\u00e9s 12 issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1214":"91 Combin\u00e9s 12 issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1215":"455 Combin\u00e9s 12 issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1314":"14 Combin\u00e9s 13 issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1315":"105 Combin\u00e9s 13 issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P1415":"15 Combin\u00e9s 14 issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P210":"45 Doubles issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P211":"55 Doubles issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P212":"66 Doubles issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P213":"78 Doubles issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P214":"91 Doubles issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P215":"105 Doubles issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P310":"120 Triples issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P311":"165 Triples issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P312":"220 Triples issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P313":"286 Triples issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P314":"364 Triples issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P315":"455 Triples issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P410":"210 Quadruples issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P411":"330 Quadruples issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P412":"495 Quadruples issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P413":"715 Quadruples issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P414":"1001 Quadruples issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P415":"1365 Quadruples issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P510":"252 Combin\u00e9s 5 issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P511":"462 Combin\u00e9s 5 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P512":"792 Combin\u00e9s 5 issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P513":"1287 Combin\u00e9s 5 issus de 13 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P514":"2002 Combin\u00e9s 5 issus de 14 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P515":"3003 Combin\u00e9s 5 issus de 15 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P610":"210 Combin\u00e9s 6 issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P611":"462 Combin\u00e9s 6 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P710":"120 Combin\u00e9s 7 issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P711":"330 Combin\u00e9s 7 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P810":"45 Combin\u00e9s 8 issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P811":"165 Combin\u00e9s 8 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P812":"495 Combin\u00e9s 8 issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P910":"10 Combin\u00e9s 9 issus de 10 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P911":"55 Combin\u00e9s 9 issus de 11 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_P912":"220 Combin\u00e9s 9 issus de 12 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_PAT":"1 Patent contient 7 paris : 3 Simples, 3 Doubles et 1 Triple","OBET_BETSLIP_MULTI_DESC_SHNZ":"1 Super-Heinz contient 120 paris sur 7 s\u00e9lections : 21 Doubles, 35 Triples, 35 Quadruples, 21 Combin\u00e9s 5, 7 Combin\u00e9s 6 et 1 Combin\u00e9 7","OBET_BETSLIP_MULTI_DESC_TBL":"1 Triple issu de 3 s\u00e9lections","OBET_BETSLIP_MULTI_DESC_TRX":"1 Trixie contient 3 Doubles et 1 Triple","OBET_BETSLIP_MULTI_DESC_YAN":"1 Yankee contient 6 Doubles, 4 Triples et 1 Quadruple","WEEKLY_LIMIT_REACHED":"Limite hebdomadaire atteint","OBET_BETSLIP_MULTI_3BY4":"3 par 4","OBET_BETSLIP_MULTI_4BY5":"4 par 5","OBET_BETSLIP_MULTI_AC10":"Pari combin\u00e9 10","OBET_BETSLIP_MULTI_AC11":"Pari combin\u00e9 11","OBET_BETSLIP_MULTI_AC12":"Pari combin\u00e9 12","OBET_BETSLIP_MULTI_AC13":"Pari combin\u00e9 13","OBET_BETSLIP_MULTI_AC14":"Pari combin\u00e9 14","OBET_BETSLIP_MULTI_AC15":"Pari combin\u00e9 15","OBET_BETSLIP_MULTI_AC16":"Pari combin\u00e9 16","OBET_BETSLIP_MULTI_AC17":"Pari combin\u00e9 17","OBET_BETSLIP_MULTI_AC18":"Pari combin\u00e9 18","OBET_BETSLIP_MULTI_AC19":"Pari combin\u00e9 19","OBET_BETSLIP_MULTI_AC20":"Pari combin\u00e9 20","OBET_BETSLIP_MULTI_AC21":"Pari combin\u00e9 21","OBET_BETSLIP_MULTI_AC22":"Pari combin\u00e9 22","OBET_BETSLIP_MULTI_AC23":"Pari combin\u00e9 23","OBET_BETSLIP_MULTI_AC24":"Pari combin\u00e9 24","OBET_BETSLIP_MULTI_AC25":"Pari combin\u00e9 25","OBET_BETSLIP_MULTI_ACC4":"Pari combin\u00e9 4","OBET_BETSLIP_MULTI_ACC5":"Pari combin\u00e9 5","OBET_BETSLIP_MULTI_ACC6":"Pari combin\u00e9 6","OBET_BETSLIP_MULTI_ACC7":"Pari combin\u00e9 7","OBET_BETSLIP_MULTI_ACC8":"Pari combin\u00e9 8","OBET_BETSLIP_MULTI_ACC9":"Pari combin\u00e9 9","OBET_BETSLIP_MULTI_CAN":"Canadian","OBET_BETSLIP_MULTI_DBL":"Double","OBET_BETSLIP_MULTI_DS10":"Double Stakes About (10)","OBET_BETSLIP_MULTI_DS11":"Double Stakes About (11)","OBET_BETSLIP_MULTI_DS12":"Double Stakes About (12)","OBET_BETSLIP_MULTI_DS13":"Double Stakes About (13)","OBET_BETSLIP_MULTI_DS14":"Double Stakes About (14)","OBET_BETSLIP_MULTI_DS15":"Double Stakes About (15)","OBET_BETSLIP_MULTI_DS2":"Double Stakes About","OBET_BETSLIP_MULTI_DS3":"Double Stakes About (3)","OBET_BETSLIP_MULTI_DS4":"Double Stakes About (4)","OBET_BETSLIP_MULTI_DS5":"Double Stakes About (5)","OBET_BETSLIP_MULTI_DS6":"Double Stakes About (6)","OBET_BETSLIP_MULTI_DS7":"Double Stakes About (7)","OBET_BETSLIP_MULTI_DS8":"Double Stakes About (8)","OBET_BETSLIP_MULTI_DS9":"Double Stakes About (9)","OBET_BETSLIP_MULTI_FLG":"Flag","OBET_BETSLIP_MULTI_FSP":"Fivespot","OBET_BETSLIP_MULTI_GOL":"Goliath","OBET_BETSLIP_MULTI_HNZ":"Heinz","OBET_BETSLIP_MULTI_L15":"Lucky 15","OBET_BETSLIP_MULTI_L31":"Lucky 31","OBET_BETSLIP_MULTI_L63":"Lucky 63","OBET_BETSLIP_MULTI_L7B":"Lucky 7 Bingo","OBET_BETSLIP_MULTI_LY10":"Lucky 10","OBET_BETSLIP_MULTI_LY11":"Lucky 11","OBET_BETSLIP_MULTI_LY6":"Lucky 6","OBET_BETSLIP_MULTI_MAG7":"Magnificent 7","OBET_BETSLIP_MULTI_MAN_BET":"Paris \u00e9crit","OBET_BETSLIP_MULTI_MAN":"Ajustement manuel","OBET_BETSLIP_MULTI_P1011":"Syst\u00e8me 10\/11","OBET_BETSLIP_MULTI_P1012":"Syst\u00e8me 10\/12","OBET_BETSLIP_MULTI_P1013":"Syst\u00e8me 10\/13","OBET_BETSLIP_MULTI_P1112":"Syst\u00e8me 11\/12","OBET_BETSLIP_MULTI_P1113":"Syst\u00e8me 11\/13","OBET_BETSLIP_MULTI_P1114":"Syst\u00e8me 11\/14","OBET_BETSLIP_MULTI_P1213":"Syst\u00e8me 12\/13","OBET_BETSLIP_MULTI_P1214":"Syst\u00e8me 12\/14","OBET_BETSLIP_MULTI_P1215":"Syst\u00e8me 12\/15","OBET_BETSLIP_MULTI_P1314":"Syst\u00e8me 13\/14","OBET_BETSLIP_MULTI_P1315":"Syst\u00e8me 13\/15","OBET_BETSLIP_MULTI_P1415":"Syst\u00e8me 14\/15","OBET_BETSLIP_MULTI_P1416":"Syst\u00e8me 14\/16","OBET_BETSLIP_MULTI_P1516":"Syst\u00e8me 15\/16","OBET_BETSLIP_MULTI_P1517":"Syst\u00e8me 15\/17","OBET_BETSLIP_MULTI_P1617":"Syst\u00e8me 16\/17","OBET_BETSLIP_MULTI_P1618":"Syst\u00e8me 16\/18","OBET_BETSLIP_MULTI_P1718":"Syst\u00e8me 17\/18","OBET_BETSLIP_MULTI_P1719":"Syst\u00e8me 17\/19","OBET_BETSLIP_MULTI_P1819":"Syst\u00e8me 18\/19","OBET_BETSLIP_MULTI_P1820":"Syst\u00e8me 18\/20","OBET_BETSLIP_MULTI_P1920":"Syst\u00e8me 19\/20","OBET_BETSLIP_MULTI_P1921":"Syst\u00e8me 19\/21","OBET_BETSLIP_MULTI_P2021":"Syst\u00e8me 20\/21","OBET_BETSLIP_MULTI_P2022":"Syst\u00e8me 20\/22","OBET_BETSLIP_MULTI_P210":"Syst\u00e8me 2\/10","OBET_BETSLIP_MULTI_P211":"Syst\u00e8me 2\/11","OBET_BETSLIP_MULTI_P2122":"Syst\u00e8me 21\/22","OBET_BETSLIP_MULTI_P2123":"Syst\u00e8me 21\/23","OBET_BETSLIP_MULTI_P212":"Syst\u00e8me 2\/12","OBET_BETSLIP_MULTI_P213":"Syst\u00e8me 2\/13","OBET_BETSLIP_MULTI_P214":"Syst\u00e8me 2\/14","OBET_BETSLIP_MULTI_P215":"Syst\u00e8me 2\/15","OBET_BETSLIP_MULTI_P216":"Syst\u00e8me 2\/16","OBET_BETSLIP_MULTI_P217":"Syst\u00e8me 2\/17","OBET_BETSLIP_MULTI_P218":"Syst\u00e8me 2\/18","OBET_BETSLIP_MULTI_P219":"Syst\u00e8me 2\/19","OBET_BETSLIP_MULTI_P220":"Syst\u00e8me 2\/20","OBET_BETSLIP_MULTI_P221":"Syst\u00e8me 2\/21","OBET_BETSLIP_MULTI_P2223":"Syst\u00e8me 22\/23","OBET_BETSLIP_MULTI_P2224":"Syst\u00e8me 22\/24","OBET_BETSLIP_MULTI_P222":"Syst\u00e8me 2\/22","OBET_BETSLIP_MULTI_P223":"Syst\u00e8me 2\/23","OBET_BETSLIP_MULTI_P224":"Syst\u00e8me 2\/24","OBET_BETSLIP_MULTI_P225":"Syst\u00e8me 2\/25","OBET_BETSLIP_MULTI_P2324":"Syst\u00e8me 23\/24","OBET_BETSLIP_MULTI_P2325":"Syst\u00e8me 23\/25","OBET_BETSLIP_MULTI_P-23":"Syst\u00e8me 2\/3","OBET_BETSLIP_MULTI_P2425":"Syst\u00e8me 24\/25","OBET_BETSLIP_MULTI_P-24":"Syst\u00e8me 2\/4","OBET_BETSLIP_MULTI_P-25":"Syst\u00e8me 2\/5","OBET_BETSLIP_MULTI_P-26":"Syst\u00e8me 2\/6","OBET_BETSLIP_MULTI_P-27":"Syst\u00e8me 2\/7","OBET_BETSLIP_MULTI_P-28":"Syst\u00e8me 2\/8","OBET_BETSLIP_MULTI_P-29":"Syst\u00e8me 2\/9","OBET_BETSLIP_MULTI_P310":"Syst\u00e8me 3\/10","OBET_BETSLIP_MULTI_P311":"Syst\u00e8me 3\/11","OBET_BETSLIP_MULTI_P312":"Syst\u00e8me 3\/12","OBET_BETSLIP_MULTI_P313":"Syst\u00e8me 3\/13","OBET_BETSLIP_MULTI_P314":"Syst\u00e8me 3\/14","OBET_BETSLIP_MULTI_P315":"Syst\u00e8me 3\/15","OBET_BETSLIP_MULTI_P-34":"Syst\u00e8me 3\/4","OBET_BETSLIP_MULTI_P-35":"Syst\u00e8me 3\/5","OBET_BETSLIP_MULTI_P-36":"Syst\u00e8me 3\/6","OBET_BETSLIP_MULTI_P-37":"Syst\u00e8me 3\/7","OBET_BETSLIP_MULTI_P-38":"Syst\u00e8me 3\/8","OBET_BETSLIP_MULTI_P-39":"Syst\u00e8me 3\/9","OBET_BETSLIP_MULTI_P410":"Syst\u00e8me 4\/10","OBET_BETSLIP_MULTI_P411":"Syst\u00e8me 4\/11","OBET_BETSLIP_MULTI_P412":"Syst\u00e8me 4\/12","OBET_BETSLIP_MULTI_P413":"Syst\u00e8me 4\/13","OBET_BETSLIP_MULTI_P414":"Syst\u00e8me 4\/14","OBET_BETSLIP_MULTI_P415":"Syst\u00e8me 4\/15","OBET_BETSLIP_MULTI_P-45":"Syst\u00e8me 4\/5","OBET_BETSLIP_MULTI_P-46":"Syst\u00e8me 4\/6","OBET_BETSLIP_MULTI_P-47":"Syst\u00e8me 4\/7","OBET_BETSLIP_MULTI_P-48":"Syst\u00e8me 4\/8","OBET_BETSLIP_MULTI_P-49":"Syst\u00e8me 4\/9","OBET_BETSLIP_MULTI_P510":"Syst\u00e8me 5\/10","OBET_BETSLIP_MULTI_P511":"Syst\u00e8me 5\/11","OBET_BETSLIP_MULTI_P512":"Syst\u00e8me 5\/12","OBET_BETSLIP_MULTI_P513":"Syst\u00e8me 5\/13","OBET_BETSLIP_MULTI_P514":"Syst\u00e8me 5\/14","OBET_BETSLIP_MULTI_P515":"Syst\u00e8me 5\/15","OBET_BETSLIP_MULTI_P-56":"Syst\u00e8me 5\/6","OBET_BETSLIP_MULTI_P-57":"Syst\u00e8me 5\/7","OBET_BETSLIP_MULTI_P-58":"Syst\u00e8me 5\/8","OBET_BETSLIP_MULTI_P-59":"Syst\u00e8me 5\/9","OBET_BETSLIP_MULTI_P610":"Syst\u00e8me 6\/10","OBET_BETSLIP_MULTI_P611":"Syst\u00e8me 6\/11","OBET_BETSLIP_MULTI_P-67":"Syst\u00e8me 6\/7","OBET_BETSLIP_MULTI_P-68":"Syst\u00e8me 6\/8","OBET_BETSLIP_MULTI_P-69":"Syst\u00e8me 6\/9","OBET_BETSLIP_MULTI_P710":"Syst\u00e8me 7\/10","OBET_BETSLIP_MULTI_P711":"Syst\u00e8me 7\/11","OBET_BETSLIP_MULTI_P-78":"Syst\u00e8me 7\/8","OBET_BETSLIP_MULTI_P-79":"Syst\u00e8me 7\/9","OBET_BETSLIP_MULTI_P810":"Syst\u00e8me 8\/10","OBET_BETSLIP_MULTI_P811":"Syst\u00e8me 8\/11","OBET_BETSLIP_MULTI_P812":"Syst\u00e8me 8\/12","OBET_BETSLIP_MULTI_P-89":"Syst\u00e8me 8\/9","OBET_BETSLIP_MULTI_P910":"Syst\u00e8me 9\/10","OBET_BETSLIP_MULTI_P911":"Syst\u00e8me 9\/11","OBET_BETSLIP_MULTI_P912":"Syst\u00e8me 9\/12","OBET_BETSLIP_MULTI_PAT":"Patent","OBET_BETSLIP_MULTI_PON":"Pontoon","OBET_BETSLIP_MULTI_ROB":"Round Robin","OBET_BETSLIP_MULTI_SHNZ":"Super Heinz","OBET_BETSLIP_MULTI_SS10":"Single Stakes About(10)","OBET_BETSLIP_MULTI_SS11":"Single Stakes About(11)","OBET_BETSLIP_MULTI_SS12":"Single Stakes About(12)","OBET_BETSLIP_MULTI_SS13":"Single Stakes About(13)","OBET_BETSLIP_MULTI_SS14":"Single Stakes About(14)","OBET_BETSLIP_MULTI_SS15":"Single Stakes About(15)","OBET_BETSLIP_MULTI_SS2":"Single Stakes About","OBET_BETSLIP_MULTI_SS3":"Single Stakes About (3)","OBET_BETSLIP_MULTI_SS4":"Single Stakes About (4)","OBET_BETSLIP_MULTI_SS5":"Single Stakes About (5)","OBET_BETSLIP_MULTI_SS6":"Single Stakes About (6)","OBET_BETSLIP_MULTI_SS7":"Single Stakes About (7)","OBET_BETSLIP_MULTI_SS8":"Single Stakes About (8)","OBET_BETSLIP_MULTI_SS9":"Single Stakes About (9)","OBET_BETSLIP_MULTI_TBL":"Triple","OBET_BETSLIP_MULTI_TRX":"Trixie","OBET_BETSLIP_MULTI_UJK":"Union Jack","OBET_BETSLIP_MULTI_YAN":"Yankee","OBET_BETSLIP_MULTI_YAP":"Yap","OBET_BETSLIP_MULTI_AC10_ACC":"Pari Combin\u00e9 (10)","OBET_BETSLIP_MULTI_AC11_ACC":"Pari Combin\u00e9 (11)","OBET_BETSLIP_MULTI_AC12_ACC":"Pari Combin\u00e9 (12)","OBET_BETSLIP_MULTI_AC13_ACC":"Pari Combin\u00e9 (13)","OBET_BETSLIP_MULTI_AC14_ACC":"Pari Combin\u00e9 (14)","OBET_BETSLIP_MULTI_AC15_ACC":"Pari Combin\u00e9 (15)","OBET_BETSLIP_MULTI_AC16_ACC":"Pari Combin\u00e9 (16)","OBET_BETSLIP_MULTI_AC17_ACC":"Pari Combin\u00e9 (17)","OBET_BETSLIP_MULTI_AC18_ACC":"Pari Combin\u00e9 (18)","OBET_BETSLIP_MULTI_AC19_ACC":"Pari Combin\u00e9 (19)","OBET_BETSLIP_MULTI_AC20_ACC":"Pari Combin\u00e9 (20)","OBET_BETSLIP_MULTI_AC21_ACC":"Pari Combin\u00e9 (21)","OBET_BETSLIP_MULTI_AC22_ACC":"Pari Combin\u00e9 (22)","OBET_BETSLIP_MULTI_AC23_ACC":"Pari Combin\u00e9 (23)","OBET_BETSLIP_MULTI_AC24_ACC":"Pari Combin\u00e9 (24)","OBET_BETSLIP_MULTI_AC25_ACC":"Pari Combin\u00e9 (25)","OBET_BETSLIP_MULTI_ACC4_ACC":"Pari Combin\u00e9 (4)","OBET_BETSLIP_MULTI_ACC5_ACC":"Pari Combin\u00e9 (5)","OBET_BETSLIP_MULTI_ACC6_ACC":"Pari Combin\u00e9 (6)","OBET_BETSLIP_MULTI_ACC7_ACC":"Pari Combin\u00e9 (7)","OBET_BETSLIP_MULTI_ACC8_ACC":"Pari Combin\u00e9 (8)","OBET_BETSLIP_MULTI_ACC9_ACC":"Pari Combin\u00e9 (9)","OBET_BETSLIP_MULTI_DBL_ACC":"Double","OBET_BETSLIP_MULTI_TBL_ACC":"Triple (s)","OBET_BETSLIP_ERROR_WEEKLY_LIMIT_REACHED @weeklyLimit":"\u003Cb\u003EAttention\u003C\/b\u003E\u003Cbr \/\u003ELe cumul de vos enjeux depuis le d\u0026eacute;but de la semaine a atteint la limite que vous vous \u0026ecirc;tes fix\u0026eacute;e: @weeklyLimit\u0026euro;\u003Cbr\u003E Comme vous avez d\u0026eacute;pass\u0026eacute; cette limite vous ne pouvez  plus parier sur nos paris sportifs jusqu\u0026apos;\u0026agrave; dimanche inclus.\u003Cbr\u003EVous pourrez miser \u0026agrave; nouveau \u0026agrave; partir de lundi matin.\u003Cbr\u003ESi vous souhaitez continuer \u0026agrave; parier vous pouvez la modifier:","OBET_BET_ERROR_WEEKLY_LIMIT_REACHED @weeklyLimit":"\u003Cb\u003EAttention\u003C\/b\u003E\u003Cbr \/\u003ELe cumul de vos enjeux depuis le d\u0026eacute;but de la semaine a atteint la limite que vous vous \u0026ecirc;tes fix\u0026eacute;e: @weeklyLimit\u0026euro;\u003Cbr\u003E Comme vous avez d\u0026eacute;pass\u0026eacute; cette limite vous ne pouvez  plus parier sur nos paris sportifs jusqu\u0026apos;\u0026agrave; dimanche inclus.\u003Cbr\u003EVous pourrez miser \u0026agrave; nouveau \u0026agrave; partir de lundi matin.\u003Cbr\u003ESi vous souhaitez continuer \u0026agrave; parier vous pouvez la modifier:","The maximum stake per line for this bet is @maxStakePerLine \u20ac":"La mise maximale par ligne pour ce pari est @maxStakePerLine \u20ac","The maximum stake for this bet is @maxStakePerLine \u20ac":"La mise maximale pour ce pari est @maxStakePerLine \u20ac","The maximum stake per line for outcome @outcomeName is @maxStakePerLine \u20ac, for event @eventName":"La mise maximale pour @outcomeName est @maxStakePerLine \u20ac, pour l\u0027\u0026eacute;v\u0026eacute;nement @eventName","The maximum stake for @betType is @maxStakePerLine \u20ac":"La mise maximum pour @betType est de @maxStakePerLine \u20ac","The minimum stake per line for this bet is @minStakePerLine \u20ac":"La mise minimum par ligne pour ce pari est @minStakePerLine \u20ac","The minimum stake per line for outcome @outcomeName is @minStakePerLine \u20ac, for event @eventName":"La mise minimum pour @outcomeName est @minStakePerLine \u20ac, pour l\u0027\u0026eacute;v\u0026eacute;nement @eventName","The minimum stake for @betType is @minStakePerLine \u20ac":"La mise minimum pour @betType est de @minStakePerLine \u20ac","Selections":"S\u00e9lections","Selection":"S\u00e9lection","REMAINING_BETS":"Paris Restants","OBET_BETSLIP_SINGLE":"Single","You just placed your @placedBetType bet. You also have @notPlacedBetsType bets remaining. Would you like to preserve these?":"Vous venez de valider vos paris @placedBetType. Vous disposez \u00e9galement de paris @notPlacedBetsType en cours. Souhaitez vous conserver ces paris?","and":"et","freebet_low_stake_confirm":"Mise invalide: Les paris gratuits doivent \u00eatre utilis\u00e9s en entier et sur un seul pari. Veuillez augmenter votre mise pour pouvoir utiliser votre pari gratuit.","BETTING_NOT_ALLOWED":"Pari Non autoris\u00e9","OBET_BETSLIP_ERROR_BETTING_NOT_ALLOWED":"Si vous voyez ce message, une action est necesssaire de votre part pour pouvoir parier de nouveau : une suppression du cache de votre navigateur est necessaire.","Error with a selection":"Probl\u00e8me sur une s\u00e9lection","Betslip Error":"Information","Attention, the price of the selection @selectionName @hcapValue has changed from @oldPrice to @newPrice":"Attention, la cote de la s\u00e9lection @selectionName @hcapValue a chang\u00e9 de @oldPrice \u00e0 @newPrice","Credit my account":"Approvisionner mon compte","The account balance is insufficient":"Le solde de votre compte est insuffisant","JACKPOT_UNAVAILABLE":"Veuillez v\u00e9rifier que la cote de votre s\u00e9lection est sup\u00e9rieure \u00e0 1,10.","Jackpot unavailable":"Jackpot unavailable","This coupon is not valid":"Ce coupon n\u0027est pas valide","Combined bets are only possible from 2 selections":"Les paris Combin\u00e9s ne sont possibles qu\u2019\u00e0 partir de 2 s\u00e9lections"},"domain":".pmu.fr","date_default_timezone":{"value":"Europe\/Paris","offset":1},"current_page_path":"event\/666562","pmu_connect_session_url":"https:\/\/connect.awl.pmu.fr\/auth\/client\/2\/session","pmu_connect_pinpad_encryption_url":"https:\/\/connect.awl.pmu.fr\/auth\/client\/2\/session\/pinpad","load_more_url":"pservices\/more_events\/","gauge":{"is_bet_machine":false,"bet_machine_alias":"bet-machine","get_selections_url":"pmu\/gauge-get-selections","get_combinations_url":"pmu\/gauge-get-combinations","modal_params":{"warning":{"title":"Votre panier de paris contient des s\u00e9lections","content":"\n\u003Cdiv class=\u0022table table-favorites\u0022\u003E\n  \u003Cdiv class=\u0022col-sm-12\u0022\u003E\n    \u003Cdiv class=\u0022row\u0022\u003E\n      \u003Cdiv class=\u0022col-sm-12 text-xsmall\u0022\u003E\n        Au clic sur une s\u00e9lection dans la Bet Machine, il sera automatiquement r\u00e9initialise.\n        \u003Cdiv class=\u0022text-bold\u0022\u003E\n          Souhaitez-vous poursuivre?        \u003C\/div\u003E\n      \u003C\/div\u003E\n    \u003C\/div\u003E\n\n    \u003Cdiv class=\u0022row mt-20\u0022\u003E\n      \u003Cdiv class=\u0022col-sm-6 text-right\u0022\u003E\n        \u003Ca href=\u0022\/#pmu_gauge_continue\u0022 id=\u0022pmu_gauge_continue\u0022 class=\u0022btn btn-cta btn-orange ctools-close-modal\u0022\u003EContinuer\u003C\/a\u003E      \u003C\/div\u003E\n\n      \u003Cdiv class=\u0022col-sm-6\u0022\u003E\n        \u003Ca href=\u0022\/#pmu_gauge_cancel\u0022 id=\u0022pmu_gauge_cancel\u0022 class=\u0022btn btn-cta btn-orange ctools-close-modal\u0022\u003EAnnuler\u003C\/a\u003E      \u003C\/div\u003E\n    \u003C\/div\u003E\n  \u003C\/div\u003E\n\u003C\/div\u003E\n","style":"favourites"}}},"pathToTheme":"profiles\/core\/themes\/pmu_theme","pmu_market_sorts":{"expanded_selection_rows":3},"currentUser":0,"multibonus_grid":{"is_multibonus_grid":false,"mg_ambb_rewards":{"TBL":"0","ACC4":"5","ACC5":"7.5","ACC6":"10","ACC7":"15","ACC8":"20","ACC9":"25","AC10":"30","AC11":"35","AC12":"40","AC13":"45","AC14":"50","AC15":"75"},"combimax_rewards":["0","5","7.5","10","15","20","25","30","35","40","45","50","75"],"combimax_min_selections_teaser":"2","combimax_min_selections_upselling":"4"},"pmu_tag_commander":{"debug_mode":0,"marketing_id":"","user_logged":"non_identifie"},"ajax":{"edit-submit":{"callback":"simple_cookie_compliance_dismiss_form_submit","progress":{"type":"none"},"wrapper":"cookie-compliance","event":"mousedown","keypress":true,"prevent":"click","url":"\/system\/ajax","submit":{"_triggering_element_name":"op","_triggering_element_value":""}}},"pmu_fantasy_league":{"is_fantasy_league":false,"refresh_balance_timer":"30000"},"pmu_jackpot":{"is_jackpot":false,"multipliers_images":{"1":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x1_0.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner.gif"},"2":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x2.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_0.gif"},"5":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x5.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_1.gif"},"10":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x10.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_2.gif"},"15":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x15.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_3.gif"},"20":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x20.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_4.gif"},"25":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x25.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_5.gif"},"30":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x30.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_6.gif"},"35":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x35.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_7.gif"},"40":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x40.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_8.gif"},"45":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x45.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_9.gif"},"50":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x50.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_10.gif"},"55":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x55.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_11.gif"},"60":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x60.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_12.gif"},"65":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x65_0.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_13.gif"},"70":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x70.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_14.gif"},"75":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x75.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_15.gif"},"80":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x80.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_16.gif"},"85":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x85.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_17.gif"},"90":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x90.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_18.gif"},"95":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x95.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_19.gif"},"100":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x100.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_20.gif"},"1000":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x1000.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner_21.gif"},"default":{"value":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/values\/x1_0.png","spinner":"https:\/\/paris-sportifs.pmu.fr\/sites\/default\/files\/multipliers\/spinners\/spinner.gif"}},"jackpot_stake_percentage":"10","spinner_display_time":"5000"},"pmu_notifications":{"acknowledge_url":"notifications\/acknowledge\/"},"bootstrap":{"anchorsFix":0,"anchorsSmoothScrolling":1,"formHasError":1,"popoverEnabled":1,"popoverOptions":{"animation":1,"html":0,"placement":"right","selector":"","trigger":"click","triggerAutoclose":1,"title":"","content":"","delay":0,"container":"body"},"tooltipEnabled":1,"tooltipOptions":{"animation":1,"html":0,"placement":"auto left","selector":"","trigger":"hover focus","delay":0,"container":"body"}}});</script>
  
        <span id="device-xs" class="visible-xs"></span>
        <span id="device-sm" class="visible-sm"></span>
        <span id="device-md" class="visible-md"></span>
        <span id="device-lg" class="visible-lg"></span><script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_TPMR84fGVZX9kGjXU8cyjw-VaehccXOc8w9cx7SahCk.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_09P-iwsAdf6Gvj_skDKyqm9jkXWeKt3-v4dt-RWJbDQ.js"></script>
<script src="https://paris-sportifs.pmu.fr/sites/default/files/js/js_ixdT0s7Wa_gytjQPy4MbkWSuyCbVe9lAu8FEzh8IKJE.js"></script>
  
<a href="#" id="popin-logout-warning-open" class="overlay-trigger" data-target-name=".popin-logout-warning" data-action="open"></a>
<aside class="popin-logout-warning">

  <header class="popin--header popin--header-orange">
    <div class="row">
      <div class="col-sm-10">
        <h6>Confirmation prise de pari</h6>
      </div>
      <div class="col-sm-2">
        <a href="#" class="overlay-trigger close-anchor" data-target-name=".popin-logout-warning" data-action="close"><span class="glyphicon glyphicon-pmu-close"></span></a>
      </div>
    </div>
  </header>

  <div class="popin--content mt-20">

    <div class="row">
      <div class="col-sm-12">
        <p>You will be logged out in <span id="remaining_seconds_to_logout"></span> seconds.</p>
      </div>
    </div>


    <div class="table mt-15 pixel-fix">
      <div class="table--row-100">
        <div class="table--row-no-border">
          <a href="#" class="logout-warning-background-refresh">
            <div class="btn btn-cta btn-small btn-centered-block btn-orange">Refresh</div>
          </a>
        </div>
      </div>
    </div>

  </div>
</aside>
  <img id="back-to-top" data-toggle="tooltip" data-placement="left" class="img-responsive" src="https://paris-sportifs.pmu.fr/profiles/core/themes/pmu_theme/resources/public/fleche.png?time=1579015308" alt="Revenir en haut de la page" title="Revenir en haut de la page" /></body>
</html>"""


class SimplePageTest(unittest.TestCase):
    """ Test to parse the simple html page below"""

    def test_parse(self):
        """ Tests the function to compute the depth of the page """
        try:
            tree = build_html_tree(TEST_PAGE)
        except Exception:
            print(Exception)
        except:
            print("genereic error")
        depth = tree.depth()
        self.assertEqual(depth, 205)
        nodes = tree.get_element_by_attribute("dataname-", '"sportif.clic.parier.sports.competition.match.cote"')
        for i in nodes:
            print(i.content)

if __name__ == '__main__':
    unittest.main()

