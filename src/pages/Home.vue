<template lang="html">
<div id="home">
  <!-- TODO: landing page with search -->
  <section id="landing">
    <div class="black-opacity">
    <form action="#" id="home-form-search">
      <div class="mdl-textfield mdl-js-textfield">
        <input class="mdl-textfield__input" type="text" id="search_home" autofocus>
        <label class="mdl-textfield__label" for="search_home">Find recipe or ingredient..</label>
      </div>
      <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored">
        <i class="material-icons">search</i>
      </button>
    </form>
    </div>
  </section>

  <!-- TODO: most 6 favorites recipe -->
  <section>

  </section>
  <!-- TODO: following user recipes -->
  <!-- TODO: invite friend, facebook friends list -->
</div>
</template>

<style>
  section#landing {
    background-image: url('../../static/img/home_bg.jpg');
    background-size: cover;
    height: 600px;
    position: relative;
  }
  #home-form-search {
    width: 800px;
    position: absolute;
    top: 50%;
    left: 50%;
    margin-left: -400px;
  }
  #home-form-search .mdl-textfield {
    width: 730px;
  }
  .mdl-textfield__input {
    border-bottom: 2px solid rgba(255, 255, 255, .25)
  }
  #home-form-search input, #home-form-search label {
    color: #eee;
    font-size: 22px;
  }
  .black-opacity {
    background-color: rgba(0, 0, 0, .45);
    height: 100%;
  }
</style>