import path from 'path'

import { routes } from './routes'

import en from './locales/en.json'
import fr from './locales/fr.json'
import nl from './locales/nl.json'
import de from './locales/de.json'
import es from './locales/es.json'
import it from './locales/it.json'
import pl from './locales/pl.json'
import ko from './locales/ko.json'

export default function () {
  this.nuxt.hook('i18n:extend-messages', (additionalMessages) => {
    additionalMessages.push({ en, fr, nl, de, es, it, pl, ko })
  })

  // Register new alias to the web-frontend directory.
  this.options.alias['@baserow_premium'] = path.resolve(__dirname, './')

  // Remove the existing index route and add our own routes.
  this.extendRoutes((configRoutes) => {
    configRoutes.push(...routes)
  })

  this.appendPlugin({
    src: path.resolve(__dirname, 'plugin.js'),
  })
  this.appendPlugin({ src: path.resolve(__dirname, 'plugins/license.js') })

  // Override Baserow's existing default.scss in favor of our own because that one
  // imports the original. We do this so that we can use the existing variables,
  // mixins, placeholders etc.
  this.options.css[0] = path.resolve(__dirname, 'assets/scss/default.scss')

  if (this.options.publicRuntimeConfig) {
    this.options.publicRuntimeConfig.BASEROW_PREMIUM_GROUPED_AGGREGATE_SERVICE_MAX_SERIES =
      process.env.BASEROW_PREMIUM_GROUPED_AGGREGATE_SERVICE_MAX_SERIES || 3
    // This environment variable exist for the SaaS to override the pricing URL, so
    // that the user can be redirected to the correct URL.
    this.options.publicRuntimeConfig.BASEROW_PRICING_URL =
      process.env.BASEROW_PRICING_URL || null
  }
}
