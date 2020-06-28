<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="message-title">
              To Keep Your Motivation Flying High.
            </h2>
          </v-col>
        </v-row>

        <!----------------------------------------------------------------------->
        <!--                             Motivation                            -->
        <!----------------------------------------------------------------------->
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="category-title ">
              Motivation
            </h2>
          </v-col>
        </v-row>

        <div v-for="motive in motiveList" :key="motive.id">
          <v-row>
            <v-col cols="3"></v-col>
            <v-col cols="7">
              <p class="writing-text motive-splitter">
                {{ motive }}
              </p>
            </v-col>
          </v-row>
        </div>
        <br />
        <!----------------------------------------------------------------------->
        <!--                         Self Transcendens                   -->
        <!----------------------------------------------------------------------->
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="category-title">
              Self Transcendence
            </h2>
          </v-col>
        </v-row>

        <div
          v-for="selfTrance in selfTranscendenceGoalList"
          :key="selfTrance.id"
        >
          <v-row>
            <v-col cols="3"></v-col>
            <v-col cols="7">
              <p class="writing-text selftrance-splitter">
                {{ selfTrance }}
              </p>
            </v-col>
          </v-row>
        </div>
        <br />
        <!----------------------------------------------------------------------->
        <!--                             Future Self                          -->
        <!----------------------------------------------------------------------->
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="category-title">
              Bad Future Self
            </h2>
          </v-col>
        </v-row>

        <div v-for="futureSelf in futureSelfList" :key="futureSelf.id">
          <v-row>
            <v-col cols="3"></v-col>
            <v-col cols="7">
              <p class="writing-text future-splitter">
                {{ futureSelf }}
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
  data: function() {
    return {
      root: "",
      valid: "",
      form: "",
      // Registration details of Three Models
      motiveList: [
        'Refactor" redirects here. For the use of "refactor" on Wikipedia, see Wikipedia:Refactoring talk pages.',
        "This article is about a behaviour-preserving change. It is not to be confused with Rewrite (programming).",
        "In computer programming and software design, code refactoring is the process of restructuring existing computer code—changing the factoring—without changing its external behavior.",
      ],
      selfTranscendenceGoalList: [
        "intended to improve the design, structure, and/or implementation of the software (its non-functional attributes), while preserving its functionality.",
        "If done poorly, it may fail the requirement that external functionality not be changed, introduce new bugs, or both.",
      ],
      futureSelfList: [
        "Refactoring is usually motivated by noticing a code smell.",
        "For example, the method at hand may be very long, or it may be a near duplicate of another nearby method.",
      ],
    };
  },
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
  border-left: 20px rgb(28, 218, 174) solid;
  padding-left: 15px;
}

.selftrance-splitter {
  border-left: 20px rgb(239, 106, 148) solid;
  padding-left: 15px;
}

.future-splitter {
  border-left: 20px rgb(75, 75, 75) solid;
  padding-left: 15px;
}

.kakoi {
  border: rgb(41, 41, 41) solid 1px;
}
</style>
