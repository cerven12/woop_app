<template>
  <div id="schedule" class="input_group">
    <v-form v-model="valid">
      <v-container
        ><v-btn @click="toggle">toggle</v-btn>
        <!--  Schedule Registerd -->
        <template v-if="rq">
          <h2>▶　スケジュールを組もう</h2>
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
          <v-btn outlined @click="scheduleRegister(start_date, deadline_date)"
            >登録！</v-btn
          ></template
        >
        <!--  Schedule Registerd  / -->
        <!-- Before Schedule Register -->
        <template v-else
          ><h2>▶　スケジュールを組もう</h2>
          start : {{ start_date }} deadline : {{ deadline_date }}
        </template>
        <!-- Before Schedule Register  / -->
      </v-container>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id"],

  data: function() {
    return {
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: "http://127.0.0.1:8000/api/v1/goals/",
      rq: true,
    };
  },
  methods: {
    toggle: function() {
      if (this.rq === true) {
        this.rq = false;
      } else {
        this, (this.rq = true);
      }
    },
    scheduleRegister: function(start, dead) {
      const vm = this;
      vm.axios
        .patch(vm.url + vm.goal_id + "/", {
          start_date: start,
          deadline: dead,
        })
        .then((response) => (vm.this_time_goal_data = response.data))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.v-stepper {
  box-shadow: none;
}

#schedule {
  background-color: #f0f0f0;

  /* border: 1px black solid; */
  border-radius: 50px;
  padding: 40px 40px 40px 40px;
  margin: 40px 40px 40px 40px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);
  /*
  border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}

#schedule:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h2,
h3 {
  color: rgb(83, 83, 83);
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
