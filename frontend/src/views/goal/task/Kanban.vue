<template>
  <div>
    <div id="css-grid">
      <!-- 難しさと満足度はVuetifyのRatingを使うとよいかも　https://vuetifyjs.com/en/components/ratings/ -->
      <v-container fluid id="view-area">
        <!-- Vew Goal Title -->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="11">
            <h1 class="message-title">
              Task Kanban Flow
            </h1>
          </v-col>
        </v-row>
        <!-- -----------------------     -------------------- -->
        <!--                      Kanban                      -->
        <!-- -----------------------     -------------------- -->
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <div class="scrolling-wrapper">
              <div v-for="(board, index) in Boards.boards" :key="board.id">
                <div class="board-wrapper">
                  <h2 class="board-title">
                    {{ board.board_title }}<span> + </span>
                  </h2>
                  <div class="board" :style="boardColor(index)">
                    <draggable
                      v-model="board.tasks"
                      group="myGroup"
                      @start="drag = true"
                      @end="drag = false"
                      :options="options"
                    >
                      <div
                        @click="showDialog(task)"
                        class="item"
                        v-for="task in board.tasks"
                        :key="task.id"
                      >
                        <p class="text_position">
                          {{ task.task_title }}
                        </p>
                        <a class="task_status">☺ → 😩 </a>
                      </div>
                    </draggable>
                  </div>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-container>

      <div class="text-xs-center">
        <Task :text="text" ref="task"></Task>
      </div>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import Task from "./Task";

export default {
  name: "Goal",
  props: ["Boards"],
  name: "dnd",
  components: { draggable, Task },
  data() {
    return {
      dialog: false,
      isClick: false,
      nowViewTask: "",
      options: {
        group: "myGroup",
        animation: 200
      }
    };
  },
  methods: {
    showDialog(item) {
      this.$refs.task.open();
      this.$refs.task.task_info = item;
    },
    boardColor(index) {
      return `background: #${this.Boards.boards[index].color}`;
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
  /* adjust white space of Kanban to other component. */
  grid-template-columns: 100%;
  grid-template-areas: " view";
  background-color: #f0f0f0;
  position: relative;
}

#view-area {
  grid-area: view;
  overflow: hidden;
  position: relative;
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
  font-kerning: nomal;
  color: #6d6d6d;
  margin-block-end: 0em;
}

.content-splitter {
  border-block-end: solid 1px #c5c5c5;
}

/*  */
/*  */
.scrolling-wrapper {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  position: relative;
}

::-webkit-scrollbar {
  display: none;
  -webkit-appearance: none;
}

.board-wrapper {
  position: relative;
}

.board {
  flex: 0 0 auto;
  overflow: scroll;
  height: 500px;
  width: 300px;
  margin: 20px;
  position: relative;
  background: #4465c0;
  padding: 0px 0px;
  border-radius: 25px;
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
}

.board-title {
  top: 0px;
  margin-left: auto;
  margin-right: auto;
  padding-top: 20px;

  font-family: Roboto;
  font-size: 24px;
  text-align: center;
  line-height: 30px;
  color: #444444;
}

.item {
  position: relative;
  /* border: solid purple 5px; */
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.25);
  margin: 20px 10px;
  padding: 20px;
  border-radius: 25px;
  background: #f0f0f0;
}

.item:hover {
  cursor: grab;
}
.item:active {
  cursor: grabbing;
}

.text_position {
  font-size: 18px;
  color: #292929;
  position: relative;
}

.task_status {
  line-height: 1em;
  padding-left: 50px;
  position: absolute;
  bottom: 5px;
  right: 20px;
}

/* -------------   --------------- */
/*           Over lay            */
/* -------------   --------------- */
.overlay-back {
  background: #f0f0f0;
  width: 1200px;
  border-radius: 50px;
  padding: 40px 60px;
  position: relative;
}
</style>
