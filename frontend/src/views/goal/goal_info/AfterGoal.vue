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

        <v-row justify="center">
          <v-col cols="8">
            <h2 class="category-title">
              Success criteria
            </h2>
          </v-col>
        </v-row>

        <v-row justify="center">
          <v-col cols="8">
            <p class="writing-text">
              Developed in Django and Vue.js. It has a login feature. Make sure
              it is usable on the net without any problems.
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

.category-title {
  /* font-family: Roboto; */
  background: rgb(128, 128, 128);
  border-radius: 25px;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #f0f0f0;
  /* padding-bottom: 15px; */
}

/* .span-arrow {
  width: 30px;
  height: 30px;
  font-size: 30px;
  color: rgb(102, 102, 102);
} */
</style>
