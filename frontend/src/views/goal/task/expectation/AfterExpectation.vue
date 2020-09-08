<template>
  <div>
    <br /><br />
    <!-- <h1 class="message&#45;title">Expectation</h1> -->
    <v-row>
      <v-col cols="7" lg="8" md="9" sm="11">
        <h2 class="message-title">
          Let's compare satisfaction and difficulty.
        </h2>
      </v-col>
    </v-row>

    <div v-for="ex in Expectations" :key="ex.id">
      <div id="css-grid-title">
        <div id="p-nav">
            <span><v-btn icon large><v-icon x-large>navigate_before</v-icon></v-btn></span>
            <span><v-btn icon large><v-icon x-large>navigate_next</v-icon></v-btn></span>
        </div>
        <div id="ex">
          <h2 class="category-title zero-margin">Prediction</h2>
          <v-chip class="zero-margin">{{
            ex.created_at | dateDelimiter
          }}</v-chip>
        </div>
        <div id="act">
          <h2 class="category-title zero-margin">Result</h2>
          <v-chip class="zero-margin">{{
            ex.finished_at | dateDelimiter
          }}</v-chip>
        </div>
      </div>
    </div>
    <br />


    <div id="css-grid">
        <h1 id="title-satis" class="category-title">
          <v-icon>sentiment_satisfied_alt</v-icon>Satisfaction
        </h1>

        <div id="exsatis">
            <div v-for="ex in Expectations" :key="ex.id">
              <!-- The API gets it in increments of 20, so it should be corrected to 1-5. -->
              <v-rating
                v-bind="conversionSatisValue(ex.tbd_satisfaction)"
                v-model="tbdSatisRating"
                empty-icon="●"
                full-icon="☺"
                size="35"
                color="red lighten-3"
                background-color="grey lighten-2"
                readonly="true"
              ></v-rating>
              <p style="witdh: 80%;">{{ ex.tbd_satis_comment }}</p>
          </div>
        </div>

        <div id="actsatis">
            <div v-for="ex in Expectations" :key="ex.id">
              <!-- The API gets it in increments of 20, so it should be corrected to 1-5. -->
              <v-rating
                v-bind="conversionSatisValueAct(ex.satisfaction)"
                v-model="tbdSatisActRating"
                empty-icon="●"
                full-icon="☺"
                size="35"
                color="red lighten-3"
                background-color="grey lighten-2"
                readonly="true"
              ></v-rating>
              <p style="witdh: 80%;">{{ ex.satis_comment }}</p>
          </div>
        </div>
      </div>

    <div id="css-grid2">
        <h1 id="title-diff" class="category-title">
          <v-icon>filter_hdr</v-icon>Difficulty
        </h1>

        <div id="exdiff">
            <div v-for="diff in Expectations" :key="diff.id">
              <v-rating
                v-bind="conversionDiffValue(diff.tbd_difficulty)"
                v-model="tbdDiffRating"
                empty-icon="▲"
                full-icon="🌋"
                size="35"
                color="red lighten-3"
                background-color="grey lighten-2"
                readonly="true"
              >
              </v-rating>
              <p style="witdh: 80%;">{{ diff.tbd_diff_comment }}</p>
          </div>
        </div>

        <div id="actdiff">
            <div v-for="diff in Expectations" :key="diff.id">
              <v-rating
                v-bind="conversionDiffValueAct(diff.difficulty)"
                v-model="tbdDiffActRating"
                empty-icon="▲"
                full-icon="🌋"
                size="35"
                color="red lighten-3"
                background-color="grey lighten-2"
                readonly="true"
              >
              </v-rating>
              <p style="witdh: 80%;">{{ diff.diff_comment }}</p>
            </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Task",
  props: ["Expectations"],
  data: () => ({
    tbdSatisRating: 0,
    tbdSatisActRating: 0,
    tbdDiffRating: 0,
    tbdDiffActRating: 0
  }),
  filters: {
    dateDelimiter: function (value) {
      let date = new Date(value);
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let dt = date.getDate();

      if (dt < 10) {
        dt = "0" + dt;
      }
      if (month < 10) {
        month = "0" + month;
      }
      return year + "-" + month + "-" + dt;
    }
  },
  methods: {
    conversionSatisValue: function (value) {
      if (value == 20) {
        this.tbdSatisRating = 1;
      }
      if (value == 40) {
        this.tbdSatisRating = 2;
      }
      if (value == 60) {
        this.tbdSatisRating = 3;
      }
      if (value == 80) {
        this.tbdSatisRating = 4;
      }
      if (value == 100) {
        this.tbdSatisRating = 5;
      }
    },
    conversionSatisValueAct: function (value) {
      if (value == 20) {
        this.tbdSatisActRating = 1;
      }
      if (value == 40) {
        this.tbdSatisActRating = 2;
      }
      if (value == 60) {
        this.tbdSatisActRating = 3;
      }
      if (value == 80) {
        this.tbdSatisActRating = 4;
      }
      if (value == 100) {
        this.tbdSatisActRating = 5;
      }
    },
    conversionDiffValue: function (value) {
      if (value == 20) {
        this.tbdDiffRating = 1;
      }
      if (value == 40) {
        this.tbdDiffRating = 2;
      }
      if (value == 60) {
        this.tbdDiffRating = 3;
      }
      if (value == 80) {
        this.tbdDiffRating = 4;
      }
      if (value == 100) {
        this.tbdDiffRating = 5;
      }
    },
    conversionDiffValueAct: function (value) {
      if (value == 20) {
        this.tbdDiffActRating = 1;
      }
      if (value == 40) {
        this.tbdDiffActRating = 2;
      }
      if (value == 60) {
        this.tbdDiffActRating = 3;
      }
      if (value == 80) {
        this.tbdDiffActRating = 4;
      }
      if (value == 100) {
        this.tbdDiffActRating = 5;
      }
    }
  }
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS    rid
 ------------------------------------------------------------*/

#css-grid-title {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 20% 40% 40%;
  grid-template-areas: "p-nav  ex  act";
  justify-items: center;
  align-items: center;
  margin: 25px 0px 0px 25px;
  padding: 30px 0px 0px 30px;
    justify-items: center;

}
#p-nav {
  grid-area: p-nav;
}
#ex {
  grid-area: ex;
}
#act {
  grid-area: act;
}

#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 20% 40% 40%;
  grid-template-areas: "title-satis exsatis actsatis";
  align-items: center;
  margin: 15px 0px 15px 20px;
  border-top: solid 1px #e0e0e0;
  padding: 20px 0px 20px 30px;
  justify-items: start;
}
#title-satis {
  grid-area: title-satis;
}

#exsatis {
  grid-area: exsatis;
  padding: 0px 70px;
}

#actsatis {
  grid-area: actsatis;
  padding: 0px 20px;
}

#css-grid2 {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 20% 40% 40%;
  grid-template-areas: "title-diff exdiff actdiff";
  align-items: center;
  margin: 15px 0px 15px 20px;
  padding: 20px 0px 20px 30px;
  background: #e6e6e6;
  border-radius: 20px;
    justify-items: start;

}
#title-diff {
  grid-area: title-diff;
}
#exdiff {
  grid-area: exdiff;
  padding: 0px 70px;
}
#actdiff {
  grid-area: actdiff;
  padding: 0px 20px;
}






@media all and (max-width: 960px) {
  .category-title {
    font-size: 18px;
  }

  #css-grid-title {
    grid-template-columns: 10% 45% 45%;
    margin: 20px 0px 0px 20px;
    padding: 30px 0px 0px 30px;
  }

  #css-grid {
    grid-template-columns: 10% 45% 45%;
    margin: 10px 0px 10px 20px;
    padding: 20px 0px 20px 30px;
  }

  #css-grid2 {
    grid-template-columns: 10% 45% 45%;
    margin: 10px 0px 10px 20px;
    padding: 20px 0px 20px 30px;
  }
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
  color: #088dda;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  color: #292929;
  line-height: 40px;
  font-weight: normal;
  font-style: normal;
}

.sub-title {
  font-family: Roboto;
  font-size: 18px;
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.back {
  background: #f0f0f0;
}

.goal-title {
  font-style: normal;
  font-weight: normal;
  color: #4465c0;
  padding: 30px 0px;
}
.zero-margin {
  margin: 0;
}

@media all and (max-width: 960px) {
  .category-title {
    font-size: 18px;
  }
}
</style>
