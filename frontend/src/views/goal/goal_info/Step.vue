<template>
  <div>
    <div class="step">
      <div class="powerline" style="z-index: 10">
        <div class="rectangle" style="background: #f0f0f0;">
          Stady of how to use django 👾👾👾
        </div>
        <div class="triangle" style="border-left: 50px solid #f0f0f0;"></div>
      </div>
      <div class="powerline" style="z-index: 9">
        <div class="rectangle" style="background: #f0f0f0;">
          Create Api with Django Rest Framework 👾👾
        </div>
        <div class="triangle" style="border-left: 50px solid #f0f0f0;"></div>
      </div>

      <div class="powerline" style="z-index: 8">
        <div class="rectangle" style="color: #f0f0f0;">
          Stady of how to use Vue.js.👾👾👾
        </div>
        <div class="triangle"></div>
      </div>

      <div class="powerline" style="z-index: 7">
        <div class="rectangle" style="background: #f0f0f0;">
          Stady of how to use django.👾👾👾
        </div>
        <div class="triangle" style="border-left: 50px solid #f0f0f0;"></div>
      </div>

      <div class="powerline" style="z-index: 6">
        <div class="rectangle" style="background: #f0f0f0;">
          Stady of how to use django.👾👾👾
        </div>
        <div class="triangle" style="border-left: 50px solid #f0f0f0;"></div>
      </div>
    </div>
  </div>
</template>

<script></script>

<style scoped>
.step {
  position: relative;
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  padding: 5px;
}

.powerline {
  display: inline-block;
  position: relative;
  filter: drop-shadow(0px 1px 1px rgba(70, 70, 70, 0.6));
  height: 100px;
}

.rectangle {
  /* width: 0;
  height: 0; */
  width: 260px;
  height: 80px;
  background: #4465c0;
  display: inline-block;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  padding: 10px 0px 20px 60px;
  font-size: 18px;
  color: rgb(43, 43, 43);
}

.triangle {
  /* width: 0;
  height: 0; */
  border-top: 40px solid transparent;
  border-bottom: 40px solid transparent;
  border-left: 50px solid #4465c0;
  display: inline-block;
  position: absolute;
}

::-webkit-scrollbar {
  display: none;
}
</style>
