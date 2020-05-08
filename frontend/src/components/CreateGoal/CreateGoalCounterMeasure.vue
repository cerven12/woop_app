<template>
  <div>
    <!--  worry and idea form -->
    <div id="countermeasure" class="input_group">
      <v-container>
        <v-row
          >{{ goal_id }} {{ url }}
          <v-col cols="12">
            <h2>▶　挫折をしないために準備する</h2>
          </v-col>
        </v-row>
        <h3>心配事と、それに対する対策を考えておきましょう</h3>
        <!-- @@@@ Worry, Idea Model Form @@@@ -->
        <div v-for="(worries, worries_index) in worryList" :key="worries_index">
          <!-- $$$$ ２つ目以降のWorryのフォームについては、Worry及びIdeaのlabelとhintを削除する $$$$ -->
          <template v-if="worries_index >= 1">
            <v-row>
              <v-col cols="11" md="11">
                <v-textarea
                  rows="1"
                  outlined
                  auto-grow
                  v-model="worries.worry"
                ></v-textarea>
              </v-col>
              <v-col cols="1">
                <v-btn
                  @click="deleteWorryIdeaForm(worries_index)"
                  text
                  depressed
                  height="55"
                  color="error"
                  >✘</v-btn
                >
              </v-col>
            </v-row>
            <!-- Idea Model Form -->
            <div
              v-for="(ideas, ideas_index) in worries.ideaList"
              :key="ideas_index"
            >
              <v-row justify="end">
                <v-col cols="2"></v-col>
                <!-- ^^^^ 2つ目以降のWorryFormにある、ネストされたIdeaFormにlabelやhintを表示しない。 ^^^^ -->
                <template v-if="ideas_index >= 1">
                  <v-col cols="9">
                    <v-textarea
                      rows="1"
                      auto-grow
                      outlined
                      v-model="ideas.idea"
                    ></v-textarea> </v-col
                  ><v-col cols="1"
                    ><v-btn
                      @click="deleteIdeaForm(worries_index, ideas_index)"
                      text
                      depressed
                      height="55"
                      color="error"
                      >✘</v-btn
                    ></v-col
                  >
                </template>
                <!-- ^^^^ ２つ目以降のIdeaのフォーム ここまで ^^^^ -->
                <!-- **** 1つ目のIdeaフォーム **** -->
                <template v-else>
                  <v-col cols="9">
                    <v-textarea
                      rows="1"
                      auto-grow
                      outlined
                      v-model="ideas.idea"
                    ></v-textarea></v-col
                  ><v-col cols="1"></v-col
                ></template>
                <!-- **** 1つ目のIdeaフォーム ここまで **** -->
              </v-row>
            </div>
          </template>
          <!-- $$$$ 2つ目以降のWorryフォーム ここまで $$$$-->
          <!-- %%%% １つ目のWorryとIdeaのフォーム %%%% -->
          <template v-else>
            <v-row>
              <v-col cols="12" md="12">
                <v-textarea
                  name="障壁"
                  label="障壁"
                  hint="行動するにあたって、不安やわからないことをたくさん書いておきましょう"
                  rows="1"
                  outlined
                  auto-grow
                  v-model="worries.worry"
                ></v-textarea>
              </v-col>
            </v-row>
            <!-- Idea Model Form -->
            <div
              v-for="(ideas, ideas_index) in worries.ideaList"
              :key="ideas_index"
            >
              <v-row justify="end">
                <v-col cols="2"></v-col>
                <!-- ^^^^ ２つ目以降のIdeaのフォームはlabelやhintを表示しない ^^^^ -->
                <template v-if="ideas_index >= 1">
                  <v-col cols="9">
                    <v-textarea
                      rows="1"
                      auto-grow
                      outlined
                      v-model="ideas.idea"
                    ></v-textarea> </v-col
                  ><v-col cols="1"
                    ><v-btn
                      @click="deleteIdeaForm(worries_index, ideas_index)"
                      text
                      depressed
                      height="55"
                      color="error"
                      >✘</v-btn
                    ></v-col
                  >
                </template>
                <!-- ^^^^ ２つ目以降のIdeaのフォーム ここまで ^^^^ -->
                <!-- **** 1つ目のIdeaフォーム **** -->
                <template v-else>
                  <v-col>
                    <v-textarea
                      name="解決策"
                      label="解決策"
                      hint="前もって障壁に対する解決策を考えておきましょう"
                      rows="1"
                      auto-grow
                      outlined
                      v-model="ideas.idea"
                    ></v-textarea></v-col
                ></template>
                <!-- **** 1つ目のIdeaフォーム ここまで **** -->
              </v-row>
            </div>
          </template>
          <!-- %%%% Idea Model Form ここまで %%%% -->
          <v-row justify="end">
            <v-col cols="1"
              ><v-btn depressed small @click="addIdeaForm(worries_index)"
                >＋</v-btn
              ></v-col
            ></v-row
          >
        </div>
        <!-- @@@@ Worry, Idea Model Form ここまで @@@@ --><v-btn
          @click="worryIdeaRegister"
          >registers</v-btn
        >
        <v-row
          ><v-col><v-btn @click="addWorryIdeaForm">add</v-btn></v-col></v-row
        >
        <div>
          <!-- reference ここから -->
          <v-btn @click="toggle">TOGGLE</v-btn>
          <template v-if="ref">
            <v-form v-model="valid">
              <v-container>
                <h3>参考にできそうな資料を登録しておきましょう</h3>
                <div
                  v-for="(references, index) in refList"
                  v-bind:key="references.id"
                >
                  <template v-if="index >= 1">
                    <v-row>
                      <v-col cols="4">
                        <v-text-field
                          outlined
                          v-model="references.reference_name"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="4">
                        <v-text-field
                          outlined
                          v-model="references.reference_use"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="3">
                        <v-text-field
                          outlined
                          v-model="references.reference_source"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="1">
                        <v-btn
                          @click="deleteRefernceForm(index)"
                          color="error"
                          text
                          >✘</v-btn
                        >
                      </v-col>
                    </v-row>
                  </template>
                  <template v-else>
                    <v-row>
                      <v-col cols="4">
                        <v-text-field
                          label="資料"
                          hint="参考にしたい資料を前もって登録しておきましょう"
                          outlined
                          v-model="references.reference_name"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="4">
                        <v-text-field
                          label="用途"
                          hint="この資料の用途を書きましょう"
                          outlined
                          v-model="references.reference_use"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="4">
                        <v-text-field
                          label="URL"
                          hint="場所など"
                          outlined
                          v-model="references.reference_source"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                  </template>
                </div>
                <v-row justify="end">
                  <v-col cols="1">
                    <v-btn @click="addReferenceForm" depressed small>
                      +
                    </v-btn>
                  </v-col> </v-row
                ><v-btn outlined @click="referenceRegister">登録！</v-btn>
              </v-container>
            </v-form>
          </template>
          <!-- reference ここまで -->
          <template v-else> </template>
        </div>
      </v-container>
    </div>
  </div>
</template>

<script>
import CounterMeasureWorryIdea from "./CounterMeasureWorryIdea.vue";

export default {
  name: "CreateGoal",
  props: ["goal_id"],
  components: {
    CounterMeasureWorryIdea,
  },

  data: function() {
    return {
      valid: "",
      this_time_goal_data: "",
      // for Worry model & Idea model.
      worryList: [
        {
          worry: "",
          ideaList: [{ idea: "" }],
        },
      ],

      parentWorryId: "",
      // for Reference Model
      refList: [
        { reference_name: "", reference_use: "", reference_source: "" },
      ],

      ref: true, // for debug
    };
  },

  computed: {
    url() {
      return this.$store.state.url;
    },
  },

  methods: {
    // for debug
    toggle: function() {
      if (this.ref === true) {
        this.ref = false;
      } else {
        this, (this.ref = true);
      }
    },

    // add form
    addWorryIdeaForm: function() {
      const form = { worry: "", ideaList: [{ idea: "" }] };
      this.worryList.push(form);
    },

    addIdeaForm: function(worries_id) {
      const form = { idea: "" };
      this.worryList[worries_id].ideaList.push(form);
    },

    addReferenceForm: function() {
      const form = {
        reference_name: "",
        reference_use: "",
        reference_source: "",
      };
      this.refList.push(form);
    },
    //  delete form
    deleteWorryIdeaForm: function(worry_id) {
      this.worryList.splice(worry_id, 1);
      console.log(this.worryList);
    },
    deleteIdeaForm: function(worries_id, ideas_id) {
      this.worryList[worries_id].ideaList.splice(ideas_id, 1);
    },

    deleteRefernceForm: function(index) {
      this.refList.splice(index, 1);
      console.log(this.refList);
    },
    // Posting `Worry` and `Idea` at the same time `axios.post`.
    worryIdeaRegister: function(worry_index) {
      let vm = this;
      vm.worryList.forEach(function(worries) {
        let judgeStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");

        if (judgeStr) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "worries/", {
              goal: vm.goal_id,
              worry: worries.worry,
            })
            .then((res) => {
              vm.parentWorryId = res.data.worry_id;
              // Take the `idea` for the current `worry` one by one from
              // the `ideaList` and post `axios.post` them in turn.
              vm.ideaRegister(worries, vm.parentWorryId);
            })
            .catch((error) => {
              console.log(`worryのエラーです${error}`);
            });
          // If the `worries` is `false`.
        } else {
          console.log("そのworryの文字列は認められませんね。");
        }
      });
    },

    // Call with a `worryIdeaRegister`
    ideaRegister: function(worries, parentWorryId) {
      const vm = this;
      console.log("worries.ideaList : " + worries.ideaList);
      worries.ideaList.forEach(function(ideas) {
        console.log(ideas);
        let judgeStr = ideas.idea.replace(/^[\s|　]+|[\s|　]+$/g, "");
        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/worries/" + parentWorryId + "/ideas/",
              {
                worry: parentWorryId,
                idea: ideas.idea,
              }
            )
            .then((res) => (vm.this_time_goal_data = res.data))
            .catch((error) => {
              console.log(`ideaのエラーです${error}`);
            });
        } else {
          console.log(`そのideaの文字列はだめです`);
        }
      });
    },
    referenceRegister: function() {
      const vm = this;
      this.refList.forEach(function(refs) {
        // Remove spaces and null strings
        const judgeStrName = refs.reference_name.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        const judgeStrUse = refs.reference_use.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        const judgeStrSource = refs.reference_source.replace(
          /^[\s|　]+|[\s|　]+$/g,
          ""
        );
        if (judgeStrName && judgeStrUse && judgeStrSource) {
          vm.axios
            .post(vm.url + vm.goal_id + "/" + "references/", {
              goal: vm.goal_id,
              reference_name: refs.reference_name,
              reference_use: refs.reference_use,
              reference_source: refs.reference_source,
            })
            .then((response) => (vm.this_time_goal_data = response.data))
            .catch((error) => {
              console.log(error);
            });
        } else {
          console.log(`その文字列はだめです`);
        }
      });
    },
  },
};
</script>

<style scoped>
#countermeasure {
  background: #f0f0f0;
  /* border: 1px black solid; */
  border-radius: 50px;
  padding: 40px 20px 40px 20px;
  margin: 40px 20px 40px 20px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}

#countermeasure:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}
</style>

<style>
.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}
</style>
``
