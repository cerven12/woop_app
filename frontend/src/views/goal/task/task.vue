<template>
  <div>
    <div id="css-grid">
      <!-- 難しさと満足度はVuetifyのRatingを使うとよいかも　https://vuetifyjs.com/en/components/ratings/ -->

      <v-container fluid id="view-area">
        <!-- Vew Goal Title -->
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10">
            <h1 class="message-title">
              Task Kanban Flow
            </h1>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="3">
            <div class="board">1</div>
          </v-col>
          <v-col cols="3">
            <div class="board">2</div>
          </v-col>
          <v-col cols="3">
            <div class="board">3</div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {};
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
  color: #4d4d4d;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  /* line-height: 1.6; */
  /* letter-spacing: 0.05em; */
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.content-splitter {
  border-block-end: solid 1px #c5c5c5;
  /* padding-bottom: 5px; */
}

.board {
  padding: 180px;
  margin: 50px;
  border: solid 1px gray;
  border-radius: 50px;
}
</style>
