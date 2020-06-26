<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row justify="center">
          <v-col cols="8">
            <div class="step">
              <div class="powerline" style="z-index: 10">
                <div class="rectangle" style="color: #f0f0f0;">
                  Stady of how to use django 👾👾👾
                </div>
                <div class="triangle"></div>
              </div>
              <div class="powerline" style="z-index: 9">
                <div class="rectangle" style="background: #f0f0f0;">
                  Create Api with Django Rest Framework 👾👾
                </div>
                <div
                  class="triangle"
                  style="border-left: 50px solid #f0f0f0;"
                ></div>
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
                <div
                  class="triangle"
                  style="border-left: 50px solid #f0f0f0;"
                ></div>
              </div>

              <div class="powerline" style="z-index: 6">
                <div class="rectangle" style="background: #f0f0f0;">
                  Stady of how to use django.👾👾👾
                </div>
                <div
                  class="triangle"
                  style="border-left: 50px solid #f0f0f0;"
                ></div>
              </div>
            </div>
          </v-col>
        </v-row>

        <v-row><v-col></v-col><v-col></v-col></v-row>
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
              <span>🔥</span> Developed in Django and Vue.js. It has a login
              feature. Make sure it is usable on the net without any problems.
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
  border-radius: 25px;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #3a3a3a;
}

.center {
  position: relative;
}

.step {
  position: relative;
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
}

.powerline {
  display: inline-block;
  position: relative;
  filter: drop-shadow(0px 3px 3px rgba(0, 0, 0, 0.6));
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
