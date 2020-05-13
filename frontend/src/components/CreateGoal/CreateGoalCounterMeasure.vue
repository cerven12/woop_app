<template>
  <div>
    <v-btn @click="toggle"></v-btn>
    <div>
      <!--  worry and idea form -->
      <div id="countermeasure" class="input_group">
        <!-- Counter Measure Registerd -->
        <transition name="countermeasure" mode="out-in">
          <div v-if="ref" key="0">
            <v-container>
              <v-row>
                <v-col cols="12">
                  <h2>▶　挫折をしないために準備する</h2>
                </v-col>
              </v-row>
            </v-container>
            <v-container>
              <h3>心配事と、それに対する対策を考えておきましょう</h3>
              <!-- @@@@ Worry, Idea Model Form @@@@ -->
              <transition-group name="form" tag="div">
                <div
                  v-for="(worries, worries_index) in worryList"
                  :key="worries_index"
                >
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
                    <transition-group name="form" tag="div">
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
                                @click="
                                  deleteIdeaForm(worries_index, ideas_index)
                                "
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
                    </transition-group>
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
                    <transition-group name="form" tag="div">
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
                                @click="
                                  deleteIdeaForm(worries_index, ideas_index)
                                "
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
                    </transition-group>
                  </template>
                  <!-- %%%% Idea Model Form ここまで %%%% -->
                  <v-row justify="end">
                    <v-col cols="1"
                      ><v-btn
                        depressed
                        small
                        @click="addIdeaForm(worries_index)"
                        >＋</v-btn
                      ></v-col
                    ></v-row
                  >
                </div>
              </transition-group>
            </v-container>
            <!-- @@@@ Worry, Idea Model Form ここまで @@@@ -->
            <v-container>
              <v-row
                ><v-col
                  ><v-btn @click="addWorryIdeaForm" text depressed
                    >＋</v-btn
                  ></v-col
                ></v-row
              >
            </v-container>
            <v-form v-model="valid">
              <v-container>
                <h3>参考にできそうな資料を登録しておきましょう</h3>
                <transition-group name="form" tag="div">
                  <div
                    v-for="(references, ref_index) in refList"
                    v-bind:key="ref_index"
                  >
                    <template v-if="ref_index >= 1">
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
                            @click="deleteRefernceForm(ref_index)"
                            color="error"
                            text
                            >✘</v-btn
                          >
                        </v-col>
                      </v-row>
                    </template>
                    <!-- if reference model is un registered -->
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
                </transition-group>
                <v-row justify="end">
                  <v-col cols="1">
                    <v-btn @click="addReferenceForm" depressed small>
                      +
                    </v-btn>
                  </v-col> </v-row
                ><v-btn outlined @click="counterMeasureAllRegister"
                  >登録！</v-btn
                >
              </v-container>
            </v-form>
          </div>
          <!-- Counter Measure Registerd  / -->

          <!-- Before Counter Measure Register -->
          <div v-else key="1">
            <!-- Worry ,Idea -->
            <v-container>
              <v-row>
                <v-col cols="12">
                  <h2>▶　挫折をしないために準備する</h2>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12">
                  <template v-for="worry in worryList">
                    <h4 :key="worry.id">{{ worry.worry }}</h4>
                    <li v-for="idea in worry.ideaList" :key="idea.id">
                      {{ idea.idea }}
                    </li>
                  </template>
                </v-col>
              </v-row>
              <!-- reference  -->
              <v-row>
                <v-col>
                  <div v-for="(refs, refs_index) in refList" :key="refs_index">
                    <ul>
                      <li>
                        {{ refs.reference_name }}
                        {{ refs.reference_use }}
                        {{ refs.reference_source }}
                      </li>
                    </ul>
                  </div>
                </v-col>
              </v-row>
            </v-container>
          </div></transition
        >
        <!-- Before register / -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateGoal",
  props: ["goal_id", "token"],

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
    counterMeasureAllRegister: function() {
      this.worryIdeaRegister();
      this.referenceRegister();
    },

    // Posting `Worry` and `Idea` at the same time `axios.post`.
    worryIdeaRegister: function(worry_index) {
      let vm = this;
      vm.worryList.forEach(function(worries) {
        let judgeStr = worries.worry.replace(/^[\s|　]+|[\s|　]+$/g, "");

        if (judgeStr) {
          vm.axios
            .post(
              vm.url + vm.goal_id + "/" + "worries/",
              {
                goal: vm.goal_id,
                worry: worries.worry,
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
              }
            )
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
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
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
            .post(
              vm.url + vm.goal_id + "/" + "references/",
              {
                goal: vm.goal_id,
                reference_name: refs.reference_name,
                reference_use: refs.reference_use,
                reference_source: refs.reference_source,
              },
              {
                //  JWT
                headers: {
                  "Content-Type": "application/json",
                  Authorization: `JWT ${vm.token}`,
                },
              }
            )
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
  padding: 40px 40px 40px 40px;
  margin: 40px 40px 40px 40px;
  transition: all 0.3s cubic-bezier(0.43, 0.49, 0.25, 0.84);

  /* border-radius: 50px;
  box-shadow: 8px 8px 16px #acabab, -8px -8px 16px rgb(255, 255, 255); */
}

#countermeasure:hover {
  border-radius: 50px;
  box-shadow: 8px 8px 15px #b9b9b9, -8px -8px 15px #fafafa;
}

.subtitle {
  padding: 0 0 0 25px;
  margin: 0 0 0 25px;
}

h2,
h3 {
  color: rgb(83, 83, 83);
}

.v-messages {
  font-size: 15px;
}
.v-messages__message {
  padding-top: 2px;
}

.countermeasure-enter-active,
.countermeasure-leave-active {
  transition: opacity 0.3s;
}
.countermeasure-enter,
.countermeasure-leave-to {
  opacity: 0;
}

/* add(delete) form */
.form-enter-active {
  animation: fadeInUp 0.3s;
  transition: opacity 0.3s;
}
.form-leave-active {
  animation: fadeInUp 0.3s reverse;
  transition: opacity 0.3s;
}
.form-enter,
.form-leave-to {
  opacity: 0;
}
</style>
``
