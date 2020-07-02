<template>
  <div>
    <v-row>
      <v-col cols="12">
        <h1 class="message-title"><slot name="task_title"></slot></h1>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <p class="writing-text"><slot name="task_description"></slot></p>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="3">
        <div class="sub-title">
          <h2>Success criteria</h2>
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <p class="writing-text"><slot name="criteria"></slot></p>
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
  color: #088dda;
}

.category-title {
  font-size: 24px;
  /* text-align: center; */
  line-height: 30px;
  color: #292929;
}

.sub-title {
  font-size: 16px;
  /* text-align: center; */
  line-height: 30px;
  color: #292929;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #292929;
  margin-block-end: 0em;
}
</style>
