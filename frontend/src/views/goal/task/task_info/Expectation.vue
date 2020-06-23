<template>
  <div>
    <h1 class="category-title">Expectation</h1>

    <div id="css-grid">
      <div id="satisfaction">
        <v-container>
          <v-row>
            <v-col cols="12">
              <h1 class="sub-title">Satisfaction</h1>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <h1>😩😩😩😩😩</h1>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <p>Because I think we can all do it.</p>
            </v-col>
          </v-row>
        </v-container>
      </div>

      <div id="difficlut">
        <v-container>
          <v-row>
            <v-col cols="12">
              <h1 class="sub-title">Difficlut</h1>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <h1>🌋🌋🌋🌋🌋</h1>
            </v-col>
          </v-row>

          <v-row>
            <v-spacer></v-spacer>
            <v-col cols="9">
              <p>
                There's a lot of knowledge that we know, so it's going to be
                pretty quick. I'll use the books I have on hand for hints.
              </p>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({}),
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
  grid-template-areas: "satisfaction difficlut";
}

#satisfaction {
  grid-area: satisfaction;
}

#difficlut {
  grid-area: difficlut;
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
  color: #24a5f0;
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
  color: #666666;
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
