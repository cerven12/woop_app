<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row justify="center">
          <v-col cols="7" lg="7" md="8" sm="10">
            <h2 class="message-title">
              To Keep Your Motivation Flying High.
            </h2>
          </v-col>
          <v-col cols="1">
            <v-btn fab small depressed color="gray" @click="switchEdit">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-col>
        </v-row>

        <!----------------------------------------------------------------------->
        <!--                             Motivation                            -->
        <!----------------------------------------------------------------------->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <h2 class="category-title">
              Motivation
            </h2>
          </v-col>
        </v-row>

        <div v-for="motive in Motives.motives" :key="motive.id">
          <v-row>
            <v-col cols="3" lg="3" md="3" sm="1"></v-col>
            <v-col cols="7" lg="7" md="7" sm="10">
              <p class="writing-text motive-splitter">
                {{ motive.motive }}
              </p>
            </v-col>
          </v-row>
        </div>
        <br />
        <!----------------------------------------------------------------------->
        <!--                         Self Transcendens                   -->
        <!----------------------------------------------------------------------->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <h2 class="category-title">
              Self Transcendence
            </h2>
          </v-col>
        </v-row>
        <div
          v-for="selfTrance in SelfTranscendence.self_transcendence_goals"
          :key="selfTrance.id"
        >
          <v-row>
            <v-col cols="3" lg="3" md="3" sm="1"></v-col>
            <v-col cols="7" lg="7" md="7" sm="10">
              <p class="writing-text selftrance-splitter">
                {{ selfTrance.self_transcendence_goal }}
              </p>
            </v-col>
          </v-row>
        </div>
        <br />
        <!----------------------------------------------------------------------->
        <!--                             Future Self                          -->
        <!----------------------------------------------------------------------->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <h2 class="category-title">
              Bad Future Self
            </h2>
          </v-col>
        </v-row>
        <div
          v-for="futureSelf in FutureSelves.future_selves"
          :key="futureSelf.id"
        >
          <v-row>
            <v-col cols="3" lg="3" md="3" sm="1"></v-col>
            <v-col cols="7" lg="7" md="7" sm="10">
              <p class="writing-text future-splitter">
                {{ futureSelf.future_self }}
              </p>
            </v-col>
          </v-row>
        </div>
        <br />
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Goal",
  props: ["Motives", "SelfTranscendence", "FutureSelves"],

  data: function () {
    return {
      root: "",
      valid: "",
      form: ""
    };
  },
  methods: {
    switchEdit: function () {
      this.$emit("startMotiveEdit");
    }
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
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 34px;
  line-height: 40px;
  color: #4465c0;
}

.category-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  color: #292929;
  /* top: 20px; */
  padding-left: 50px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  /* line-height: 1.6; */
  /* letter-spacing: 0.05em; */
  font-kerning: nomal;
  color: rgb(41, 41, 41);
  margin-block-end: 0em;
}

.motive-splitter {
  border-left: 20px #3994bf solid;
  padding-left: 15px;
}

.selftrance-splitter {
  border-left: 20px rgb(239, 106, 148) solid;
  padding-left: 15px;
}

.future-splitter {
  border-left: 20px #794dbf solid;
  padding-left: 15px;
}

.kakoi {
  border: rgb(41, 41, 41) solid 1px;
}
</style>
