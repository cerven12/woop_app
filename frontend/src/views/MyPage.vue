<template>
  <div>
    <div id="css-grid">
      <div id="goals-area">
        <v-container fluid>
          <v-row>
            <v-col cols="1"></v-col>
            <div class="scrolling-wrapper">
              <div class="circle">P</div>
              <div class="circle">S</div>
            </div>
          </v-row>

          <v-row justify="center">
            <v-col cols="1"></v-col>
            <v-col cols="10">
              <nav>
                <h1 class="yourgoal">
                  Your Goals<router-link :to="{ name: 'create' }">
                    <span>+</span></router-link
                  >
                </h1>
              </nav>
            </v-col>
          </v-row>

          <v-row>
            <v-col cols="1" lg="1" md="1" sm="1"></v-col>
            <v-col cols="8" lg="8" md="10" sm="11">
              <div v-for="(goal, index) in Goals" :key="index">
                <nav>
                  <router-link
                    :to="{ name: 'goal', params: { id: goal.goal_id } }"
                  >
                    <div class="goals-list">
                      {{ goal.goal_title }}
                    </div>
                  </router-link>
                </nav>
              </div>
            </v-col>
          </v-row>
        </v-container>
      </div>
      <div id="tasks-area"><v-container></v-container></div>
      <div id="memos-area"><v-container></v-container></div>
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  components: {},
  data: function () {
    return {
      Goals: {}
    };
  },
  methods: {},
  mounted: function () {
    let vm = this;
    // goalの小モデルの情報は取得しないAPIを作成し、それを使ったほうが省エネになりそう
    api.get("goals/").then(function (responce) {
      vm.Goals = responce.data;
    });
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 30% 35% 35%;
  grid-template-areas: "goals tasks memos";
}

@media all and (max-width: 10000px) {
  #css-grid {
    grid-template-rows: 50% 50%;
    grid-template-columns: 45% 55%;
    grid-template-areas:
      "goals tasks"
      "goals memos";
  }
  #tasks-area {
    grid-area: tasks;
    background: #56ccf2;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 80px 0px 0px 80px;
    position: relative;
    width: 200%;
    min-height: 950px;
  }

  #memos-area {
    grid-area: memos;
    background: #2d9cdb;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 80px 0px 0px 80px;
    position: relative;
  }
}

@media all and (max-width: 960px) {
  #css-grid {
    grid-template-rows: 40% 10% 50%;
    grid-template-columns: 100%;
    grid-template-areas:
      "goals"
      "tasks"
      "memos";
  }
  #tasks-area {
    grid-area: tasks;
    border-radius: 80px 80px 0px 0px;
    width: 100%;
  }
  #memos-area {
    grid-area: memos;
    border-radius: 80px 80px 0px 0px;
  }
}

#goals-area {
  grid-area: goals;
}

.goals-list {
  background: #f5f5f5;
  color: #4465c0;
  font-size: 20px;
  border-radius: 20px;
  width: 550px;
  min-height: 70px;
  padding: 25px 30px;
  margin: 25px 15px;
  font-weight: 700;
}
.goals-list:hover {
  box-shadow: 9px 7px 18px 2px rgba(0, 0, 0, 0.1);
}

a {
  text-decoration: none;
}

.yourgoal {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  /* font-size: 34px; */
  line-height: 40px;
  color: #404040;
  font-size: 34px;
}

.circle {
  display: inline-block;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: skyblue;
  text-align: center;
  line-height: 80px;
  font-size: 32px;
  color: #404040;
  flex: 0 0 auto;
  position: relative;
  overflow: scroll;
  margin: 20px;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.scrolling-wrapper {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
}
span {
  margin: 0px 15px;
  color: #404040;
}
</style>
