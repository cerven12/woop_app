<template>
  <div>
    <div class="accordion" v-bind:class="theme">
      <div class="header" v-on:click="toggle">
        <slot name="header"></slot>
      </div>
      <transition
        name="accordion"
        v-on:before-enter="beforeEnter"
        v-on:enter="enter"
        v-on:before-leave="beforeLeave"
        v-on:leave="leave"
      >
        <div class="body" v-show="show">
          <div class="body-inner">
            <slot name="body"></slot>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  props: ["theme"],

  data() {
    return {
      show: false,
    };
  },

  methods: {
    toggle: function() {
      this.show = !this.show;
    },
    beforeEnter: function(el) {
      el.style.height = "0";
    },
    enter: function(el) {
      el.style.height = el.scrollHeight + "px";
    },
    beforeLeave: function(el) {
      el.style.height = el.scrollHeight + "px";
    },
    leave: function(el) {
      el.style.height = "0";
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Lato");

.accordion {
  max-width: auto;
  margin-bottom: 30px;
  background-color: #2d9cdb;
  border-radius: 27.5px;
}

.accordion .header {
  height: 90px;
  line-height: 70px;
  padding: 0 40px 0 30px;
  font-size: 24px;
  position: relative;
  color: rgb(241, 241, 241);
  cursor: pointer;
  z-index: 10;
}

.accordion .header-icon {
  position: absolute;
  top: 5px;
  right: 8px;
  transform: rotate(0deg);
  transition-duration: 0.3s;
}

.accordion .body {
  /*   display: none; */
  overflow: hidden;
  background-color: #f0f0f0;
  border-top: 0;
  border-bottom-left-radius: 6px;
  border-bottom-right-radius: 6px;
  transition: 150ms ease-out;
  border-radius: 27.5px;
  position: relative;
  z-index: 20;
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
  right: 3px;
  top: -3px;
}

.accordion .body-inner {
  padding: 40px 60px;
  overflow-wrap: break-word;
  /*   white-space: pre-wrap; */
}

.accordion .header-icon.rotate {
  transform: rotate(180deg);
  transition-duration: 0.3s;
}

.accordion.purple {
  background-color: #8c618d;
}

.accordion.purple .body {
  border-color: #8c618d;
}
</style>
