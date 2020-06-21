<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <!-- Vew Goal Title -->
        <v-row justify="center">
          <v-col cols="8">
            <h1 class="goal_title">
              Create Web SPA Todo App at use Django Rest Framework and Vue.
            </h1>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8">
            <p class="writing-text">
              A task management app that incorporates the Woop concept. When you
              set goals, it asks various questions to motivate you and prevent
              setbacks. Set small goals (tasks) to reach your goals and complete
              them one by one.A task management app that incorporates the Woop
              concept. When you set goals, it asks various questions to motivate
              you and prevent setbacks. Set small goals (tasks) to reach your
              goals and complete them one by one.
            </p>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 100%;
  grid-template-areas: "view";
  background-color: #f0f0f0;
}

#view-area {
  grid-area: view;
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.goal_title {
  color: #4465c0;
  font-style: normal;
  font-weight: normal;
  font-size: 50px;
  line-height: 56px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 1.6;
  color: #292929;
  /* letter-spacing: 0.05em; */
}
</style>
