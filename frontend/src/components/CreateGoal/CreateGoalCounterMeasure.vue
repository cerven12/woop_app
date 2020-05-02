<template>
  <div>
    <div>
      <!--  worry and idea form -->
      <v-container>
        <v-row>
          <v-col cols="12">
            <h2>挫折をしないために準備する</h2>
          </v-col></v-row
        ></v-container
      >
      <div id="countermeasure" class="input_group">
        <CounterMeasureWorryIdea
          ref="child"
          :goal_id="goal_id"
          v-for="n in worryideacomponent"
          v-bind:key="n.id"
        ></CounterMeasureWorryIdea>
        <v-btn @click.prevent="worryideacomponent++">増やす</v-btn>
        <div>
          <!-- reference form -->
          <v-form v-model="valid">
            <v-container>
              <v-row>
                <v-col cols="4">
                  <v-text-field
                    label="資料"
                    hint="参考にしたい資料を前もって登録しておきましょう"
                    outlined
                  ></v-text-field>
                </v-col>
                <v-col cols="4">
                  <v-text-field
                    label="用途"
                    hint="この資料の用途を書きましょう"
                    outlined
                  ></v-text-field>
                </v-col>
                <v-col cols="4">
                  <v-text-field label="URL" 　outlined></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
              </v-row>
            </v-container>
          </v-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CounterMeasureWorryIdea from "./CounterMeasureWorryIdea.vue";

export default {
  name: "CreateGoal",
  props: ["goal_id"],
  components: {
    CounterMeasureWorryIdea,
  },

  data: function() {
    return {
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",
      worryideacomponent: 1,
    };
  },
  methods: {},
};
</script>

<style scoped>
#countermeasure {
  /* background: rgba(79, 79, 80, 0.288); */
  border-radius: 4px;
  padding: 20px;
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}
</style>
