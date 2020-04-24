/*
<template>
  <div>
    <v-app>
      <div id="back">
        <div id="goal" class="input_group">
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <h3>あなたが達成したい目標を書きましょう</h3>
              </v-col>
            </v-row>
            <v-row justify="start">
              <v-col cols="9"
                ><v-layout justify-end
                  ><h1>{{ goal_title }}</h1></v-layout
                >
              </v-col>
              <v-spacer></v-spacer>
              <v-col cols="2">
                <h2 v-show="new_goal_registered" id="check">
                  <v-icon x-large color="blue">mdi-check-bold</v-icon>
                </h2>
              </v-col>
            </v-row>
            <v-row>
              <v-col>
                <input
                  type="text"
                  v-model="goal_title"
                  style="border-bottom: 2px solid gray;"
                />
                <v-text-field
                  label="Solo"
                  placeholder="Placeholder"
                  solo
                  v-model="goal_title"
                ></v-text-field>
                <v-btn
                  class="ma-2"
                  outlined
                  color="black"
                  v-on:click="new_goal_register"
                  >登録</v-btn
                >
              </v-col>
            </v-row>
          </v-container>
        </div>

        <div id="step">
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-stepper alt-labels>
                  <v-stepper-header>
                    <v-stepper-step color="blue" complete step="1">
                      目標を決める
                    </v-stepper-step>
                    <v-divider></v-divider>
                    <v-stepper-step color="orange" complete step="2"
                      >モチベーションを高める</v-stepper-step
                    >
                    <v-divider></v-divider>
                    <v-stepper-step color="brown" complete step="3">
                      挫折をしないために準備する
                    </v-stepper-step>
                    <v-divider></v-divider>
                    <v-stepper-step color="green" complete step="4">
                      スケジュールを組もう
                    </v-stepper-step>
                  </v-stepper-header>
                </v-stepper>
              </v-col>
            </v-row>
          </v-container>
        </div>

        <div id="motivation" class="input_group">
          <v-form v-model="valid">
            <v-container>
              <v-row>
                <h2>モチベーションを高める</h2>
                <v-col cols="12" md="12">
                  <v-text-field
                    label="理由"
                    hint="目標を叶えたい理由を書きましょう"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
              </v-row>
            </v-container>
          </v-form>
          <div>
            <v-form v-model="valid">
              <v-container>
                <v-row>
                  <v-col cols="12" md="12">
                    <v-text-field
                      label="周囲への影響"
                      hint="目標を達成した時、周りの人々や環境にどのような良い影響が与えるか、想像してみてください"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row justify="end">
                  <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
                </v-row>
              </v-container>
            </v-form>
          </div>
          <div>
            <v-form v-model="valid">
              <v-container>
                <v-row>
                  <v-col cols="12" md="12">
                    <v-text-field
                      label="後悔"
                      hint="もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row justify="end">
                  <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
                </v-row>
              </v-container>
            </v-form>
          </div>
        </div>

        <div id="countermeasure" class="input_group">
          <v-form v-model="valid">
            <v-container>
              <h2>挫折をしないために準備する</h2>
              <v-row>
                <v-col cols="12" md="12">
                  <v-text-field
                    label="障壁"
                    hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col cols="2"><v-btn depressed small>＋</v-btn></v-col>
                <v-col cols="9">
                  <v-text-field
                    label="解決策"
                    hint="前もって障壁に対する解決策を考えておきましょう"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="end">
                <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
              </v-row>
            </v-container>
          </v-form>
          <div>
            <v-form v-model="valid">
              <v-container>
                <v-row>
                  <v-col cols="4">
                    <v-text-field
                      label="資料"
                      hint="参考にしたい資料を前もって登録しておきましょう"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      label="用途"
                      hint="この資料の用途を書きましょう"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field label="URL"></v-text-field>
                  </v-col>
                </v-row>
                <v-row justify="end">
                  <v-col cols="1"><v-btn depressed small>＋</v-btn></v-col>
                </v-row>
              </v-container>
            </v-form>
          </div>
        </div>

        <div id="schedule" class="input_group">
          <v-form v-model="valid">
            <v-container>
              <h2>スケジュールを組もう</h2>
              <v-row>
                <v-col cols="6" md="6">
                  <v-menu
                    ref="start"
                    v-model="start"
                    :close-on-content-click="false"
                    :return-value.sync="start_date"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="start_date"
                        label="開始日"
                        prepend-icon=""
                        readonly
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="start_date" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="#37474F" @click="start = false"
                        >Cancel</v-btn
                      >
                      <v-btn
                        text
                        color="#37474F"
                        @click="$refs.start.save(start_date)"
                        >OK</v-btn
                      >
                    </v-date-picker>
                  </v-menu>
                </v-col>

                <v-col cols="6" md="6">
                  <v-menu
                    ref="deadline"
                    v-model="deadline"
                    :close-on-content-click="false"
                    :return-value.sync="deadline_date"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                    <template v-slot:activator="{ on }">
                      <v-text-field
                        v-model="deadline_date"
                        label="締め切り"
                        prepend-icon=""
                        readonly
                        v-on="on"
                      ></v-text-field>
                    </template>
                    <v-date-picker v-model="deadline_date" no-title scrollable>
                      <v-spacer></v-spacer>
                      <v-btn text color="#37474F" @click="deadline = false"
                        >Cancel</v-btn
                      >
                      <v-btn
                        text
                        color="#37474F"
                        @click="$refs.deadline.save(deadline_date)"
                        >OK</v-btn
                      >
                    </v-date-picker>
                  </v-menu>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </div>
      </div>
    </v-app>
  </div>
</template>

<script>
export default {
  name: "NewGoal",

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
    };
  },
  methods: {
    new_goal_register: function() {
      const vm = this;
      vm.new_goal_registered = true;
    },
  },
};
</script>

<style scoped>
.input_group {
  margin: 20px;
  transition: all 0.2s;
}

#motivation {
  /* background: rgba(105, 105, 105, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#countermeasure {
  /* background: rgba(79, 79, 80, 0.288); */
  border-radius: 4px;
  padding: 20px;
}

#goal {
  padding: 20px;
}

.v-stepper {
  box-shadow: none;
}
</style>
