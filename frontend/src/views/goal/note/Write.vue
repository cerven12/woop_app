<template>
  <div>
    <div id="css-grid">
      <v-container fluid >
        <v-row>
          <v-col cols="12">
            <div class="editorx_body">
              <!--editorjs id-->
              <div class id="codex-editor" />
            </div>
            <button
              style="margin-left: 30%;"
              type="button"
              name="button"
              @click="save()"
            >
              save
            </button>
          </v-col>
        </v-row>
      </v-container>

      <!-- <v&#45;container fluid id="tips&#45;area"> -->
      <!--   <v&#45;row> -->
      <!--     <v&#45;col cols="12"> -->
      <!--       <div> -->
      <!--         <pre>{{ value }}</pre> -->
      <!--       </div> -->
      <!--     </v&#45;col> -->
      <!--   </v&#45;row> -->
      <!-- </v&#45;container> -->
    </div>
  </div>
</template>

<script>
import EditorJS from "@editorjs/editorjs";
import Header from "@editorjs/header";
import Paragraph from "@editorjs/paragraph";
import List from "@editorjs/list";
import Checklist from "@editorjs/checklist";
import Quote from "@editorjs/quote";
import Warning from "@editorjs/warning";
import CodeTool from "@editorjs/code";
import Marker from "@editorjs/marker";
import Table from "@editorjs/table";
import SimpleImage from "@editorjs/simple-image";
import Delimiter from "@editorjs/delimiter";
import InlineCode from "@editorjs/inline-code";

export default {
  data() {
    return {
      value: null,
      text: `{
  "time": 1594288606243,
  "blocks": [
    {
      "type": "header",
      "data": {
        "text": "メモです。",
        "level": 2
      }
    },
    {
      "type": "paragraph",
      "data": {
        "text": "こちらはメモです。以下にリストを記載します。"
      }
    },
    {
      "type": "list",
      "data": {
        "style": "ordered",
        "items": [
          "メモです",
          "メモです２",
          "メモです３"
        ]
      }
    },
    {
      "type": "delimiter",
      "data": {}
    },
    {
      "type": "quote",
      "data": {
        "text": "引用してください。",
        "caption": "takuto",
        "alignment": "left"
      }
    },
    {
      "type": "delimiter",
      "data": {}
    },
    {
      "type": "checklist",
      "data": {
        "items": [
          {
            "text": "チェックリスト１",
            "checked": false
          },
          {
            "text": "２",
            "checked": false
          }
        ]
      }
    },
    {
      "type": "warning",
      "data": {
        "title": "注意してください。",
        "message": "注意してください。２<br>"
      }
    },
    {
      "type": "code",
      "data": {
        "code": "import As as P"
      }
    },
    {
      "type": "table",
      "data": {
        "content": [
          [
            "a",
            "a"
          ],
          [
            "a",
            "a"
          ]
        ]
      }
    }
  ],
  "version": "2.18.0"
}`
    };
  },
  methods: {
    save: function () {
      editor.save().then(savedData => {
        console.log(savedData);
        this.value = savedData;
      });
    },
    myEditor: function () {
      window.editor = new EditorJS({
        holder: "codex-editor",
        autofocus: true,
        /**
         * This Tool will be used as default
         */
        initialBlock: "paragraph",
        data: JSON.parse(this.text),
        tools: {
          header: {
            class: Header,
            shortcut: "CMD+SHIFT+H",
            inlineToolbar: true
          },
          image: SimpleImage,
          delimiter: Delimiter,
          list: {
            class: List,
            inlineToolbar: true
          },
          checklist: {
            class: Checklist,
            inlineToolbar: true
          },
          quote: {
            class: Quote,
            inlineToolbar: true,
            config: {
              quotePlaceholder: "Enter a quote",
              captionPlaceholder: "Quote's author"
            },
            shortcut: "CMD+SHIFT+O"
          },
          warning: Warning,
          inlineCode: {
            class: InlineCode,
            shortcut: "CMD+SHIFT+M"
          },
          marker: {
            class: Marker,
            shortcut: "CMD+SHIFT+M"
          },
          code: {
            class: CodeTool,
            shortcut: "CMD+SHIFT+C"
          },
          table: {
            class: Table,
            inlineToolbar: true,
            shortcut: "CMD+ALT+T"
          },
          paragraph: {
            class: Paragraph,
            config: {
              placeholder: ".",
              inlineToolbar: true
            }
          }
        },
        onChange: function () {
          console.log("change");
        }
      });
    }
  },
  mounted: function () {
    this.myEditor();
  }
};
</script>

<style lang="css" scoped>
/*   ------------------------------------------------------------
                            CSS Grid
 ------------------------------------------------------------*/
/* #css-grid { */
/*   display: grid; */
/*   grid-template-rows: 1fr; */
/*   grid-template-columns: 50% 50%; */
/*   grid-template-areas: "form tips"; */
/* } */
/*  */
/* #form-area { */
/*   grid-area: form; */
/* } */
/* #tips-area { */
/*   grid-area: tips; */
/* } */
/*  */
.editorx_body {
   box-sizing: border-box;
  border-radius: 50px; 
   /* padding: 50px;  */
  /* box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);  */
 } 
</style>
