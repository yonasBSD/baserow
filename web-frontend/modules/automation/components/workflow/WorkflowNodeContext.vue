<template>
  <Context class="workflow-node__context">
    <ul class="select__items">
      <li
        v-for="nodeType in nodeTypes"
        :key="nodeType.getType()"
        class="select__item"
      >
        <a class="select__item-link" @click="onChange(nodeType.getType())"
          ><div class="select__item-name">
            <i
              v-if="!nodeType.image"
              class="select__item-icon"
              :class="nodeType.iconClass"
            />
            <img
              v-else
              :alt="nodeType.name"
              :src="nodeType.image"
              class="select__item-image"
            />
            <span :title="nodeType.name" class="select__item-name-text">{{
              nodeType.name
            }}</span>
          </div>
          <div class="select__item-description">
            {{ nodeType.description }}
          </div></a
        >
      </li>
    </ul>
  </Context>
</template>

<script>
import context from '@baserow/modules/core/mixins/context'
export default {
  name: 'WorkflowNodeContext',
  mixins: [context],
  props: {
    node: {
      type: Object,
      required: false,
      default: () => null,
    },
  },
  computed: {
    editingTriggerNode() {
      return this.node
        ? this.$registry.get('node', this.node.type).isTrigger
        : false
    },
    /**
     * Returns an array of node types that can be listed in the context.
     * If we are offering the option to replace an existing node's type,
     * then we will omit `this.node.type` from the array, and then present
     * other nodes of the same 'category' (i.e. trigger or action). If we
     * aren't replacing an existing node, then we will show all node types
     * for a single category (i.e. trigger or action), depending on whether
     * there is a trigger or not.
     */
    nodeTypes() {
      return this.$registry
        .getOrderedList('node')
        .filter(
          (nodeType) =>
            this.node?.type !== nodeType.type &&
            (this.editingTriggerNode
              ? nodeType.isTrigger
              : nodeType.isWorkflowAction)
        )
    },
  },
  methods: {
    onChange(nodeType) {
      this.hide()
      this.$emit('change', nodeType)
    },
  },
}
</script>
