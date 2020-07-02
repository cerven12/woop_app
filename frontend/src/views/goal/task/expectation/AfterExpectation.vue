<template>
  <div>
    <h1 class="message-title">Expectation</h1>

    <div id="css-grid">
      <div id="satisfaction">
        <v-container>
          <v-row>
            <v-col cols="12">
              <h1 class="sub-title">Satisfaction</h1>
            </v-col>
          </v-row>

            <div v-for="ex in Expectations" :key="ex.id"> 
          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
            <template>
              <v-rating
                v-bind="conversionSatisValue(ex.tbd_satisfaction)"
                v-model="tbdSatisRating"
                empty-icon="●"
                full-icon="☺"
                size=32
                color='red lighten-3'
                background-color="grey lighten-2"
                readonly=true
              ></v-rating>
            </template>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <p>{{ ex.tbd_satis_comment }}</p>
            </v-col>
          </v-row>
         </div>
        </v-container>
      </div>

      <div id="difficulty">
        <v-container>
          <v-row>
            <v-col cols="12">
              <h1 class="sub-title">Difficulty</h1>
            </v-col>
          </v-row>

            <div v-for="diff in Expectations" :key="diff.id">
          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
            <template>
              <v-rating
                v-bind="conversionDiffValue(diff.tbd_difficulty)"
                v-model="tbdDiffRating"
                empty-icon="▲"
                full-icon="🌋"
                size=32
                color='red lighten-3'
                background-color="grey lighten-2"
                readonly=true>
              </v-rating>
            </template>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <p>{{ diff.tbd_diff_comment }} </p>
            </v-col>
          </v-row>
          </div>
        </v-container>
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
    tbdDiffRating: 0,
  }),
  methods:{
    conversionSatisValue: function(value){
      if (value == 20){this.tbdSatisRating = 1}
      if (value == 40){this.tbdSatisRating = 2}
      if (value == 60){this.tbdSatisRating = 3}
      if (value == 80){this.tbdSatisRating = 4}
      if (value == 100){this.tbdSatisRating = 5}
     },
    conversionDiffValue: function(value){
      if (value == 20){this.tbdDiffRating = 1}
      if (value == 40){this.tbdDiffRating = 2}
      if (value == 60){this.tbdDiffRating = 3}
      if (value == 80){this.tbdDiffRating = 4}
      if (value == 100){this.tbdDiffRating = 5}
     },

  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            CSS    rid
 ------------------------------------------------------------*/
#css-grid {
  display: grid;
  grid-template-rows: 1fr;
  grid-template-columns: 50% 50%;
  grid-template-areas: "satisfaction difficulty";
}

#satisfaction {
  grid-area: satisfaction;
}

#difficlut {
  grid-area: difficulty;
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
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
  padding-bottom: 15px;
}

.sub-title {
  font-family: Roboto;
  font-size: 18px;
  /* text-align: center; */
  line-height: 30px;
  color: #4d4d4d;
  padding-bottom: 15px;
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
</style>
