<template>
  <div class="editor">
    <!------------------------------------------------------------------------>
    <!--                       Editor Menu Bar                              -->
    <!------------------------------------------------------------------------>
    <editor-menu-bar :editor="editor" v-slot="{ commands, isActive }">
      <div class="menubar">
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bold() }"
          @click="commands.bold"
        >
          <span class="material-icons">
<img src="../../../assets/icons/bold.svg" width="20" height="20">
          </span>
        </button>
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.italic() }"
          @click="commands.italic"
        >
<img src="../../../assets/icons/italic.svg" width="20" height="20">

        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.strike() }"
          @click="commands.strike"
        >
<img src="../../../assets/icons/strike.svg" width="20" height="20">

        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.underline() }"
          @click="commands.underline"
        >
<img src="../../../assets/icons/underline.svg" width="20" height="20">

        </button>

        <button
          class="menubar__button"
          :class="{ 'is-ctive': isActive.code() }"
          @click="commands.code"
        >
<img src="../../../assets/icons/code.svg" width="20" height="20">

        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.paragraph() }"
          @click="commands.paragraph"
        >
<img src="../../../assets/icons/paragraph.svg" width="20" height="20">
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          <!-- <icon name="ul" /> -->
         <img src="../../../assets/icons/ul.svg" width="20" height="20">

        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          <!-- <icon name="ol" /> -->
         <img src="../../../assets/icons/ol.svg" width="20" height="20">
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.blockquote() }"
          @click="commands.blockquote"
        >
          <!-- <icon name="quote" /> -->
         <img src="../../../assets/icons/quote.svg" width="20" height="20">
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code_block() }"
          @click="commands.code_block"
        >
          <!-- <icon name="code" /> -->
         <img src="../../../assets/icons/code.svg" width="20" height="20">
        </button>

        <button class="menubar__button" @click="commands.horizontal_rule">
          <!-- <icon name="hr" /> -->
         <img src="../../../assets/icons/hr.svg" width="20" height="20">
        </button>

        <button class="menubar__button" @click="commands.undo">
          <!-- <icon name="undo" /> -->
         <img src="../../../assets/icons/undo.svg" width="20" height="20">
        </button>

        <button class="menubar__button" @click="commands.redo">
          <!-- <icon name="redo" /> -->
         <img src="../../../assets/icons/redo.svg" width="20" height="20">
        </button>
      </div>
    </editor-menu-bar>

    <!------------------------------------------------------------------------>
    <!--                       Editor Floating Bar                              -->
    <!------------------------------------------------------------------------>

    <editor-floating-menu
      :editor="editor"
      v-slot="{ commands, isActive, menu }"
    >
      <div
        class="editor__floating-menu"
        :class="{ 'is-active': menu.isActive }"
        :style="`top: ${menu.top}px`"
      >
        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 1 }) }"
          @click="commands.heading({ level: 1 })"
        >
          H1
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 2 }) }"
          @click="commands.heading({ level: 2 })"
        >
          H2
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.heading({ level: 3 }) }"
          @click="commands.heading({ level: 3 })"
        >
          H3
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.bullet_list() }"
          @click="commands.bullet_list"
        >
          <icon name="ul" /> ul
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.ordered_list() }"
          @click="commands.ordered_list"
        >
          <icon name="ol" /> ol
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.blockquote() }"
          @click="commands.blockquote"
        >
          <icon name="quote" /> quote
        </button>

        <button
          class="menubar__button"
          :class="{ 'is-active': isActive.code_block() }"
          @click="commands.code_block"
        >
          <icon name="code" /> code
        </button>
      </div>
    </editor-floating-menu>

    <div class="editor-view">
      <editor-content class="editor__content" :editor="editor" />
    </div>

    <!--   clear & output as HTML / JSON    -->
    <div class="actions">
      <button class="button" @click="clearContent">
        Clear Content
      </button>
      <button class="button" @click="setContent">
        Set Content
      </button>
    </div>

    <div class="export">
      <h3>JSON</h3>
      <pre><code v-html="json"></code></pre>

      <h3>HTML</h3>
      <pre><code>{{ html }}</code></pre>
    </div>
  </div>
</template>

<script>
// import Icon from 'Components/Icon'
import {
  Editor,
  EditorContent,
  EditorMenuBar,
  EditorFloatingMenu
} from "tiptap";
import {
  Blockquote,
  CodeBlock,
  HardBreak,
  Heading,
  HorizontalRule,
  OrderedList,
  BulletList,
  ListItem,
  TodoItem,
  TodoList,
  Bold,
  Code,
  Italic,
  Link,
  Strike,
  Underline,
  History
} from "tiptap-extensions";

export default {
  components: {
    EditorContent,
    EditorMenuBar,
    EditorFloatingMenu
    // Icon,
  },
  data() {
    return {
      editor: new Editor({
        extensions: [
          new Blockquote(),
          new BulletList(),
          new CodeBlock(),
          new HardBreak(),
          new Heading({ levels: [1, 2, 3] }),
          new HorizontalRule(),
          new ListItem(),
          new OrderedList(),
          new TodoItem(),
          new TodoList(),
          new Link(),
          new Bold(),
          new Code(),
          new Italic(),
          new Strike(),
          new Underline(),
          new History()
        ],
        content: `<h2>Hi there,</h2><p>this is a very <em>basic</em> example of tiptap.</p><pre><code>body { display: none; }</code></pre><ul><li><p>A regular list</p></li><li><p>With regular ite</p></li></ul><blockquote><p>It's amazing 👏 <br>– mom</p></blockquote>`,
        onUpdate: ({ getJSON, getHTML }) => {
          this.json = getJSON();
          this.html = getHTML();
        }
      }),
      json: "Update content to see changes",
      html: "Update content to see changes"
    };
  },
  beforeDestroy() {
    this.editor.destroy();
  },
  methods: {
    clearContent() {
      this.editor.clearContent(true);
      this.editor.focus();
    },
    setContent() {
      // you can pass a json document
      this.editor.setContent(
        {
          type: "doc",
          content: [
            {
              type: "paragraph",
              content: [
                {
                  type: "text",
                  text: "This is some inserted text. 👋"
                }
              ]
            }
          ]
        },
        true
      );

      // HTML string is also supported
      // this.editor.setContent('<p>This is some inserted text. 👋</p>')

      this.editor.focus();
    }
  }
};
</script>

<style scoped lang="scss">
.editor {
  background: #f8f8f8;
}

.editor {
  position: relative;
  &__floating-menu {
    position: absolute;
    z-index: 1;
    margin-top: -0.25rem;
    visibility: hidden;
    opacity: 0;
    transition: opacity 0.2s, visibility 0.2s;
    &.is-active {
      opacity: 1;
      visibility: visible;
    }
  }
}

.editor-view {
  box-shadow: 5px 5px 4px rgba(0, 0, 0, 0.25);
}
</style>


<style scoped>
.editor {
  position: relative;
  max-width: 30rem;
  margin: 0 auto 5rem auto;
}
.editor__content {
  overflow-wrap: break-word;
  word-wrap: break-word;
  word-break: break-word;
}
.editor__content * {
  caret-color: currentColor;
}
.editor__content pre {
  padding: 0.7rem 1rem;
  border-radius: 5px;
  background: black;
  color: white;
  font-size: 0.8rem;
  overflow-x: auto;
}
.editor__content pre code {
  display: block;
}
.editor__content p code {
  padding: 0.2rem 0.4rem;
  border-radius: 5px;
  font-size: 0.8rem;
  font-weight: bold;
  background: rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.8);
}
.editor__content ul,
.editor__content ol {
  padding-left: 1rem;
}
.editor__content li > p,
.editor__content li > ol,
.editor__content li > ul {
  margin: 0;
}
.editor__content a {
  color: inherit;
}
.editor__content blockquote {
  border-left: 3px solid rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.8);
  padding-left: 0.8rem;
  font-style: italic;
}
.editor__content blockquote p {
  margin: 0;
}
.editor__content img {
  max-width: 100%;
  border-radius: 3px;
}
.editor__content table {
  border-collapse: collapse;
  table-layout: fixed;
  width: 100%;
  margin: 0;
  overflow: hidden;
}
.editor__content table td, .editor__content table th {
  min-width: 1em;
  border: 2px solid grey;
  padding: 3px 5px;
  vertical-align: top;
  box-sizing: border-box;
  position: relative;
}
.editor__content table td > *, .editor__content table th > * {
  margin-bottom: 0;
}
.editor__content table th {
  font-weight: bold;
  text-align: left;
}
.editor__content table .selectedCell:after {
  z-index: 2;
  position: absolute;
  content: "";
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background: rgba(200, 200, 255, 0.4);
  pointer-events: none;
}
.editor__content table .column-resize-handle {
  position: absolute;
  right: -2px;
  top: 0;
  bottom: 0;
  width: 4px;
  z-index: 20;
  background-color: #adf;
  pointer-events: none;
}
.editor__content .tableWrapper {
  margin: 1em 0;
  overflow-x: auto;
}
.editor__content .resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}
</style>