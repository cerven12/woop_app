<template>
  <div id="schedule" class="input_group">
    <v-form v-model="valid">
      <v-container>
        <h2>スケジュールを組もう</h2>
        <v-row>
          <v-col cols="6" md="6">
            <v-menu
              ref="start"
              v-model="start"
              :close-on-content-click="false"
              :return-value.sync="start_date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="start_date"
                  label="開始日"
                  prepend-icon=""
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="start_date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="#37474F" @click="start = false"
                  >Cancel</v-btn
                >
                <v-btn
                  text
                  color="#37474F"
                  @click="$refs.start.save(start_date)"
                  >OK</v-btn
                >
              </v-date-picker>
            </v-menu>
          </v-col>

          <v-col cols="6" md="6">
            <v-menu
              ref="deadline"
              v-model="deadline"
              :close-on-content-click="false"
              :return-value.sync="deadline_date"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="deadline_date"
                  label="締め切り"
                  prepend-icon=""
                  readonly
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker v-model="deadline_date" no-title scrollable>
                <v-spacer></v-spacer>
                <v-btn text color="#37474F" @click="deadline = false"
                  >Cancel</v-btn
                >
                <v-btn
                  text
                  color="#37474F"
                  @click="$refs.deadline.save(deadline_date)"
                  >OK</v-btn
                >
              </v-date-picker>
            </v-menu>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
</template>
<script>
export default {
  name: "CreateGoal",

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
    };
  },
};
</script>

<style scoped>
.input_group {
  margin: 20px;
  transition: all 0.2s;
}

#motivation {
  /* background: rgba(105, 105, 105, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#countermeasure {
  /* background: rgba(79, 79, 80, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#goal {
  padding: 20px;
}
.v-stepper {
  box-shadow: none;
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
</style>
