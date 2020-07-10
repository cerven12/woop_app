<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="message-title">Note <span>+</span></h2>
          </v-col>
        </v-row>
        <v-row> </v-row>

        <v-row>
          <v-col>
            <template>
              <div class="text-center">
                <v-pagination
                  v-model="page"
                  :length="6"
                  color="#4465c0"
                  circle
                ></v-pagination>
              </div>
            </template>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col cols="3"></v-col>
          <v-col cols="6">
            <div v-for="note in Notes.notes" :key="note.id">
          
              <Accordion>
                <div slot="source">
                  @task#23
                </div>
                <div slot="header">{{ note.note_title }}</div>
                <div slot="body">{{ note.note_main }}</div>
              </Accordion>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import Accordion from "../note/Accordion";

export default {
  name: "Goal",
  props: ["Notes"],

  components: {
    Accordion,
  },
  data: function() {
    return {
      start_date: "2019-01-06",
      deadline: "2019-05-08",
      page: 1,
      noteList: [],
    };
  },
  // mounted: function() {
  //   let vm = this;
  //   vm.noteList = vm.$store.state.goalData.notes;
  // },
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
  /* font-size: 34px; */
  line-height: 40px;
  color: #4465c0;
  font-size: 34px;
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
</style>
