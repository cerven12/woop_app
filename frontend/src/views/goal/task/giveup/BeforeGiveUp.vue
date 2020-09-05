<template>
  <div>

    <!-- Split | Left Side "form"| Right Side "TIps" | -->
    <div id="css-grid">
      <!----------------------------------------------------------------------->
      <!--                       Left Side "form"                         -->
      <!----------------------------------------------------------------------->
      <v-container fluid id="form-area">
        <div id="line">
          <!-- Label -->
          <v-row>
            <v-col cols="10">
              <h2 class="message-title">Lets preparations for not give up.</h2>
            </v-col>
            <v-col>
              <v-btn small color="gray" @click="editHurdle()">OK!</v-btn>
            </v-col>
          </v-row>

          <!----------------------------------------------------------------------->
          <!--            Obstacle & Countermeasure.                 -->
          <!----------------------------------------------------------------------->
          <h3 class="category-title">Obstacle & Countermeasure.</h3>
          <transition-group name="form" tag="div">
            <div
              v-for="(hurdles, hurdles_index) in HurdlesData"
              :key="hurdles_index"
            >
              <!-- If it's two or more Worry Model forms, show ✘, and label and hint is hide of Worry. solution Model form. -->
              <template v-if="hurdles_index >= 1">
                <v-row>
                  <v-col cols="11" md="11">
                    <v-textarea
                      rows="1"
                      auto-grow
                      v-model="hurdles.hurdle"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="1">
                    <v-btn
                      @click="
                        deleteHurdleSolutionForm(
                          hurdles.hurdle_id,
                          hurdles_index
                        )
                      "
                      text
                      depressed
                      height="55"
                      color="error"
                    >
                      ✘
                    </v-btn>
                  </v-col>
                </v-row>

                <!-- solution Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(solutions, solutions_index) in hurdles.solutions"
                    :key="solutions_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>
                      <!--The second and subsequent solution model forms belonging to the Worry model form will not be labeled or named. -->
                      <template v-if="solutions_index >= 1">
                        <v-col cols="9">
                          <v-textarea
                            rows="1"
                            auto-grow
                            v-model="solutions.solution"
                          ></v-textarea>
                        </v-col>

                        <v-col cols="1">
                          <v-btn
                            @click="
                              deleteSolutionForm(
                                hurdles.hurdle_id,
                                solutions.solution_id,
                                hurdles_index,
                                solutions_index
                              )
                            "
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>

                      <!-- First solution Model form -->
                      <template v-else>
                        <v-col cols="9">
                          <v-textarea
                            rows="1"
                            auto-grow
                            v-model="solutions.solution"
                          >
                          </v-textarea>
                        </v-col>
                        <v-col cols="1"> </v-col>
                      </template>
                    </v-row>
                  </div>
                </transition-group>
              </template>
              <!-- This is the end of the Worry Model form after 2. -->

              <!-- First Worry Model form -->
              <template v-else>
                <v-row>
                  <v-col cols="12">
                    <v-textarea
                      name="障壁"
                      label="Obstacle"
                      hint=""
                      rows="1"
                      auto-grow
                      v-model="hurdles.hurdle"
                    ></v-textarea>
                  </v-col>
                </v-row>

                <!-- solution Model Form -->
                <transition-group name="form" tag="div">
                  <div
                    v-for="(solutions, solutions_index) in hurdles.solutions"
                    :key="solutions_index"
                  >
                    <v-row justify="end">
                      <v-col cols="2"></v-col>

                      <!-- If it's two or more solution Model forms, show ✘, and label and hint is hide. -->
                      <template v-if="solutions_index >= 1">
                        <v-col cols="9">
                          <v-textarea
                            rows="1"
                            auto-grow
                            v-model="solutions.solution"
                          >
                          </v-textarea>
                        </v-col>
                        <v-col cols="1">
                          <v-btn
                            @click="
                              deleteSolutionForm(
                                hurdles.hurdle_id,
                                solutions.solution_id,
                                hurdles_index,
                                solutions_index
                              )
                            "
                            text
                            depressed
                            height="55"
                            color="error"
                          >
                            ✘
                          </v-btn>
                        </v-col>
                      </template>
                      <!-- This is the end of the solution Model form after 2.  -->

                      <!-- First solution Model form -->
                      <template v-else>
                        <v-col>
                          <v-textarea
                            name="解決策"
                            label="Countermeasure."
                            hint=""
                            rows="1"
                            auto-grow
                            v-model="solutions.solution"
                          ></v-textarea></v-col
                      ></template>
                      <!-- This is the end of the First solution Model form. -->
                    </v-row>
                  </div>
                </transition-group>
              </template>

              <v-row justify="end">
                <v-col cols="1">
                  <v-btn
                    depressed
                    small
                    @click="addSolutionForm(hurdles_index)"
                  >
                    ＋
                  </v-btn>
                </v-col>
              </v-row>
            </div>
          </transition-group>

          <v-row>
            <v-col>
              <v-btn @click="addHurdlesolutionForm" text depressed>＋</v-btn>
            </v-col>
          </v-row>
        </div>
      </v-container>
      <v-container fluid id="tips-area">
        <h1>Tips</h1>
        <pre>Hurdle  {{ HurdlesData }}</pre>
        <pre>Original {{ OriginalHurdlesData }}</pre>
      </v-container>
    </div>
  </div>
</template>
<script>
import api from "@/services/api.js";

export default {
  name: "Task",
  props: ["Hurdles", "OriginalHurdles", "taskId"],
  data: function () {
    return {
      HurdlesData: this.Hurdles,
      OriginalHurdlesData: this.OriginalHurdles
    };
  },

  methods: {
    endEdit: function () {
      this.$emit("close");
    },
    addHurdlesolutionForm: function () {
      const form = { hurdle: "", solutions: [{ solution: "" }] };
      this.HurdlesData.push(form);
    },
    addSolutionForm: function (hurdles_id) {
      const form = { solutions: "" };
      this.HurdlesData[hurdles_id].solutions.push(form);
    },

    //   delete
    deleteHurdleSolutionForm(hurdle_id, index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (hurdle_id == null) {
        vm.HurdlesData.splice(index, 1);
        } else {
          api
            .delete(`goals/${goalid}/tasks/${vm.taskId}/hurdles/${hurdle_id}/`)
            .then(response => console.log(response))
            .catch(error => console.log(error));
          vm.HurdlesData.splice(index, 1);
          vm.OriginalHurdlesData.splice(index, 1);
      }
    },

    deleteSolutionForm(hurdle_id, solution_id, hurdle_index, solution_index) {
      const vm = this;
      let goalid = vm.$route.params.id;
      if (solution_id == null) {
        vm.HurdlesData[hurdle_index].solutions.splice(solution_index, 1);
        } else {
          api
            .delete(`goals/${goalid}/tasks/${vm.taskId}/hurdles/${hurdle_id}/solutions/${solution_id}/`)
            .then(response => console.log(response))
            .catch(error => console.log(error));
          vm.HurdlesData[hurdle_index].solutions.splice(solution_index, 1);
          vm.OriginalHurdlesData[hurdle_index].solutions.splice(
          solution_index,
            1
          );
      }
    },

    editHurdle: function () {
      const vm = this;
      // Stores the object whose content has changed.
      let ChangeData = [];
      let NewData = [];
      let postPromises = []; // post datas
      let editPromises = []; // patch datas
      let NewSolutionDada = [];
      let ChangeSolutionData = [];
      let postSolutionPromises = [];
      let editSolutionPromises = [];
      let goalId = vm.$route.params.id;

      Array.from(vm.HurdlesData).forEach((hurdle, index) => {
        // For compute to difference by `OriginalMotives`.
        let originalMo = vm.OriginalHurdlesData[index];
        let solutionList = [];

        // If existence new `hurdle`
        if (!hurdle.hurdle_id) {
          // add new `solutions`
          solutionList = hurdle.solutions.map(solution => {
            return { solution: solution.solution  };
          });
          NewData.push({
            hurdle: hurdle.hurdle,
            solutions: solutionList // solutionList = { solution: '', hurdle: 1}, { solution: '', hurdle:1}, ......
          });
        }

        // edit
        else if (hurdle.hurdle !== originalMo.hurdle) {
          ChangeData.push({
            hurdle_id: hurdle.hurdle_id,
            hurdle: hurdle.hurdle
          });
          if (hurdle.solutions !== originalMo.solutions) {
          Array.from(hurdle.solutions).forEach((solution, index) => {
            let original = originalMo.solutions[index];
            let currenthurdleId = hurdle.hurdle_id;
            if (!solution.solution_id) {
              // solution = new input data, original = original
              NewSolutionDada.push({
                hurdle: hurdle.hurdle_id,
                solution: solution.solution
              });
            } else if (solution.solution !== original.solution) {
              ChangeSolutionData.push({
                solution_id: original.solution_id,
                solution: solution.solution,
                hurdle: original.hurdle
              });
            }
          });
        }
        }

        // `solution` diff
        else if (hurdle.solutions !== originalMo.solutions) {
          Array.from(hurdle.solutions).forEach((solution, index) => {
            let original = originalMo.solutions[index];
            let currenthurdleId = hurdle.hurdle_id;
            if (!solution.solution_id) {
              // solution = new input data, original = original
              NewSolutionDada.push({
                hurdle: hurdle.hurdle_id,
                solution: solution.solution
              });
            } else if (solution.solution !== original.solution) {
              ChangeSolutionData.push({
                solution_id: original.solution_id,
                solution: solution.solution,
                hurdle: original.hurdle
              });
            }
          });
        }
      });

      //create post datas and axios.all
      NewData.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/tasks/${vm.taskId}/hurdles/`,
          data: {
            hurdle: item.hurdle,
            solutions: item.solutions,
            task: vm.taskId
          },
          useCredentails: true
        });
        postPromises.push(newPostPromise);
      });

      // solution
      NewSolutionDada.forEach(function (item, index) {
        let newPostPromise = api({
          method: "post",
          url: `goals/${goalId}/tasks/${vm.taskId}/hurdles/${item.hurdle}/solutions/`,
          data: { solution: item.solution, hurdle: item.hurdle },
          useCredentails: true
        });
        postSolutionPromises.push(newPostPromise);
      });

      // create patch datas
      ChangeData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/tasks/${vm.taskId}/hurdles/${item.hurdle_id}/`,
          data: {
            hurdle: item.hurdle
          },
          useCredentails: true
        });
        editPromises.push(newPromise);
      });

      // solution
      ChangeSolutionData.forEach(function (item, index) {
        let newPromise = api({
          method: "patch",
          url: `goals/${goalId}/tasks/${vm.taskId}/hurdles/${item.hurdle}/solutions/${item.solution_id}/`,
          data: {
            solution: item.solution
          },
          useCredentails: true
        });
        editSolutionPromises.push(newPromise);
      })

      // post
      Promise.all(postPromises).then(responses => {
        responses.forEach(res => {
          vm.OriginalHurdlesData.push(res.data);
          vm.$set(
          vm.HurdlesData, "hurdles", JSON.parse(JSON.stringify(vm.OriginalHurdlesData))
          );
        });
      });

      Promise.all(postSolutionPromises).then(responses => {
        responses.forEach(res => {
          let postsolution = res.data;
          // Identifying the Parent Object.
          if (
            vm.OriginalHurdlesData.find(
              item => item.hurdle_id == postsolution.hurdle
            )
          ) {
            vm.OriginalHurdlesData.find(
              item => item.hurdle_id == postsolution.hurdle
            ).solutions.push(postsolution);

          vm.$set(

            vm.HurdlesData,'hurdles', JSON.parse(JSON.stringify(vm.OriginalHurdlesData))
            );
          }
        });
      });

      // patch
      Promise.all(editPromises).then(responses => {
        responses.forEach(res => {
          let currentId = res.data.hurdle_id;
          // Find the object to be changed by `OriginalMotive`.
          // superscription motive.
          if (
            vm.OriginalHurdlesData.find(item => item.hurdle_id == currentId)
          ) {
            vm.OriginalHurdlesData.find(
              item => item.hurdle_id == currentId
            ).hurdle = res.data.hurdle;

                      vm.$set(
            vm.HurdlesData, 'hurdles', JSON.parse(JSON.stringify(vm.OriginalHurdlesData))
            );
          }
        });
      });

      Promise.all(editSolutionPromises).then(responses => {
        responses.forEach(res => {
          let postsolution = res.data;
          // Identifying the Parent Object.
          if (
            vm.OriginalHurdlesData.find(
              item => item.hurdle_id == postsolution.hurdle
            )
          ) {
            vm.OriginalHurdlesData.find(
              item => item.hurdle_id == postsolution.hurdle
            ).solutions.find(
              i => i.solution_id == postsolution.solution_id
            ).solution = postsolution.solution;

                      vm.$set(
            vm.HurdlesData, 'hurdles', JSON.parse(
              JSON.stringify(vm.OriginalHurdlesData)
              )
            );
          }
        });
      });

      vm.$emit("close");
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
  background-color: #f0f0f0;
}

#form-area {
  grid-area: form;
}
#tips-area {
  grid-area: tips;
}

@media all and (max-width: 100000px) {
  #css-grid {
    grid-template-columns: 55% 45%;
    grid-template-areas: "form tips";
    padding: 0px 17%;
  }
}

@media all and (max-width: 1264px) {
  #css-grid {
    grid-template-columns: 100%;
    grid-template-areas:
      "form"
      "tips";
    padding: 0px 13%;
  }
}

@media all and (max-width: 960px) {
  #css-grid {
    padding: 0px 5%;
  }
}

/*   ------------------------------------------------------------
                          Transition
 ------------------------------------------------------------*/
.countermeasure-enter-active,
.countermeasure-leave-active {
  transition: opacity 0.3s;
}
.countermeasure-enter,
.countermeasure-leave-t {
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

@keyframes fadeInUp {
  0% {
    transform: translateX(20px);
    opacity: 0;
  }
  60% {
    opacity: 0.3;
  }
  100% {
    transform: translateX(0px);
    opacity: 1;
  }
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
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  color: #3c3d3d;
}</style
>o
