<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="message-title">
              Note
            </h2>
          </v-col>
        </v-row>
        <v-row> </v-row>

        <v-row>
          <v-col cols="3"></v-col>
          <v-col cols="6">
            <div v-for="note in noteList" :key="note.id">
              <accordion>
                <div slot="header">
                  {{ note.title }}
                  <span slot="parent" class="atto">@countermeasure#44</span>
                </div>
                <div></div>
                <div slot="body">{{ note.main }}</div>
              </accordion>
              <accordion theme="purple">
                <div slot="header">TIPS</div>
                Purple accordion
              </accordion>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import accordion from "./Accordion";

export default {
  components: {
    accordion,
  },
  data: function() {
    return {
      start_date: "2019-01-06",
      deadline: "2019-05-08",
      noteList: [
        {
          main:
            "<h1>React</h1>React and Vue share many similarities. They both:<p>・utilize a virtual DOM</p><p>・provide reactive and composable view components</p><p>・maintain focus in the</p>core library, with concerns such as routing 　and global state management handled by companion libraries Being so similar in scope, we’ve put more time into fine-tuning this comparison than any other. We want to ensure not only technical accuracy, but also balance. We point out where React  outshines Vue, for example in the richness of their ecosystem and abundance of their custom renderers. With that said, it’s inevitable that the comparison would appear biased towards Vue to some React users, as many of the subjects explored are to some extent subjective. We acknowledge the existence of varying technical taste, and this comparison primarily aims to outline the reasons why Vue could potentially be a better fit if your preferences happen to coincide with ours. Some of the sections below may also be slightly outdated due to recent updates in React 16+, and we are planning to work with the React community to revamp this section in the near future.",
          title: "Hello World",
        },
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
.atto {
  padding: -90px;
  margin: 0;
  font-size: 14px;
}
</style>
