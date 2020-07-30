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

              <v-dialog v-model="addBoardDialog" width="400" persistent>
                <template v-slot:activator="{ on, attrs }">
                  <span v-bind="attrs" v-on="on">+</span>
                </template>
                <v-card style="border-radius: 25px; padding: 20px;">
                  <v-card-title style="font-weight: 500;"
                    >Borad Title & Color</v-card-title
                  >

                  <v-card-text>
                    <v-container>
                      <v-row>
                        <v-col cols="12">
                          <v-text-field
                            label="Title*"
                            required
                            v-model="boardTitle"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="12" sm="12">
                          <v-color-picker
                            v-model="showColor"
                            show-swatches
                            flat
                          ></v-color-picker>
                        </v-col>
                      </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                  </v-card-text>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="red" text @click="addBoardDialog = false"
                      >Disagree</v-btn
                    >
                    <v-btn
                      color="blue"
                      text
                      @click="
                        addBoardDialog = false;
                        addBoard(boardTitle, showColor);
                      "
                      >Agree</v-btn
                    >
                  </v-card-actions>
                </v-card>
              </v-dialog>
            </h1>
          </v-col>
        </v-row>
        <!-- -----------------------     -------------------- -->
        <!--                      Kanban                      -->
        <!-- -----------------------     -------------------- -->
        {{ Boards }}
        <v-row justify="center">
          <v-col cols="8" lg="8" md="9" sm="12">
            <div class="scrolling-wrapper">
              <div v-for="(board, index) in Boards.boards" :key="board.id">
                <div class="board-wrapper">
                  <h2 class="board-title">
                    <div
                      @click.stop="clickBoardTitle(board, index)"
                      style="display: inline;"
                    >
                      {{ board.board_title }}
                    </div>
                    <span> + </span>
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

        <v-dialog v-model="editBoardDialog" width="400" persistent>
          <v-card style="border-radius: 25px; padding: 20px;">
            <v-card-title style="font-weight: 500;"
              >Change Borad Title & Color</v-card-title
            >
            {{ currentBoard }}
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      label="Title*"
                      required
                      v-model="currentBoard.board_title"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12">
                    <v-color-picker
                      show-swatches
                      flat
                      v-model="currentBoard.color"
                    ></v-color-picker>
                  </v-col>
                </v-row>
              </v-container>
              <small>*indicates required field</small>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="red" text @click="editBoardDialog = false"
                >Disagree</v-btn
              >
              <v-btn
                color="blue"
                text
                @click="
                  editBoardDialog = false;
                  editBoard(
                    currentBoard.board_title,
                    currentBoard.color,
                    currentBoard.id,
                    currentIndex
                  );
                "
                >Agree</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
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
import api from "@/services/api";

export default {
  name: "Goal",
  props: ["Boards"],
  name: "dnd",
  components: { draggable, Task },
  data() {
    return {
      dialog: false,
      addBoardDialog: false,
      editBoardDialog: false,
      boardTitle: "",
      showColor: "#4465c0",
      currentBoard: {},
      currentIndex: "",
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
      const color = this.Boards.boards[index].color;
      if (color.slice(0, 1) == "#") {
        return `background: ${this.Boards.boards[index].color}`;
      } else {
        return `background: #${this.Boards.boards[index].color}`;
      }
    },
    addBoard(title, color) {
      const data = {
        goal: this.$route.params.id,
        board_title: title,
        color: color,
        tasks: []
      };
      this.Boards.boards.push(data);
      this.boardTitle = "";
      this.showColor = "#4465c0";
    },
    editBoard(title, color, id, index) {
      const vm = this;
      let goalId = this.$route.params.id;
      api
        .patch(
          `goals/${goalId}/boards/${id}/`,
          {
            board_title: title,
            color: color
          },
          { useCredentails: true }
        )
        .then(function (response) {
          // Overwrite the data in the changed part.
          // Use `splice` to reflect it immediately.
          vm.Boards.boards.splice(index, 1, response.data);
          vm.editBoardDialog = false;
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    clickBoardTitle(board, index) {
      this.$set(this.currentBoard, "board_title", board.board_title);
      this.$set(this.currentBoard, "color", board.color);
      this.$set(this.currentBoard, "id", board.board_id);
      this.currentIndex = index;
      this.editBoardDialog = true;
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
