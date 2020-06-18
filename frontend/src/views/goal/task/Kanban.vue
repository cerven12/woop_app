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
        <!-- ------------------------------------------------ -->
        <v-row>
          <v-col cols="1"></v-col>

          <v-col cols="3">
            <div class="board">
              <h3 class="category-title">Todo</h3>
              <draggable
                v-model="itemsA"
                group="myGroup"
                @start="drag = true"
                @end="drag = false"
                :options="options"
              >
                <div class="item" v-for="item in itemsA" :key="item.id">
                  {{ item.name }}
                </div>
              </draggable>
            </div>
          </v-col>

          <v-col cols="3">
            <div class="board" style="background:#27AE60;">
              <h3 class="category-title">Success</h3>
              <draggable
                v-model="itemsB"
                group="myGroup"
                @start="drag = true"
                @end="drag = false"
                :options="options"
              >
                <div class="item" v-for="item in itemsB" :key="item.id">
                  {{ item.name }}
                </div>
              </draggable>
            </div>
          </v-col>

          <v-col cols="3">
            <div class="board" style="background:#828282;">
              <h3 class="category-title">Wait</h3>
              <draggable
                v-model="itemsC"
                group="myGroup"
                @start="drag = true"
                @end="drag = false"
                :options="options"
              >
                <div class="item" v-for="item in itemsC" :key="item.id">
                  {{ item.name }}
                </div>
              </draggable>
            </div>
          </v-col>
        </v-row>
        <!-- ------------------------------------------------ -->
      </v-container>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  name: "dnd",
  components: { draggable },
  data() {
    return {
      options: {
        animation: 200,
      },
      options: {
        group: "myGroup",
        animation: 200,
      },
      itemsA: [
        { id: 1, name: "name01" },
        { id: 2, name: "name02" },
        { id: 3, name: "name03" },
        { id: 4, name: "name04" },
        { id: 5, name: "name05" },
      ],
      itemsB: [
        { id: 6, name: "name06" },
        { id: 7, name: "name07" },
        { id: 8, name: "name08" },
        { id: 9, name: "name09" },
        { id: 10, name: "name10" },
      ],
      itemsC: [
        { id: 11, name: "name11" },
        { id: 12, name: "name12" },
        { id: 13, name: "name13" },
        { id: 14, name: "name14" },
        { id: 15, name: "name15" },
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
  font-size: 28px;
  line-height: 40px;
  color: #5f75b0;
}

.category-title {
  font-family: Roboto;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #ebebeb;
  padding-bottom: 15px;
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
  padding: 19px;
  margin: 20px;
  border-radius: 50px;
  background: #2d9cdb;
  position: relative;
}

.item {
  display: inline-block;
  margin-bottom: 15px;
  padding: 30px 130px;
  /* width: 30px; */
  border-radius: 25px;
  background-color: #f0f0f0;
  position: relative;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.25);

  /* box-shadow: 1px; */
}
.item:hover {
  cursor: grab;
}
.item:active {
  cursor: grabbing;
}
</style>
