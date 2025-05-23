<template>
  <ABFormGroup
    :label="labelResolved"
    :required="element.required"
    :error-message="displayFormDataError ? $t('error.requiredField') : ''"
  >
    <Rating
      :value="inputValue"
      :max-value="element.max_value"
      :custom-color="resolveColor(element.color, colorVariables)"
      :rating-style="element.rating_style || 'star'"
      show-unselected
      @update="inputValue = $event"
    />
  </ABFormGroup>
</template>

<script>
import Rating from '@baserow/modules/database/components/Rating'
import formElement from '@baserow/modules/builder/mixins/formElement'
import {
  ensurePositiveInteger,
  ensureString,
} from '@baserow/modules/core/utils/validator'
import { useVuelidate } from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default {
  name: 'RatingInputElement',
  components: {
    Rating,
  },
  mixins: [formElement],
  setup() {
    return { v$: useVuelidate() }
  },
  computed: {
    resolvedDefaultValue() {
      try {
        return ensurePositiveInteger(this.resolveFormula(this.element.value))
      } catch {
        return 0
      }
    },
    labelResolved() {
      return ensureString(this.resolveFormula(this.element.label))
    },
    rules() {
      return {
        formElementData: {
          value: this.element.required ? { required } : {},
        },
      }
    },
  },
  watch: {
    resolvedDefaultValue: {
      handler(value) {
        this.inputValue = value
      },
      immediate: true,
    },
  },
  validations() {
    return this.rules
  },
}
</script>
