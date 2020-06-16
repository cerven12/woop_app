<template>
  <div id="css-grid">
    <!----------------------------------------------------------------------->
    <!--                       Left Side "form"                         -->
    <!----------------------------------------------------------------------->
    <v-container fluid id="form-area">
      <div id="line">
        <v-form v-model="valid">
          <!--  Schedule Registerd -->
          <transition name="schedule" mode="out-in">
            <div>
              <h2 class="message-title">Schedule</h2>
              <v-row>
                <!----------------------------------------------------------------------->
                <!--                      Staer date calendar                     -->
                <!----------------------------------------------------------------------->
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
                        label="Start"
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

                <!----------------------------------------------------------------------->
                <!--                   Deadline date calendar                   -->
                <!----------------------------------------------------------------------->
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
                        label="Dead line"
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

              <v-btn
                outlined
                @click="scheduleRegister(start_date, deadline_date)"
              >
                登録！
              </v-btn>
            </div>
          </transition>
        </v-form>
      </div>
    </v-container>

    <v-container fluid id="tips-area">
      <h1>Tips</h1>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id", "token"],

  data: function() {
    return {
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      valid: "",
    };
  },
  methods: {},
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 55% 45%;
  grid-template-areas: "form tips";
  background-color: #f0f0f0;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

/*   ------------------------------------------------------------
                            Form Design
 ------------------------------------------------------------*/
#line {
  margin: 80px;
  padding: 60px 100px;
  border-radius: 77px;
  box-shadow: 5px 5px 5px #b9b9b9, -5px -5px 5px #fafafa;
}

/*   ------------------------------------------------------------
                            Transition
 ------------------------------------------------------------*/
.schedule-enter-active,
.schedule-leave-active {
  transition: opacity 0.3s;
}
.schedule-enter,
.schedule-leave-to {
  opacity: 0;
}

/*   ------------------------------------------------------------
                            Font Desiign
 ------------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 28px;
  line-height: 40px;
  color: #5f75b0;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 40px;
  color: #3c3d3d;
}
</style>
