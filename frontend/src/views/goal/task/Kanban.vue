<template>
  <div>
    <div id="css-grid">
      <!-- 難しさと満足度はVuetifyのRatingを使うとよいかも　https://vuetifyjs.com/en/components/ratings/ -->
      <v-container fluid id="view-area">
        <!-- Vew Goal Title -->
        <v-row>
          <v-col cols="10">
            <h1 class="message-title">
              Task Kanban Flow
            </h1>
          </v-col>
        </v-row>
        <!-- -----------------------     -------------------- -->
        <!--                      Kanban                      -->
        <!-- -----------------------     -------------------- -->
        <v-row>
          <div class="scrolling-wrapper">
            <div class="board-wrapper">
              <h2 class="board-title">Todo</h2>
              <div class="board">
                <draggable
                  v-model="itemsA"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsA" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Wait</h2>
              <div class="board">
                <draggable
                  v-model="itemsC"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsC" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <div class="board-wrapper">
              <h2 class="board-title">Success</h2>
              <div class="board">
                <draggable
                  v-model="itemsB"
                  group="myGroup"
                  @start="drag = true"
                  @end="drag = false"
                  :options="options"
                >
                  <div class="item" v-for="item in itemsB" :key="item.id">
                    <div>
                      <p class="text_position">
                        {{ item.name }}
                      </p>
                      <a class="task_status">☺ -2 -> ? 😩 4 -> ?</a>
                    </div>
                  </div>
                </draggable>
              </div>
            </div>

            <!--  -->
            <!--  -->
            <!--  -->
          </div>
        </v-row>
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
        { id: 1, name: "Add new icon." },
        { id: 2, name: "Design to UI, UX by UI create tool Figma. #57" },
        { id: 3, name: "Add new Buttom in a input form." },
        { id: 4, name: "name04" },
        { id: 1, name: "Add new icon." },
        { id: 2, name: "Design to UI, UX by UI create tool Figma. #57" },
        { id: 3, name: "Add new Buttom in a input form." },
        { id: 1, name: "Add new icon." },
        { id: 2, name: "Design to UI, UX by UI create tool Figma. #57" },
        { id: 3, name: "Add new Buttom in a input form." },
        { id: 1, name: "Add new icon." },
        { id: 2, name: "Design to UI, UX by UI create tool Figma. #57" },
        { id: 3, name: "Add new Buttom in a input form." },
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
        { id: 16, name: "name16" },
        { id: 17, name: "name17" },
        { id: 18, name: "name18" },
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
  /* adjust white space of Kanban to other component. */
  grid-template-columns: 16.5% 70%;
  grid-template-areas: "... view";
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
</style>
