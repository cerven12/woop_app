<template>
  <div>
    <v-app>
      <div id="back">
        <div id="goal" class="input_group">
          <v-container>
            <v-row>
              <v-col cols="12" md="12">
                <h3>あなたが達成したい目標を書きましょう{{ this_time_goal_data }}</h3>
              </v-col>
            </v-row>
            <v-row justify="start">
              <v-col cols="9" md="10" lg="9"
                ><h1>{{ goal_title }}</h1>
              </v-col>
              <v-spacer></v-spacer>
              <v-col cols="2">
                <v-icon
                  x-large
                  color="blue"
                  v-show="new_goal_registered"
                  id="check"
                  >mdi-check-bold</v-icon
                >
              </v-col>
            </v-row>
            <v-row>
              <v-col cols="10">
                <v-text-field
                  label="目標を決めよう"
                  placeholder=""
                  solo
                  v-model="goal_title"
                ></v-text-field>
              </v-col>
              <v-col cols="2">
                <v-btn
                  class="ma-2"
                  outlined
                  color="black"
                  @click="newGoalRegister(goal_title)"
                  >決定</v-btn
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
            <v-textarea
              placeholder=""
              name="理由"
              label="理由"
              value=""
              hint="目標を叶えたい理由を書きましょう"
              rows="1"
              auto-grow
              v-model="motive"
            ></v-textarea>
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
              <v-textarea
                name="自己超越目標"
                label="周囲への影響"
                value=""
                hint="目標を達成した時、周りの人々や環境にどのような良い影響が与えるか、想像してみてください"
                rows="1"
                auto-grow
                v-model="self_transcendence_goal"
              ></v-textarea>
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
              <v-textarea
                name="後悔"
                label="後悔"
                value=""
                hint="もし行動しなかった場合。10年度、20年後のあなたの後悔を想像してみましょう"
                rows="1"
                auto-grow
                v-model="future_self"
              ></v-textarea>
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
                <v-textarea
                  name="詳しく"
                  label="詳しく"
                  value=""
                  hint="達成したとみなす水準"
                  rows="3"
                  auto-grow
                  placeholder="どこで、なにを、どのように、どの水準で達成したいか"
                  v-model="goal_description"
                ></v-textarea>
              </v-col>
            </v-row>
        <v-row>
          <v-col cols="12" md="12">
            <v-textarea
              name="障壁"
              label="障壁"
              value=""
              hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
              rows="1"
              auto-grow
              v-model="worry"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-row justify="end">
          <v-col cols="2"><v-btn depressed small>＋</v-btn></v-col>
          <v-col cols="9">
            <v-textarea
              name="解決策"
              label="解決策"
              value=""
              hint="前もって障壁に対する解決策を考えておきましょう"
              rows="1"
              auto-grow
            ></v-textarea>
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

    <v-btn @click='updateGoal(goal_description, start_date, deadline_date)'>Goalモデルの追加項目を登録！</v-btn>
    <v-btn @click="newGoalChildRegister()">子モデルmotiveの登録！！！</v-btn>
  </div>
      </div>

      <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
    </v-app>
  </div>
</template>

<script>


export default {
  components: {

  },

  data: function() {
    return {
      goal_title:
        "Django Rest FrameworkとVue CLI&Vuetifyで、SPAなタスク管理アプリケーションを作成する。",
      start_date: new Date().toISOString().substr(0, 10),
      deadline_date: new Date().toISOString().substr(0, 10),
      start: false,
      deadline: false,
      new_goal_registered: false,
      valid: "",
      this_time_goal_data: "",
      url: 'http://127.0.0.1:8000/api/v1/goals/',
      start_date: '',
      goal_description: '',
      motive: '',
      self_transcendence_goal: '',
      future_self: '',
      worry: '',
    };
  },
  methods: {
    newGoalRegister: function(goal_title) {
      const vm = this;
      vm.axios.post(vm.url, { goal_title : goal_title })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      .then(vm.new_goal_registered = true);
    },
    updateGoal: function(goal_description, start_date, deadline_date){
      const vm = this;
      vm.axios.put(vm.url+vm.this_time_goal_data.id+'/',
      {
        id: vm.this_time_goal_data.id,
        goal_title: vm.this_time_goal_data.goal_title,
        goal_description: goal_description,
        start_date: start_date,
        deadline: deadline_date,
        })
    },
    newGoalChildRegister: function(){
      const vm = this;
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'motives/',
      { goal: vm.this_time_goal_data.id, motive: vm.motive })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'self_transcendence_goals/',
      { goal: vm.this_time_goal_data.id, self_transcendence_goal: vm.self_transcendence_goal })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'future_selves/',
      { goal: vm.this_time_goal_data.id, future_self: vm.future_self })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
      vm.axios.post(vm.url+vm.this_time_goal_data.id+'/'+'worries/',
      { goal: vm.this_time_goal_data.id, worry: vm.worry })
      .then(response => vm.this_time_goal_data = response.data)
      .catch((error) =>{ console.log(error) })
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

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message{
  padding-top: 2px;
}
</style>
