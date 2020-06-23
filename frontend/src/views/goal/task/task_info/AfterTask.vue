<template>
  <div>
    <v-row>
      <v-col cols="12">
        <h1 class="message-title"><slot></slot></h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <h1 class="writing-text ">
          A task management app that incorporates the Woop concept. When you set
          goals, it asks various questions to motivate you and prevent setbacks.
          Set small goals (tasks) to reach your goals and complete them one by
          one.A task management app that incorporates the Woop concept. When you
          set goals, it asks various questions to motivate you and prevent
          setbacks. Set small goals (tasks) to reach your goals and complete
          them one by one.
        </h1>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({}),
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #24a5f0;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
  padding-bottom: 15px;
}

.sub-title {
  font-family: Roboto;
  font-size: 18px;
  /* text-align: center; */
  line-height: 30px;
  color: #666666;
  padding-bottom: 15px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}
</style>
