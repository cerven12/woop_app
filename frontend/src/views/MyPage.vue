<template>
  <div>
    <div id="css-grid">
      <div id="goals-area">
        <h1>My Page</h1>
        <pre style="font-size:10px;">{{ Goals }}</pre>

        <div v-for="(goal, index) in Goals" :key="index">
          <nav>
            <router-link
              :to="{ name: 'goal', params: { id: goal.goal_id } }"
              >{{ goal.goal_title }}</router-link
            >
          </nav>
        </div>
      </div>
    </div>
    <div id="tasks-area">sas</div>
    <div id="memos-area">adadff</div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  components: {},
  data: function () {
    return {
      Goals: {},
      test: ""
    };
  },
  methods: {
  },
  mounted: function () {
    let vm = this;
    // goalの小モデルの情報は取得しないAPIを作成し、それを使ったほうが省エネになりそう
    api.get("goals/").then(function (responce) {
      vm.Goals = responce.data;
    });
  }
};
</script>

<style>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 800px 100px 100px;
  grid-template-areas: "goals tasks memos";
}

#goals-area {
  grid-area: goals;
}
#tasks-area {
  grid-area: tasks;
  background: blue;
}
#memos-area {
  grid-area: memos;
  background: yellow;
}
</style>
