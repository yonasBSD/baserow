import Vue from 'vue'

import ABButton from '@baserow/modules/builder/components/elements/baseComponents/ABButton'
import ABInput from '@baserow/modules/builder/components/elements/baseComponents/ABInput'
import ABFormGroup from '@baserow/modules/builder/components/elements/baseComponents/ABFormGroup'
import ABLink from '@baserow/modules/builder/components/elements/baseComponents/ABLink'
import ABHeading from '@baserow/modules/builder/components/elements/baseComponents/ABHeading'
import ABDropdown from '@baserow/modules/builder/components/elements/baseComponents/ABDropdown'
import ABDropdownItem from '@baserow/modules/builder/components/elements/baseComponents/ABDropdownItem'

function setupVueForAB(Vue) {
  Vue.component('ABButton', ABButton)
  Vue.component('ABInput', ABInput)
  Vue.component('ABFormGroup', ABFormGroup)
  Vue.component('ABLink', ABLink)
  Vue.component('ABHeading', ABHeading)
  Vue.component('ABDropdown', ABDropdown)
  Vue.component('ABDropdownItem', ABDropdownItem)
}

setupVueForAB(Vue)

export { setupVueForAB }
