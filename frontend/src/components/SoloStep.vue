<template>
  <div class="step">
    <div class="powerline" style="z-index: 10">
      <div class="rectangle">
        Stady of how to use django 👾👾👾
      </div>
      <div class="triangle"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.step {
  position: relative;
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  /* To keep the borders from sticking out. */
  padding: 10px;
}
.powerline {
  display: inline-block;
  position: relative;
  filter: drop-shadow(0px 1px 1px rgba(70, 70, 70, 0.6));
  height: 50px;
}

.rectangle {
  /* width: 0;
  height: 0; */
  width: 200px;
  height: 50px;
  background: #4465c0;
  display: inline-block;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
  padding: 5px 0px 20px 20px;
  font-size: 14px;
  font-style: nomal;
  font-kerning: nomal;

  color: rgb(234, 234, 234);
}

.triangle {
  /* width: 0;
  height: 0; */

  /* Border top & bottom is the upper and lower half parts. */
  border-top: 25px solid transparent;
  border-bottom: 25px solid transparent;

  border-left: 50px solid #4465c0;
  display: inline-block;
  position: absolute;
}
</style>
