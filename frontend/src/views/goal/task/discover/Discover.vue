<template>
  <div>
    <v-row>
      <v-col cols="12">
        <h2 class="message-title">
          Discover
        </h2>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="9" lg="8" md="9" sm="10" xs="11">
        <div v-for="discover in Discovers" :key="discover.id">
          <AccordionForDiscover>
            <div slot="source">{{ discover.created_at }}</div>
            <div slot="header">
              {{ discover.discover_title }}
            </div>
            <div slot="body">
              {{ discover.discover_main }}
            </div>
          </AccordionForDiscover>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import AccordionForDiscover from "./AccordionForDiscover.vue";

export default {
  name: "Task",
  props: ["Discovers"],
  components: {
    AccordionForDiscover,
  },
  data: function() {
    return {
    };
  },
};
</script>

<style scoped>
/*   ------------------------------------------------------------
                            Font Desiign
 -----------------------------------------------------------*/
.message-title {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  /* font-size: 34px; */
  line-height: 40px;
  color: #088dda;
  font-size: 34px;
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
@media only screen and (max-width: 600px) {
.col-9 {
    flex: 0 0 100%;
    max-width: 100%;
}
.message-title{
 font-size: 30px;
}
}
</style>
