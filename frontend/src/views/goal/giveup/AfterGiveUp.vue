<template>
  <div>
    <div id="css-grid">
      <v-container fluid id="view-area">
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="7">
            <h2 class="message-title">
              Lets preparations for not give up.
            </h2>
          </v-col>
          <v-col cols="1">
            <v-btn fab small depressed color="gray" @click="switchEdit">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
          </v-col>
        </v-row>

        <!----------------------------------------------------------------------->
        <!--                             Obstacles                            -->
        <!----------------------------------------------------------------------->
        <v-row>
          <v-col cols="2"></v-col>
          <v-col cols="8">
            <h2 class="category-title">
              Obstacle & Countermeasure.
            </h2>
          </v-col>
        </v-row>

        <div v-for="Obstacle in Worries.worries" :key="Obstacle.id">
          <v-row>
            <v-col cols="3"></v-col>
            <v-col cols="7">
              <p class="writing-text obst-splitter">
                {{ Obstacle.worry }}
              </p>
            </v-col>
          </v-row>

          <div v-for="ideas in Obstacle.ideas" :key="ideas.id">
            <v-row>
              <v-col cols="4"></v-col>
              <v-col cols="6">
                <p class="writing-text idea-splitter">
                  {{ ideas.idea }}
                </p>
              </v-col>
            </v-row>
          </div>
          <br /><br />
        </div>
        <br />

        <!----------------------------------------------------------------------->
        <!--                                 Reference                         -->
        <!----------------------------------------------------------------------->
        <!-- <v&#45;row> -->
        <!--   <v&#45;col cols="2"></v&#45;col> -->
        <!--   <v&#45;col cols="8"> -->
        <!--     <h2 class="category&#45;title"> -->
        <!--       Reference -->
        <!--     </h2> -->
        <!--   </v&#45;col> -->
        <!-- </v&#45;row> -->
        <!--  -->
        <!-- <!&#45;&#45; <div v&#45;for="Reference in References" :key="Reference.id"> &#45;&#45;> -->
        <!--  -->
        <!-- <v&#45;row> -->
        <!--   <v&#45;col> -->
        <!--     <template> -->
        <!--       <div class="text&#45;center"> -->
        <!--         <v&#45;pagination -->
        <!--           v&#45;model="page" -->
        <!--           :length="6" -->
        <!--           color="#4465c0" -->
        <!--           circle -->
        <!--         ></v&#45;pagination> -->
        <!--       </div> -->
        <!--     </template> -->
        <!--   </v&#45;col> -->
        <!-- </v&#45;row> -->
        <!--  -->
        <!-- <v&#45;row> -->
        <!--   <v&#45;col cols="2"></v&#45;col> -->
        <!--   <v&#45;col cols="8"> -->
        <!--     <template> -->
        <!--       <v&#45;simple&#45;table fixed&#45;header height="1200px"> -->
        <!--         <template v&#45;slot:default> -->
        <!--           <thead> -->
        <!--             <tr> -->
        <!--               <th class="text&#45;left" style="background:#f0f0f0;"></th> -->
        <!--               <th class="text&#45;left" style="background:#f0f0f0;"> -->
        <!--                 Name -->
        <!--               </th> -->
        <!--               <th class="text&#45;left" style="background:#f0f0f0;"> -->
        <!--                 How to Use? -->
        <!--               </th> -->
        <!--             </tr> -->
        <!--           </thead> -->
        <!--           <tbody> -->
        <!--             <tr v&#45;for="item in refList" :key="item.id"> -->
        <!--               <td -->
        <!--                 style="text&#45;align:center; " -->
        <!--                 class="table&#45;color&#45;change" -->
        <!--               > -->
        <!--                 <img :src="item.reference_img" class="resize" /> -->
        <!--               </td> -->
        <!--               <td class="table&#45;color&#45;change"> -->
        <!--                 <a -->
        <!--                   class="writing&#45;text font&#45;16" -->
        <!--                   target="_blank" -->
        <!--                   rel="noopener noreferrer" -->
        <!--                   :href="item.reference_source" -->
        <!--                   >{{ item.reference_name }}</a -->
        <!--                 > -->
        <!--               </td> -->
        <!--               <td class="table&#45;color&#45;change writing&#45;text font&#45;16"> -->
        <!--                 {{ item.reference_use }} -->
        <!--               </td> -->
        <!--             </tr> -->
        <!--           </tbody> -->
        <!--         </template> -->
        <!--       </v&#45;simple&#45;table> -->
        <!--     </template> -->
        <!--   </v&#45;col> -->
        <!-- </v&#45;row> -->
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  name: "Goal",
  props: ["Worries"],

  data: function () {
    return {
      valid: "",
      page: 1,
      goalData: "",
      refList: [
        {
          reference_name: "Woop App",
          reference_use: "Thinking of design",
          reference_source: "http://192.168.129.16:8080/goal",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/top.png")
        },
        {
          reference_name:
            "Learn the basics of website development with Wakaba-Chan",
          reference_use:
            "I work hard at my studies while worshipping my wakaba chan.",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%8F%E3%81%8B%E3%81%B0%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E5%AD%A6%E3%81%B6-Web%E3%82%B5%E3%82%A4%E3%83%88%E5%88%B6%E4%BD%9C%E3%81%AE%E5%9F%BA%E6%9C%AC-%E6%B9%8A%E5%B7%9D%E3%81%82%E3%81%84-ebook/dp/B01L8CANVO?ref_=s9_apbd_ps_hd_bw_b1x4K&pf_rd_r=53K0M7HN8Q97C3MESMGV&pf_rd_p=fedc39c9-dd8f-5c8f-b647-f8112fd79df4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=465392",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/wakaba.jpg")
        },
        {
          reference_name:
            "Why Create in Object-Oriented Systems, 2nd Edition Kindle Edition",
          reference_use: "Learn the Object-oriented",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E6%8C%87%E5%90%91%E3%81%A7%E3%81%AA%E3%81%9C%E3%81%A4%E3%81%8F%E3%82%8B%E3%81%AE%E3%81%8B-%E7%AC%AC2%E7%89%88-%E5%B9%B3%E6%BE%A4-%E7%AB%A0-ebook/dp/B00ISP0QB2/ref=msx_wsirn_v1_4/356-4593790-2043255?_encoding=UTF8&pd_rd_i=B00ISP0QB2&pd_rd_r=acafd903-6c7c-4aec-9729-5d26ccff6cef&pd_rd_w=F9scb&pd_rd_wg=9MZ69&pf_rd_p=8acfbc98-0f10-4ca5-ab7c-019f8ea70a4e&pf_rd_r=2FDPYFAE2WJGA78F58XX&psc=1&refRID=2FDPYFAE2WJGA78F58XX",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/object.jpg")
        },
        {
          reference_name: "Know what a design pattern is.",
          reference_use:
            "An Introduction to Design Patterns in Java Language (Expanded and Revised Edition) Kindle edition",
          reference_source:
            "https://www.amazon.co.jp/%E5%A2%97%E8%A3%9C%E6%94%B9%E8%A8%82%E7%89%88-Java%E8%A8%80%E8%AA%9E%E3%81%A7%E5%AD%A6%E3%81%B6%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E5%85%A5%E9%96%80-%E7%B5%90%E5%9F%8E-%E6%B5%A9-ebook/dp/B00I8ATHGW/ref=msx_wsirn_v1_2/356-4593790-2043255?_encoding=UTF8&pd_rd_i=B00I8ATHGW&pd_rd_r=23c708f0-847e-4c74-90d4-e8fddb3f2c7f&pd_rd_w=YKOlR&pd_rd_wg=FGtaR&pf_rd_p=8acfbc98-0f10-4ca5-ab7c-019f8ea70a4e&pf_rd_r=9WC76FT7EKXDHB3R94T8&psc=1&refRID=9WC76FT7EKXDHB3R94T8",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/pattaern.jpg")
        },
        {
          reference_name: "Login Page",
          reference_use: "Login",
          reference_source:
            "https://www.amazon.co.jp/%E5%A2%97%E8%A3%9C%E6%94%B9%E8%A8%82%E7%89%88-Java%E8%A8%80%E8%AA%9E%E3%81%A7%E5%AD%A6%E3%81%B6%E3%83%87%E3%82%B6%E3%82%A4%E3%83%B3%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E5%85%A5%E9%96%80-%E7%B5%90%E5%9F%8E-%E6%B5%A9-ebook/dp/B00I8ATHGW/ref=msx_wsirn_v1_2/356-4593790-2043255?_encoding=UTF8&pd_rd_i=B00I8ATHGW&pd_rd_r=23c708f0-847e-4c74-90d4-e8fddb3f2c7f&pd_rd_w=YKOlR&pd_rd_wg=FGtaR&pf_rd_p=8acfbc98-0f10-4ca5-ab7c-019f8ea70a4e&pf_rd_r=9WC76FT7EKXDHB3R94T8&psc=1&refRID=9WC76FT7EKXDHB3R94T8",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/login.png")
        },
        {
          reference_name:
            "Learn the basics of website development with Wakaba-Chan",
          reference_use:
            "I work hard at my studies while worshipping my wakaba chan.",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%8F%E3%81%8B%E3%81%B0%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E5%AD%A6%E3%81%B6-Web%E3%82%B5%E3%82%A4%E3%83%88%E5%88%B6%E4%BD%9C%E3%81%AE%E5%9F%BA%E6%9C%AC-%E6%B9%8A%E5%B7%9D%E3%81%82%E3%81%84-ebook/dp/B01L8CANVO?ref_=s9_apbd_ps_hd_bw_b1x4K&pf_rd_r=53K0M7HN8Q97C3MESMGV&pf_rd_p=fedc39c9-dd8f-5c8f-b647-f8112fd79df4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=465392",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/wakaba.jpg")
        },
        {
          reference_name:
            "Learn the basics of website development with Wakaba-Chan",
          reference_use:
            "I work hard at my studies while worshipping my wakaba chan.",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%8F%E3%81%8B%E3%81%B0%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E5%AD%A6%E3%81%B6-Web%E3%82%B5%E3%82%A4%E3%83%88%E5%88%B6%E4%BD%9C%E3%81%AE%E5%9F%BA%E6%9C%AC-%E6%B9%8A%E5%B7%9D%E3%81%82%E3%81%84-ebook/dp/B01L8CANVO?ref_=s9_apbd_ps_hd_bw_b1x4K&pf_rd_r=53K0M7HN8Q97C3MESMGV&pf_rd_p=fedc39c9-dd8f-5c8f-b647-f8112fd79df4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=465392",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/wakaba.jpg")
        },
        {
          reference_name:
            "Learn the basics of website development with Wakaba-Chan",
          reference_use:
            "I work hard at my studies while worshipping my wakaba chan.",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%8F%E3%81%8B%E3%81%B0%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E5%AD%A6%E3%81%B6-Web%E3%82%B5%E3%82%A4%E3%83%88%E5%88%B6%E4%BD%9C%E3%81%AE%E5%9F%BA%E6%9C%AC-%E6%B9%8A%E5%B7%9D%E3%81%82%E3%81%84-ebook/dp/B01L8CANVO?ref_=s9_apbd_ps_hd_bw_b1x4K&pf_rd_r=53K0M7HN8Q97C3MESMGV&pf_rd_p=fedc39c9-dd8f-5c8f-b647-f8112fd79df4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=465392",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/wakaba.jpg")
        },
        {
          reference_name:
            "Learn the basics of website development with Wakaba-Chan",
          reference_use:
            "I work hard at my studies while worshipping my wakaba chan.",
          reference_source:
            "https://www.amazon.co.jp/%E3%82%8F%E3%81%8B%E3%81%B0%E3%81%A1%E3%82%83%E3%82%93%E3%81%A8%E5%AD%A6%E3%81%B6-Web%E3%82%B5%E3%82%A4%E3%83%88%E5%88%B6%E4%BD%9C%E3%81%AE%E5%9F%BA%E6%9C%AC-%E6%B9%8A%E5%B7%9D%E3%81%82%E3%81%84-ebook/dp/B01L8CANVO?ref_=s9_apbd_ps_hd_bw_b1x4K&pf_rd_r=53K0M7HN8Q97C3MESMGV&pf_rd_p=fedc39c9-dd8f-5c8f-b647-f8112fd79df4&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=465392",
          reference_img: require("/Users/takuto/python1/woop_app/frontend/src/assets/wakaba.jpg")
        }
      ]
    };
  },
  methods: {
    switchEdit: function () {
      this.$emit("startGiveUpEdit");
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
  color: #292929;
  padding-left: 50px;
}

.writing-text {
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  font-kerning: nomal;
  color: rgb(41, 41, 41);
  margin-block-end: 0em;
}

.obst-splitter {
border-left: 20px #494359 solid;
  padding-left: 15px;
}

.idea-splitter {
border-left: 20px #F2953D solid;
padding-left: 15px;
}

.resize {
  width: auto;
  height: 100px;
}

.table-color-change {
  background: #f0f0f0;
}

.font-16 {
  font-size: 16px;
}

.splitter {
  border-left: 20px rgb(142, 100, 170) solid;
  padding-left: 15px;
}
</style>
