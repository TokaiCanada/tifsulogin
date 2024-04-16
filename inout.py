def find_difference(css_block1, css_block2):
    # Split CSS blocks into lines
    lines1 = css_block1.split('\n')
    lines2 = css_block2.split('\n')

    # Find lines in css_block1 but not in css_block2
    not_in_css_block2 = [line for line in lines1 if line not in lines2]

    # Find lines in css_block2 but not in css_block1
    not_in_css_block1 = [line for line in lines2 if line not in lines1]

    return not_in_css_block2, not_in_css_block1

# Example CSS blocks
css_block1 = """/*!
 * Bootstrap v5.0.0-beta1 (https://getbootstrap.com/)
 * Copyright 2011-2020 The Bootstrap Authors
 * Copyright 2011-2020 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
 */
/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
:root {
  --bs-blue: #0d6efd;
  --bs-indigo: #6610f2;
  --bs-purple: #6f42c1;
  --bs-pink: #d63384;
  --bs-red: #dc3545;
  --bs-orange: #fd7e14;
  --bs-yellow: #ffc107;
  --bs-green: #198754;
  --bs-teal: #20c997;
  --bs-cyan: #0dcaf0;
  --bs-white: #fff;
  --bs-gray: #6c757d;
  --bs-gray-dark: #343a40;
  --bs-primary: #222222;
  --bs-secondary: #767676;
  --bs-success: #def2d7;
  --bs-info: #cde9f6;
  --bs-warning: #f7f3d7;
  --bs-danger: #ecc8c5;
  --bs-light: #e4e4e4;
  --bs-lighter: #faf9f8;
  --bs-dark: #222222;
  --bs-red: #c32929;
  --bs-beige: #b9a16b;
  --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

@media (prefers-reduced-motion: no-preference) {
  :root {
    scroll-behavior: smooth;
  }
}

body {
  margin: 0;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

[tabindex="-1"]:focus:not(:focus-visible) {
  outline: 0 !important;
}

hr {
  margin: 1rem 0;
  color: inherit;
  background-color: currentColor;
  border: 0;
  opacity: 0.25;
}

hr:not([size]) {
  height: 1px;
}

h1,
.h1,
h2,
.h2,
h3,
.h3,
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
}

h1,
.h1 {
  font-size: calc(1.5625rem + 3.75vw);
}

@media (min-width: 1200px) {

  h1,
  .h1 {
    font-size: 4.375rem;
  }
}

h2,
.h2 {
  font-size: calc(1.3rem + 0.6vw);
}

@media (min-width: 1200px) {

  h2,
  .h2 {
    font-size: 1.75rem;
  }
}

h3,
.h3 {
  font-size: calc(1.2875rem + 0.45vw);
}

@media (min-width: 1200px) {

  h3,
  .h3 {
    font-size: 1.625rem;
  }
}

h4,
.h4 {
  font-size: 1.25rem;
}

h5,
.h5 {
  font-size: 1.125rem;
}

h6,
.h6 {
  font-size: 1rem;
}

p {
  margin-top: 0;
  margin-bottom: 1rem;
}

abbr[title],
abbr[data-bs-original-title] {
  text-decoration: underline;
  text-decoration: underline dotted;
  cursor: help;
  text-decoration-skip-ink: none;
}

address {
  margin-bottom: 1rem;
  font-style: normal;
  line-height: inherit;
}

ol,
ul {
  padding-left: 2rem;
}

ol,
ul,
dl {
  margin-top: 0;
  margin-bottom: 1rem;
}

ol ol,
ul ul,
ol ul,
ul ol {
  margin-bottom: 0;
}

dt {
  font-weight: 700;
}

dd {
  margin-bottom: .5rem;
  margin-left: 0;
}

blockquote {
  margin: 0 0 1rem;
}

b,
strong {
  font-weight: bolder;
}

small,
.small {
  font-size: 0.875em;
}

mark,
.mark {
  padding: 0.2em;
  background-color: #fcf8e3;
}

sub,
sup {
  position: relative;
  font-size: 0.75em;
  line-height: 0;
  vertical-align: baseline;
}

sub {
  bottom: -.25em;
}

sup {
  top: -.5em;
}

a {
  color: #222222;
  text-decoration: none;
}

a:hover {
  color: #1b1b1b;
}

a:not([href]):not([class]),
a:not([href]):not([class]):hover {
  color: inherit;
  text-decoration: none;
}

pre,
code,
kbd,
samp {
  font-family: var(--bs-font-monospace);
  font-size: 1em;
  direction: ltr
    /* rtl:ignore */
  ;
  unicode-bidi: bidi-override;
}

pre {
  display: block;
  margin-top: 0;
  margin-bottom: 1rem;
  overflow: auto;
  font-size: 0.875em;
}

pre code {
  font-size: inherit;
  color: inherit;
  word-break: normal;
}

code {
  font-size: 0.875em;
  color: #d63384;
  word-wrap: break-word;
}

a>code {
  color: inherit;
}

kbd {
  padding: 0.2rem 0.4rem;
  font-size: 0.875em;
  color: #fff;
  background-color: #222222;
  border-radius: 0.2rem;
}

kbd kbd {
  padding: 0;
  font-size: 1em;
  font-weight: 700;
}

figure {
  margin: 0 0 1rem;
}

img,
svg {
  vertical-align: middle;
}

table {
  caption-side: bottom;
  border-collapse: collapse;
}

caption {
  padding-top: 1.53125rem;
  padding-bottom: 1.53125rem;
  color: #6c757d;
  text-align: left;
}

th {
  font-weight: 500;
  text-align: inherit;
  text-align: -webkit-match-parent;
}

thead,
tbody,
tfoot,
tr,
td,
th {
  border-color: inherit;
  border-style: solid;
  border-width: 0;
}

label {
  display: inline-block;
}

button {
  border-radius: 0;
}

button:focus {
  outline: 0;
}

input,
button,
select,
optgroup,
textarea {
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

button,
select {
  text-transform: none;
}

[role="button"] {
  cursor: pointer;
}

select {
  word-wrap: normal;
}

[list]::-webkit-calendar-picker-indicator {
  display: none;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

button:not(:disabled),
[type="button"]:not(:disabled),
[type="reset"]:not(:disabled),
[type="submit"]:not(:disabled) {
  cursor: pointer;
}

::-moz-focus-inner {
  padding: 0;
  border-style: none;
}

textarea {
  resize: vertical;
}

fieldset {
  min-width: 0;
  padding: 0;
  margin: 0;
  border: 0;
}

legend {
  float: left;
  width: 100%;
  padding: 0;
  margin-bottom: 0.5rem;
  font-size: calc(1.275rem + 0.3vw);
  line-height: inherit;
}

@media (min-width: 1200px) {
  legend {
    font-size: 1.5rem;
  }
}

legend+* {
  clear: left;
}

::-webkit-datetime-edit-fields-wrapper,
::-webkit-datetime-edit-text,
::-webkit-datetime-edit-minute,
::-webkit-datetime-edit-hour-field,
::-webkit-datetime-edit-day-field,
::-webkit-datetime-edit-month-field,
::-webkit-datetime-edit-year-field {
  padding: 0;
}

::-webkit-inner-spin-button {
  height: auto;
}

[type="search"] {
  outline-offset: -2px;
  -webkit-appearance: textfield;
}

/* rtl:raw:
[type="tel"],
[type="url"],
[type="email"],
[type="number"] {
  direction: ltr;
}
*/
::-webkit-search-decoration {
  -webkit-appearance: none;
}

::-webkit-color-swatch-wrapper {
  padding: 0;
}

::file-selector-button {
  font: inherit;
}

::-webkit-file-upload-button {
  font: inherit;
  -webkit-appearance: button;
}

output {
  display: inline-block;
}

iframe {
  border: 0;
}

summary {
  display: list-item;
  cursor: pointer;
}

progress {
  vertical-align: baseline;
}

[hidden] {
  display: none !important;
}

.lead {
  font-size: 1.25rem;
  font-weight: 300;
}

.display-1 {
  font-size: calc(1.625rem + 4.5vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-1 {
    font-size: 5rem;
  }
}

.display-2 {
  font-size: calc(1.575rem + 3.9vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-2 {
    font-size: 4.5rem;
  }
}

.display-3 {
  font-size: calc(1.525rem + 3.3vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-3 {
    font-size: 4rem;
  }
}

.display-4 {
  font-size: calc(1.475rem + 2.7vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-4 {
    font-size: 3.5rem;
  }
}

.display-5 {
  font-size: calc(1.425rem + 2.1vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-5 {
    font-size: 3rem;
  }
}

.display-6 {
  font-size: calc(1.375rem + 1.5vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-6 {
    font-size: 2.5rem;
  }
}

.list-unstyled {
  padding-left: 0;
  list-style: none;
}

.list-inline {
  padding-left: 0;
  list-style: none;
}

.list-inline-item {
  display: inline-block;
}

.list-inline-item:not(:last-child) {
  margin-right: 0.5rem;
}

.initialism {
  font-size: 0.875em;
  text-transform: uppercase;
}

.blockquote {
  margin-bottom: 1rem;
  font-size: 1rem;
}

.blockquote> :last-child {
  margin-bottom: 0;
}

.blockquote-footer {
  margin-top: -1rem;
  margin-bottom: 1rem;
  font-size: 0.875rem;
  color: #6c757d;
}

.blockquote-footer::before {
  content: "\2014\00A0";
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.img-thumbnail {
  padding: 0.25rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  max-width: 100%;
  height: auto;
}

.figure {
  display: inline-block;
}

.figure-img {
  margin-bottom: 0.5rem;
  line-height: 1;
}

.figure-caption {
  font-size: 0.875em;
  color: #6c757d;
}

.container,
.container-fluid,
.container-sm,
.container-md,
.container-lg,
.container-xl,
.container-xxl {
  width: 100%;
  padding-right: var(--bs-gutter-x, 0.9375rem);
  padding-left: var(--bs-gutter-x, 0.9375rem);
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 576px) {

  .container,
  .container-sm {
    max-width: 540px;
  }
}

@media (min-width: 768px) {

  .container,
  .container-sm,
  .container-md {
    max-width: 720px;
  }
}

@media (min-width: 992px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg {
    max-width: 960px;
  }
}

@media (min-width: 1200px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl {
    max-width: 1140px;
  }
}

@media (min-width: 1500px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl,
  .container-xxl {
    max-width: 1440px;
  }
}

.fade {
  transition: opacity 0.15s linear;
}

@media (prefers-reduced-motion: reduce) {
  .fade {
    transition: none;
  }
}

.fade:not(.show) {
  opacity: 0;
}

.collapse:not(.show) {
  display: none;
}

.collapsing {
  height: 0;
  overflow: hidden;
  transition: height 0.35s ease;
}

@media (prefers-reduced-motion: reduce) {
  .collapsing {
    transition: none;
  }
}

.dropup,
.dropend,
.dropdown,
.dropstart {
  position: relative;
}

.dropdown-toggle {
  white-space: nowrap;
}

.dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid;
  border-right: 0.3em solid transparent;
  border-bottom: 0;
  border-left: 0.3em solid transparent;
}

.dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0.125rem 0 0;
  font-size: 1rem;
  color: #222222;
  text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem;
}

.dropdown-menu[style] {
  right: auto !important;
}

.dropdown-menu-start {
  --bs-position: start;
  right: auto
    /* rtl:ignore */
  ;
  left: 0
    /* rtl:ignore */
  ;
}

.dropdown-menu-end {
  --bs-position: end;
  right: 0
    /* rtl:ignore */
  ;
  left: auto
    /* rtl:ignore */
  ;
}

@media (min-width: 576px) {
  .dropdown-menu-sm-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-sm-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 768px) {
  .dropdown-menu-md-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-md-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 992px) {
  .dropdown-menu-lg-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-lg-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1200px) {
  .dropdown-menu-xl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1500px) {
  .dropdown-menu-xxl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xxl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1700px) {
  .dropdown-menu-xxxl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xxxl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

.dropup .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-top: 0;
  margin-bottom: 0.125rem;
}

.dropup .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0;
  border-right: 0.3em solid transparent;
  border-bottom: 0.3em solid;
  border-left: 0.3em solid transparent;
}

.dropup .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropend .dropdown-menu {
  top: 0;
  right: auto;
  left: 100%;
  margin-top: 0;
  margin-left: 0.125rem;
}

.dropend .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0;
  border-bottom: 0.3em solid transparent;
  border-left: 0.3em solid;
}

.dropend .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropend .dropdown-toggle::after {
  vertical-align: 0;
}

.dropstart .dropdown-menu {
  top: 0;
  right: 100%;
  left: auto;
  margin-top: 0;
  margin-right: 0.125rem;
}

.dropstart .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
}

.dropstart .dropdown-toggle::after {
  display: none;
}

.dropstart .dropdown-toggle::before {
  display: inline-block;
  margin-right: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0.3em solid;
  border-bottom: 0.3em solid transparent;
}

.dropstart .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropstart .dropdown-toggle::before {
  vertical-align: 0;
}

.dropdown-divider {
  height: 0;
  margin: 0.5rem 0;
  overflow: hidden;
  border-top: 1px solid rgba(0, 0, 0, 0.15);
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: 0.25rem 1rem;
  clear: both;
  font-weight: 400;
  color: #222222;
  text-align: inherit;
  white-space: nowrap;
  background-color: transparent;
  border: 0;
}

.dropdown-item:hover,
.dropdown-item:focus {
  color: #1f1f1f;
  background-color: #f8f9fa;
}

.dropdown-item.active,
.dropdown-item:active {
  color: #fff;
  text-decoration: none;
  background-color: #222222;
}

.dropdown-item.disabled,
.dropdown-item:disabled {
  color: #6c757d;
  pointer-events: none;
  background-color: transparent;
}

.dropdown-menu.show {
  display: block;
}

.dropdown-header {
  display: block;
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  color: #6c757d;
  white-space: nowrap;
}

.dropdown-item-text {
  display: block;
  padding: 0.25rem 1rem;
  color: #222222;
}

.dropdown-menu-dark {
  color: #dee2e6;
  background-color: #343a40;
  border-color: rgba(0, 0, 0, 0.15);
}

.dropdown-menu-dark .dropdown-item {
  color: #dee2e6;
}

.dropdown-menu-dark .dropdown-item:hover,
.dropdown-menu-dark .dropdown-item:focus {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.15);
}

.dropdown-menu-dark .dropdown-item.active,
.dropdown-menu-dark .dropdown-item:active {
  color: #fff;
  background-color: #222222;
}

.dropdown-menu-dark .dropdown-item.disabled,
.dropdown-menu-dark .dropdown-item:disabled {
  color: #adb5bd;
}

.dropdown-menu-dark .dropdown-divider {
  border-color: rgba(0, 0, 0, 0.15);
}

.dropdown-menu-dark .dropdown-item-text {
  color: #dee2e6;
}

.dropdown-menu-dark .dropdown-header {
  color: #adb5bd;
}

.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-flex;
  vertical-align: middle;
}

.btn-group>.btn,
.btn-group-vertical>.btn {
  position: relative;
  flex: 1 1 auto;
}

.btn-group>.btn-check:checked+.btn,
.btn-group>.btn-check:focus+.btn,
.btn-group>.btn:hover,
.btn-group>.btn:focus,
.btn-group>.btn:active,
.btn-group>.btn.active,
.btn-group-vertical>.btn-check:checked+.btn,
.btn-group-vertical>.btn-check:focus+.btn,
.btn-group-vertical>.btn:hover,
.btn-group-vertical>.btn:focus,
.btn-group-vertical>.btn:active,
.btn-group-vertical>.btn.active {
  z-index: 1;
}

.btn-toolbar {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.btn-toolbar .input-group {
  width: auto;
}

.btn-group>.btn:not(:first-child),
.btn-group>.btn-group:not(:first-child) {
  margin-left: -1px;
}

.btn-group>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group>.btn-group:not(:last-child)>.btn {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.btn-group>.btn:nth-child(n + 3),
.btn-group> :not(.btn-check)+.btn,
.btn-group>.btn-group:not(:first-child)>.btn {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.dropdown-toggle-split {
  padding-right: 2.34375rem;
  padding-left: 2.34375rem;
}

.dropdown-toggle-split::after,
.dropup .dropdown-toggle-split::after,
.dropend .dropdown-toggle-split::after {
  margin-left: 0;
}

.dropstart .dropdown-toggle-split::before {
  margin-right: 0;
}

.btn-sm+.dropdown-toggle-split,
.btn-group-sm>.btn+.dropdown-toggle-split {
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
}

.btn-lg+.dropdown-toggle-split,
.btn-group-lg>.btn+.dropdown-toggle-split {
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
}

.btn-group-vertical {
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.btn-group-vertical>.btn,
.btn-group-vertical>.btn-group {
  width: 100%;
}

.btn-group-vertical>.btn:not(:first-child),
.btn-group-vertical>.btn-group:not(:first-child) {
  margin-top: -1px;
}

.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group-vertical>.btn-group:not(:last-child)>.btn {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.btn-group-vertical>.btn~.btn,
.btn-group-vertical>.btn-group:not(:first-child)>.btn {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.navbar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.navbar>.container,
.navbar>.container-fluid,
.navbar>.container-sm,
.navbar>.container-md,
.navbar>.container-lg,
.navbar>.container-xl,
.navbar>.container-xxl {
  display: flex;
  flex-wrap: inherit;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  padding-top: 0.3125rem;
  padding-bottom: 0.3125rem;
  margin-right: 1rem;
  font-size: 1.25rem;
  white-space: nowrap;
}

.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.navbar-nav .nav-link {
  padding-right: 0;
  padding-left: 0;
}

.navbar-nav .dropdown-menu {
  position: static;
}

.navbar-text {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.navbar-collapse {
  align-items: center;
  width: 100%;
}

.navbar-toggler {
  padding: 0.25rem 0.75rem;
  font-size: 1.25rem;
  line-height: 1;
  background-color: transparent;
  border: 1px solid transparent;
  border-radius: 0.25rem;
  transition: box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .navbar-toggler {
    transition: none;
  }
}

.navbar-toggler:hover {
  text-decoration: none;
}

.navbar-toggler:focus {
  text-decoration: none;
  outline: 0;
  box-shadow: 0 0 0 0.25rem;
}

.navbar-toggler-icon {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
}

@media (min-width: 576px) {
  .navbar-expand-sm {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-sm .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-sm .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-sm .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-sm .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-sm .navbar-toggler {
    display: none;
  }
}

@media (min-width: 768px) {
  .navbar-expand-md {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-md .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-md .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-md .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-md .navbar-toggler {
    display: none;
  }
}

@media (min-width: 992px) {
  .navbar-expand-lg {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-lg .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-lg .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-lg .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-lg .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-lg .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1200px) {
  .navbar-expand-xl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xl .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1500px) {
  .navbar-expand-xxl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xxl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xxl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xxl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xxl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xxl .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1700px) {
  .navbar-expand-xxxl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xxxl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xxxl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xxxl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xxxl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xxxl .navbar-toggler {
    display: none;
  }
}

.navbar-expand {
  flex-wrap: nowrap;
  justify-content: flex-start;
}

.navbar-expand .navbar-nav {
  flex-direction: row;
}

.navbar-expand .navbar-nav .dropdown-menu {
  position: absolute;
}

.navbar-expand .navbar-nav .nav-link {
  padding-right: 0.5rem;
  padding-left: 0.5rem;
}

.navbar-expand .navbar-collapse {
  display: flex !important;
}

.navbar-expand .navbar-toggler {
  display: none;
}

.navbar-light .navbar-brand {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-brand:hover,
.navbar-light .navbar-brand:focus {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 0.55);
}

.navbar-light .navbar-nav .nav-link:hover,
.navbar-light .navbar-nav .nav-link:focus {
  color: rgba(0, 0, 0, 0.7);
}

.navbar-light .navbar-nav .nav-link.disabled {
  color: rgba(0, 0, 0, 0.3);
}

.navbar-light .navbar-nav .show>.nav-link,
.navbar-light .navbar-nav .nav-link.active {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-toggler {
  color: rgba(0, 0, 0, 0.55);
  border-color: rgba(0, 0, 0, 0.1);
}

.navbar-light .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%280, 0, 0, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-light .navbar-text {
  color: rgba(0, 0, 0, 0.55);
}

.navbar-light .navbar-text a,
.navbar-light .navbar-text a:hover,
.navbar-light .navbar-text a:focus {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-dark .navbar-brand {
  color: #fff;
}

.navbar-dark .navbar-brand:hover,
.navbar-dark .navbar-brand:focus {
  color: #fff;
}

.navbar-dark .navbar-nav .nav-link {
  color: rgba(255, 255, 255, 0.55);
}

.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus {
  color: rgba(255, 255, 255, 0.75);
}

.navbar-dark .navbar-nav .nav-link.disabled {
  color: rgba(255, 255, 255, 0.25);
}

.navbar-dark .navbar-nav .show>.nav-link,
.navbar-dark .navbar-nav .nav-link.active {
  color: #fff;
}

.navbar-dark .navbar-toggler {
  color: rgba(255, 255, 255, 0.55);
  border-color: rgba(255, 255, 255, 0.1);
}

.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-dark .navbar-text {
  color: rgba(255, 255, 255, 0.55);
}

.navbar-dark .navbar-text a,
.navbar-dark .navbar-text a:hover,
.navbar-dark .navbar-text a:focus {
  color: #fff;
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}

.card>hr {
  margin-right: 0;
  margin-left: 0;
}

.card>.list-group {
  border-top: inherit;
  border-bottom: inherit;
}

.card>.list-group:first-child {
  border-top-width: 0;
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.card>.list-group:last-child {
  border-bottom-width: 0;
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card>.card-header+.list-group,
.card>.list-group+.card-footer {
  border-top: 0;
}

.card-body {
  flex: 1 1 auto;
  padding: 1rem 1rem;
}

.card-title {
  margin-bottom: 0.5rem;
}

.card-subtitle {
  margin-top: -0.25rem;
  margin-bottom: 0;
}

.card-text:last-child {
  margin-bottom: 0;
}

.card-link:hover {
  text-decoration: none;
}

.card-link+.card-link {
  margin-left: 1rem
    /* rtl:ignore */
  ;
}

.card-header {
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  background-color: rgba(0, 0, 0, 0.03);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}

.card-header:first-child {
  border-radius: calc(0.25rem - 1px) calc(0.25rem - 1px) 0 0;
}

.card-footer {
  padding: 0.5rem 1rem;
  background-color: rgba(0, 0, 0, 0.03);
  border-top: 1px solid rgba(0, 0, 0, 0.125);
}

.card-footer:last-child {
  border-radius: 0 0 calc(0.25rem - 1px) calc(0.25rem - 1px);
}

.card-header-tabs {
  margin-right: -0.5rem;
  margin-bottom: -0.5rem;
  margin-left: -0.5rem;
  border-bottom: 0;
}

.card-header-pills {
  margin-right: -0.5rem;
  margin-left: -0.5rem;
}

.card-img-overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 1rem;
  border-radius: calc(0.25rem - 1px);
}

.card-img,
.card-img-top,
.card-img-bottom {
  width: 100%;
}

.card-img,
.card-img-top {
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.card-img,
.card-img-bottom {
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-group>.card {
  margin-bottom: 0.75rem;
}

@media (min-width: 576px) {
  .card-group {
    display: flex;
    flex-flow: row wrap;
  }

  .card-group>.card {
    flex: 1 0 0%;
    margin-bottom: 0;
  }

  .card-group>.card+.card {
    margin-left: 0;
    border-left: 0;
  }

  .card-group>.card:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  .card-group>.card:not(:last-child) .card-img-top,
  .card-group>.card:not(:last-child) .card-header {
    border-top-right-radius: 0;
  }

  .card-group>.card:not(:last-child) .card-img-bottom,
  .card-group>.card:not(:last-child) .card-footer {
    border-bottom-right-radius: 0;
  }

  .card-group>.card:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  .card-group>.card:not(:first-child) .card-img-top,
  .card-group>.card:not(:first-child) .card-header {
    border-top-left-radius: 0;
  }

  .card-group>.card:not(:first-child) .card-img-bottom,
  .card-group>.card:not(:first-child) .card-footer {
    border-bottom-left-radius: 0;
  }
}

.accordion-button {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  border-radius: 0;
  overflow-anchor: none;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, border-radius 0.15s ease;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button {
    transition: none;
  }
}

.accordion-button::after {
  flex-shrink: 0;
  margin-left: auto;
  content: "";
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  transform: rotate(90deg);
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button::after {
    transition: none;
  }
}

.accordion-button.collapsed {
  border-bottom-width: 0;
}

.accordion-button:hover {
  z-index: 2;
}

.accordion-button:focus {
  z-index: 3;
  outline: 0;
}

.accordion-header {
  margin-bottom: 0;
}

.accordion-item:last-of-type .accordion-button.collapsed {
  border-bottom-width: 1px;
}

.accordion-item:last-of-type .accordion-collapse {
  border-bottom-width: 1px;
}

.accordion-collapse {
  border: solid #eeeeee;
  border-width: 0 1px;
}

.accordion-flush .accordion-button {
  border-right: 0;
  border-left: 0;
  border-radius: 0;
}

.accordion-flush .accordion-collapse {
  border-width: 0;
}

.accordion-flush .accordion-item:first-of-type .accordion-button {
  border-top-width: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.accordion-flush .accordion-item:last-of-type .accordion-button.collapsed {
  border-bottom-width: 0;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  padding: 0 0;
  margin-bottom: 1rem;
  list-style: none;
}

.breadcrumb-item+.breadcrumb-item {
  padding-left: 0.5rem;
}

.breadcrumb-item+.breadcrumb-item::before {
  float: left;
  padding-right: 0.5rem;
  color: #6c757d;
  content: var(--bs-breadcrumb-divider, "/")
    /* rtl: var(--bs-breadcrumb-divider, "/") */
  ;
}

.breadcrumb-item.active {
  color: #6c757d;
}

.pagination {
  display: flex;
  padding-left: 0;
  list-style: none;
}

.page-link {
  position: relative;
  display: block;
  color: #222222;
  background-color: #fff;
  border: 1px solid #dee2e6;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .page-link {
    transition: none;
  }
}

.page-link:hover {
  z-index: 2;
  color: #1b1b1b;
  background-color: #e9ecef;
  border-color: #dee2e6;
}

.page-link:focus {
  z-index: 3;
  color: #1b1b1b;
  background-color: #e9ecef;
  outline: 0;
  box-shadow: none;
}

.page-item:not(:first-child) .page-link {
  margin-left: -1px;
}

.page-item.active .page-link {
  z-index: 3;
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.page-item.disabled .page-link {
  color: #6c757d;
  pointer-events: none;
  background-color: #fff;
  border-color: #dee2e6;
}

.page-link {
  padding: 0.375rem 0.75rem;
}

.page-item:first-child .page-link {
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}

.page-item:last-child .page-link {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}

.pagination-lg .page-link {
  padding: 0.75rem 1.5rem;
  font-size: 1.25rem;
}

.pagination-lg .page-item:first-child .page-link {
  border-top-left-radius: 0.3rem;
  border-bottom-left-radius: 0.3rem;
}

.pagination-lg .page-item:last-child .page-link {
  border-top-right-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem;
}

.pagination-sm .page-link {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}

.pagination-sm .page-item:first-child .page-link {
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem;
}

.pagination-sm .page-item:last-child .page-link {
  border-top-right-radius: 0.2rem;
  border-bottom-right-radius: 0.2rem;
}

.badge {
  display: inline-block;
  padding: 0.35em 0.65em;
  font-size: 0.75em;
  font-weight: 700;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25rem;
}

.badge:empty {
  display: none;
}

.btn .badge {
  position: relative;
  top: -1px;
}

@keyframes progress-bar-stripes {
  0% {
    background-position-x: 1rem;
  }
}

.progress {
  display: flex;
  height: 1rem;
  overflow: hidden;
  font-size: 0.875rem;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  background-color: #222222;
  transition: width 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
  .progress-bar {
    transition: none;
  }
}

.progress-bar-striped {
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 1rem 1rem;
}

.progress-bar-animated {
  animation: 1s linear infinite progress-bar-stripes;
}

@media (prefers-reduced-motion: reduce) {
  .progress-bar-animated {
    animation: none;
  }
}

.list-group {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  border-radius: 0.25rem;
}

.list-group-item-action {
  width: 100%;
  color: #495057;
  text-align: inherit;
}

.list-group-item-action:hover,
.list-group-item-action:focus {
  z-index: 1;
  color: #495057;
  text-decoration: none;
  background-color: #f8f9fa;
}

.list-group-item-action:active {
  color: #222222;
  background-color: #e9ecef;
}

.list-group-item {
  position: relative;
  display: block;
  padding: 0.5rem 1rem;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.125);
}

.list-group-item:first-child {
  border-top-left-radius: inherit;
  border-top-right-radius: inherit;
}

.list-group-item:last-child {
  border-bottom-right-radius: inherit;
  border-bottom-left-radius: inherit;
}

.list-group-item.disabled,
.list-group-item:disabled {
  color: #6c757d;
  pointer-events: none;
  background-color: #fff;
}

.list-group-item.active {
  z-index: 2;
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.list-group-item+.list-group-item {
  border-top-width: 0;
}

.list-group-item+.list-group-item.active {
  margin-top: -1px;
  border-top-width: 1px;
}

.list-group-horizontal {
  flex-direction: row;
}

.list-group-horizontal>.list-group-item:first-child {
  border-bottom-left-radius: 0.25rem;
  border-top-right-radius: 0;
}

.list-group-horizontal>.list-group-item:last-child {
  border-top-right-radius: 0.25rem;
  border-bottom-left-radius: 0;
}

.list-group-horizontal>.list-group-item.active {
  margin-top: 0;
}

.list-group-horizontal>.list-group-item+.list-group-item {
  border-top-width: 1px;
  border-left-width: 0;
}

.list-group-horizontal>.list-group-item+.list-group-item.active {
  margin-left: -1px;
  border-left-width: 1px;
}

@media (min-width: 576px) {
  .list-group-horizontal-sm {
    flex-direction: row;
  }

  .list-group-horizontal-sm>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-sm>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-sm>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-sm>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-sm>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 768px) {
  .list-group-horizontal-md {
    flex-direction: row;
  }

  .list-group-horizontal-md>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-md>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-md>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-md>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-md>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 992px) {
  .list-group-horizontal-lg {
    flex-direction: row;
  }

  .list-group-horizontal-lg>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-lg>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-lg>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-lg>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-lg>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1200px) {
  .list-group-horizontal-xl {
    flex-direction: row;
  }

  .list-group-horizontal-xl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1500px) {
  .list-group-horizontal-xxl {
    flex-direction: row;
  }

  .list-group-horizontal-xxl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xxl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xxl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xxl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xxl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1700px) {
  .list-group-horizontal-xxxl {
    flex-direction: row;
  }

  .list-group-horizontal-xxxl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

.list-group-flush {
  border-radius: 0;
}

.list-group-flush>.list-group-item {
  border-width: 0 0 1px;
}

.list-group-flush>.list-group-item:last-child {
  border-bottom-width: 0;
}

.list-group-item-primary {
  color: #141414;
  background-color: lightgray;
}

.list-group-item-primary.list-group-item-action:hover,
.list-group-item-primary.list-group-item-action:focus {
  color: #141414;
  background-color: #bebebe;
}

.list-group-item-primary.list-group-item-action.active {
  color: #fff;
  background-color: #141414;
  border-color: #141414;
}

.list-group-item-secondary {
  color: #474747;
  background-color: #e4e4e4;
}

.list-group-item-secondary.list-group-item-action:hover,
.list-group-item-secondary.list-group-item-action:focus {
  color: #474747;
  background-color: #cdcdcd;
}

.list-group-item-secondary.list-group-item-action.active {
  color: #fff;
  background-color: #474747;
  border-color: #474747;
}

.list-group-item-success {
  color: #596156;
  background-color: #f8fcf7;
}

.list-group-item-success.list-group-item-action:hover,
.list-group-item-success.list-group-item-action:focus {
  color: #596156;
  background-color: #dfe3de;
}

.list-group-item-success.list-group-item-action.active {
  color: #fff;
  background-color: #596156;
  border-color: #596156;
}

.list-group-item-info {
  color: #525d62;
  background-color: #f5fbfd;
}

.list-group-item-info.list-group-item-action:hover,
.list-group-item-info.list-group-item-action:focus {
  color: #525d62;
  background-color: #dde2e4;
}

.list-group-item-info.list-group-item-action.active {
  color: #fff;
  background-color: #525d62;
  border-color: #525d62;
}

.list-group-item-warning {
  color: #636156;
  background-color: #fdfdf7;
}

.list-group-item-warning.list-group-item-action:hover,
.list-group-item-warning.list-group-item-action:focus {
  color: #636156;
  background-color: #e4e4de;
}

.list-group-item-warning.list-group-item-action.active {
  color: #fff;
  background-color: #636156;
  border-color: #636156;
}

.list-group-item-danger {
  color: #5e504f;
  background-color: #fbf4f3;
}

.list-group-item-danger.list-group-item-action:hover,
.list-group-item-danger.list-group-item-action:focus {
  color: #5e504f;
  background-color: #e2dcdb;
}

.list-group-item-danger.list-group-item-action.active {
  color: #fff;
  background-color: #5e504f;
  border-color: #5e504f;
}

.list-group-item-light {
  color: #5b5b5b;
  background-color: #fafafa;
}

.list-group-item-light.list-group-item-action:hover,
.list-group-item-light.list-group-item-action:focus {
  color: #5b5b5b;
  background-color: #e1e1e1;
}

.list-group-item-light.list-group-item-action.active {
  color: #fff;
  background-color: #5b5b5b;
  border-color: #5b5b5b;
}

.list-group-item-lighter {
  color: #646463;
  background-color: #fefefe;
}

.list-group-item-lighter.list-group-item-action:hover,
.list-group-item-lighter.list-group-item-action:focus {
  color: #646463;
  background-color: #e5e5e5;
}

.list-group-item-lighter.list-group-item-action.active {
  color: #fff;
  background-color: #646463;
  border-color: #646463;
}

.list-group-item-dark {
  color: #141414;
  background-color: lightgray;
}

.list-group-item-dark.list-group-item-action:hover,
.list-group-item-dark.list-group-item-action:focus {
  color: #141414;
  background-color: #bebebe;
}

.list-group-item-dark.list-group-item-action.active {
  color: #fff;
  background-color: #141414;
  border-color: #141414;
}

.list-group-item-red {
  color: #751919;
  background-color: #f3d4d4;
}

.list-group-item-red.list-group-item-action:hover,
.list-group-item-red.list-group-item-action:focus {
  color: #751919;
  background-color: #dbbfbf;
}

.list-group-item-red.list-group-item-action.active {
  color: #fff;
  background-color: #751919;
  border-color: #751919;
}

.list-group-item-beige {
  color: #6f6140;
  background-color: #f1ece1;
}

.list-group-item-beige.list-group-item-action:hover,
.list-group-item-beige.list-group-item-action:focus {
  color: #6f6140;
  background-color: #d9d4cb;
}

.list-group-item-beige.list-group-item-action.active {
  color: #fff;
  background-color: #6f6140;
  border-color: #6f6140;
}

.toast {
  width: 350px;
  max-width: 100%;
  font-size: 0.875rem;
  pointer-events: auto;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem;
}

.toast:not(.showing):not(.show) {
  opacity: 0;
}

.toast.hide {
  display: none;
}

.toast-container {
  width: max-content;
  max-width: 100%;
  pointer-events: none;
}

.toast-container> :not(:last-child) {
  margin-bottom: 0.75rem;
}

.toast-header {
  display: flex;
  align-items: center;
  padding: 0.5rem 0.75rem;
  color: #6c757d;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.toast-header .btn-close {
  margin-right: -0.375rem;
  margin-left: 0.75rem;
}

.toast-body {
  padding: 0.75rem;
}

.modal-open {
  overflow: hidden;
}

.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  display: none;
  width: 100%;
  height: 100%;
  overflow: hidden;
  outline: 0;
}

.modal-dialog {
  position: relative;
  width: auto;
  margin: 0.5rem;
  pointer-events: none;
}

.modal.fade .modal-dialog {
  transition: transform 0.3s ease-out;
  transform: translate(0, -50px);
}

@media (prefers-reduced-motion: reduce) {
  .modal.fade .modal-dialog {
    transition: none;
  }
}

.modal.show .modal-dialog {
  transform: none;
}

.modal.modal-static .modal-dialog {
  transform: scale(1.02);
}

.modal-dialog-scrollable {
  height: calc(100% - 1rem);
}

.modal-dialog-scrollable .modal-content {
  max-height: 100%;
  overflow: hidden;
}

.modal-dialog-scrollable .modal-body {
  overflow-y: auto;
}

.modal-dialog-centered {
  display: flex;
  align-items: center;
  min-height: calc(100% - 1rem);
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  outline: 0;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1040;
  width: 100vw;
  height: 100vh;
  background-color: #000;
}

.modal-backdrop.fade {
  opacity: 0;
}

.modal-backdrop.show {
  opacity: 0.5;
}

.modal-header {
  display: flex;
  flex-shrink: 0;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2.5rem;
  border-bottom: 1px solid #dee2e6;
  border-top-left-radius: calc(0.3rem - 1px);
  border-top-right-radius: calc(0.3rem - 1px);
}

.modal-header .btn-close {
  padding: 0.75rem 1.25rem;
  margin: -0.75rem -1.25rem -0.75rem auto;
}

.modal-title {
  margin-bottom: 0;
  line-height: 1.5;
}

.modal-body {
  position: relative;
  flex: 1 1 auto;
  padding: 1.875rem 2.5rem;
}

.modal-footer {
  display: flex;
  flex-wrap: wrap;
  flex-shrink: 0;
  align-items: center;
  justify-content: flex-end;
  padding: 1.875rem 2.5rem-0.25rem;
  border-top: 1px solid #dee2e6;
  border-bottom-right-radius: calc(0.3rem - 1px);
  border-bottom-left-radius: calc(0.3rem - 1px);
}

.modal-footer>* {
  margin: 0.25rem;
}

.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 500px;
    margin: 1.75rem auto;
  }

  .modal-dialog-scrollable {
    height: calc(100% - 3.5rem);
  }

  .modal-dialog-centered {
    min-height: calc(100% - 3.5rem);
  }

  .modal-sm {
    max-width: 300px;
  }
}

@media (min-width: 992px) {

  .modal-lg,
  .modal-xl {
    max-width: 800px;
  }
}

@media (min-width: 1200px) {
  .modal-xl {
    max-width: 1140px;
  }
}

.modal-fullscreen {
  width: 100vw;
  max-width: none;
  height: 100%;
  margin: 0;
}

.modal-fullscreen .modal-content {
  height: 100%;
  border: 0;
  border-radius: 0;
}

.modal-fullscreen .modal-header {
  border-radius: 0;
}

.modal-fullscreen .modal-body {
  overflow-y: auto;
}

.modal-fullscreen .modal-footer {
  border-radius: 0;
}

@media (max-width: 575.98px) {
  .modal-fullscreen-sm-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-sm-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-sm-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-sm-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-sm-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 767.98px) {
  .modal-fullscreen-md-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-md-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-md-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-md-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-md-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 991.98px) {
  .modal-fullscreen-lg-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-lg-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-lg-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-lg-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-lg-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1199.98px) {
  .modal-fullscreen-xl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xl-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1499.98px) {
  .modal-fullscreen-xxl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xxl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xxl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xxl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xxl-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1699.98px) {
  .modal-fullscreen-xxxl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xxxl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xxxl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xxxl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xxxl-down .modal-footer {
    border-radius: 0;
  }
}

.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  margin: 0;
  font-family: "Jost", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.7143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.8125rem;
  word-wrap: break-word;
  opacity: 0;
}

.tooltip.show {
  opacity: 1;
}

.tooltip .tooltip-arrow {
  position: absolute;
  display: block;
  width: 0.8rem;
  height: 0.4rem;
}

.tooltip .tooltip-arrow::before {
  position: absolute;
  content: "";
  border-color: transparent;
  border-style: solid;
}

.bs-tooltip-top,
.bs-tooltip-auto[data-popper-placement^="top"] {
  padding: 0.4rem 0;
}

.bs-tooltip-top .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="top"] .tooltip-arrow {
  bottom: 0;
}

.bs-tooltip-top .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="top"] .tooltip-arrow::before {
  top: -1px;
  border-width: 0.4rem 0.4rem 0;
  border-top-color: #000;
}

.bs-tooltip-end,
.bs-tooltip-auto[data-popper-placement^="right"] {
  padding: 0 0.4rem;
}

.bs-tooltip-end .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="right"] .tooltip-arrow {
  left: 0;
  width: 0.4rem;
  height: 0.8rem;
}

.bs-tooltip-end .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="right"] .tooltip-arrow::before {
  right: -1px;
  border-width: 0.4rem 0.4rem 0.4rem 0;
  border-right-color: #000;
}

.bs-tooltip-bottom,
.bs-tooltip-auto[data-popper-placement^="bottom"] {
  padding: 0.4rem 0;
}

.bs-tooltip-bottom .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-arrow {
  top: 0;
}

.bs-tooltip-bottom .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-arrow::before {
  bottom: -1px;
  border-width: 0 0.4rem 0.4rem;
  border-bottom-color: #000;
}

.bs-tooltip-start,
.bs-tooltip-auto[data-popper-placement^="left"] {
  padding: 0 0.4rem;
}

.bs-tooltip-start .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="left"] .tooltip-arrow {
  right: 0;
  width: 0.4rem;
  height: 0.8rem;
}

.bs-tooltip-start .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="left"] .tooltip-arrow::before {
  left: -1px;
  border-width: 0.4rem 0 0.4rem 0.4rem;
  border-left-color: #000;
}

.tooltip-inner {
  max-width: 200px;
  padding: 0.25rem 0.5rem;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 0.25rem;
}

.popover {
  position: absolute;
  top: 0;
  left: 0
    /* rtl:ignore */
  ;
  z-index: 1060;
  display: block;
  max-width: 276px;
  font-family: "Jost", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.7143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
}

.popover .popover-arrow {
  position: absolute;
  display: block;
  width: 1rem;
  height: 0.5rem;
  margin: 0 0.3rem;
}

.popover .popover-arrow::before,
.popover .popover-arrow::after {
  position: absolute;
  display: block;
  content: "";
  border-color: transparent;
  border-style: solid;
}

.bs-popover-top,
.bs-popover-auto[data-popper-placement^="top"] {
  margin-bottom: 0.5rem !important;
}

.bs-popover-top>.popover-arrow,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow {
  bottom: calc(-0.5rem - 1px);
}

.bs-popover-top>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow::before {
  bottom: 0;
  border-width: 0.5rem 0.5rem 0;
  border-top-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-top>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow::after {
  bottom: 1px;
  border-width: 0.5rem 0.5rem 0;
  border-top-color: #fff;
}

.bs-popover-end,
.bs-popover-auto[data-popper-placement^="right"] {
  margin-left: 0.5rem !important;
}

.bs-popover-end>.popover-arrow,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow {
  left: calc(-0.5rem - 1px);
  width: 0.5rem;
  height: 1rem;
  margin: 0.3rem 0;
}

.bs-popover-end>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow::before {
  left: 0;
  border-width: 0.5rem 0.5rem 0.5rem 0;
  border-right-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-end>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow::after {
  left: 1px;
  border-width: 0.5rem 0.5rem 0.5rem 0;
  border-right-color: #fff;
}

.bs-popover-bottom,
.bs-popover-auto[data-popper-placement^="bottom"] {
  margin-top: 0.5rem !important;
}

.bs-popover-bottom>.popover-arrow,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow {
  top: calc(-0.5rem - 1px);
}

.bs-popover-bottom>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow::before {
  top: 0;
  border-width: 0 0.5rem 0.5rem 0.5rem;
  border-bottom-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-bottom>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow::after {
  top: 1px;
  border-width: 0 0.5rem 0.5rem 0.5rem;
  border-bottom-color: #fff;
}

.bs-popover-bottom .popover-header::before,
.bs-popover-auto[data-popper-placement^="bottom"] .popover-header::before {
  position: absolute;
  top: 0;
  left: 50%;
  display: block;
  width: 1rem;
  margin-left: -0.5rem;
  content: "";
  border-bottom: 1px solid #f0f0f0;
}

.bs-popover-start,
.bs-popover-auto[data-popper-placement^="left"] {
  margin-right: 0.5rem !important;
}

.bs-popover-start>.popover-arrow,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow {
  right: calc(-0.5rem - 1px);
  width: 0.5rem;
  height: 1rem;
  margin: 0.3rem 0;
}

.bs-popover-start>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow::before {
  right: 0;
  border-width: 0.5rem 0 0.5rem 0.5rem;
  border-left-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-start>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow::after {
  right: 1px;
  border-width: 0.5rem 0 0.5rem 0.5rem;
  border-left-color: #fff;
}

.popover-header {
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  background-color: #f0f0f0;
  border-bottom: 1px solid #d8d8d8;
  border-top-left-radius: calc(0.3rem - 1px);
  border-top-right-radius: calc(0.3rem - 1px);
}

.popover-header:empty {
  display: none;
}

.popover-body {
  padding: 1rem 1rem;
  color: #222222;
}

.carousel {
  position: relative;
}

.carousel.pointer-event {
  touch-action: pan-y;
}

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.carousel-inner::after {
  display: block;
  clear: both;
  content: "";
}

.carousel-item {
  position: relative;
  display: none;
  float: left;
  width: 100%;
  margin-right: -100%;
  backface-visibility: hidden;
  transition: transform 0.6s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .carousel-item {
    transition: none;
  }
}

.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
  display: block;
}

/* rtl:begin:ignore */
.carousel-item-next:not(.carousel-item-start),
.active.carousel-item-end {
  transform: translateX(100%);
}

.carousel-item-prev:not(.carousel-item-end),
.active.carousel-item-start {
  transform: translateX(-100%);
}

/* rtl:end:ignore */
.carousel-fade .carousel-item {
  opacity: 0;
  transition-property: opacity;
  transform: none;
}

.carousel-fade .carousel-item.active,
.carousel-fade .carousel-item-next.carousel-item-start,
.carousel-fade .carousel-item-prev.carousel-item-end {
  z-index: 1;
  opacity: 1;
}

.carousel-fade .active.carousel-item-start,
.carousel-fade .active.carousel-item-end {
  z-index: 0;
  opacity: 0;
  transition: opacity 0s 0.6s;
}

@media (prefers-reduced-motion: reduce) {

  .carousel-fade .active.carousel-item-start,
  .carousel-fade .active.carousel-item-end {
    transition: none;
  }
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 15%;
  color: #fff;
  text-align: center;
  opacity: 0.5;
  transition: opacity 0.15s ease;
}

@media (prefers-reduced-motion: reduce) {

  .carousel-control-prev,
  .carousel-control-next {
    transition: none;
  }
}

.carousel-control-prev:hover,
.carousel-control-prev:focus,
.carousel-control-next:hover,
.carousel-control-next:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  opacity: 0.9;
}

.carousel-control-prev {
  left: 0;
}

.carousel-control-next {
  right: 0;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  background-repeat: no-repeat;
  background-position: 50%;
  background-size: 100% 100%;
}

/* rtl:options: {
  "autoRename": true,
  "stringMap":[ {
    "name"    : "prev-next",
    "search"  : "prev",
    "replace" : "next"
  } ]
} */
.carousel-control-prev-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e");
}

.carousel-control-next-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
}

.carousel-indicators {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  display: flex;
  justify-content: center;
  padding-left: 0;
  margin-right: 15%;
  margin-left: 15%;
  list-style: none;
}

.carousel-indicators li {
  box-sizing: content-box;
  flex: 0 1 auto;
  width: 30px;
  height: 3px;
  margin-right: 3px;
  margin-left: 3px;
  text-indent: -999px;
  cursor: pointer;
  background-color: #fff;
  background-clip: padding-box;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  opacity: 0.5;
  transition: opacity 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
  .carousel-indicators li {
    transition: none;
  }
}

.carousel-indicators .active {
  opacity: 1;
}

.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 1.25rem;
  left: 15%;
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
  color: #fff;
  text-align: center;
}

.carousel-dark .carousel-control-prev-icon,
.carousel-dark .carousel-control-next-icon {
  filter: invert(1) grayscale(100);
}

.carousel-dark .carousel-indicators li {
  background-color: #000;
}

.carousel-dark .carousel-caption {
  color: #000;
}

@keyframes spinner-border {
  to {
    transform: rotate(360deg)
      /* rtl:ignore */
    ;
  }
}

.spinner-border {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  border: 0.25em solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: 0.75s linear infinite spinner-border;
}

.spinner-border-sm {
  width: 1rem;
  height: 1rem;
  border-width: 0.2em;
}

@keyframes spinner-grow {
  0% {
    transform: scale(0);
  }

  50% {
    opacity: 1;
    transform: none;
  }
}

.spinner-grow {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  background-color: currentColor;
  border-radius: 50%;
  opacity: 0;
  animation: 0.75s linear infinite spinner-grow;
}

.spinner-grow-sm {
  width: 1rem;
  height: 1rem;
}

@media (prefers-reduced-motion: reduce) {

  .spinner-border,
  .spinner-grow {
    animation-duration: 1.5s;
  }
}

.clearfix::after {
  display: block;
  clear: both;
  content: "";
}

.link-primary {
  color: #222222;
}

.link-primary:hover,
.link-primary:focus {
  color: #1b1b1b;
}

.link-secondary {
  color: #767676;
}

.link-secondary:hover,
.link-secondary:focus {
  color: #5e5e5e;
}

.link-success {
  color: #def2d7;
}

.link-success:hover,
.link-success:focus {
  color: #e5f5df;
}

.link-info {
  color: #cde9f6;
}

.link-info:hover,
.link-info:focus {
  color: #d7edf8;
}

.link-warning {
  color: #f7f3d7;
}

.link-warning:hover,
.link-warning:focus {
  color: #f9f5df;
}

.link-danger {
  color: #ecc8c5;
}

.link-danger:hover,
.link-danger:focus {
  color: #f0d3d1;
}

.link-light {
  color: #e4e4e4;
}

.link-light:hover,
.link-light:focus {
  color: #e9e9e9;
}

.link-lighter {
  color: #faf9f8;
}

.link-lighter:hover,
.link-lighter:focus {
  color: #fbfaf9;
}

.link-dark {
  color: #222222;
}

.link-dark:hover,
.link-dark:focus {
  color: #1b1b1b;
}

.link-red {
  color: #c32929;
}

.link-red:hover,
.link-red:focus {
  color: #9c2121;
}

.link-beige {
  color: #b9a16b;
}

.link-beige:hover,
.link-beige:focus {
  color: #c7b489;
}

.ratio {
  position: relative;
  width: 100%;
}

.ratio::before {
  display: block;
  padding-top: var(--aspect-ratio);
  content: "";
}

.ratio>* {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.ratio-1x1 {
  --aspect-ratio: 100%;
}

.ratio-4x3 {
  --aspect-ratio: calc(3 / 4 * 100%);
}

.ratio-16x9 {
  --aspect-ratio: calc(9 / 16 * 100%);
}

.ratio-21x9 {
  --aspect-ratio: calc(9 / 21 * 100%);
}

.fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030;
}

.fixed-bottom {
  position: fixed;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1030;
}

.sticky-top {
  position: sticky;
  top: 0;
  z-index: 1020;
}

@media (min-width: 576px) {
  .sticky-sm-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 768px) {
  .sticky-md-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 992px) {
  .sticky-lg-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1200px) {
  .sticky-xl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1500px) {
  .sticky-xxl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1700px) {
  .sticky-xxxl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

.visually-hidden,
.visually-hidden-focusable:not(:focus) {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

.stretched-link::after {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  content: "";
}

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.align-baseline {
  vertical-align: baseline !important;
}

.align-top {
  vertical-align: top !important;
}

.align-middle {
  vertical-align: middle !important;
}

.align-bottom {
  vertical-align: bottom !important;
}

.align-text-bottom {
  vertical-align: text-bottom !important;
}

.align-text-top {
  vertical-align: text-top !important;
}

.float-start {
  float: left !important;
}

.float-end {
  float: right !important;
}

.float-none {
  float: none !important;
}

.overflow-auto {
  overflow: auto !important;
}

.overflow-hidden {
  overflow: hidden !important;
}

.overflow-visible {
  overflow: visible !important;
}

.overflow-scroll {
  overflow: scroll !important;
}

.d-inline {
  display: inline !important;
}

.d-inline-block {
  display: inline-block !important;
}

.d-block {
  display: block !important;
}

.d-grid {
  display: grid !important;
}

.d-table {
  display: table !important;
}

.d-table-row {
  display: table-row !important;
}

.d-table-cell {
  display: table-cell !important;
}

.d-flex {
  display: flex !important;
}

.d-inline-flex {
  display: inline-flex !important;
}

.d-none {
  display: none !important;
}

.shadow {
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05) !important;
}

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
}

.shadow-lg {
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important;
}

.shadow-none {
  box-shadow: none !important;
}

.position-static {
  position: static !important;
}

.position-relative {
  position: relative !important;
}

.position-absolute {
  position: absolute !important;
}

.position-fixed {
  position: fixed !important;
}

.position-sticky {
  position: sticky !important;
}

.top-0 {
  top: 0 !important;
}

.top-50 {
  top: 50% !important;
}

.top-100 {
  top: 100% !important;
}

.bottom-0 {
  bottom: 0 !important;
}

.bottom-50 {
  bottom: 50% !important;
}

.bottom-100 {
  bottom: 100% !important;
}

.start-0 {
  left: 0 !important;
}

.start-50 {
  left: 50% !important;
}

.start-100 {
  left: 100% !important;
}

.end-0 {
  right: 0 !important;
}

.end-50 {
  right: 50% !important;
}

.end-100 {
  right: 100% !important;
}

.translate-middle {
  transform: translate(-50%, -50%) !important;
}

.translate-middle-x {
  transform: translateX(-50%) !important;
}

.translate-middle-y {
  transform: translateY(-50%) !important;
}

.border {
  border: 1px solid #e4e4e4 !important;
}

.border-0 {
  border: 0 !important;
}

.border-top {
  border-top: 1px solid #e4e4e4 !important;
}

.border-top-0 {
  border-top: 0 !important;
}

.border-end {
  border-right: 1px solid #e4e4e4 !important;
}

.border-end-0 {
  border-right: 0 !important;
}

.border-bottom {
  border-bottom: 1px solid #e4e4e4 !important;
}

.border-bottom-0 {
  border-bottom: 0 !important;
}

.border-start {
  border-left: 1px solid #e4e4e4 !important;
}

.border-start-0 {
  border-left: 0 !important;
}

.border-primary {
  border-color: #222222 !important;
}

.border-secondary {
  border-color: #767676 !important;
}

.border-success {
  border-color: #def2d7 !important;
}

.border-info {
  border-color: #cde9f6 !important;
}

.border-warning {
  border-color: #f7f3d7 !important;
}

.border-danger {
  border-color: #ecc8c5 !important;
}

.border-light {
  border-color: #e4e4e4 !important;
}

.border-lighter {
  border-color: #faf9f8 !important;
}

.border-dark {
  border-color: #222222 !important;
}

.border-red {
  border-color: #c32929 !important;
}

.border-beige {
  border-color: #b9a16b !important;
}

.border-white {
  border-color: #fff !important;
}

.border-0 {
  border-width: 0 !important;
}

.border-1 {
  border-width: 1px !important;
}

.border-2 {
  border-width: 2px !important;
}

.border-3 {
  border-width: 3px !important;
}

.border-4 {
  border-width: 4px !important;
}

.border-5 {
  border-width: 5px !important;
}

.w-25 {
  width: 25% !important;
}

.w-50 {
  width: 50% !important;
}

.w-75 {
  width: 75% !important;
}

.w-100 {
  width: 100% !important;
}

.w-auto {
  width: auto !important;
}

.mw-100 {
  max-width: 100% !important;
}

.vw-100 {
  width: 100vw !important;
}

.min-vw-100 {
  min-width: 100vw !important;
}

.h-25 {
  height: 25% !important;
}

.h-50 {
  height: 50% !important;
}

.h-75 {
  height: 75% !important;
}

.h-100 {
  height: 100% !important;
}

.h-auto {
  height: auto !important;
}

.mh-100 {
  max-height: 100% !important;
}

.vh-100 {
  height: 100vh !important;
}

.min-vh-100 {
  min-height: 100vh !important;
}

.flex-fill {
  flex: 1 1 auto !important;
}

.flex-row {
  flex-direction: row !important;
}

.flex-column {
  flex-direction: column !important;
}

.flex-row-reverse {
  flex-direction: row-reverse !important;
}

.flex-column-reverse {
  flex-direction: column-reverse !important;
}

.flex-grow-0 {
  flex-grow: 0 !important;
}

.flex-grow-1 {
  flex-grow: 1 !important;
}

.flex-shrink-0 {
  flex-shrink: 0 !important;
}

.flex-shrink-1 {
  flex-shrink: 1 !important;
}

.flex-wrap {
  flex-wrap: wrap !important;
}

.flex-nowrap {
  flex-wrap: nowrap !important;
}

.flex-wrap-reverse {
  flex-wrap: wrap-reverse !important;
}

.gap-0 {
  gap: 0 !important;
}

.gap-1 {
  gap: 0.25rem !important;
}

.gap-2 {
  gap: 0.5rem !important;
}

.gap-3 {
  gap: 1rem !important;
}

.gap-4 {
  gap: 1.5rem !important;
}

.gap-5 {
  gap: 3rem !important;
}

.justify-content-start {
  justify-content: flex-start !important;
}

.justify-content-end {
  justify-content: flex-end !important;
}

.justify-content-center {
  justify-content: center !important;
}

.justify-content-between {
  justify-content: space-between !important;
}

.justify-content-around {
  justify-content: space-around !important;
}

.justify-content-evenly {
  justify-content: space-evenly !important;
}

.align-items-start {
  align-items: flex-start !important;
}

.align-items-end {
  align-items: flex-end !important;
}

.align-items-center {
  align-items: center !important;
}

.align-items-baseline {
  align-items: baseline !important;
}

.align-items-stretch {
  align-items: stretch !important;
}

.align-content-start {
  align-content: flex-start !important;
}

.align-content-end {
  align-content: flex-end !important;
}

.align-content-center {
  align-content: center !important;
}

.align-content-between {
  align-content: space-between !important;
}

.align-content-around {
  align-content: space-around !important;
}

.align-content-stretch {
  align-content: stretch !important;
}

.align-self-auto {
  align-self: auto !important;
}

.align-self-start {
  align-self: flex-start !important;
}

.align-self-end {
  align-self: flex-end !important;
}

.align-self-center {
  align-self: center !important;
}

.align-self-baseline {
  align-self: baseline !important;
}

.align-self-stretch {
  align-self: stretch !important;
}

.order-first {
  order: -1 !important;
}

.order-0 {
  order: 0 !important;
}

.order-1 {
  order: 1 !important;
}

.order-2 {
  order: 2 !important;
}

.order-3 {
  order: 3 !important;
}

.order-4 {
  order: 4 !important;
}

.order-5 {
  order: 5 !important;
}

.order-last {
  order: 6 !important;
}

.m-0 {
  margin: 0 !important;
}

.m-1 {
  margin: 0.25rem !important;
}

.m-2 {
  margin: 0.5rem !important;
}

.m-3 {
  margin: 1rem !important;
}

.m-4 {
  margin: 1.5rem !important;
}

.m-5 {
  margin: 3rem !important;
}

.m-auto {
  margin: auto !important;
}

.mx-0 {
  margin-right: 0 !important;
  margin-left: 0 !important;
}

.mx-1 {
  margin-right: 0.25rem !important;
  margin-left: 0.25rem !important;
}

.mx-2 {
  margin-right: 0.5rem !important;
  margin-left: 0.5rem !important;
}

.mx-3 {
  margin-right: 1rem !important;
  margin-left: 1rem !important;
}

.mx-4 {
  margin-right: 1.5rem !important;
  margin-left: 1.5rem !important;
}

.mx-5 {
  margin-right: 3rem !important;
  margin-left: 3rem !important;
}

.mx-auto {
  margin-right: auto !important;
  margin-left: auto !important;
}

.my-0 {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.my-1 {
  margin-top: 0.25rem !important;
  margin-bottom: 0.25rem !important;
}

.my-2 {
  margin-top: 0.5rem !important;
  margin-bottom: 0.5rem !important;
}

.my-3 {
  margin-top: 1rem !important;
  margin-bottom: 1rem !important;
}

.my-4 {
  margin-top: 1.5rem !important;
  margin-bottom: 1.5rem !important;
}

.my-5 {
  margin-top: 3rem !important;
  margin-bottom: 3rem !important;
}

.my-auto {
  margin-top: auto !important;
  margin-bottom: auto !important;
}

.mt-0 {
  margin-top: 0 !important;
}

.mt-1 {
  margin-top: 0.25rem !important;
}

.mt-2 {
  margin-top: 0.5rem !important;
}

.mt-3 {
  margin-top: 1rem !important;
}

.mt-4 {
  margin-top: 1.5rem !important;
}

.mt-5 {
  margin-top: 3rem !important;
}

.mt-auto {
  margin-top: auto !important;
}

.me-0 {
  margin-right: 0 !important;
}

.me-1 {
  margin-right: 0.25rem !important;
}

.me-2 {
  margin-right: 0.5rem !important;
}

.me-3 {
  margin-right: 1rem !important;
}

.me-4 {
  margin-right: 1.5rem !important;
}

.me-5 {
  margin-right: 3rem !important;
}

.me-auto {
  margin-right: auto !important;
}

.mb-0 {
  margin-bottom: 0 !important;
}

.mb-1 {
  margin-bottom: 0.25rem !important;
}

.mb-2 {
  margin-bottom: 0.5rem !important;
}

.mb-3 {
  margin-bottom: 1rem !important;
}

.mb-4 {
  margin-bottom: 1.5rem !important;
}

.mb-5 {
  margin-bottom: 3rem !important;
}

.mb-auto {
  margin-bottom: auto !important;
}

.ms-0 {
  margin-left: 0 !important;
}

.ms-1 {
  margin-left: 0.25rem !important;
}

.ms-2 {
  margin-left: 0.5rem !important;
}

.ms-3 {
  margin-left: 1rem !important;
}

.ms-4 {
  margin-left: 1.5rem !important;
}

.ms-5 {
  margin-left: 3rem !important;
}

.ms-auto {
  margin-left: auto !important;
}

.p-0 {
  padding: 0 !important;
}

.p-1 {
  padding: 0.25rem !important;
}

.p-2 {
  padding: 0.5rem !important;
}

.p-3 {
  padding: 1rem !important;
}

.p-4 {
  padding: 1.5rem !important;
}

.p-5 {
  padding: 3rem !important;
}

.px-0 {
  padding-right: 0 !important;
  padding-left: 0 !important;
}

.px-1 {
  padding-right: 0.25rem !important;
  padding-left: 0.25rem !important;
}

.px-2 {
  padding-right: 0.5rem !important;
  padding-left: 0.5rem !important;
}

.px-3 {
  padding-right: 1rem !important;
  padding-left: 1rem !important;
}

.px-4 {
  padding-right: 1.5rem !important;
  padding-left: 1.5rem !important;
}

.px-5 {
  padding-right: 3rem !important;
  padding-left: 3rem !important;
}

.py-0 {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

.py-1 {
  padding-top: 0.25rem !important;
  padding-bottom: 0.25rem !important;
}

.py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}

.py-3 {
  padding-top: 1rem !important;
  padding-bottom: 1rem !important;
}

.py-4 {
  padding-top: 1.5rem !important;
  padding-bottom: 1.5rem !important;
}

.py-5 {
  padding-top: 3rem !important;
  padding-bottom: 3rem !important;
}

.pt-0 {
  padding-top: 0 !important;
}

.pt-1 {
  padding-top: 0.25rem !important;
}

.pt-2 {
  padding-top: 0.5rem !important;
}

.pt-3 {
  padding-top: 1rem !important;
}

.pt-4 {
  padding-top: 1.5rem !important;
}

.pt-5 {
  padding-top: 3rem !important;
}

.pe-0 {
  padding-right: 0 !important;
}

.pe-1 {
  padding-right: 0.25rem !important;
}

.pe-2 {
  padding-right: 0.5rem !important;
}

.pe-3 {
  padding-right: 1rem !important;
}

.pe-4 {
  padding-right: 1.5rem !important;
}

.pe-5 {
  padding-right: 3rem !important;
}

.pb-0 {
  padding-bottom: 0 !important;
}

.pb-1 {
  padding-bottom: 0.25rem !important;
}

.pb-2 {
  padding-bottom: 0.5rem !important;
}

.pb-3 {
  padding-bottom: 1rem !important;
}

.pb-4 {
  padding-bottom: 1.5rem !important;
}

.pb-5 {
  padding-bottom: 3rem !important;
}

.ps-0 {
  padding-left: 0 !important;
}

.ps-1 {
  padding-left: 0.25rem !important;
}

.ps-2 {
  padding-left: 0.5rem !important;
}

.ps-3 {
  padding-left: 1rem !important;
}

.ps-4 {
  padding-left: 1.5rem !important;
}

.ps-5 {
  padding-left: 3rem !important;
}

.fs-1 {
  font-size: calc(1.625rem + 4.5vw) !important;
}

.fs-2 {
  font-size: calc(1.325rem + 0.9vw) !important;
}

.fs-3 {
  font-size: calc(1.2875rem + 0.45vw) !important;
}

.fs-4 {
  font-size: 1.25rem !important;
}

.fs-5 {
  font-size: 1.125rem !important;
}

.fs-6 {
  font-size: 1rem !important;
}

.fst-italic {
  font-style: italic !important;
}

.fst-normal {
  font-style: normal !important;
}

.fw-light {
  font-weight: 300 !important;
}

.fw-lighter {
  font-weight: lighter !important;
}

.fw-normal {
  font-weight: 400 !important;
}

.fw-medium {
  font-weight: 500 !important;
}

.fw-bold {
  font-weight: 700 !important;
}

.fw-bolder {
  font-weight: bolder !important;
}

.text-lowercase {
  text-transform: lowercase !important;
}

.text-uppercase {
  text-transform: uppercase !important;
}

.text-capitalize {
  text-transform: capitalize !important;
}

.text-start {
  text-align: left !important;
}

.text-end {
  text-align: right !important;
}

.text-center {
  text-align: center !important;
}

.text-primary {
  color: #222222 !important;
}

.text-secondary {
  color: #767676 !important;
}

.text-success {
  color: #def2d7 !important;
}

.text-info {
  color: #cde9f6 !important;
}

.text-warning {
  color: #f7f3d7 !important;
}

.text-danger {
  color: #ecc8c5 !important;
}

.text-light {
  color: #e4e4e4 !important;
}

.text-lighter {
  color: #faf9f8 !important;
}

.text-dark {
  color: #222222 !important;
}

.text-red {
  color: #c32929 !important;
}

.text-beige {
  color: #b9a16b !important;
}

.text-white {
  color: #fff !important;
}

.text-body {
  color: #222222 !important;
}

.text-muted {
  color: #6c757d !important;
}

.text-black-50 {
  color: rgba(0, 0, 0, 0.5) !important;
}

.text-white-50 {
  color: rgba(255, 255, 255, 0.5) !important;
}

.text-reset {
  color: inherit !important;
}

.lh-1 {
  line-height: 1 !important;
}

.lh-sm {
  line-height: 1.25 !important;
}

.lh-base {
  line-height: 1.7143 !important;
}

.lh-lg {
  line-height: 2 !important;
}

.bg-primary {
  background-color: #222222 !important;
}

.bg-secondary {
  background-color: #767676 !important;
}

.bg-success {
  background-color: #def2d7 !important;
}

.bg-info {
  background-color: #cde9f6 !important;
}

.bg-warning {
  background-color: #f7f3d7 !important;
}

.bg-danger {
  background-color: #ecc8c5 !important;
}

.bg-light {
  background-color: #e4e4e4 !important;
}

.bg-lighter {
  background-color: #faf9f8 !important;
}

.bg-dark {
  background-color: #222222 !important;
}

.bg-red {
  background-color: #c32929 !important;
}

.bg-beige {
  background-color: #b9a16b !important;
}

.bg-body {
  background-color: #ffffff !important;
}

.bg-white {
  background-color: #fff !important;
}

.bg-transparent {
  background-color: transparent !important;
}

.bg-gradient {
  background-image: var(--bs-gradient) !important;
}

.text-wrap {
  white-space: normal !important;
}

.text-nowrap {
  white-space: nowrap !important;
}

.text-decoration-none {
  text-decoration: none !important;
}

.text-decoration-underline {
  text-decoration: underline !important;
}

.text-decoration-line-through {
  text-decoration: line-through !important;
}

/* rtl:begin:remove */
.text-break {
  word-wrap: break-word !important;
  word-break: break-word !important;
}

/* rtl:end:remove */
.font-monospace {
  font-family: var(--bs-font-monospace) !important;
}

.user-select-all {
  user-select: all !important;
}

.user-select-auto {
  user-select: auto !important;
}

.user-select-none {
  user-select: none !important;
}

.pe-none {
  pointer-events: none !important;
}

.pe-auto {
  pointer-events: auto !important;
}

.rounded {
  border-radius: 0 !important;
}

.rounded-0 {
  border-radius: 0 !important;
}

.rounded-1 {
  border-radius: 0.2rem !important;
}

.rounded-2 {
  border-radius: 0 !important;
}

.rounded-3 {
  border-radius: 0.3rem !important;
}

.rounded-circle {
  border-radius: 50% !important;
}

.rounded-pill {
  border-radius: 50rem !important;
}

.rounded-top {
  border-top-left-radius: 0 !important;
  border-top-right-radius: 0 !important;
}

.rounded-end {
  border-top-right-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

.rounded-bottom {
  border-bottom-right-radius: 0 !important;
  border-bottom-left-radius: 0 !important;
}

.rounded-start {
  border-bottom-left-radius: 0 !important;
  border-top-left-radius: 0 !important;
}

.visible {
  visibility: visible !important;
}

.invisible {
  visibility: hidden !important;
}

@media (min-width: 576px) {
  .float-sm-start {
    float: left !important;
  }

  .float-sm-end {
    float: right !important;
  }

  .float-sm-none {
    float: none !important;
  }

  .d-sm-inline {
    display: inline !important;
  }

  .d-sm-inline-block {
    display: inline-block !important;
  }

  .d-sm-block {
    display: block !important;
  }

  .d-sm-grid {
    display: grid !important;
  }

  .d-sm-table {
    display: table !important;
  }

  .d-sm-table-row {
    display: table-row !important;
  }

  .d-sm-table-cell {
    display: table-cell !important;
  }

  .d-sm-flex {
    display: flex !important;
  }

  .d-sm-inline-flex {
    display: inline-flex !important;
  }

  .d-sm-none {
    display: none !important;
  }

  .flex-sm-fill {
    flex: 1 1 auto !important;
  }

  .flex-sm-row {
    flex-direction: row !important;
  }

  .flex-sm-column {
    flex-direction: column !important;
  }

  .flex-sm-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-sm-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-sm-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-sm-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-sm-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-sm-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-sm-wrap {
    flex-wrap: wrap !important;
  }

  .flex-sm-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-sm-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-sm-0 {
    gap: 0 !important;
  }

  .gap-sm-1 {
    gap: 0.25rem !important;
  }

  .gap-sm-2 {
    gap: 0.5rem !important;
  }

  .gap-sm-3 {
    gap: 1rem !important;
  }

  .gap-sm-4 {
    gap: 1.5rem !important;
  }

  .gap-sm-5 {
    gap: 3rem !important;
  }

  .justify-content-sm-start {
    justify-content: flex-start !important;
  }

  .justify-content-sm-end {
    justify-content: flex-end !important;
  }

  .justify-content-sm-center {
    justify-content: center !important;
  }

  .justify-content-sm-between {
    justify-content: space-between !important;
  }

  .justify-content-sm-around {
    justify-content: space-around !important;
  }

  .justify-content-sm-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-sm-start {
    align-items: flex-start !important;
  }

  .align-items-sm-end {
    align-items: flex-end !important;
  }

  .align-items-sm-center {
    align-items: center !important;
  }

  .align-items-sm-baseline {
    align-items: baseline !important;
  }

  .align-items-sm-stretch {
    align-items: stretch !important;
  }

  .align-content-sm-start {
    align-content: flex-start !important;
  }

  .align-content-sm-end {
    align-content: flex-end !important;
  }

  .align-content-sm-center {
    align-content: center !important;
  }

  .align-content-sm-between {
    align-content: space-between !important;
  }

  .align-content-sm-around {
    align-content: space-around !important;
  }

  .align-content-sm-stretch {
    align-content: stretch !important;
  }

  .align-self-sm-auto {
    align-self: auto !important;
  }

  .align-self-sm-start {
    align-self: flex-start !important;
  }

  .align-self-sm-end {
    align-self: flex-end !important;
  }

  .align-self-sm-center {
    align-self: center !important;
  }

  .align-self-sm-baseline {
    align-self: baseline !important;
  }

  .align-self-sm-stretch {
    align-self: stretch !important;
  }

  .order-sm-first {
    order: -1 !important;
  }

  .order-sm-0 {
    order: 0 !important;
  }

  .order-sm-1 {
    order: 1 !important;
  }

  .order-sm-2 {
    order: 2 !important;
  }

  .order-sm-3 {
    order: 3 !important;
  }

  .order-sm-4 {
    order: 4 !important;
  }

  .order-sm-5 {
    order: 5 !important;
  }

  .order-sm-last {
    order: 6 !important;
  }

  .m-sm-0 {
    margin: 0 !important;
  }

  .m-sm-1 {
    margin: 0.25rem !important;
  }

  .m-sm-2 {
    margin: 0.5rem !important;
  }

  .m-sm-3 {
    margin: 1rem !important;
  }

  .m-sm-4 {
    margin: 1.5rem !important;
  }

  .m-sm-5 {
    margin: 3rem !important;
  }

  .m-sm-auto {
    margin: auto !important;
  }

  .mx-sm-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-sm-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-sm-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-sm-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-sm-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-sm-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-sm-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-sm-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-sm-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-sm-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-sm-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-sm-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-sm-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-sm-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-sm-0 {
    margin-top: 0 !important;
  }

  .mt-sm-1 {
    margin-top: 0.25rem !important;
  }

  .mt-sm-2 {
    margin-top: 0.5rem !important;
  }

  .mt-sm-3 {
    margin-top: 1rem !important;
  }

  .mt-sm-4 {
    margin-top: 1.5rem !important;
  }

  .mt-sm-5 {
    margin-top: 3rem !important;
  }

  .mt-sm-auto {
    margin-top: auto !important;
  }

  .me-sm-0 {
    margin-right: 0 !important;
  }

  .me-sm-1 {
    margin-right: 0.25rem !important;
  }

  .me-sm-2 {
    margin-right: 0.5rem !important;
  }

  .me-sm-3 {
    margin-right: 1rem !important;
  }

  .me-sm-4 {
    margin-right: 1.5rem !important;
  }

  .me-sm-5 {
    margin-right: 3rem !important;
  }

  .me-sm-auto {
    margin-right: auto !important;
  }

  .mb-sm-0 {
    margin-bottom: 0 !important;
  }

  .mb-sm-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-sm-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-sm-3 {
    margin-bottom: 1rem !important;
  }

  .mb-sm-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-sm-5 {
    margin-bottom: 3rem !important;
  }

  .mb-sm-auto {
    margin-bottom: auto !important;
  }

  .ms-sm-0 {
    margin-left: 0 !important;
  }

  .ms-sm-1 {
    margin-left: 0.25rem !important;
  }

  .ms-sm-2 {
    margin-left: 0.5rem !important;
  }

  .ms-sm-3 {
    margin-left: 1rem !important;
  }

  .ms-sm-4 {
    margin-left: 1.5rem !important;
  }

  .ms-sm-5 {
    margin-left: 3rem !important;
  }

  .ms-sm-auto {
    margin-left: auto !important;
  }

  .p-sm-0 {
    padding: 0 !important;
  }

  .p-sm-1 {
    padding: 0.25rem !important;
  }

  .p-sm-2 {
    padding: 0.5rem !important;
  }

  .p-sm-3 {
    padding: 1rem !important;
  }

  .p-sm-4 {
    padding: 1.5rem !important;
  }

  .p-sm-5 {
    padding: 3rem !important;
  }

  .px-sm-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-sm-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-sm-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-sm-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-sm-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-sm-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-sm-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-sm-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-sm-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-sm-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-sm-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-sm-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-sm-0 {
    padding-top: 0 !important;
  }

  .pt-sm-1 {
    padding-top: 0.25rem !important;
  }

  .pt-sm-2 {
    padding-top: 0.5rem !important;
  }

  .pt-sm-3 {
    padding-top: 1rem !important;
  }

  .pt-sm-4 {
    padding-top: 1.5rem !important;
  }

  .pt-sm-5 {
    padding-top: 3rem !important;
  }

  .pe-sm-0 {
    padding-right: 0 !important;
  }

  .pe-sm-1 {
    padding-right: 0.25rem !important;
  }

  .pe-sm-2 {
    padding-right: 0.5rem !important;
  }

  .pe-sm-3 {
    padding-right: 1rem !important;
  }

  .pe-sm-4 {
    padding-right: 1.5rem !important;
  }

  .pe-sm-5 {
    padding-right: 3rem !important;
  }

  .pb-sm-0 {
    padding-bottom: 0 !important;
  }

  .pb-sm-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-sm-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-sm-3 {
    padding-bottom: 1rem !important;
  }

  .pb-sm-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-sm-5 {
    padding-bottom: 3rem !important;
  }

  .ps-sm-0 {
    padding-left: 0 !important;
  }

  .ps-sm-1 {
    padding-left: 0.25rem !important;
  }

  .ps-sm-2 {
    padding-left: 0.5rem !important;
  }

  .ps-sm-3 {
    padding-left: 1rem !important;
  }

  .ps-sm-4 {
    padding-left: 1.5rem !important;
  }

  .ps-sm-5 {
    padding-left: 3rem !important;
  }

  .text-sm-start {
    text-align: left !important;
  }

  .text-sm-end {
    text-align: right !important;
  }

  .text-sm-center {
    text-align: center !important;
  }
}

@media (min-width: 768px) {
  .float-md-start {
    float: left !important;
  }

  .float-md-end {
    float: right !important;
  }

  .float-md-none {
    float: none !important;
  }

  .d-md-inline {
    display: inline !important;
  }

  .d-md-inline-block {
    display: inline-block !important;
  }

  .d-md-block {
    display: block !important;
  }

  .d-md-grid {
    display: grid !important;
  }

  .d-md-table {
    display: table !important;
  }

  .d-md-table-row {
    display: table-row !important;
  }

  .d-md-table-cell {
    display: table-cell !important;
  }

  .d-md-flex {
    display: flex !important;
  }

  .d-md-inline-flex {
    display: inline-flex !important;
  }

  .d-md-none {
    display: none !important;
  }

  .flex-md-fill {
    flex: 1 1 auto !important;
  }

  .flex-md-row {
    flex-direction: row !important;
  }

  .flex-md-column {
    flex-direction: column !important;
  }

  .flex-md-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-md-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-md-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-md-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-md-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-md-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-md-wrap {
    flex-wrap: wrap !important;
  }

  .flex-md-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-md-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-md-0 {
    gap: 0 !important;
  }

  .gap-md-1 {
    gap: 0.25rem !important;
  }

  .gap-md-2 {
    gap: 0.5rem !important;
  }

  .gap-md-3 {
    gap: 1rem !important;
  }

  .gap-md-4 {
    gap: 1.5rem !important;
  }

  .gap-md-5 {
    gap: 3rem !important;
  }

  .justify-content-md-start {
    justify-content: flex-start !important;
  }

  .justify-content-md-end {
    justify-content: flex-end !important;
  }

  .justify-content-md-center {
    justify-content: center !important;
  }

  .justify-content-md-between {
    justify-content: space-between !important;
  }

  .justify-content-md-around {
    justify-content: space-around !important;
  }

  .justify-content-md-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-md-start {
    align-items: flex-start !important;
  }

  .align-items-md-end {
    align-items: flex-end !important;
  }

  .align-items-md-center {
    align-items: center !important;
  }

  .align-items-md-baseline {
    align-items: baseline !important;
  }

  .align-items-md-stretch {
    align-items: stretch !important;
  }

  .align-content-md-start {
    align-content: flex-start !important;
  }

  .align-content-md-end {
    align-content: flex-end !important;
  }

  .align-content-md-center {
    align-content: center !important;
  }

  .align-content-md-between {
    align-content: space-between !important;
  }

  .align-content-md-around {
    align-content: space-around !important;
  }

  .align-content-md-stretch {
    align-content: stretch !important;
  }

  .align-self-md-auto {
    align-self: auto !important;
  }

  .align-self-md-start {
    align-self: flex-start !important;
  }

  .align-self-md-end {
    align-self: flex-end !important;
  }

  .align-self-md-center {
    align-self: center !important;
  }

  .align-self-md-baseline {
    align-self: baseline !important;
  }

  .align-self-md-stretch {
    align-self: stretch !important;
  }

  .order-md-first {
    order: -1 !important;
  }

  .order-md-0 {
    order: 0 !important;
  }

  .order-md-1 {
    order: 1 !important;
  }

  .order-md-2 {
    order: 2 !important;
  }

  .order-md-3 {
    order: 3 !important;
  }

  .order-md-4 {
    order: 4 !important;
  }

  .order-md-5 {
    order: 5 !important;
  }

  .order-md-last {
    order: 6 !important;
  }

  .m-md-0 {
    margin: 0 !important;
  }

  .m-md-1 {
    margin: 0.25rem !important;
  }

  .m-md-2 {
    margin: 0.5rem !important;
  }

  .m-md-3 {
    margin: 1rem !important;
  }

  .m-md-4 {
    margin: 1.5rem !important;
  }

  .m-md-5 {
    margin: 3rem !important;
  }

  .m-md-auto {
    margin: auto !important;
  }

  .mx-md-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-md-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-md-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-md-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-md-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-md-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-md-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-md-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-md-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-md-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-md-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-md-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-md-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-md-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-md-0 {
    margin-top: 0 !important;
  }

  .mt-md-1 {
    margin-top: 0.25rem !important;
  }

  .mt-md-2 {
    margin-top: 0.5rem !important;
  }

  .mt-md-3 {
    margin-top: 1rem !important;
  }

  .mt-md-4 {
    margin-top: 1.5rem !important;
  }

  .mt-md-5 {
    margin-top: 3rem !important;
  }

  .mt-md-auto {
    margin-top: auto !important;
  }

  .me-md-0 {
    margin-right: 0 !important;
  }

  .me-md-1 {
    margin-right: 0.25rem !important;
  }

  .me-md-2 {
    margin-right: 0.5rem !important;
  }

  .me-md-3 {
    margin-right: 1rem !important;
  }

  .me-md-4 {
    margin-right: 1.5rem !important;
  }

  .me-md-5 {
    margin-right: 3rem !important;
  }

  .me-md-auto {
    margin-right: auto !important;
  }

  .mb-md-0 {
    margin-bottom: 0 !important;
  }

  .mb-md-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-md-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-md-3 {
    margin-bottom: 1rem !important;
  }

  .mb-md-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-md-5 {
    margin-bottom: 3rem !important;
  }

  .mb-md-auto {
    margin-bottom: auto !important;
  }

  .ms-md-0 {
    margin-left: 0 !important;
  }

  .ms-md-1 {
    margin-left: 0.25rem !important;
  }

  .ms-md-2 {
    margin-left: 0.5rem !important;
  }

  .ms-md-3 {
    margin-left: 1rem !important;
  }

  .ms-md-4 {
    margin-left: 1.5rem !important;
  }

  .ms-md-5 {
    margin-left: 3rem !important;
  }

  .ms-md-auto {
    margin-left: auto !important;
  }

  .p-md-0 {
    padding: 0 !important;
  }

  .p-md-1 {
    padding: 0.25rem !important;
  }

  .p-md-2 {
    padding: 0.5rem !important;
  }

  .p-md-3 {
    padding: 1rem !important;
  }

  .p-md-4 {
    padding: 1.5rem !important;
  }

  .p-md-5 {
    padding: 3rem !important;
  }

  .px-md-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-md-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-md-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-md-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-md-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-md-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-md-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-md-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-md-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-md-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-md-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-md-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-md-0 {
    padding-top: 0 !important;
  }

  .pt-md-1 {
    padding-top: 0.25rem !important;
  }

  .pt-md-2 {
    padding-top: 0.5rem !important;
  }

  .pt-md-3 {
    padding-top: 1rem !important;
  }

  .pt-md-4 {
    padding-top: 1.5rem !important;
  }

  .pt-md-5 {
    padding-top: 3rem !important;
  }

  .pe-md-0 {
    padding-right: 0 !important;
  }

  .pe-md-1 {
    padding-right: 0.25rem !important;
  }

  .pe-md-2 {
    padding-right: 0.5rem !important;
  }

  .pe-md-3 {
    padding-right: 1rem !important;
  }

  .pe-md-4 {
    padding-right: 1.5rem !important;
  }

  .pe-md-5 {
    padding-right: 3rem !important;
  }

  .pb-md-0 {
    padding-bottom: 0 !important;
  }

  .pb-md-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-md-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-md-3 {
    padding-bottom: 1rem !important;
  }

  .pb-md-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-md-5 {
    padding-bottom: 3rem !important;
  }

  .ps-md-0 {
    padding-left: 0 !important;
  }

  .ps-md-1 {
    padding-left: 0.25rem !important;
  }

  .ps-md-2 {
    padding-left: 0.5rem !important;
  }

  .ps-md-3 {
    padding-left: 1rem !important;
  }

  .ps-md-4 {
    padding-left: 1.5rem !important;
  }

  .ps-md-5 {
    padding-left: 3rem !important;
  }

  .text-md-start {
    text-align: left !important;
  }

  .text-md-end {
    text-align: right !important;
  }

  .text-md-center {
    text-align: center !important;
  }
}

@media (min-width: 992px) {
  .float-lg-start {
    float: left !important;
  }

  .float-lg-end {
    float: right !important;
  }

  .float-lg-none {
    float: none !important;
  }

  .d-lg-inline {
    display: inline !important;
  }

  .d-lg-inline-block {
    display: inline-block !important;
  }

  .d-lg-block {
    display: block !important;
  }

  .d-lg-grid {
    display: grid !important;
  }

  .d-lg-table {
    display: table !important;
  }

  .d-lg-table-row {
    display: table-row !important;
  }

  .d-lg-table-cell {
    display: table-cell !important;
  }

  .d-lg-flex {
    display: flex !important;
  }

  .d-lg-inline-flex {
    display: inline-flex !important;
  }

  .d-lg-none {
    display: none !important;
  }

  .flex-lg-fill {
    flex: 1 1 auto !important;
  }

  .flex-lg-row {
    flex-direction: row !important;
  }

  .flex-lg-column {
    flex-direction: column !important;
  }

  .flex-lg-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-lg-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-lg-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-lg-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-lg-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-lg-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-lg-wrap {
    flex-wrap: wrap !important;
  }

  .flex-lg-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-lg-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-lg-0 {
    gap: 0 !important;
  }

  .gap-lg-1 {
    gap: 0.25rem !important;
  }

  .gap-lg-2 {
    gap: 0.5rem !important;
  }

  .gap-lg-3 {
    gap: 1rem !important;
  }

  .gap-lg-4 {
    gap: 1.5rem !important;
  }

  .gap-lg-5 {
    gap: 3rem !important;
  }

  .justify-content-lg-start {
    justify-content: flex-start !important;
  }

  .justify-content-lg-end {
    justify-content: flex-end !important;
  }

  .justify-content-lg-center {
    justify-content: center !important;
  }

  .justify-content-lg-between {
    justify-content: space-between !important;
  }

  .justify-content-lg-around {
    justify-content: space-around !important;
  }

  .justify-content-lg-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-lg-start {
    align-items: flex-start !important;
  }

  .align-items-lg-end {
    align-items: flex-end !important;
  }

  .align-items-lg-center {
    align-items: center !important;
  }

  .align-items-lg-baseline {
    align-items: baseline !important;
  }

  .align-items-lg-stretch {
    align-items: stretch !important;
  }

  .align-content-lg-start {
    align-content: flex-start !important;
  }

  .align-content-lg-end {
    align-content: flex-end !important;
  }

  .align-content-lg-center {
    align-content: center !important;
  }

  .align-content-lg-between {
    align-content: space-between !important;
  }

  .align-content-lg-around {
    align-content: space-around !important;
  }

  .align-content-lg-stretch {
    align-content: stretch !important;
  }

  .align-self-lg-auto {
    align-self: auto !important;
  }

  .align-self-lg-start {
    align-self: flex-start !important;
  }

  .align-self-lg-end {
    align-self: flex-end !important;
  }

  .align-self-lg-center {
    align-self: center !important;
  }

  .align-self-lg-baseline {
    align-self: baseline !important;
  }

  .align-self-lg-stretch {
    align-self: stretch !important;
  }

  .order-lg-first {
    order: -1 !important;
  }

  .order-lg-0 {
    order: 0 !important;
  }

  .order-lg-1 {
    order: 1 !important;
  }

  .order-lg-2 {
    order: 2 !important;
  }

  .order-lg-3 {
    order: 3 !important;
  }

  .order-lg-4 {
    order: 4 !important;
  }

  .order-lg-5 {
    order: 5 !important;
  }

  .order-lg-last {
    order: 6 !important;
  }

  .m-lg-0 {
    margin: 0 !important;
  }

  .m-lg-1 {
    margin: 0.25rem !important;
  }

  .m-lg-2 {
    margin: 0.5rem !important;
  }

  .m-lg-3 {
    margin: 1rem !important;
  }

  .m-lg-4 {
    margin: 1.5rem !important;
  }

  .m-lg-5 {
    margin: 3rem !important;
  }

  .m-lg-auto {
    margin: auto !important;
  }

  .mx-lg-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-lg-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-lg-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-lg-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-lg-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-lg-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-lg-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-lg-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-lg-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-lg-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-lg-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-lg-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-lg-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-lg-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-lg-0 {
    margin-top: 0 !important;
  }

  .mt-lg-1 {
    margin-top: 0.25rem !important;
  }

  .mt-lg-2 {
    margin-top: 0.5rem !important;
  }

  .mt-lg-3 {
    margin-top: 1rem !important;
  }

  .mt-lg-4 {
    margin-top: 1.5rem !important;
  }

  .mt-lg-5 {
    margin-top: 3rem !important;
  }

  .mt-lg-auto {
    margin-top: auto !important;
  }

  .me-lg-0 {
    margin-right: 0 !important;
  }

  .me-lg-1 {
    margin-right: 0.25rem !important;
  }

  .me-lg-2 {
    margin-right: 0.5rem !important;
  }

  .me-lg-3 {
    margin-right: 1rem !important;
  }

  .me-lg-4 {
    margin-right: 1.5rem !important;
  }

  .me-lg-5 {
    margin-right: 3rem !important;
  }

  .me-lg-auto {
    margin-right: auto !important;
  }

  .mb-lg-0 {
    margin-bottom: 0 !important;
  }

  .mb-lg-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-lg-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-lg-3 {
    margin-bottom: 1rem !important;
  }

  .mb-lg-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-lg-5 {
    margin-bottom: 3rem !important;
  }

  .mb-lg-auto {
    margin-bottom: auto !important;
  }

  .ms-lg-0 {
    margin-left: 0 !important;
  }

  .ms-lg-1 {
    margin-left: 0.25rem !important;
  }

  .ms-lg-2 {
    margin-left: 0.5rem !important;
  }

  .ms-lg-3 {
    margin-left: 1rem !important;
  }

  .ms-lg-4 {
    margin-left: 1.5rem !important;
  }

  .ms-lg-5 {
    margin-left: 3rem !important;
  }

  .ms-lg-auto {
    margin-left: auto !important;
  }

  .p-lg-0 {
    padding: 0 !important;
  }

  .p-lg-1 {
    padding: 0.25rem !important;
  }

  .p-lg-2 {
    padding: 0.5rem !important;
  }

  .p-lg-3 {
    padding: 1rem !important;
  }

  .p-lg-4 {
    padding: 1.5rem !important;
  }

  .p-lg-5 {
    padding: 3rem !important;
  }

  .px-lg-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-lg-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-lg-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-lg-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-lg-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-lg-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-lg-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-lg-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-lg-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-lg-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-lg-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-lg-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-lg-0 {
    padding-top: 0 !important;
  }

  .pt-lg-1 {
    padding-top: 0.25rem !important;
  }

  .pt-lg-2 {
    padding-top: 0.5rem !important;
  }

  .pt-lg-3 {
    padding-top: 1rem !important;
  }

  .pt-lg-4 {
    padding-top: 1.5rem !important;
  }

  .pt-lg-5 {
    padding-top: 3rem !important;
  }

  .pe-lg-0 {
    padding-right: 0 !important;
  }

  .pe-lg-1 {
    padding-right: 0.25rem !important;
  }

  .pe-lg-2 {
    padding-right: 0.5rem !important;
  }

  .pe-lg-3 {
    padding-right: 1rem !important;
  }

  .pe-lg-4 {
    padding-right: 1.5rem !important;
  }

  .pe-lg-5 {
    padding-right: 3rem !important;
  }

  .pb-lg-0 {
    padding-bottom: 0 !important;
  }

  .pb-lg-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-lg-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-lg-3 {
    padding-bottom: 1rem !important;
  }

  .pb-lg-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-lg-5 {
    padding-bottom: 3rem !important;
  }

  .ps-lg-0 {
    padding-left: 0 !important;
  }

  .ps-lg-1 {
    padding-left: 0.25rem !important;
  }

  .ps-lg-2 {
    padding-left: 0.5rem !important;
  }

  .ps-lg-3 {
    padding-left: 1rem !important;
  }

  .ps-lg-4 {
    padding-left: 1.5rem !important;
  }

  .ps-lg-5 {
    padding-left: 3rem !important;
  }

  .text-lg-start {
    text-align: left !important;
  }

  .text-lg-end {
    text-align: right !important;
  }

  .text-lg-center {
    text-align: center !important;
  }
}

@media (min-width: 1200px) {
  .float-xl-start {
    float: left !important;
  }

  .float-xl-end {
    float: right !important;
  }

  .float-xl-none {
    float: none !important;
  }

  .d-xl-inline {
    display: inline !important;
  }

  .d-xl-inline-block {
    display: inline-block !important;
  }

  .d-xl-block {
    display: block !important;
  }

  .d-xl-grid {
    display: grid !important;
  }

  .d-xl-table {
    display: table !important;
  }

  .d-xl-table-row {
    display: table-row !important;
  }

  .d-xl-table-cell {
    display: table-cell !important;
  }

  .d-xl-flex {
    display: flex !important;
  }

  .d-xl-inline-flex {
    display: inline-flex !important;
  }

  .d-xl-none {
    display: none !important;
  }

  .flex-xl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xl-row {
    flex-direction: row !important;
  }

  .flex-xl-column {
    flex-direction: column !important;
  }

  .flex-xl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xl-0 {
    gap: 0 !important;
  }

  .gap-xl-1 {
    gap: 0.25rem !important;
  }

  .gap-xl-2 {
    gap: 0.5rem !important;
  }

  .gap-xl-3 {
    gap: 1rem !important;
  }

  .gap-xl-4 {
    gap: 1.5rem !important;
  }

  .gap-xl-5 {
    gap: 3rem !important;
  }

  .justify-content-xl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xl-center {
    justify-content: center !important;
  }

  .justify-content-xl-between {
    justify-content: space-between !important;
  }

  .justify-content-xl-around {
    justify-content: space-around !important;
  }

  .justify-content-xl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xl-start {
    align-items: flex-start !important;
  }

  .align-items-xl-end {
    align-items: flex-end !important;
  }

  .align-items-xl-center {
    align-items: center !important;
  }

  .align-items-xl-baseline {
    align-items: baseline !important;
  }

  .align-items-xl-stretch {
    align-items: stretch !important;
  }

  .align-content-xl-start {
    align-content: flex-start !important;
  }

  .align-content-xl-end {
    align-content: flex-end !important;
  }

  .align-content-xl-center {
    align-content: center !important;
  }

  .align-content-xl-between {
    align-content: space-between !important;
  }

  .align-content-xl-around {
    align-content: space-around !important;
  }

  .align-content-xl-stretch {
    align-content: stretch !important;
  }

  .align-self-xl-auto {
    align-self: auto !important;
  }

  .align-self-xl-start {
    align-self: flex-start !important;
  }

  .align-self-xl-end {
    align-self: flex-end !important;
  }

  .align-self-xl-center {
    align-self: center !important;
  }

  .align-self-xl-baseline {
    align-self: baseline !important;
  }

  .align-self-xl-stretch {
    align-self: stretch !important;
  }

  .order-xl-first {
    order: -1 !important;
  }

  .order-xl-0 {
    order: 0 !important;
  }

  .order-xl-1 {
    order: 1 !important;
  }

  .order-xl-2 {
    order: 2 !important;
  }

  .order-xl-3 {
    order: 3 !important;
  }

  .order-xl-4 {
    order: 4 !important;
  }

  .order-xl-5 {
    order: 5 !important;
  }

  .order-xl-last {
    order: 6 !important;
  }

  .m-xl-0 {
    margin: 0 !important;
  }

  .m-xl-1 {
    margin: 0.25rem !important;
  }

  .m-xl-2 {
    margin: 0.5rem !important;
  }

  .m-xl-3 {
    margin: 1rem !important;
  }

  .m-xl-4 {
    margin: 1.5rem !important;
  }

  .m-xl-5 {
    margin: 3rem !important;
  }

  .m-xl-auto {
    margin: auto !important;
  }

  .mx-xl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xl-0 {
    margin-top: 0 !important;
  }

  .mt-xl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xl-3 {
    margin-top: 1rem !important;
  }

  .mt-xl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xl-5 {
    margin-top: 3rem !important;
  }

  .mt-xl-auto {
    margin-top: auto !important;
  }

  .me-xl-0 {
    margin-right: 0 !important;
  }

  .me-xl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xl-3 {
    margin-right: 1rem !important;
  }

  .me-xl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xl-5 {
    margin-right: 3rem !important;
  }

  .me-xl-auto {
    margin-right: auto !important;
  }

  .mb-xl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xl-auto {
    margin-bottom: auto !important;
  }

  .ms-xl-0 {
    margin-left: 0 !important;
  }

  .ms-xl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xl-3 {
    margin-left: 1rem !important;
  }

  .ms-xl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xl-5 {
    margin-left: 3rem !important;
  }

  .ms-xl-auto {
    margin-left: auto !important;
  }

  .p-xl-0 {
    padding: 0 !important;
  }

  .p-xl-1 {
    padding: 0.25rem !important;
  }

  .p-xl-2 {
    padding: 0.5rem !important;
  }

  .p-xl-3 {
    padding: 1rem !important;
  }

  .p-xl-4 {
    padding: 1.5rem !important;
  }

  .p-xl-5 {
    padding: 3rem !important;
  }

  .px-xl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xl-0 {
    padding-top: 0 !important;
  }

  .pt-xl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xl-3 {
    padding-top: 1rem !important;
  }

  .pt-xl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xl-5 {
    padding-top: 3rem !important;
  }

  .pe-xl-0 {
    padding-right: 0 !important;
  }

  .pe-xl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xl-3 {
    padding-right: 1rem !important;
  }

  .pe-xl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xl-5 {
    padding-right: 3rem !important;
  }

  .pb-xl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xl-0 {
    padding-left: 0 !important;
  }

  .ps-xl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xl-3 {
    padding-left: 1rem !important;
  }

  .ps-xl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xl-5 {
    padding-left: 3rem !important;
  }

  .text-xl-start {
    text-align: left !important;
  }

  .text-xl-end {
    text-align: right !important;
  }

  .text-xl-center {
    text-align: center !important;
  }
}

@media (min-width: 1500px) {
  .float-xxl-start {
    float: left !important;
  }

  .float-xxl-end {
    float: right !important;
  }

  .float-xxl-none {
    float: none !important;
  }

  .d-xxl-inline {
    display: inline !important;
  }

  .d-xxl-inline-block {
    display: inline-block !important;
  }

  .d-xxl-block {
    display: block !important;
  }

  .d-xxl-grid {
    display: grid !important;
  }

  .d-xxl-table {
    display: table !important;
  }

  .d-xxl-table-row {
    display: table-row !important;
  }

  .d-xxl-table-cell {
    display: table-cell !important;
  }

  .d-xxl-flex {
    display: flex !important;
  }

  .d-xxl-inline-flex {
    display: inline-flex !important;
  }

  .d-xxl-none {
    display: none !important;
  }

  .flex-xxl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xxl-row {
    flex-direction: row !important;
  }

  .flex-xxl-column {
    flex-direction: column !important;
  }

  .flex-xxl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xxl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xxl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xxl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xxl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xxl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xxl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xxl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xxl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xxl-0 {
    gap: 0 !important;
  }

  .gap-xxl-1 {
    gap: 0.25rem !important;
  }

  .gap-xxl-2 {
    gap: 0.5rem !important;
  }

  .gap-xxl-3 {
    gap: 1rem !important;
  }

  .gap-xxl-4 {
    gap: 1.5rem !important;
  }

  .gap-xxl-5 {
    gap: 3rem !important;
  }

  .justify-content-xxl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xxl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xxl-center {
    justify-content: center !important;
  }

  .justify-content-xxl-between {
    justify-content: space-between !important;
  }

  .justify-content-xxl-around {
    justify-content: space-around !important;
  }

  .justify-content-xxl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xxl-start {
    align-items: flex-start !important;
  }

  .align-items-xxl-end {
    align-items: flex-end !important;
  }

  .align-items-xxl-center {
    align-items: center !important;
  }

  .align-items-xxl-baseline {
    align-items: baseline !important;
  }

  .align-items-xxl-stretch {
    align-items: stretch !important;
  }

  .align-content-xxl-start {
    align-content: flex-start !important;
  }

  .align-content-xxl-end {
    align-content: flex-end !important;
  }

  .align-content-xxl-center {
    align-content: center !important;
  }

  .align-content-xxl-between {
    align-content: space-between !important;
  }

  .align-content-xxl-around {
    align-content: space-around !important;
  }

  .align-content-xxl-stretch {
    align-content: stretch !important;
  }

  .align-self-xxl-auto {
    align-self: auto !important;
  }

  .align-self-xxl-start {
    align-self: flex-start !important;
  }

  .align-self-xxl-end {
    align-self: flex-end !important;
  }

  .align-self-xxl-center {
    align-self: center !important;
  }

  .align-self-xxl-baseline {
    align-self: baseline !important;
  }

  .align-self-xxl-stretch {
    align-self: stretch !important;
  }

  .order-xxl-first {
    order: -1 !important;
  }

  .order-xxl-0 {
    order: 0 !important;
  }

  .order-xxl-1 {
    order: 1 !important;
  }

  .order-xxl-2 {
    order: 2 !important;
  }

  .order-xxl-3 {
    order: 3 !important;
  }

  .order-xxl-4 {
    order: 4 !important;
  }

  .order-xxl-5 {
    order: 5 !important;
  }

  .order-xxl-last {
    order: 6 !important;
  }

  .m-xxl-0 {
    margin: 0 !important;
  }

  .m-xxl-1 {
    margin: 0.25rem !important;
  }

  .m-xxl-2 {
    margin: 0.5rem !important;
  }

  .m-xxl-3 {
    margin: 1rem !important;
  }

  .m-xxl-4 {
    margin: 1.5rem !important;
  }

  .m-xxl-5 {
    margin: 3rem !important;
  }

  .m-xxl-auto {
    margin: auto !important;
  }

  .mx-xxl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xxl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xxl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xxl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xxl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xxl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xxl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xxl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xxl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xxl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xxl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xxl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xxl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xxl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xxl-0 {
    margin-top: 0 !important;
  }

  .mt-xxl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xxl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xxl-3 {
    margin-top: 1rem !important;
  }

  .mt-xxl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xxl-5 {
    margin-top: 3rem !important;
  }

  .mt-xxl-auto {
    margin-top: auto !important;
  }

  .me-xxl-0 {
    margin-right: 0 !important;
  }

  .me-xxl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xxl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xxl-3 {
    margin-right: 1rem !important;
  }

  .me-xxl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xxl-5 {
    margin-right: 3rem !important;
  }

  .me-xxl-auto {
    margin-right: auto !important;
  }

  .mb-xxl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xxl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xxl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xxl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xxl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xxl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xxl-auto {
    margin-bottom: auto !important;
  }

  .ms-xxl-0 {
    margin-left: 0 !important;
  }

  .ms-xxl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xxl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xxl-3 {
    margin-left: 1rem !important;
  }

  .ms-xxl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xxl-5 {
    margin-left: 3rem !important;
  }

  .ms-xxl-auto {
    margin-left: auto !important;
  }

  .p-xxl-0 {
    padding: 0 !important;
  }

  .p-xxl-1 {
    padding: 0.25rem !important;
  }

  .p-xxl-2 {
    padding: 0.5rem !important;
  }

  .p-xxl-3 {
    padding: 1rem !important;
  }

  .p-xxl-4 {
    padding: 1.5rem !important;
  }

  .p-xxl-5 {
    padding: 3rem !important;
  }

  .px-xxl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xxl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xxl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xxl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xxl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xxl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xxl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xxl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xxl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xxl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xxl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xxl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xxl-0 {
    padding-top: 0 !important;
  }

  .pt-xxl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xxl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xxl-3 {
    padding-top: 1rem !important;
  }

  .pt-xxl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xxl-5 {
    padding-top: 3rem !important;
  }

  .pe-xxl-0 {
    padding-right: 0 !important;
  }

  .pe-xxl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xxl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xxl-3 {
    padding-right: 1rem !important;
  }

  .pe-xxl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xxl-5 {
    padding-right: 3rem !important;
  }

  .pb-xxl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xxl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xxl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xxl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xxl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xxl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xxl-0 {
    padding-left: 0 !important;
  }

  .ps-xxl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xxl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xxl-3 {
    padding-left: 1rem !important;
  }

  .ps-xxl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xxl-5 {
    padding-left: 3rem !important;
  }

  .text-xxl-start {
    text-align: left !important;
  }

  .text-xxl-end {
    text-align: right !important;
  }

  .text-xxl-center {
    text-align: center !important;
  }
}

@media (min-width: 1700px) {
  .float-xxxl-start {
    float: left !important;
  }

  .float-xxxl-end {
    float: right !important;
  }

  .float-xxxl-none {
    float: none !important;
  }

  .d-xxxl-inline {
    display: inline !important;
  }

  .d-xxxl-inline-block {
    display: inline-block !important;
  }

  .d-xxxl-block {
    display: block !important;
  }

  .d-xxxl-grid {
    display: grid !important;
  }

  .d-xxxl-table {
    display: table !important;
  }

  .d-xxxl-table-row {
    display: table-row !important;
  }

  .d-xxxl-table-cell {
    display: table-cell !important;
  }

  .d-xxxl-flex {
    display: flex !important;
  }

  .d-xxxl-inline-flex {
    display: inline-flex !important;
  }

  .d-xxxl-none {
    display: none !important;
  }

  .flex-xxxl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xxxl-row {
    flex-direction: row !important;
  }

  .flex-xxxl-column {
    flex-direction: column !important;
  }

  .flex-xxxl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xxxl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xxxl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xxxl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xxxl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xxxl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xxxl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xxxl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xxxl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xxxl-0 {
    gap: 0 !important;
  }

  .gap-xxxl-1 {
    gap: 0.25rem !important;
  }

  .gap-xxxl-2 {
    gap: 0.5rem !important;
  }

  .gap-xxxl-3 {
    gap: 1rem !important;
  }

  .gap-xxxl-4 {
    gap: 1.5rem !important;
  }

  .gap-xxxl-5 {
    gap: 3rem !important;
  }

  .justify-content-xxxl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xxxl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xxxl-center {
    justify-content: center !important;
  }

  .justify-content-xxxl-between {
    justify-content: space-between !important;
  }

  .justify-content-xxxl-around {
    justify-content: space-around !important;
  }

  .justify-content-xxxl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xxxl-start {
    align-items: flex-start !important;
  }

  .align-items-xxxl-end {
    align-items: flex-end !important;
  }

  .align-items-xxxl-center {
    align-items: center !important;
  }

  .align-items-xxxl-baseline {
    align-items: baseline !important;
  }

  .align-items-xxxl-stretch {
    align-items: stretch !important;
  }

  .align-content-xxxl-start {
    align-content: flex-start !important;
  }

  .align-content-xxxl-end {
    align-content: flex-end !important;
  }

  .align-content-xxxl-center {
    align-content: center !important;
  }

  .align-content-xxxl-between {
    align-content: space-between !important;
  }

  .align-content-xxxl-around {
    align-content: space-around !important;
  }

  .align-content-xxxl-stretch {
    align-content: stretch !important;
  }

  .align-self-xxxl-auto {
    align-self: auto !important;
  }

  .align-self-xxxl-start {
    align-self: flex-start !important;
  }

  .align-self-xxxl-end {
    align-self: flex-end !important;
  }

  .align-self-xxxl-center {
    align-self: center !important;
  }

  .align-self-xxxl-baseline {
    align-self: baseline !important;
  }

  .align-self-xxxl-stretch {
    align-self: stretch !important;
  }

  .order-xxxl-first {
    order: -1 !important;
  }

  .order-xxxl-0 {
    order: 0 !important;
  }

  .order-xxxl-1 {
    order: 1 !important;
  }

  .order-xxxl-2 {
    order: 2 !important;
  }

  .order-xxxl-3 {
    order: 3 !important;
  }

  .order-xxxl-4 {
    order: 4 !important;
  }

  .order-xxxl-5 {
    order: 5 !important;
  }

  .order-xxxl-last {
    order: 6 !important;
  }

  .m-xxxl-0 {
    margin: 0 !important;
  }

  .m-xxxl-1 {
    margin: 0.25rem !important;
  }

  .m-xxxl-2 {
    margin: 0.5rem !important;
  }

  .m-xxxl-3 {
    margin: 1rem !important;
  }

  .m-xxxl-4 {
    margin: 1.5rem !important;
  }

  .m-xxxl-5 {
    margin: 3rem !important;
  }

  .m-xxxl-auto {
    margin: auto !important;
  }

  .mx-xxxl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xxxl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xxxl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xxxl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xxxl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xxxl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xxxl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xxxl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xxxl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xxxl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xxxl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xxxl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xxxl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xxxl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xxxl-0 {
    margin-top: 0 !important;
  }

  .mt-xxxl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xxxl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xxxl-3 {
    margin-top: 1rem !important;
  }

  .mt-xxxl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xxxl-5 {
    margin-top: 3rem !important;
  }

  .mt-xxxl-auto {
    margin-top: auto !important;
  }

  .me-xxxl-0 {
    margin-right: 0 !important;
  }

  .me-xxxl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xxxl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xxxl-3 {
    margin-right: 1rem !important;
  }

  .me-xxxl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xxxl-5 {
    margin-right: 3rem !important;
  }

  .me-xxxl-auto {
    margin-right: auto !important;
  }

  .mb-xxxl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xxxl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xxxl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xxxl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xxxl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xxxl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xxxl-auto {
    margin-bottom: auto !important;
  }

  .ms-xxxl-0 {
    margin-left: 0 !important;
  }

  .ms-xxxl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xxxl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xxxl-3 {
    margin-left: 1rem !important;
  }

  .ms-xxxl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xxxl-5 {
    margin-left: 3rem !important;
  }

  .ms-xxxl-auto {
    margin-left: auto !important;
  }

  .p-xxxl-0 {
    padding: 0 !important;
  }

  .p-xxxl-1 {
    padding: 0.25rem !important;
  }

  .p-xxxl-2 {
    padding: 0.5rem !important;
  }

  .p-xxxl-3 {
    padding: 1rem !important;
  }

  .p-xxxl-4 {
    padding: 1.5rem !important;
  }

  .p-xxxl-5 {
    padding: 3rem !important;
  }

  .px-xxxl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xxxl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xxxl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xxxl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xxxl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xxxl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xxxl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xxxl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xxxl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xxxl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xxxl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xxxl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xxxl-0 {
    padding-top: 0 !important;
  }

  .pt-xxxl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xxxl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xxxl-3 {
    padding-top: 1rem !important;
  }

  .pt-xxxl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xxxl-5 {
    padding-top: 3rem !important;
  }

  .pe-xxxl-0 {
    padding-right: 0 !important;
  }

  .pe-xxxl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xxxl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xxxl-3 {
    padding-right: 1rem !important;
  }

  .pe-xxxl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xxxl-5 {
    padding-right: 3rem !important;
  }

  .pb-xxxl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xxxl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xxxl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xxxl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xxxl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xxxl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xxxl-0 {
    padding-left: 0 !important;
  }

  .ps-xxxl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xxxl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xxxl-3 {
    padding-left: 1rem !important;
  }

  .ps-xxxl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xxxl-5 {
    padding-left: 3rem !important;
  }

  .text-xxxl-start {
    text-align: left !important;
  }

  .text-xxxl-end {
    text-align: right !important;
  }

  .text-xxxl-center {
    text-align: center !important;
  }
}

@media (min-width: 1200px) {
  .fs-1 {
    font-size: 5rem !important;
  }

  .fs-2 {
    font-size: 2rem !important;
  }

  .fs-3 {
    font-size: 1.625rem !important;
  }

  .fs-sm-1 {
    font-size: 5rem !important;
  }

  .fs-sm-2 {
    font-size: 2rem !important;
  }

  .fs-sm-3 {
    font-size: 1.625rem !important;
  }

  .fs-md-1 {
    font-size: 5rem !important;
  }

  .fs-md-2 {
    font-size: 2rem !important;
  }

  .fs-md-3 {
    font-size: 1.625rem !important;
  }

  .fs-lg-1 {
    font-size: 5rem !important;
  }

  .fs-lg-2 {
    font-size: 2rem !important;
  }

  .fs-lg-3 {
    font-size: 1.625rem !important;
  }
}

@media print {
  .d-print-inline {
    display: inline !important;
  }

  .d-print-inline-block {
    display: inline-block !important;
  }

  .d-print-block {
    display: block !important;
  }

  .d-print-grid {
    display: grid !important;
  }

  .d-print-table {
    display: table !important;
  }

  .d-print-table-row {
    display: table-row !important;
  }

  .d-print-table-cell {
    display: table-cell !important;
  }

  .d-print-flex {
    display: flex !important;
  }

  .d-print-inline-flex {
    display: inline-flex !important;
  }

  .d-print-none {
    display: none !important;
  }
}

/*! =========================================================
 * bootstrap-slider.js
 *
 * Maintainers:
 *    Kyle Kemp
 *      - Twitter: @seiyria
 *      - Github:  seiyria
 *    Rohit Kalkur
 *      - Twitter: @Rovolutionary
 *      - Github:  rovolution
 *
 * =========================================================
 *
 * bootstrap-slider is released under the MIT License
 * Copyright (c) 2019 Kyle Kemp, Rohit Kalkur, and contributors
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * ========================================================= */
/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
.slider {
  display: inline-block;
  vertical-align: middle;
  position: relative;
}

.slider.slider-horizontal {
  width: 100%;
  height: 18px;
}

.slider.slider-horizontal .slider-track {
  height: 6px;
  width: 100%;
  margin-top: 6px;
  top: 0;
  left: 0;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
}

.slider.slider-horizontal .slider-selection,
.slider.slider-horizontal .slider-track-low,
.slider.slider-horizontal .slider-track-high {
  height: 100%;
  top: 0;
  bottom: 0;
}

.slider.slider-horizontal .slider-tick,
.slider.slider-horizontal .slider-handle {
  margin-left: -9px;
}

.slider.slider-horizontal .slider-tick.triangle,
.slider.slider-horizontal .slider-handle.triangle {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  border-width: 0 9px 9px 9px;
  width: 0;
  height: 0;
  border-bottom-color: #151515;
  margin-top: 0;
}

.slider.slider-horizontal .slider-handle.min-slider-handle {
  margin-left: 0;
}

.slider.slider-horizontal .slider-handle.max-slider-handle {
  margin-left: -18px;
}

.slider.slider-horizontal .slider-tick-container {
  white-space: nowrap;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
}

.slider.slider-horizontal .slider-tick-label-container {
  white-space: nowrap;
  margin-top: 18px;
}

.slider.slider-horizontal .slider-tick-label-container .slider-tick-label {
  display: inline-block;
  text-align: center;
}

.slider.slider-horizontal.slider-rtl .slider-track {
  left: initial;
  right: 0;
}

.slider.slider-horizontal.slider-rtl .slider-tick,
.slider.slider-horizontal.slider-rtl .slider-handle {
  margin-left: initial;
  margin-right: -9px;
}

.slider.slider-horizontal.slider-rtl .slider-tick-container {
  left: initial;
  right: 0;
}

.slider.slider-vertical {
  height: 210px;
  width: 18px;
}

.slider.slider-vertical .slider-track {
  width: 9px;
  height: 100%;
  left: 25%;
  top: 0;
}

.slider.slider-vertical .slider-selection {
  width: 100%;
  left: 0;
  top: 0;
  bottom: 0;
}

.slider.slider-vertical .slider-track-low,
.slider.slider-vertical .slider-track-high {
  width: 100%;
  left: 0;
  right: 0;
}

.slider.slider-vertical .slider-tick,
.slider.slider-vertical .slider-handle {
  margin-top: -6px;
}

.slider.slider-vertical .slider-tick.triangle,
.slider.slider-vertical .slider-handle.triangle {
  border-width: 9px 0 9px 9px;
  width: 1px;
  height: 1px;
  border-left-color: #151515;
  margin-left: 0;
}

.slider.slider-vertical .slider-tick-label-container {
  white-space: nowrap;
}

.slider.slider-vertical .slider-tick-label-container .slider-tick-label {
  padding-left: 3.6px;
}

.slider.slider-vertical.slider-rtl .slider-track {
  left: initial;
  right: 25%;
}

.slider.slider-vertical.slider-rtl .slider-selection {
  left: initial;
  right: 0;
}

.slider.slider-vertical.slider-rtl .slider-tick.triangle,
.slider.slider-vertical.slider-rtl .slider-handle.triangle {
  border-width: 9px 9px 9px 0;
}

.slider.slider-vertical.slider-rtl .slider-tick-label-container .slider-tick-label {
  padding-left: initial;
  padding-right: 3.6px;
}

.slider.slider-disabled .slider-handle {
  background-color: #cfcfcf;
  background-image: -moz-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#DFDFDF), to(#BEBEBE));
  background-image: -webkit-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: -o-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: linear-gradient(to bottom, #DFDFDF, #BEBEBE);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#DFDFDF', endColorstr='#BEBEBE', GradientType=0);
}

.slider.slider-disabled .slider-track {
  background-color: #e7e7e7;
  background-image: -moz-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#E5E5E5), to(#E9E9E9));
  background-image: -webkit-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: -o-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: linear-gradient(to bottom, #E5E5E5, #E9E9E9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#E5E5E5', endColorstr='#E9E9E9', GradientType=0);
  cursor: not-allowed;
}

.slider input {
  display: none;
}

.slider .tooltip-inner {
  white-space: nowrap;
  max-width: none;
  border: 1px solid #e7e7ec;
  border-radius: 0;
  background-color: #fff;
  color: #222222;
  box-shadow: 0 8px 15px 0 rgba(140, 152, 164, 0.1);
}

.slider .bs-tooltip-top .tooltip-inner,
.slider .bs-tooltip-auto[data-popper-placement^="top"] .tooltip-inner,
.slider .bs-tooltip-bottom .tooltip-inner,
.slider .bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-inner {
  position: relative;
  left: -50%;
}

.slider.bs-tooltip-left .tooltip-inner,
.slider.bs-tooltip-right .tooltip-inner {
  position: relative;
  top: -100%;
}

.slider .tooltip {
  pointer-events: none;
}

.slider .tooltip.bs-tooltip-top .arrow,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="top"] .arrow,
.slider .tooltip.bs-tooltip-bottom .arrow,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="bottom"] .arrow {
  left: -.4rem;
}

.slider .tooltip.bs-tooltip-top,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="top"] {
  margin-top: -44px;
}

.slider .tooltip.bs-tooltip-bottom,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="bottom"] {
  margin-top: 2px;
}

.slider .tooltip.bs-tooltip-left,
.slider .tooltip.bs-tooltip-right {
  margin-top: -14px;
}

.slider .tooltip.bs-tooltip-left .arrow,
.slider .tooltip.bs-tooltip-right .arrow {
  top: 8px;
}

.slider .tooltip.tooltip-min {
  transform: translateX(50%);
}

.slider .tooltip.tooltip-max {
  transform: translateX(-50%);
}

.slider .hide {
  display: none;
}

.slider-track {
  position: absolute;
  background-color: #e4e4e4;
  cursor: pointer;
}

.slider-selection {
  position: absolute;
  background-color: #222222;
}

.slider-selection.tick-slider-selection {
  background-color: #6f5858;
  background-image: -moz-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#7e5454), to(#5f5b5b));
  background-image: -webkit-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -o-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: linear-gradient(to bottom, #7e5454, #5f5b5b);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#7e5454', endColorstr='#5f5b5b', GradientType=0);
}

.slider-track-low,
.slider-track-high {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  position: absolute;
  background: transparent;
}

.slider-handle {
  position: absolute;
  top: 0;
  width: 18px;
  height: 18px;
  background-color: #ffffff;
  border: 0.125rem solid #222222;
}

.slider-handle:hover {
  cursor: pointer;
}

.slider-handle.round {
  -webkit-border-radius: 18px;
  -moz-border-radius: 18px;
  border-radius: 18px;
}

.slider-handle.triangle {
  background: transparent none;
}

.slider-handle.custom {
  background: transparent none;
}

.slider-handle.custom::before {
  line-height: 18px;
  font-size: 20px;
  content: '\2605';
  color: #726204;
}

.slider-tick {
  background-color: #f7f7f7;
  background-image: -moz-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#F5F5F5), to(#F9F9F9));
  background-image: -webkit-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: -o-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: linear-gradient(to bottom, #F5F5F5, #F9F9F9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#F5F5F5', endColorstr='#F9F9F9', GradientType=0);
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -moz-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  position: absolute;
  cursor: pointer;
  width: 18px;
  height: 18px;
  filter: none;
  opacity: 0.8;
  border: 0px solid transparent;
}

.slider-tick.round {
  border-radius: 50%;
}

.slider-tick.triangle {
  background: transparent none;
}

.slider-tick.custom {
  background: transparent none;
}

.slider-tick.custom::before {
  line-height: 18px;
  font-size: 20px;
  content: '\2605';
  color: #726204;
}

.slider-tick.in-selection {
  background-color: #6f5858;
  background-image: -moz-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#7e5454), to(#5f5b5b));
  background-image: -webkit-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -o-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: linear-gradient(to bottom, #7e5454, #5f5b5b);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#7e5454', endColorstr='#5f5b5b', GradientType=0);
  opacity: 1;
}

/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
body {
  background-color: #ffffff;
}

.flex-1 {
  flex: 1 !important;
}

.bg-black {
  background-color: #222222 !important;
}

.bg-grey-faf9f8 {
  background-color: #FAF9F8 !important;
}

.bg-grey-eeeeee {
  background-color: #EEE !important;
}

.bg-grey-f7f5ee {
  background-color: #f7f5ee !important;
}

.bg-yellow {
  background-color: #F3EDDF !important;
}

.bg-yellow-ffd35b {
  background-color: #FFD35B !important;
}

.bg-light-green-e4f5f2 {
  background-color: #e4f5f2 !important;
}

.color-white {
  color: #fff !important;
}

.color-gray-5a5a5a {
  color: #5a5a5a !important;
}

.bottom-3 {
  bottom: 3rem !important;
}

.object-fit-cover {
  object-fit: cover;
}

.object-position-top {
  object-position: top;
}

.background-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
}

.background-img_overlay::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(34, 34, 34, 0.4);
}

.hover__content,
.js-hidden-content {
  position: absolute;
  top: 100%;
  width: 100%;
  min-width: 16rem;
  transition: all 0.2s ease;
  background-color: #ffffff;
  box-shadow: 0 0 1.5625rem 0 rgba(34, 34, 34, 0.05);
  opacity: 0;
  visibility: hidden;
  z-index: 1000;
}

.hover-container:hover .hover__content,
.hover-container.js-content_visible .js-hidden-content {
  opacity: 1;
  visibility: visible;
}

.content_abs {
  position: absolute;
  --content-space: 1.875rem;
}

.content_center {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.content_top {
  top: var(--content-space);
  padding-bottom: var(--content-space);
}

.content_right {
  right: var(--content-space);
  padding-left: var(--content-space);
}

.content_bottom {
  bottom: var(--content-space);
  padding-top: var(--content-space);
}

.content_left {
  left: var(--content-space);
  padding-right: var(--content-space);
}

@media (min-width: 768px) {
  .content_top-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_right-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_bottom-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_left-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 1200px) {
  .content_top-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_right-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_bottom-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_left-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 992px) {
  .h-md-100 {
    height: 100% !important;
  }
}

.pos_right-center {
  left: 50%;
}

.pos_right-center-71 {
  left: 71%;
}

@media (min-width: 992px) {
  .pos_right-center {
    left: 60%;
  }

  .pos_right-center-70 {
    left: 70%;
  }
}

.scrollbar-gray ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  height: .25rem;
  background-color: #eeeeee;
}

.scrollbar-gray ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #767676;
}

.sticky-content {
  position: sticky;
  top: 0;
  padding-bottom: 1px;
}

.border-circle {
  border-radius: 10rem !important;
}

.border-radius-0 {
  border-radius: 0 !important;
}

.border-radius-4 {
  border-radius: 4px !important;
}

.border-radius-8 {
  border-radius: 8px !important;
}

.border-radius-10 {
  border-radius: 10px !important;
}

.swiper-scrollbar {
  height: 4px;
}

.left-auto {
  left: auto !important;
}

.right-auto {
  right: auto !important;
}

.left-0 {
  left: 0 !important;
}

.right-0 {
  right: 0 !important;
}

.position-center {
  left: 50% !important;
  top: 50% !important;
  transform: translate(-50%, -50%) !important;
}

.position-top-center {
  left: 50% !important;
  top: 0;
  transform: translateX(-50%) !important;
}

.position-right-center {
  left: auto !important;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  max-width: 50%;
}

.position-right-bottom {
  left: auto !important;
  right: 0;
  top: auto;
  bottom: 0;
  max-width: 50%;
}

.left-50 {
  left: 50%;
  transform: translateX(-50%);
}

@media (min-width: 1200px) {
  .row-cols-xl-8>* {
    flex: 0 0 auto;
    width: 12.5% !important;
  }
}

.minh-100 {
  min-height: 100vh;
}

.minh-240 {
  min-height: 16rem;
}

.rect-circle {
  width: 100%;
  padding-top: 100%;
  position: relative;
  border-radius: 10rem;
}

.bg-image {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.bg-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bg-video {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-video {
  position: absolute;
  left: 0.3125rem;
  right: 0.3125rem;
  top: 0.3125rem;
  bottom: 0.3125rem;
  z-index: -1;
  width: calc(100% - 0.625rem);
  height: calc(100% - 0.625rem);
  object-fit: cover;
}

.border-left-0 {
  border-left: 0;
}

@media (min-width: 992px) {
  .border-left-lg-1 {
    border-left: 1px solid #eee;
  }
}

.border-top-1 {
  border-top: 1px solid #eee;
}

@media (min-width: 992px) {
  .border-top-lg-0 {
    border-top: 0;
  }
}

.border-1 {
  border: 1px solid #eee !important;
}

.border-white {
  border-color: #fff !important;
}

.object-position-right {
  object-position: 90% center;
}

.popover {
  border: 0;
  box-shadow: 0 0 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0;
}

.popover img {
  width: 170px;
}

.bs-popover-end>.popover-arrow,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow {
  margin: 0;
}

.bs-popover-end>.popover-arrow:before,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow:before {
  border-color: transparent;
}

.text-yellow-bg-rounded {
  display: inline-block;
  background-color: #FFD35B;
  padding: 0.5125rem 1rem 0.3125rem;
  border-radius: 2rem;
}

.mb--1 {
  margin-bottom: -1px;
}

.mb-1px {
  margin-bottom: 1px;
}

.body-color {
  color: #222222 !important;
}

.body-color-secondary {
  color: #767676 !important;
}

.theme-color {
  color: #193174 !important;
}

.theme-bg-color {
  background-color: #193174 !important;
}

.theme-color-secondary {
  color: #EBB73F !important;
}

.theme-bg-color-secondary {
  background-color: #EBB73F !important;
}

.theme-color-third {
  color: #86BC42 !important;
}

.theme-bg-color-third {
  background-color: #86BC42 !important;
}

.text-shadow-white {
  text-shadow: 0 0 0.1rem #ffffff;
}

.text-outline-white {
  color: #222222; /* Fill color of the text */
  text-shadow: 
  -1px -1px 0 1px #afafaf,  
  1px -1px 0 1px #afafaf,
  -1px 1px 0 1px #afafaf,
  1px 1px 0 1px #afafaf; /* Width and color of the outline */
}


@media (min-width: 768px) {
  .h-md-100 {
    height: 100% !important;
  }
}

@media (min-width: 576px) {
  .h-sm-100 {
    height: 100% !important;
  }
}

svg.flaticon {
  display: block;
}

.transparent-bg {
  background-color: transparent !important;
}

.bg-white-overlay {
  background-color: rgba(255, 255, 255, 0.9);
}

.pt-100per {
  padding-top: 100% !important;
}

@media (min-width: 768px) {
  .text-md-right {
    text-align: right !important;
  }

  .order-md-12 {
    order: 12;
  }
}

@media (min-width: 992px) {
  .order-lg--1 {
    order: -1;
  }
}

@media (min-width: 992px) {
  .mt-lg--5 {
    margin-top: -13rem !important;
  }
}

.mt--3 {
  margin-top: -3rem !important;
}

.swiper-scrollbar-drag {
  background-color: rgba(0, 0, 0, 0.5);
}

@font-face {
  font-family: 'SofiaProBold';
  src: url(../fonts/SofiaProBold.woff);
}

body {
  color: #222222;
  font-family: "Jost", sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
}

/*============================================*/
/*================= Headings =================*/
/*============================================*/
h1,
.h1,
h2,
.h2,
h3,
.h3,
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  color: #222222;
  font-family: "Jost", sans-serif;
  font-weight: 500;
}

.font-special {
  font-family: "Allura", cursive;
}

.font-courgette {
  font-family: Courgette;
}

.fs-base,
.form-title {
  font-size: 0.875rem !important;
}

.font-sofia {
  font-family: 'SofiaProBold';
}

.third-color {
  color: #b9a16b !important;
}

.white-color {
  color: #fff !important;
}

.mark-grey-color {
  -webkit-text-stroke-color: #c2c2c2;
}

.page-title {
  font-weight: 700;
}

@media (min-width: 992px) {
  .page-title {
    font-size: 3.125rem;
  }
}

.section-title {
  font-size: 1.625rem;
}

@media (min-width: 992px) {
  .section-title {
    font-size: 2.1875rem;
  }
}

.lh-30 {
  line-height: 1.875rem !important;
}

.lh-2rem {
  line-height: 2rem !important;
}

.block-title {
  margin-bottom: 1rem;
  font-size: 1rem;
}

/*============================================*/
/*=================== Texts ==================*/
/*============================================*/
.character_markup {
  display: none;
}

@media (min-width: 1500px) {
  .character_markup {
    display: block;
    position: absolute;
    bottom: 5rem;
    margin-left: -1.5em;
    -webkit-text-stroke-width: 3px;
    -webkit-text-stroke-color: #ffffff;
    color: transparent;
    font-size: 7.5rem;
    transform: rotate(90deg);
    transform-origin: bottom right;
    opacity: 0.8;
  }

  .character_markup.type2 {
    transform: none;
    font-size: 15.625rem;
    -webkit-text-stroke-color: #767676;
    font-weight: 700;
    bottom: 0;
    line-height: 1;
    left: auto;
    margin: 0;
    right: 0;
    opacity: 0.3;
    letter-spacing: 0.05em;
    z-index: -1;
  }
}

.content {
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  line-height: 1.7143;
}

.blockquote {
  padding: calc(1.4rem + 1.8vw) calc(1.3625rem + 1.35vw) calc(1.35625rem + 1.275vw) calc(1.4875rem + 2.85vw);
  background-color: #faf9f8;
}

@media (min-width: 1200px) {
  .blockquote {
    padding: 2.75rem 2.375rem 2.3125rem 3.625rem;
  }
}

.blockquote__content {
  margin-bottom: 0;
  font-size: 1rem;
  font-style: italic;
  font-weight: 500;
  line-height: 1.375;
}

.blockquote__footer {
  margin-top: 1.5rem;
  color: #767676;
  font-size: 0.875rem;
}

.text-list {
  padding-left: 1.25em;
}

.text-list__item {
  line-height: 3.143;
}

.list_dot_darkgray ::marker {
  color: #767676;
  font-size: 1rem;
}

.list-style_checkbox {
  display: flex;
  align-items: center;
}

.text_dash {
  position: relative;
  padding-left: 3.25rem;
}

.text_dash::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 2.5rem;
  height: 2px;
  margin-top: -1px;
  background-color: currentColor;
  color: inherit;
}

.text_dash_half {
  position: relative;
  padding-left: 2rem;
}

.text_dash_half::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 1.25rem;
  height: 2px;
  margin-top: -1px;
  background-color: currentColor;
  color: inherit;
}

.stroke-text {
  --stroke-color: #222222;
  --stroke-width: 1px;
  color: #eeeeee;
  font-size: 2.25rem;
  opacity: 0.4;
  text-shadow: var(--stroke-width) 0 0 var(--stroke-color), calc(var(--stroke-width) * -1) 0 0 var(--stroke-color), 0 var(--stroke-width) 0 var(--stroke-color), 0 calc(var(--stroke-width) * -1) 0 var(--stroke-color);
}

@media (min-width: 992px) {
  .stroke-text {
    --stroke-width: 2px;
    font-size: 3.375rem;
  }
}

@media (min-width: 1200px) {
  .stroke-text {
    font-size: 5.625rem;
  }
}

.smooth-16 {
  text-shadow: calc(var(--stroke-width) * 1) calc(var(--stroke-width) * 0) 0 var(--stroke-color), calc(var(--stroke-width) * 0.9239) calc(var(--stroke-width) * 0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * 0.7071) calc(var(--stroke-width) * 0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * 0.3827) calc(var(--stroke-width) * 0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0) calc(var(--stroke-width) * 1) 0 var(--stroke-color), calc(var(--stroke-width) * -0.3827) calc(var(--stroke-width) * 0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * -0.7071) calc(var(--stroke-width) * 0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * -0.9239) calc(var(--stroke-width) * 0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * -1) calc(var(--stroke-width) * 0) 0 var(--stroke-color), calc(var(--stroke-width) * -0.9239) calc(var(--stroke-width) * -0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * -0.7071) calc(var(--stroke-width) * -0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * -0.3827) calc(var(--stroke-width) * -0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0) calc(var(--stroke-width) * -1) 0 var(--stroke-color), calc(var(--stroke-width) * 0.3827) calc(var(--stroke-width) * -0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0.7071) calc(var(--stroke-width) * -0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * 0.9239) calc(var(--stroke-width) * -0.3827) 0 var(--stroke-color);
}

@media (min-width: 992px) {
  .text-lg-right {
    text-align: right !important;
  }
}

.fs-12 {
  font-size: 0.75rem !important;
}

.fs-13 {
  font-size: 0.8125rem !important;
}

.fs-15 {
  font-size: 0.9375rem !important;
}

.fs-18 {
  font-size: 1.125rem !important;
}

.fs-20 {
  font-size: 1.25rem;
}

.fs-22 {
  font-size: calc(1.2625rem + 0.15vw);
}

@media (min-width: 1200px) {
  .fs-22 {
    font-size: 1.375rem;
  }
}

.fs-25 {
  font-size: calc(1.28125rem + 0.375vw);
}

@media (min-width: 1200px) {
  .fs-25 {
    font-size: 1.5625rem;
  }
}

.fs-30 {
  font-size: calc(1.3125rem + 0.75vw);
}

@media (min-width: 1200px) {
  .fs-30 {
    font-size: 1.875rem;
  }
}

.fs-35 {
  font-size: calc(1.34375rem + 1.125vw);
}

@media (min-width: 1200px) {
  .fs-35 {
    font-size: 2.1875rem;
  }
}

.fs-40 {
  font-size: calc(1.375rem + 1.5vw);
}

@media (min-width: 1200px) {
  .fs-40 {
    font-size: 2.5rem;
  }
}

.fs-45 {
  font-size: calc(1.40625rem + 1.875vw);
}

@media (min-width: 1200px) {
  .fs-45 {
    font-size: 2.8125rem;
  }
}

.fs-50 {
  font-size: calc(1.4375rem + 2.25vw);
}

@media (min-width: 1200px) {
  .fs-50 {
    font-size: 3.125rem;
  }
}

.fs-70 {
  font-size: calc(1.5625rem + 3.75vw);
}

@media (min-width: 1200px) {
  .fs-70 {
    font-size: 4.375rem;
  }
}

.fs-100 {
  font-size: calc(1.75rem + 6vw);
}

@media (min-width: 1200px) {
  .fs-100 {
    font-size: 6.25rem;
  }
}

.fw-semi-bold {
  font-weight: 600 !important;
}

th[align="right"] {
  text-align: right;
}

@keyframes moveDown {
  0% {
    transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
  }

  100% {
    transform: translateY(0);
    -webkit-transform: translateY(0);
  }
}

.animate {
  transition: all ease-in .5s;
  transition: all cubic-bezier(0.445, 0.05, 0.55, 0.95) 0.5s;
}

.animate_fade {
  opacity: 0;
  visibility: hidden;
}

.animate_rtl {
  position: relative;
  right: -2.5rem;
}

.animate_btt {
  position: relative;
  bottom: -2.5rem;
}

.animate_delay-1 {
  transition-delay: 0.1s;
}

.animate_delay-2 {
  transition-delay: 0.2s;
}

.animate_delay-3 {
  transition-delay: 0.3s;
}

.animate_delay-4 {
  transition-delay: 0.4s;
}

.animate_delay-5 {
  transition-delay: 0.5s;
}

.animate_delay-6 {
  transition-delay: 0.6s;
}

.animate_delay-7 {
  transition-delay: 0.7s;
}

.animate_delay-8 {
  transition-delay: 0.8s;
}

.animate_delay-9 {
  transition-delay: 0.9s;
}

.animate_delay-10 {
  transition-delay: 1s;
}

.swiper-slide-active .animate_fade {
  opacity: 1;
  visibility: visible;
}

.swiper-slide-active .animate_rtl {
  right: 0;
}

.swiper-slide-active .animate_btt {
  bottom: 0;
}

.anim_appear-fade {
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-fade {
  opacity: 1;
  visibility: visible;
}

.anim_appear-bottom {
  bottom: -0.625rem;
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-bottom {
  bottom: 0.625rem;
  opacity: 1;
  visibility: visible;
}

.anim_appear-right {
  right: -0.625rem;
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-right {
  right: 0;
  opacity: 1;
  visibility: visible;
}

.row {
  --bs-gutter-x: 1.875rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

.row>* {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) / 2);
  padding-left: calc(var(--bs-gutter-x) / 2);
  margin-top: var(--bs-gutter-y);
}

.col {
  flex: 1 0 0%;
}

.row-cols-auto>* {
  flex: 0 0 auto;
  width: auto;
}

.row-cols-1>* {
  flex: 0 0 auto;
  width: 100%;
}

.row-cols-2>* {
  flex: 0 0 auto;
  width: 50%;
}

.row-cols-3>* {
  flex: 0 0 auto;
  width: 33.3333333333%;
}

.row-cols-4>* {
  flex: 0 0 auto;
  width: 25%;
}

.row-cols-5>* {
  flex: 0 0 auto;
  width: 20%;
}

.row-cols-6>* {
  flex: 0 0 auto;
  width: 16.6666666667%;
}

.col-auto {
  flex: 0 0 auto;
  width: auto;
}

.col-1 {
  flex: 0 0 auto;
  width: 8.3333333333%;
}

.col-2 {
  flex: 0 0 auto;
  width: 16.6666666667%;
}

.col-3 {
  flex: 0 0 auto;
  width: 25%;
}

.col-4 {
  flex: 0 0 auto;
  width: 33.3333333333%;
}

.col-5 {
  flex: 0 0 auto;
  width: 41.6666666667%;
}

.col-6 {
  flex: 0 0 auto;
  width: 50%;
}

.col-7 {
  flex: 0 0 auto;
  width: 58.3333333333%;
}

.col-8 {
  flex: 0 0 auto;
  width: 66.6666666667%;
}

.col-9 {
  flex: 0 0 auto;
  width: 75%;
}

.col-10 {
  flex: 0 0 auto;
  width: 83.3333333333%;
}

.col-11 {
  flex: 0 0 auto;
  width: 91.6666666667%;
}

.col-12 {
  flex: 0 0 auto;
  width: 100%;
}

.offset-1 {
  margin-left: 8.3333333333%;
}

.offset-2 {
  margin-left: 16.6666666667%;
}

.offset-3 {
  margin-left: 25%;
}

.offset-4 {
  margin-left: 33.3333333333%;
}

.offset-5 {
  margin-left: 41.6666666667%;
}

.offset-6 {
  margin-left: 50%;
}

.offset-7 {
  margin-left: 58.3333333333%;
}

.offset-8 {
  margin-left: 66.6666666667%;
}

.offset-9 {
  margin-left: 75%;
}

.offset-10 {
  margin-left: 83.3333333333%;
}

.offset-11 {
  margin-left: 91.6666666667%;
}

.g-0,
.gx-0 {
  --bs-gutter-x: 0;
}

.g-0,
.gy-0 {
  --bs-gutter-y: 0;
}

.g-1,
.gx-1 {
  --bs-gutter-x: 0.25rem;
}

.g-1,
.gy-1 {
  --bs-gutter-y: 0.25rem;
}

.g-2,
.gx-2 {
  --bs-gutter-x: 0.5rem;
}

.g-2,
.gy-2 {
  --bs-gutter-y: 0.5rem;
}

.g-3,
.gx-3 {
  --bs-gutter-x: 1rem;
}

.g-3,
.gy-3 {
  --bs-gutter-y: 1rem;
}

.g-4,
.gx-4 {
  --bs-gutter-x: 1.5rem;
}

.g-4,
.gy-4 {
  --bs-gutter-y: 1.5rem;
}

.g-5,
.gx-5 {
  --bs-gutter-x: 3rem;
}

.g-5,
.gy-5 {
  --bs-gutter-y: 3rem;
}

@media (min-width: 576px) {
  .col-sm {
    flex: 1 0 0%;
  }

  .row-cols-sm-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-sm-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-sm-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-sm-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-sm-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-sm-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-sm-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-sm-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-sm-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-sm-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-sm-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-sm-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-sm-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-sm-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-sm-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-sm-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-sm-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-sm-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-sm-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-sm-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-sm-0 {
    margin-left: 0;
  }

  .offset-sm-1 {
    margin-left: 8.3333333333%;
  }

  .offset-sm-2 {
    margin-left: 16.6666666667%;
  }

  .offset-sm-3 {
    margin-left: 25%;
  }

  .offset-sm-4 {
    margin-left: 33.3333333333%;
  }

  .offset-sm-5 {
    margin-left: 41.6666666667%;
  }

  .offset-sm-6 {
    margin-left: 50%;
  }

  .offset-sm-7 {
    margin-left: 58.3333333333%;
  }

  .offset-sm-8 {
    margin-left: 66.6666666667%;
  }

  .offset-sm-9 {
    margin-left: 75%;
  }

  .offset-sm-10 {
    margin-left: 83.3333333333%;
  }

  .offset-sm-11 {
    margin-left: 91.6666666667%;
  }

  .g-sm-0,
  .gx-sm-0 {
    --bs-gutter-x: 0;
  }

  .g-sm-0,
  .gy-sm-0 {
    --bs-gutter-y: 0;
  }

  .g-sm-1,
  .gx-sm-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-sm-1,
  .gy-sm-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-sm-2,
  .gx-sm-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-sm-2,
  .gy-sm-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-sm-3,
  .gx-sm-3 {
    --bs-gutter-x: 1rem;
  }

  .g-sm-3,
  .gy-sm-3 {
    --bs-gutter-y: 1rem;
  }

  .g-sm-4,
  .gx-sm-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-sm-4,
  .gy-sm-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-sm-5,
  .gx-sm-5 {
    --bs-gutter-x: 3rem;
  }

  .g-sm-5,
  .gy-sm-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 768px) {
  .col-md {
    flex: 1 0 0%;
  }

  .row-cols-md-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-md-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-md-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-md-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-md-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-md-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-md-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-md-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-md-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-md-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-md-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-md-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-md-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-md-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-md-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-md-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-md-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-md-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-md-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-md-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-md-0 {
    margin-left: 0;
  }

  .offset-md-1 {
    margin-left: 8.3333333333%;
  }

  .offset-md-2 {
    margin-left: 16.6666666667%;
  }

  .offset-md-3 {
    margin-left: 25%;
  }

  .offset-md-4 {
    margin-left: 33.3333333333%;
  }

  .offset-md-5 {
    margin-left: 41.6666666667%;
  }

  .offset-md-6 {
    margin-left: 50%;
  }

  .offset-md-7 {
    margin-left: 58.3333333333%;
  }

  .offset-md-8 {
    margin-left: 66.6666666667%;
  }

  .offset-md-9 {
    margin-left: 75%;
  }

  .offset-md-10 {
    margin-left: 83.3333333333%;
  }

  .offset-md-11 {
    margin-left: 91.6666666667%;
  }

  .g-md-0,
  .gx-md-0 {
    --bs-gutter-x: 0;
  }

  .g-md-0,
  .gy-md-0 {
    --bs-gutter-y: 0;
  }

  .g-md-1,
  .gx-md-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-md-1,
  .gy-md-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-md-2,
  .gx-md-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-md-2,
  .gy-md-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-md-3,
  .gx-md-3 {
    --bs-gutter-x: 1rem;
  }

  .g-md-3,
  .gy-md-3 {
    --bs-gutter-y: 1rem;
  }

  .g-md-4,
  .gx-md-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-md-4,
  .gy-md-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-md-5,
  .gx-md-5 {
    --bs-gutter-x: 3rem;
  }

  .g-md-5,
  .gy-md-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 992px) {
  .col-lg {
    flex: 1 0 0%;
  }

  .row-cols-lg-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-lg-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-lg-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-lg-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-lg-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-lg-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-lg-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-lg-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-lg-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-lg-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-lg-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-lg-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-lg-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-lg-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-lg-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-lg-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-lg-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-lg-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-lg-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-lg-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-lg-0 {
    margin-left: 0;
  }

  .offset-lg-1 {
    margin-left: 8.3333333333%;
  }

  .offset-lg-2 {
    margin-left: 16.6666666667%;
  }

  .offset-lg-3 {
    margin-left: 25%;
  }

  .offset-lg-4 {
    margin-left: 33.3333333333%;
  }

  .offset-lg-5 {
    margin-left: 41.6666666667%;
  }

  .offset-lg-6 {
    margin-left: 50%;
  }

  .offset-lg-7 {
    margin-left: 58.3333333333%;
  }

  .offset-lg-8 {
    margin-left: 66.6666666667%;
  }

  .offset-lg-9 {
    margin-left: 75%;
  }

  .offset-lg-10 {
    margin-left: 83.3333333333%;
  }

  .offset-lg-11 {
    margin-left: 91.6666666667%;
  }

  .g-lg-0,
  .gx-lg-0 {
    --bs-gutter-x: 0;
  }

  .g-lg-0,
  .gy-lg-0 {
    --bs-gutter-y: 0;
  }

  .g-lg-1,
  .gx-lg-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-lg-1,
  .gy-lg-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-lg-2,
  .gx-lg-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-lg-2,
  .gy-lg-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-lg-3,
  .gx-lg-3 {
    --bs-gutter-x: 1rem;
  }

  .g-lg-3,
  .gy-lg-3 {
    --bs-gutter-y: 1rem;
  }

  .g-lg-4,
  .gx-lg-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-lg-4,
  .gy-lg-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-lg-5,
  .gx-lg-5 {
    --bs-gutter-x: 3rem;
  }

  .g-lg-5,
  .gy-lg-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1200px) {
  .col-xl {
    flex: 1 0 0%;
  }

  .row-cols-xl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xl-0 {
    margin-left: 0;
  }

  .offset-xl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xl-3 {
    margin-left: 25%;
  }

  .offset-xl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xl-6 {
    margin-left: 50%;
  }

  .offset-xl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xl-9 {
    margin-left: 75%;
  }

  .offset-xl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xl-0,
  .gx-xl-0 {
    --bs-gutter-x: 0;
  }

  .g-xl-0,
  .gy-xl-0 {
    --bs-gutter-y: 0;
  }

  .g-xl-1,
  .gx-xl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xl-1,
  .gy-xl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xl-2,
  .gx-xl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xl-2,
  .gy-xl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xl-3,
  .gx-xl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xl-3,
  .gy-xl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xl-4,
  .gx-xl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xl-4,
  .gy-xl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xl-5,
  .gx-xl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xl-5,
  .gy-xl-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1500px) {
  .col-xxl {
    flex: 1 0 0%;
  }

  .row-cols-xxl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xxl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xxl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xxl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xxl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xxl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xxl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xxl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xxl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xxl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xxl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xxl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xxl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xxl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xxl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xxl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xxl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xxl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xxl-0 {
    margin-left: 0;
  }

  .offset-xxl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xxl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xxl-3 {
    margin-left: 25%;
  }

  .offset-xxl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xxl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xxl-6 {
    margin-left: 50%;
  }

  .offset-xxl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xxl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xxl-9 {
    margin-left: 75%;
  }

  .offset-xxl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xxl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xxl-0,
  .gx-xxl-0 {
    --bs-gutter-x: 0;
  }

  .g-xxl-0,
  .gy-xxl-0 {
    --bs-gutter-y: 0;
  }

  .g-xxl-1,
  .gx-xxl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xxl-1,
  .gy-xxl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xxl-2,
  .gx-xxl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xxl-2,
  .gy-xxl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xxl-3,
  .gx-xxl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xxl-3,
  .gy-xxl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xxl-4,
  .gx-xxl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xxl-4,
  .gy-xxl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xxl-5,
  .gx-xxl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xxl-5,
  .gy-xxl-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1700px) {
  .col-xxxl {
    flex: 1 0 0%;
  }

  .row-cols-xxxl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xxxl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xxxl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xxxl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xxxl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xxxl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xxxl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxxl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xxxl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xxxl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxxl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xxxl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xxxl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xxxl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xxxl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xxxl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xxxl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xxxl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xxxl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xxxl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xxxl-0 {
    margin-left: 0;
  }

  .offset-xxxl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xxxl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xxxl-3 {
    margin-left: 25%;
  }

  .offset-xxxl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xxxl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xxxl-6 {
    margin-left: 50%;
  }

  .offset-xxxl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xxxl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xxxl-9 {
    margin-left: 75%;
  }

  .offset-xxxl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xxxl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xxxl-0,
  .gx-xxxl-0 {
    --bs-gutter-x: 0;
  }

  .g-xxxl-0,
  .gy-xxxl-0 {
    --bs-gutter-y: 0;
  }

  .g-xxxl-1,
  .gx-xxxl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xxxl-1,
  .gy-xxxl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xxxl-2,
  .gx-xxxl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xxxl-2,
  .gy-xxxl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xxxl-3,
  .gx-xxxl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xxxl-3,
  .gy-xxxl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xxxl-4,
  .gx-xxxl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xxxl-4,
  .gy-xxxl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xxxl-5,
  .gx-xxxl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xxxl-5,
  .gy-xxxl-5 {
    --bs-gutter-y: 3rem;
  }
}

body ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  height: .25rem;
  background-color: #ffffff;
}

body ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #e4e4e4;
}

@media (max-width: 991.98px) {
  .snap main {
    overflow-x: hidden;
  }
}

img {
  max-width: 100%;
}

.block {
  margin: 2.125rem 0;
}

.full-width_padding {
  overflow: hidden;
}

@media (min-width: 1500px) {
  .full-width_padding {
    width: 100%;
    padding: 0 3.75rem;
  }
}

.full-width_padding-20 {
  width: 100%;
  padding: 0 1.25rem;
}

@media (max-width: 1499.98px) {
  .full-width_border {
    border: 0 !important;
  }
}

@media (min-width: 1500px) {
  .full-width_border {
    padding: 0.625rem;
    border-style: solid;
  }
}

.page-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  transition: all 0.32s cubic-bezier(0.55, 0.085, 0.68, 0.53);
  background-color: rgba(34, 34, 34, 0.4);
  opacity: 0;
  visibility: hidden;
  z-index: 1040;
}

.page-overlay_visible {
  opacity: 1;
  visibility: visible;
}

#scrollTop {
  position: fixed !important;
  right: 0;
  bottom: 0rem;
  z-index: 1030;
  width: 45px;
  height: 45px;
  background-color: #eeeeee;
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23222222'/%3e%3c/svg%3e");
  background-position: center center;
  background-repeat: no-repeat;
  cursor: pointer;
  clip: auto !important;
  transition: all 0.28s;
}

@media (min-width: 768px) {
  #scrollTop {
    bottom: 0;
  }
}

.mw-1620 {
  width: 1620px !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.mw-1170 {
  width: 1200px !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.mw-930 {
  width: 58.125rem !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.mw-930-2 {
  width: 40.125rem !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.w-740 {
  width: 46.25rem;
  max-width: 100%;
}

.w-100px {
  width: 6.25rem;
}

.h-100px {
  height: 6.25rem;
}

.gradient-bg {
  background-image: url(../../images/home/demo3/slider_bg.jpg);
  background-position: top center;
  background-repeat: no-repeat;
  background-size: 100% auto;
}

.gradient-bg-10 {
  background-image: url(../../images/home/demo10/slider_bg.png);
  background-position: top center;
  background-repeat: no-repeat;
  background-size: auto 84rem;
}

@media (min-width: 992px) {
  .gradient-bg-10 {
    background-size: 100% auto;
  }
}

@media (min-width: 1200px) {
  .col-xl-20per {
    flex: 0 0 auto;
    width: 20%;
  }
}

@media (min-width: 1200px) {
  .col-xl-40per {
    flex: 0 0 auto;
    width: 40%;
  }
}

@media (min-width: 1200px) {
  .col-xl-60per {
    flex: 0 0 auto;
    width: 60%;
  }
}

@media (min-width: 1200px) {
  .col-xl-80per {
    flex: 0 0 auto;
    width: 80%;
  }
}

.gutters-20 .row {
  --bs-gutter-x: 1.25rem;
}

.btn-close,
.btn-close-lg,
.btn-close-xs {
  padding: 0;
  border: 0;
  box-sizing: content-box;
  color: #000;
  border-radius: 0;
  opacity: 1;
}

.btn-close:hover,
.btn-close-lg:hover,
.btn-close-xs:hover {
  color: #000;
  text-decoration: none;
  opacity: 0.75;
}

.btn-close:focus,
.btn-close-lg:focus,
.btn-close-xs:focus {
  outline: none;
  box-shadow: none;
  opacity: 1;
}

.btn-close:disabled,
.btn-close.disabled,
.btn-close-lg:disabled,
.btn-close-lg.disabled,
.btn-close-xs:disabled,
.btn-close-xs.disabled {
  pointer-events: none;
  user-select: none;
  opacity: 0.25;
}

.btn-close {
  width: 1.375rem;
  height: 1.375rem;
  padding: 0.25em 0.25em;
  background: transparent url("data:image/svg+xml,%3csvg width='23' height='22' viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23000'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23000'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.btn-close-lg {
  width: 1rem;
  height: 1rem;
  background: transparent url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.414336 14.1421L14.5565 0L15.9707 1.41421L1.82855 15.5563L0.414336 14.1421Z' fill='%23000'/%3e%3cpath d='M1.41421 0.142113L15.5563 14.2842L14.1421 15.6985L0 1.55633L1.41421 0.142113Z' fill='%23000'/%3e%3c/svg%3e") center/1rem auto no-repeat;
}

.btn-close-xs {
  width: 0.625rem;
  height: 0.625rem;
  padding: 0;
  background: transparent url("data:image/svg+xml,%3csvg width='10' height='10' viewBox='0 0 10 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.259435 8.85506L9.11449 0L10 0.885506L1.14494 9.74056L0.259435 8.85506Z' fill='%23767676'/%3e%3cpath d='M0.885506 0.0889838L9.74057 8.94404L8.85506 9.82955L0 0.97449L0.885506 0.0889838Z' fill='%23767676'/%3e%3c/svg%3e") center/0.625rem auto no-repeat;
}

.btn-close-white {
  filter: invert(1) grayscale(100%) brightness(200%);
}

.accordion-item_shadow {
  box-shadow: 0 0 1.5625rem 0 rgba(34, 34, 34, 0.05);
}

.accordion-button {
  padding: 1.75rem 1.875rem 1.125rem;
  border: 1px solid #eeeeee;
  color: #222222;
  background-color: #ffffff;
  font-size: 1.625rem;
  font-weight: 500;
  line-height: 1.375;
  outline: none;
}

.accordion-button::after {
  content: none;
}

.accordion-button.collapsed {
  background-color: transparent;
  color: #222222;
}

.accordion-button.collapsed .accordion-button__icon {
  transform: rotate(0deg);
}

.accordion-button.collapsed .accordion-button__icon .svg-path-horizontal {
  opacity: 1;
}

.accordion-button.collapsed .accordion-button__icon.type2 {
  transform: rotate(180deg);
}

.accordion-button__icon {
  width: 0.875rem;
  height: 0.875rem;
  margin-left: auto;
  fill: #222222;
  transform: rotate(90deg);
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button__icon {
    transition: none;
  }
}

.accordion-button__icon .svg-path-vertical {
  transform: rotate(90deg);
  transform-origin: center;
}

.accordion-button__icon .svg-path-horizontal {
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button__icon .svg-path-horizontal {
    transition: none;
  }
}

.accordion-button__icon.type2 {
  transform: rotate(0deg);
}

.accordion-body {
  padding: 1.5rem 1.875rem 1.75rem;
}

.faq-accordion .accordion-item {
  margin-bottom: 1.25rem;
}

.faq-accordion .accordion-button {
  border: 0;
  border-bottom: 1px solid #e4e4e4;
  padding: 0.625rem 0;
  text-align: left;
}

.faq-accordion .accordion-collapse {
  border: 0;
}

.faq-accordion .accordion-body {
  padding: 1.5rem 0;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.nav-link {
  display: block;
  padding: 0.6875rem 1.75rem 0.4375rem;
  color: #222222;
  font-weight: 500;
  line-height: 1.375;
  outline: none;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .nav-link {
    transition: none;
  }
}

.nav-link.disabled {
  color: #6c757d;
  pointer-events: none;
  cursor: default;
}

@media (min-width: 992px) {
  .nav-link {
    font-size: 1rem;
  }
}

.nav-link_underscore {
  position: relative;
  padding: 0.6875rem 1.5625rem 0.4375rem;
  color: #767676;
}

.nav-link_underscore:after {
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 1.5625rem;
  width: 0;
  height: 2px;
  background-color: #222222;
  transition: width 0.36s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@media (prefers-reduced-motion: reduce) {
  .nav-link_underscore:after {
    transition: none;
  }
}

.nav-link_underscore.theme-color:after {
  background-color: #193174;
}

.nav-link_underscore:hover,
.nav-link_underscore:focus,
.nav-link_underscore.active,
.nav-item.show .nav-link_underscore {
  color: #222222;
}

.nav-link_underscore:hover:after,
.nav-link_underscore:focus:after,
.nav-link_underscore.active:after,
.nav-item.show .nav-link_underscore:after {
  width: calc(100% - 3.125rem);
}

.nav-link_underscore.underscore-sm:hover:after,
.nav-link_underscore.underscore-sm:focus:after,
.nav-link_underscore.underscore-sm.active:after,
.nav-item.show .nav-link_underscore.underscore-sm:after {
  width: 2rem;
}

.nav-link_underscore.underscore-md:hover:after,
.nav-link_underscore.underscore-md:focus:after,
.nav-link_underscore.underscore-md.active:after,
.nav-item.show .nav-link_underscore.underscore-md:after {
  width: calc((100% - 1.5625rem * 2) * 0.7);
}

.nav-link_underscore.disabled {
  color: #6c757d;
  background-color: transparent;
  border-color: transparent;
}

.nav-link_rline:before {
  content: '';
  position: absolute;
  top: 49%;
  left: 0;
  width: 0px;
  height: 2px;
  background-color: #222222;
  transition: width 0.36s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@media (prefers-reduced-motion: reduce) {
  .nav-link_rline:before {
    transition: none;
  }
}

.nav-link_rline.active:before {
  width: 100%;
}

.rline-content {
  display: inline-block;
  position: relative;
  padding-right: 1.5em;
  background-color: #ffffff;
}

@media (min-width: 768px) {
  .rline-content {
    padding-right: 2.5em;
  }
}

@media (min-width: 1200px) {
  .rline-content {
    padding-right: 3.5em;
  }
}

.nav-pills .nav-link {
  border-radius: 0;
}

.nav-pills .nav-link.active,
.nav-pills .show>.nav-link {
  color: #ffffff;
  background-color: #222222;
}

.nav-fill>.nav-link,
.nav-fill .nav-item {
  flex: 1 1 auto;
  text-align: center;
}

.nav-justified>.nav-link,
.nav-justified .nav-item {
  flex-basis: 0;
  flex-grow: 1;
  text-align: center;
}

.tab-content>.tab-pane {
  display: none;
}

.tab-content>.active {
  display: block;
}

.checkbox__mark {
  display: -ms-inline-flexbox;
  display: inline-flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  width: 1.125rem;
  height: 1.125rem;
  margin-right: .625rem;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10l3 3l6-6'/%3e%3c/svg%3e");
  background-position: center;
  background-repeat: no-repeat;
  background-size: 66.666667%;
}

.checkbox__mark_gray {
  background-color: #767676;
}

.checkbox__mark_round {
  border-radius: 100%;
}

.table {
  --bs-table-bg: transparent;
  --bs-table-striped-color: #222222;
  --bs-table-striped-bg: #faf9f8;
  --bs-table-active-color: #222222;
  --bs-table-active-bg: rgba(0, 0, 0, 0.1);
  --bs-table-hover-color: #222222;
  --bs-table-hover-bg: rgba(0, 0, 0, 0.075);
  width: 100%;
  margin-bottom: 1rem;
  color: #222222;
  line-height: 1.5;
  vertical-align: top;
  border-color: transparent;
}

.table> :not(caption)>tr>td,
.table> :not(caption)>tr>th {
  background-image: linear-gradient(var(--bs-table-accent-bg), var(--bs-table-accent-bg));
  border-bottom-width: 0;
}

.table> :not(caption)>tr>td {
  padding: 1.53125rem 1.5rem;
  background-color: var(--bs-table-bg);
}

.table> :not(caption)>tr>th {
  padding: 1.625rem 1.5rem 1.25rem;
  background-color: #222222;
  color: #ffffff;
  font-size: 1rem;
  font-weight: 500;
}

.table>tbody {
  vertical-align: inherit;
}

.table>thead {
  vertical-align: bottom;
}

.table> :not(:last-child)>tr:last-child>th,
.table> :not(:last-child)>tr:last-child>td {
  border-bottom-color: currentColor;
}

.caption-top {
  caption-side: top;
}

.table-sm> :not(caption)>tr>th,
.table-sm> :not(caption)>tr>td {
  padding: 0.25rem 0.25rem;
}

.table-bordered> :not(caption)>tr {
  border-width: 0 0;
}

.table-bordered> :not(caption)>tr>th,
.table-bordered> :not(caption)>tr>td {
  border-width: 0 0;
}

.table-borderless> :not(caption)>tr {
  border-bottom-width: 0;
}

.table-striped>tbody>tr:nth-of-type(even) {
  --bs-table-accent-bg: var(--bs-table-striped-bg);
  color: var(--bs-table-striped-color);
}

.table-active {
  --bs-table-accent-bg: var(--bs-table-active-bg);
  color: var(--bs-table-active-color);
}

.table-hover>tbody>tr:hover {
  --bs-table-accent-bg: var(--bs-table-hover-bg);
  color: var(--bs-table-hover-color);
}

.table-primary {
  --bs-table-bg: #ffffff;
  --bs-table-striped-bg: #f2f2f2;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #e6e6e6;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #ececec;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #e6e6e6;
}

.table-secondary {
  --bs-table-bg: #e4e4e4;
  --bs-table-striped-bg: #d9d9d9;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #cdcdcd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: lightgray;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #cdcdcd;
}

.table-success {
  --bs-table-bg: #def2d7;
  --bs-table-striped-bg: #d3e6cc;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #c8dac2;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #cde0c7;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #c8dac2;
}

.table-info {
  --bs-table-bg: #cde9f6;
  --bs-table-striped-bg: #c3ddea;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #b9d2dd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #bed8e4;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #b9d2dd;
}

.table-warning {
  --bs-table-bg: #f7f3d7;
  --bs-table-striped-bg: #ebe7cc;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #dedbc2;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #e4e1c7;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #dedbc2;
}

.table-danger {
  --bs-table-bg: #ecc8c5;
  --bs-table-striped-bg: #e0bebb;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #d4b4b1;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #dab9b6;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #d4b4b1;
}

.table-light {
  --bs-table-bg: #e4e4e4;
  --bs-table-striped-bg: #d9d9d9;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #cdcdcd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: lightgray;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #cdcdcd;
}

.table-dark {
  --bs-table-bg: #222222;
  --bs-table-striped-bg: #2d2d2d;
  --bs-table-striped-color: #fff;
  --bs-table-active-bg: #383838;
  --bs-table-active-color: #fff;
  --bs-table-hover-bg: #333333;
  --bs-table-hover-color: #fff;
  color: #fff;
  border-color: #383838;
}

.table-responsive {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 575.98px) {
  .table-responsive-sm {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 767.98px) {
  .table-responsive-md {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 991.98px) {
  .table-responsive-lg {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1199.98px) {
  .table-responsive-xl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1499.98px) {
  .table-responsive-xxl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1699.98px) {
  .table-responsive-xxxl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

.table-primary thead>tr>th {
  color: #ffffff;
  font-size: 1rem;
  font-weight: 500;
}

.alert {
  position: relative;
  padding: 1.6875rem 1.875rem 1.375rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  font-weight: 500;
  border-radius: 0;
}

.alert-heading {
  color: inherit;
}

.alert-link {
  font-weight: 700;
}

.alert-dismissible {
  padding-right: 3rem;
}

.alert-dismissible .btn-close {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  padding: 1.85625rem 1.875rem 1.375rem;
}

.alert-success {
  color: #5b7052;
  background-color: #def2d7;
  border-color: #def2d7;
}

.alert-success .alert-link {
  color: #495a42;
}

.alert-success .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%235b7052'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%235b7052'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-info {
  color: #4780aa;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.alert-info .alert-link {
  color: #396688;
}

.alert-info .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%234780aa'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%234780aa'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-warning {
  color: #927238;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.alert-warning .alert-link {
  color: #755b2d;
}

.alert-warning .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23927238'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23927238'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-danger {
  color: #ab3331;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.alert-danger .alert-link {
  color: #892927;
}

.alert-danger .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23ab3331'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23ab3331'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.btn {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #222222;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  user-select: none;
  background-color: #ffffff;
  border: 1px solid transparent;
  padding: 0.375rem 3.125rem;
  font-size: 0.875rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
  font-size: 0.875rem;
  padding-top: 0.703125rem;
  padding-bottom: 0.5625rem;
}

@media (prefers-reduced-motion: reduce) {
  .btn {
    transition: none;
  }
}

@media (max-width: 575.98px) {
  .btn {
    padding-left: 1.125rem;
    padding-right: 1.125rem;
  }
}

.btn:hover {
  color: #222222;
}

.btn-55 {
  height: 3.4375rem;
}

.btn-50 {
  height: 3.125rem;
}

.btn-45 {
  height: 2.8125rem;
}

.btn-40 {
  height: 2.5rem;
}

.btn-check:focus+.btn,
.btn:focus {
  outline: 0;
  box-shadow: none;
}

.btn-check:checked+.btn,
.btn-check:active+.btn,
.btn:active,
.btn.active {
  box-shadow: none;
}

.btn-check:checked+.btn:focus,
.btn-check:active+.btn:focus,
.btn:active:focus,
.btn.active:focus {
  box-shadow: none;
}

.btn:disabled,
.btn.disabled,
fieldset:disabled .btn {
  pointer-events: none;
  opacity: 0.65;
  box-shadow: none;
}

@media (min-width: 1500px) {
  .btn {
    font-size: 1rem;
    padding-top: 0.9375rem;
    padding-bottom: 0.75rem;
  }
}

.btn-primary {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
  box-shadow: none;
}

.btn-primary:hover {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
}

.btn-check:focus+.btn-primary,
.btn-primary:focus {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-check:checked+.btn-primary,
.btn-check:active+.btn-primary,
.btn-primary:active,
.btn-primary.active,
.show>.btn-primary.dropdown-toggle {
  color: #fff;
  background-color: #1b1b1b;
  border-color: #1a1a1a;
}

.btn-check:checked+.btn-primary:focus,
.btn-check:active+.btn-primary:focus,
.btn-primary:active:focus,
.btn-primary.active:focus,
.show>.btn-primary.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-primary:disabled,
.btn-primary.disabled {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-outline-primary {
  color: #222222;
  border-color: #222222;
}

.btn-outline-primary:hover {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:focus+.btn-outline-primary,
.btn-outline-primary:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-primary,
.btn-check:active+.btn-outline-primary,
.btn-outline-primary:active,
.btn-outline-primary.active,
.btn-outline-primary.dropdown-toggle.show {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:checked+.btn-outline-primary:focus,
.btn-check:active+.btn-outline-primary:focus,
.btn-outline-primary:active:focus,
.btn-outline-primary.active:focus,
.btn-outline-primary.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-primary:disabled,
.btn-outline-primary.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-hover-primary:hover {
  background-color: #222222;
  color: #fff;
}

.btn-secondary {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
  box-shadow: none;
}

.btn-secondary:hover {
  color: #fff;
  background-color: #646464;
  border-color: #5e5e5e;
}

.btn-check:focus+.btn-secondary,
.btn-secondary:focus {
  color: #fff;
  background-color: #646464;
  border-color: #5e5e5e;
  box-shadow: 0 0 0 0 rgba(139, 139, 139, 0.5);
}

.btn-check:checked+.btn-secondary,
.btn-check:active+.btn-secondary,
.btn-secondary:active,
.btn-secondary.active,
.show>.btn-secondary.dropdown-toggle {
  color: #fff;
  background-color: #5e5e5e;
  border-color: #595959;
}

.btn-check:checked+.btn-secondary:focus,
.btn-check:active+.btn-secondary:focus,
.btn-secondary:active:focus,
.btn-secondary.active:focus,
.show>.btn-secondary.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(139, 139, 139, 0.5);
}

.btn-secondary:disabled,
.btn-secondary.disabled {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-outline-secondary {
  color: #767676;
  border-color: #767676;
}

.btn-outline-secondary:hover {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-check:focus+.btn-outline-secondary,
.btn-outline-secondary:focus {
  box-shadow: 0 0 0 0 rgba(118, 118, 118, 0.5);
}

.btn-check:checked+.btn-outline-secondary,
.btn-check:active+.btn-outline-secondary,
.btn-outline-secondary:active,
.btn-outline-secondary.active,
.btn-outline-secondary.dropdown-toggle.show {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-check:checked+.btn-outline-secondary:focus,
.btn-check:active+.btn-outline-secondary:focus,
.btn-outline-secondary:active:focus,
.btn-outline-secondary.active:focus,
.btn-outline-secondary.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(118, 118, 118, 0.5);
}

.btn-outline-secondary:disabled,
.btn-outline-secondary.disabled {
  color: #767676;
  background-color: transparent;
}

.btn-hover-secondary:hover {
  background-color: #767676;
  color: #fff;
}

.btn-success {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
  box-shadow: none;
}

.btn-success:hover {
  color: #000;
  background-color: #e3f4dd;
  border-color: #e1f3db;
}

.btn-check:focus+.btn-success,
.btn-success:focus {
  color: #000;
  background-color: #e3f4dd;
  border-color: #e1f3db;
  box-shadow: 0 0 0 0 rgba(189, 206, 183, 0.5);
}

.btn-check:checked+.btn-success,
.btn-check:active+.btn-success,
.btn-success:active,
.btn-success.active,
.show>.btn-success.dropdown-toggle {
  color: #000;
  background-color: #e5f5df;
  border-color: #e1f3db;
}

.btn-check:checked+.btn-success:focus,
.btn-check:active+.btn-success:focus,
.btn-success:active:focus,
.btn-success.active:focus,
.show>.btn-success.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(189, 206, 183, 0.5);
}

.btn-success:disabled,
.btn-success.disabled {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-outline-success {
  color: #def2d7;
  border-color: #def2d7;
}

.btn-outline-success:hover {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-check:focus+.btn-outline-success,
.btn-outline-success:focus {
  box-shadow: 0 0 0 0 rgba(222, 242, 215, 0.5);
}

.btn-check:checked+.btn-outline-success,
.btn-check:active+.btn-outline-success,
.btn-outline-success:active,
.btn-outline-success.active,
.btn-outline-success.dropdown-toggle.show {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-check:checked+.btn-outline-success:focus,
.btn-check:active+.btn-outline-success:focus,
.btn-outline-success:active:focus,
.btn-outline-success.active:focus,
.btn-outline-success.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(222, 242, 215, 0.5);
}

.btn-outline-success:disabled,
.btn-outline-success.disabled {
  color: #def2d7;
  background-color: transparent;
}

.btn-hover-success:hover {
  background-color: #def2d7;
  color: #fff;
}

.btn-info {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
  box-shadow: none;
}

.btn-info:hover {
  color: #000;
  background-color: #d5ecf7;
  border-color: #d2ebf7;
}

.btn-check:focus+.btn-info,
.btn-info:focus {
  color: #000;
  background-color: #d5ecf7;
  border-color: #d2ebf7;
  box-shadow: 0 0 0 0 rgba(174, 198, 209, 0.5);
}

.btn-check:checked+.btn-info,
.btn-check:active+.btn-info,
.btn-info:active,
.btn-info.active,
.show>.btn-info.dropdown-toggle {
  color: #000;
  background-color: #d7edf8;
  border-color: #d2ebf7;
}

.btn-check:checked+.btn-info:focus,
.btn-check:active+.btn-info:focus,
.btn-info:active:focus,
.btn-info.active:focus,
.show>.btn-info.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(174, 198, 209, 0.5);
}

.btn-info:disabled,
.btn-info.disabled {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-outline-info {
  color: #cde9f6;
  border-color: #cde9f6;
}

.btn-outline-info:hover {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-check:focus+.btn-outline-info,
.btn-outline-info:focus {
  box-shadow: 0 0 0 0 rgba(205, 233, 246, 0.5);
}

.btn-check:checked+.btn-outline-info,
.btn-check:active+.btn-outline-info,
.btn-outline-info:active,
.btn-outline-info.active,
.btn-outline-info.dropdown-toggle.show {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-check:checked+.btn-outline-info:focus,
.btn-check:active+.btn-outline-info:focus,
.btn-outline-info:active:focus,
.btn-outline-info.active:focus,
.btn-outline-info.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(205, 233, 246, 0.5);
}

.btn-outline-info:disabled,
.btn-outline-info.disabled {
  color: #cde9f6;
  background-color: transparent;
}

.btn-hover-info:hover {
  background-color: #cde9f6;
  color: #fff;
}

.btn-warning {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
  box-shadow: none;
}

.btn-warning:hover {
  color: #000;
  background-color: #f8f5dd;
  border-color: #f8f4db;
}

.btn-check:focus+.btn-warning,
.btn-warning:focus {
  color: #000;
  background-color: #f8f5dd;
  border-color: #f8f4db;
  box-shadow: 0 0 0 0 rgba(210, 207, 183, 0.5);
}

.btn-check:checked+.btn-warning,
.btn-check:active+.btn-warning,
.btn-warning:active,
.btn-warning.active,
.show>.btn-warning.dropdown-toggle {
  color: #000;
  background-color: #f9f5df;
  border-color: #f8f4db;
}

.btn-check:checked+.btn-warning:focus,
.btn-check:active+.btn-warning:focus,
.btn-warning:active:focus,
.btn-warning.active:focus,
.show>.btn-warning.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(210, 207, 183, 0.5);
}

.btn-warning:disabled,
.btn-warning.disabled {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-outline-warning {
  color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-outline-warning:hover {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-check:focus+.btn-outline-warning,
.btn-outline-warning:focus {
  box-shadow: 0 0 0 0 rgba(247, 243, 215, 0.5);
}

.btn-check:checked+.btn-outline-warning,
.btn-check:active+.btn-outline-warning,
.btn-outline-warning:active,
.btn-outline-warning.active,
.btn-outline-warning.dropdown-toggle.show {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-check:checked+.btn-outline-warning:focus,
.btn-check:active+.btn-outline-warning:focus,
.btn-outline-warning:active:focus,
.btn-outline-warning.active:focus,
.btn-outline-warning.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(247, 243, 215, 0.5);
}

.btn-outline-warning:disabled,
.btn-outline-warning.disabled {
  color: #f7f3d7;
  background-color: transparent;
}

.btn-hover-warning:hover {
  background-color: #f7f3d7;
  color: #fff;
}

.btn-danger {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
  box-shadow: none;
}

.btn-danger:hover {
  color: #000;
  background-color: #efd0ce;
  border-color: #eececb;
}

.btn-check:focus+.btn-danger,
.btn-danger:focus {
  color: #000;
  background-color: #efd0ce;
  border-color: #eececb;
  box-shadow: 0 0 0 0 rgba(201, 170, 167, 0.5);
}

.btn-check:checked+.btn-danger,
.btn-check:active+.btn-danger,
.btn-danger:active,
.btn-danger.active,
.show>.btn-danger.dropdown-toggle {
  color: #000;
  background-color: #f0d3d1;
  border-color: #eececb;
}

.btn-check:checked+.btn-danger:focus,
.btn-check:active+.btn-danger:focus,
.btn-danger:active:focus,
.btn-danger.active:focus,
.show>.btn-danger.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(201, 170, 167, 0.5);
}

.btn-danger:disabled,
.btn-danger.disabled {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-outline-danger {
  color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-outline-danger:hover {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-check:focus+.btn-outline-danger,
.btn-outline-danger:focus {
  box-shadow: 0 0 0 0 rgba(236, 200, 197, 0.5);
}

.btn-check:checked+.btn-outline-danger,
.btn-check:active+.btn-outline-danger,
.btn-outline-danger:active,
.btn-outline-danger.active,
.btn-outline-danger.dropdown-toggle.show {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-check:checked+.btn-outline-danger:focus,
.btn-check:active+.btn-outline-danger:focus,
.btn-outline-danger:active:focus,
.btn-outline-danger.active:focus,
.btn-outline-danger.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(236, 200, 197, 0.5);
}

.btn-outline-danger:disabled,
.btn-outline-danger.disabled {
  color: #ecc8c5;
  background-color: transparent;
}

.btn-hover-danger:hover {
  background-color: #ecc8c5;
  color: #fff;
}

.btn-dark {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
  box-shadow: none;
}

.btn-dark:hover {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
}

.btn-check:focus+.btn-dark,
.btn-dark:focus {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-check:checked+.btn-dark,
.btn-check:active+.btn-dark,
.btn-dark:active,
.btn-dark.active,
.show>.btn-dark.dropdown-toggle {
  color: #fff;
  background-color: #1b1b1b;
  border-color: #1a1a1a;
}

.btn-check:checked+.btn-dark:focus,
.btn-check:active+.btn-dark:focus,
.btn-dark:active:focus,
.btn-dark.active:focus,
.show>.btn-dark.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-dark:disabled,
.btn-dark.disabled {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-outline-dark {
  color: #222222;
  border-color: #222222;
}

.btn-outline-dark:hover {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:focus+.btn-outline-dark,
.btn-outline-dark:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-dark,
.btn-check:active+.btn-outline-dark,
.btn-outline-dark:active,
.btn-outline-dark.active,
.btn-outline-dark.dropdown-toggle.show {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:checked+.btn-outline-dark:focus,
.btn-check:active+.btn-outline-dark:focus,
.btn-outline-dark:active:focus,
.btn-outline-dark.active:focus,
.btn-outline-dark.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-dark:disabled,
.btn-outline-dark.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-hover-dark:hover {
  background-color: #222222;
  color: #fff;
}

.btn-red {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
  box-shadow: none;
}

.btn-red:hover {
  color: #fff;
  background-color: #a62323;
  border-color: #9c2121;
}

.btn-check:focus+.btn-red,
.btn-red:focus {
  color: #fff;
  background-color: #a62323;
  border-color: #9c2121;
  box-shadow: 0 0 0 0 rgba(204, 73, 73, 0.5);
}

.btn-check:checked+.btn-red,
.btn-check:active+.btn-red,
.btn-red:active,
.btn-red.active,
.show>.btn-red.dropdown-toggle {
  color: #fff;
  background-color: #9c2121;
  border-color: #921f1f;
}

.btn-check:checked+.btn-red:focus,
.btn-check:active+.btn-red:focus,
.btn-red:active:focus,
.btn-red.active:focus,
.show>.btn-red.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(204, 73, 73, 0.5);
}

.btn-red:disabled,
.btn-red.disabled {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-outline-red {
  color: #c32929;
  border-color: #c32929;
}

.btn-outline-red:hover {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-check:focus+.btn-outline-red,
.btn-outline-red:focus {
  box-shadow: 0 0 0 0 rgba(195, 41, 41, 0.5);
}

.btn-check:checked+.btn-outline-red,
.btn-check:active+.btn-outline-red,
.btn-outline-red:active,
.btn-outline-red.active,
.btn-outline-red.dropdown-toggle.show {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-check:checked+.btn-outline-red:focus,
.btn-check:active+.btn-outline-red:focus,
.btn-outline-red:active:focus,
.btn-outline-red.active:focus,
.btn-outline-red.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(195, 41, 41, 0.5);
}

.btn-outline-red:disabled,
.btn-outline-red.disabled {
  color: #c32929;
  background-color: transparent;
}

.btn-hover-red:hover {
  background-color: #c32929;
  color: #fff;
}

.btn-beige {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
  box-shadow: none;
}

.btn-beige:hover {
  color: #ffffff;
  background-color: #c0aa7a;
  border-color: #c0aa7a;
}

.btn-check:focus+.btn-beige,
.btn-beige:focus {
  color: #ffffff;
  background-color: #c0aa7a;
  border-color: #c0aa7a;
  box-shadow: 0 0 0 0 rgba(196, 175, 129, 0.5);
}

.btn-check:checked+.btn-beige,
.btn-check:active+.btn-beige,
.btn-beige:active,
.btn-beige.active,
.show>.btn-beige.dropdown-toggle {
  color: #000;
  background-color: #948156;
  border-color: #8b7950;
}

.btn-check:checked+.btn-beige:focus,
.btn-check:active+.btn-beige:focus,
.btn-beige:active:focus,
.btn-beige.active:focus,
.show>.btn-beige.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(196, 175, 129, 0.5);
}

.btn-beige:disabled,
.btn-beige.disabled {
  color: #000;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-outline-beige {
  color: #b9a16b;
  border-color: #b9a16b;
}

.btn-outline-beige:hover {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-check:focus+.btn-outline-beige,
.btn-outline-beige:focus {
  box-shadow: 0 0 0 0 rgba(185, 161, 107, 0.5);
}

.btn-check:checked+.btn-outline-beige,
.btn-check:active+.btn-outline-beige,
.btn-outline-beige:active,
.btn-outline-beige.active,
.btn-outline-beige.dropdown-toggle.show {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-check:checked+.btn-outline-beige:focus,
.btn-check:active+.btn-outline-beige:focus,
.btn-outline-beige:active:focus,
.btn-outline-beige.active:focus,
.btn-outline-beige.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(185, 161, 107, 0.5);
}

.btn-outline-beige:disabled,
.btn-outline-beige.disabled {
  color: #b9a16b;
  background-color: transparent;
}

.btn-light {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
  box-shadow: none;
}

.btn-light:hover {
  color: #222222;
  background-color: #e7e7e7;
  border-color: #e7e7e7;
}

.btn-check:focus+.btn-light,
.btn-light:focus {
  color: #222222;
  background-color: #e7e7e7;
  border-color: #e7e7e7;
  box-shadow: 0 0 0 0 rgba(199, 199, 199, 0.5);
}

.btn-check:checked+.btn-light,
.btn-check:active+.btn-light,
.btn-light:active,
.btn-light.active,
.show>.btn-light.dropdown-toggle {
  color: #000;
  background-color: #e9e9e9;
  border-color: #e7e7e7;
}

.btn-check:checked+.btn-light:focus,
.btn-check:active+.btn-light:focus,
.btn-light:active:focus,
.btn-light.active:focus,
.show>.btn-light.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(199, 199, 199, 0.5);
}

.btn-light:disabled,
.btn-light.disabled {
  color: #000;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-outline-light {
  color: #222222;
  border-color: #222222;
  border-color: #e4e4e4;
}

.btn-outline-light:hover {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-check:focus+.btn-outline-light,
.btn-outline-light:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-light,
.btn-check:active+.btn-outline-light,
.btn-outline-light:active,
.btn-outline-light.active,
.btn-outline-light.dropdown-toggle.show {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-check:checked+.btn-outline-light:focus,
.btn-check:active+.btn-outline-light:focus,
.btn-outline-light:active:focus,
.btn-outline-light.active:focus,
.btn-outline-light.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-light:disabled,
.btn-outline-light.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-link {
  display: inline-block;
  position: relative;
  padding: 0;
  border: 0;
  background-color: transparent;
  color: #222222;
  font-weight: 400;
  text-decoration: none;
}

.btn-link:hover {
  color: #1b1b1b;
}

.btn-link:disabled,
.btn-link.disabled {
  color: #6c757d;
}

.btn-link:after {
  content: '';
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  width: 0;
  max-width: 100%;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.btn-link:hover:after,
.btn-link.btn-link_active:after {
  width: 3.125rem;
}

.btn-link.default-underline:after {
  width: 3.125rem;
}

.btn-link.default-underline:hover:after {
  width: 100%;
}

.btn-link_lg:hover:after,
.btn-link_lg.btn-link_active:after {
  width: calc(100% - 1rem);
}

.btn-link_lg.default-underline:after {
  width: 86%;
}

.btn-link_lg.default-underline:hover:after {
  width: 100%;
}

.btn-link_md:hover:after,
.btn-link_md.btn-link_active:after {
  width: 70%;
}

.btn-link_md.default-underline:after {
  width: 70%;
}

.btn-link_md.default-underline:hover:after {
  width: 100%;
}

.btn-link_sm:hover:after,
.btn-link_sm.btn-link_active:after {
  width: 45%;
}

.btn-link_sm.default-underline:after {
  width: 45%;
}

.btn-link_sm.default-underline:hover:after {
  width: 100%;
}

.btn-link_f:hover:after,
.btn-link_f.btn-link_active:after {
  width: 100%;
}

.btn-round {
  width: 1.875rem;
  height: 1.875rem;
  padding: 0;
  border-radius: 100%;
}

@media (min-width: 768px) {
  .btn-round {
    width: 2.5rem;
    height: 2.5rem;
  }
}

.btn-round-sm {
  width: 2.1875rem;
  height: 2.1875rem;
  padding: 0;
  border-radius: 100%;
}

.btn-square {
  width: 2.8125rem;
  height: 2.8125rem;
  padding: 0;
}

.btn-lg,
.btn-group-lg>.btn {
  padding: 0.5rem 1.25rem;
  font-size: 0.875rem;
  border-radius: 0;
  line-height: 1.5rem;
}

.btn-sm,
.btn-group-sm>.btn {
  padding: 0.375rem 1.25rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.nav-icon {
  display: block;
  fill: currentColor;
}

.btn-icon {
  border: 0;
  background-color: transparent;
}

.btn-text {
  text-decoration: underline;
}

.swiper-pagination-bullet {
  position: relative;
  width: 1.875rem;
  height: 1.875rem;
  margin: 0 4px;
  border: 2px solid currentColor;
  background-color: transparent;
  color: transparent;
  opacity: 1;
  outline: none;
}

.swiper-pagination-bullet:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0.375rem;
  height: 0.375rem;
  margin-top: -0.1875rem;
  margin-left: -0.1875rem;
  border-radius: 100%;
  background-color: currentColor;
  color: #ddc2bd;
  content: '';
}

.swiper-pagination-bullet:first-child {
  margin-left: 0;
}

.swiper-pagination-bullets.dark-bullet .swiper-pagination-bullet:after {
  color: #222;
}

.swiper-pagination-bullet-active {
  color: #222222;
}

.swiper-pagination-bullet-active:after {
  color: inherit;
}

.swiper-pagination-white .swiper-pagination-bullet-active {
  color: #fff;
}

.swiper-pagination-bullets.theme-color .swiper-pagination-bullet-active {
  color: #193174;
}

.swatch-color {
  display: block;
  position: relative;
  width: 1.75rem;
  height: 1.75rem;
  margin-right: .75rem;
  margin-bottom: .75rem;
  border-radius: 50%;
}

.swatch-color:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1rem;
  height: 1rem;
  margin-top: -0.5rem;
  margin-left: -0.5rem;
  border-radius: 100%;
  background-color: currentColor;
  color: inherit;
  content: '';
}

.swatch-color.swatch_active {
  border: 2px solid #222222;
}

.hover-container .swatch-color {
  margin: 0;
}

.swatch-size.swatch_active {
  background-color: #e4e4e4;
}

.filter-tag {
  padding: 0 1rem;
  border: 0;
  background-color: #e4e4e4;
  font-size: 11px;
  line-height: 1.875rem;
}

.filter-tag.swatch_active {
  display: none !important;
}

.form-label {
  margin-bottom: 0.5rem;
}

.col-form-label {
  padding-top: 1.0625rem;
  padding-bottom: 1.0625rem;
  margin-bottom: 0;
  font-size: inherit;
  line-height: 1.7143;
}

.col-form-label-lg {
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
  font-size: 1.25rem;
}

.col-form-label-sm {
  padding-top: 0.875rem;
  padding-bottom: 0.875rem;
  font-size: 0.875rem;
}

.form-text {
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #6c757d;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.9375rem 0.9375rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
  color: #222222;
  background-color: #fff;
  background-clip: padding-box;
  border: 0.125rem solid #e4e4e4;
  appearance: none;
  border-radius: 0;
  box-shadow: none;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control {
    transition: none;
  }
}

.form-control[type="file"] {
  overflow: hidden;
}

.form-control[type="file"]:not(:disabled):not([readonly]) {
  cursor: pointer;
}

.form-control:focus {
  color: #222222;
  background-color: #fff;
  border-color: #222222;
  outline: 0;
  box-shadow: none;
}

.form-control::-webkit-date-and-time-value {
  height: 1.7143em;
}

.form-control::placeholder {
  color: #6c757d;
  opacity: 1;
}

.form-control:disabled,
.form-control[readonly] {
  background-color: #fff;
  opacity: 1;
}

.form-control::file-selector-button {
  padding: 0.9375rem 0.9375rem 0.75rem;
  margin: -0.9375rem -0.9375rem;
  margin-inline-end: 0.9375rem;
  color: #222222;
  background-color: #e9ecef;
  pointer-events: none;
  border-color: inherit;
  border-style: solid;
  border-width: 0;
  border-inline-end-width: 0.125rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control::file-selector-button {
    transition: none;
  }
}

.form-control:hover:not(:disabled):not([readonly])::file-selector-button {
  background-color: #dde0e3;
}

.form-control::-webkit-file-upload-button {
  padding: 0.9375rem 0.9375rem 0.75rem;
  margin: -0.9375rem -0.9375rem;
  margin-inline-end: 0.9375rem;
  color: #222222;
  background-color: #e9ecef;
  pointer-events: none;
  border-color: inherit;
  border-style: solid;
  border-width: 0;
  border-inline-end-width: 0.125rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control::-webkit-file-upload-button {
    transition: none;
  }
}

.form-control:hover:not(:disabled):not([readonly])::-webkit-file-upload-button {
  background-color: #dde0e3;
}

.form-control[type="password"] {
  font-family: 'Trebuchet MS', sans-serif;
  letter-spacing: 0.18em;
}

.form-control_gray {
  border-color: #e4e4e4;
}

.form-control-plaintext {
  display: block;
  width: 100%;
  padding: 0.9375rem 0;
  margin-bottom: 0;
  line-height: 1.7143;
  color: #222222;
  background-color: transparent;
  border: solid transparent;
  border-width: 0.125rem 0;
}

.form-control-plaintext.form-control-sm,
.form-control-plaintext.form-control-lg {
  padding-right: 0;
  padding-left: 0;
}

.form-control-sm {
  min-height: calc(1.5em + 0.5rem + 2px);
  padding: 0.75rem 1.125rem 0.6rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.form-control-sm::file-selector-button {
  padding: 0.75rem 1.125rem 0.6rem;
  margin: -0.75rem -1.125rem;
  margin-inline-end: 1.125rem;
}

.form-control-sm::-webkit-file-upload-button {
  padding: 0.75rem 1.125rem 0.6rem;
  margin: -0.75rem -1.125rem;
  margin-inline-end: 1.125rem;
}

.form-control-lg {
  min-height: calc(1.5em + 1rem + 2px);
  padding: 1.125rem 1.3125rem 0.9rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.form-control-lg::file-selector-button {
  padding: 1.125rem 1.3125rem 0.9rem;
  margin: -1.125rem -1.3125rem;
  margin-inline-end: 1.3125rem;
}

.form-control-lg::-webkit-file-upload-button {
  padding: 1.125rem 1.3125rem 0.9rem;
  margin: -1.125rem -1.3125rem;
  margin-inline-end: 1.3125rem;
}

textarea.form-control {
  min-height: calc(1.5em + 0.75rem + 2px);
}

textarea.form-control-sm {
  min-height: calc(1.5em + 0.5rem + 2px);
}

textarea.form-control-lg {
  min-height: calc(1.5em + 1rem + 2px);
}

.form-control-color {
  max-width: 3rem;
  height: auto;
  padding: 0.9375rem;
}

.form-control-color:not(:disabled):not([readonly]) {
  cursor: pointer;
}

.form-control-color::-moz-color-swatch {
  height: 1.7143em;
  border-radius: 0;
}

.form-control-color::-webkit-color-swatch {
  height: 1.7143em;
  border-radius: 0;
}

.form-select {
  display: block;
  width: 100%;
  padding: 0.9375rem 0.9375rem 0.75rem;
  padding-right: 2.34375rem;
  font-size: 0.95rem;
  font-weight: 400;
  line-height: 1.7143;
  border: 0.125rem solid #e4e4e4;
  box-shadow: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.9375rem center;
  background-size: 16px 12px;
  color: #222222;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0;
}

/* test */
.custom-select {
  position: relative;
  width: 100%; /* Adjust width as needed */
  z-index: 2;
  display: block;
  padding: 0.9375rem 0.9375rem 0.75rem;
  padding-right: 2.34375rem;
  font-size: 0.95rem;
  font-weight: 400;
  line-height: 1.7143;
  border: 0.125rem solid #e4e4e4;
  box-shadow: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.9375rem center;
  background-size: 16px 12px;
  color: #222222;
  appearance: none;
  border-radius: 0;
}

.custom-select select {
  display: none;
}

.custom-select .select-selected {
  background-color: #fff;
  /* border: 1px solid #ccc;
  padding: 5px 10px; */
  cursor: pointer;
}

.custom-select .select-selected:after {
  position: absolute;
  /* top: 50%;
  right: 10px;
  transform: translateY(-50%); */
}

/* .custom-select .select-items {
  display: none;
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  border-bottom: none; 
  width: 100%;
  max-height: 150px; 
  overflow-y: auto;
  top: 100%; 
} */

/* .custom-select .select-items div {
  padding: 5px 10px;
  cursor: pointer;
} */

/* .custom-select .select-items div:hover {
  background-color: #f2f2f2;
} */


/* test */

.form-select[multiple],
.form-select[size]:not([size="1"]) {
  padding-right: 0.75rem;
  background-image: none;
}

.form-select:disabled {
  color: #6c757d;
  background-color: #e9ecef;
}

.form-select:-moz-focusring {
  color: transparent;
  text-shadow: 0 0 0 #222222;
}

.form-select-sm {
  width: auto;
  padding: 0.75rem 1.125rem 0.6rem;
  padding-right: 2.025rem;
  background-position: right 0.5625rem center;
}

.form-select-lg {
  padding: 1.125rem 1.3125rem 0.9rem;
}

.multi-select .multi-select__actor {
  background-color: #fff;
}

.multi-select__actor {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center;
  background-repeat: no-repeat;
  background-size: 16px 12px;
  cursor: pointer;
}

.multi-select__item {
  display: flex;
  align-items: center;
  position: relative;
  width: 100%;
  padding: 0.5rem 0;
  color: #767676;
  cursor: pointer;
}

.multi-select__item:hover {
  color: #3b3b3b;
}

.multi-select__item:before {
  content: '';
  display: block;
  width: 1rem;
  height: 1rem;
  color: #e4e4e4;
  border: 0.125rem solid currentColor;
  border-radius: 0;
  margin-right: 0.75rem;
}

.multi-select__item:after {
  content: '';
  display: block;
  position: absolute;
  left: 0.25rem;
  top: 50%;
  transform: translateY(-50%);
  width: 0.5rem;
  height: 0.5rem;
  background-color: transparent;
  border-radius: 0;
}

.mult-select__item_selected {
  color: #222222;
}

.mult-select__item_selected:before {
  color: #222222;
}

.mult-select__item_selected:after {
  background-color: #222222;
}

.form-check {
  display: block;
  position: relative;
  min-height: 1.5rem;
  padding-left: 1.625rem;
  margin-bottom: 1rem;
}

.form-check .form-check-input {
  float: left;
  margin-left: -1.625rem;
}

.form-check-input {
  width: 1rem;
  height: 1rem;
  margin-top: 0.25000625rem;
  vertical-align: top;
  background-color: #fff;
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  border: 0.125rem solid #e4e4e4;
  appearance: none;
  color-adjust: exact;
  transition: background-color 0.15s ease-in-out, background-position 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-check-input {
    transition: none;
  }
}

.form-check-input[type="checkbox"] {
  border-radius: 0;
}

.form-check-input[type="radio"] {
  border-radius: 50%;
}

.form-check-input[type="radio"]:after {
  border-radius: 50%;
}

.form-check-input.form-check-input_fill {
  position: relative;
  border-width: 0.125rem;
}

.form-check-input.form-check-input_fill:after {
  content: '';
  display: block;
  position: absolute;
  left: 0.125rem;
  top: 50%;
  transform: translateY(-50%);
  width: 0.5rem;
  height: 0.5rem;
  background-color: transparent;
}

.form-check-input:focus {
  border-color: #222222;
  outline: 0;
  box-shadow: none;
}

.form-check-input:checked {
  background-color: #222222;
  border-color: #222222;
}

.form-check-input:checked[type="checkbox"] {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10l3 3l6-6'/%3e%3c/svg%3e");
}

.form-check-input:checked[type="radio"] {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='2' fill='%23fff'/%3e%3c/svg%3e");
}

.form-check-input:checked.form-check-input_fill {
  background-image: none;
  background-color: #ffffff;
}

.form-check-input:checked.form-check-input_fill:after {
  background-color: #222222;
}

.form-check-input[type="checkbox"]:indeterminate {
  background-color: #222222;
  border-color: #222222;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/%3e%3c/svg%3e");
}

.form-check-input:disabled {
  pointer-events: none;
  opacity: 0.5;
}

.form-check-input[disabled]~.form-check-label,
.form-check-input:disabled~.form-check-label {
  opacity: 0.5;
}

.form-switch {
  min-height: 1.875rem;
  padding-left: 4.625rem;
}

.form-switch .form-check-input {
  width: 3.75rem;
  height: 1.875rem;
  margin-top: 0;
  margin-left: -4.625rem;
  border-radius: 2em;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23767676'/%3e%3c/svg%3e");
  background-position: left center;
}

.form-switch .form-check-input:focus {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23222222'/%3e%3c/svg%3e");
}

.form-switch .form-check-input:checked {
  background-position: right center;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e");
}

.form-switch .form-check-label {
  line-height: 1.875rem;
}

.form-check-inline {
  display: inline-block;
  margin-right: 1rem;
}

.btn-check {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}

.btn-check[disabled]+.btn,
.btn-check:disabled+.btn {
  pointer-events: none;
  opacity: 0.65;
}

.form-range {
  width: 100%;
  height: 1.5rem;
  padding: 0;
  background-color: transparent;
  appearance: none;
}

.form-range:focus {
  outline: none;
}

.form-range:focus::-webkit-slider-thumb {
  box-shadow: 0 0 0 1px #fff, none;
}

.form-range:focus::-moz-range-thumb {
  box-shadow: 0 0 0 1px #fff, none;
}

.form-range::-moz-focus-outer {
  border: 0;
}

.form-range::-webkit-slider-thumb {
  width: 1rem;
  height: 1rem;
  margin-top: -0.25rem;
  background-color: #222222;
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.1rem 0.25rem rgba(0, 0, 0, 0.1);
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  appearance: none;
}

@media (prefers-reduced-motion: reduce) {
  .form-range::-webkit-slider-thumb {
    transition: none;
  }
}

.form-range::-webkit-slider-thumb:active {
  background-color: #bdbdbd;
}

.form-range::-webkit-slider-runnable-track {
  width: 100%;
  height: 0.5rem;
  color: transparent;
  cursor: pointer;
  background-color: #dee2e6;
  border-color: transparent;
  border-radius: 1rem;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);
}

.form-range::-moz-range-thumb {
  width: 1rem;
  height: 1rem;
  background-color: #222222;
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.1rem 0.25rem rgba(0, 0, 0, 0.1);
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  appearance: none;
}

@media (prefers-reduced-motion: reduce) {
  .form-range::-moz-range-thumb {
    transition: none;
  }
}

.form-range::-moz-range-thumb:active {
  background-color: #bdbdbd;
}

.form-range::-moz-range-track {
  width: 100%;
  height: 0.5rem;
  color: transparent;
  cursor: pointer;
  background-color: #dee2e6;
  border-color: transparent;
  border-radius: 1rem;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);
}

.form-range:disabled {
  pointer-events: none;
}

.form-range:disabled::-webkit-slider-thumb {
  background-color: #adb5bd;
}

.form-range:disabled::-moz-range-thumb {
  background-color: #adb5bd;
}

.form-floating {
  position: relative;
}

.form-floating>.form-control,
.form-floating>.form-select {
  height: calc(3.625rem + 2px);
  padding: 1.125rem 1.3125rem 0.9rem;
}

.form-floating>label {
  position: absolute;
  top: 1rem;
  left: 0.75rem;
  padding: 0 0.5rem;
  pointer-events: none;
  border: 0.125rem solid transparent;
  transform-origin: 0 0;
  transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out;
  color: #767676;
}

@media (prefers-reduced-motion: reduce) {
  .form-floating>label {
    transition: none;
  }
}

.form-floating>.form-control::placeholder {
  color: transparent;
}

.form-floating>.form-control:-webkit-autofill {
  padding-top: 1.625rem;
  padding-bottom: 0.625rem;
}

.form-floating>.form-select {
  padding-top: 1.625rem;
  padding-bottom: 0.625rem;
}

.form-floating>.form-control:focus~label,
.form-floating>.form-control:not(:placeholder-shown)~label,
.form-floating>.form-select~label {
  background-color: #ffffff;
  color: #222222;
  transform: translateY(-1.9rem);
}

.form-floating>.form-control:-webkit-autofill~label {
  background-color: #ffffff;
  color: #222222;
  transform: translateY(-1.9rem);
}

.form-label-fixed {
  position: relative;
}

.form-label-fixed>.form-label {
  position: absolute;
  top: -1.00000625rem;
  left: 1rem;
  margin: 0;
  padding: 0.25rem 0.5rem 0.25rem 0.5rem;
  background-color: #ffffff;
  color: #222222;
  z-index: 1;
}

.input-group {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.input-group>.form-control,
.input-group>.form-select {
  position: relative;
  flex: 1 1 auto;
  width: 1%;
  min-width: 0;
}

.input-group>.form-control:focus,
.input-group>.form-select:focus {
  z-index: 3;
}

.input-group .btn {
  position: relative;
  z-index: 2;
}

.input-group .btn:focus {
  z-index: 3;
}

.input-group-text {
  display: flex;
  align-items: center;
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
  color: #222222;
  text-align: center;
  white-space: nowrap;
  background-color: #e9ecef;
  border: 0.125rem solid #ced4da;
  border-radius: 0;
}

.input-group-lg>.form-control,
.input-group-lg>.form-select,
.input-group-lg>.input-group-text,
.input-group-lg>.btn {
  padding: 1.125rem 1.3125rem;
  font-size: 1.25rem;
  border-radius: 0;
}

.input-group-sm>.form-control,
.input-group-sm>.form-select,
.input-group-sm>.input-group-text,
.input-group-sm>.btn {
  padding: 0.75rem 1.125rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.input-group-lg>.form-select,
.input-group-sm>.form-select {
  padding-right: 1.75rem;
}

.input-group:not(.has-validation)> :not(:last-child):not(.dropdown-toggle):not(.dropdown-menu),
.input-group:not(.has-validation)>.dropdown-toggle:nth-last-child(n + 3) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.input-group.has-validation> :nth-last-child(n + 3):not(.dropdown-toggle):not(.dropdown-menu),
.input-group.has-validation>.dropdown-toggle:nth-last-child(n + 4) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.input-group> :not(:first-child):not(.dropdown-menu):not(.valid-tooltip):not(.valid-feedback):not(.invalid-tooltip):not(.invalid-feedback) {
  margin-left: -0.125rem;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.valid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #198754;
}

.valid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  color: #fff;
  background-color: rgba(25, 135, 84, 0.9);
  border-radius: 0.25rem;
}

.was-validated :valid~.valid-feedback,
.was-validated :valid~.valid-tooltip,
.is-valid~.valid-feedback,
.is-valid~.valid-tooltip {
  display: block;
}

.was-validated .form-control:valid,
.form-control.is-valid {
  border-color: #198754;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-control:valid:focus,
.form-control.is-valid:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated textarea.form-control:valid,
textarea.form-control.is-valid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
}

.was-validated .form-select:valid,
.form-select.is-valid {
  border-color: #198754;
  padding-right: calc(0.75em + 2.3125rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e"), url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center, center right 1.75rem;
  background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-select:valid:focus,
.form-select.is-valid:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated .form-check-input:valid,
.form-check-input.is-valid {
  border-color: #198754;
}

.was-validated .form-check-input:valid:checked,
.form-check-input.is-valid:checked {
  background-color: #198754;
}

.was-validated .form-check-input:valid:focus,
.form-check-input.is-valid:focus {
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated .form-check-input:valid~.form-check-label,
.form-check-input.is-valid~.form-check-label {
  color: #198754;
}

.form-check-inline .form-check-input~.valid-feedback {
  margin-left: .5em;
}

.invalid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #dc3545;
}

.invalid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  color: #fff;
  background-color: rgba(220, 53, 69, 0.9);
  border-radius: 0.25rem;
}

.was-validated :invalid~.invalid-feedback,
.was-validated :invalid~.invalid-tooltip,
.is-invalid~.invalid-feedback,
.is-invalid~.invalid-tooltip {
  display: block;
}

.was-validated .form-control:invalid,
.form-control.is-invalid {
  border-color: #dc3545;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-control:invalid:focus,
.form-control.is-invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated textarea.form-control:invalid,
textarea.form-control.is-invalid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
}

.was-validated .form-select:invalid,
.form-select.is-invalid {
  border-color: #dc3545;
  padding-right: calc(0.75em + 2.3125rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e"), url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center, center right 1.75rem;
  background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-select:invalid:focus,
.form-select.is-invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated .form-check-input:invalid,
.form-check-input.is-invalid {
  border-color: #dc3545;
}

.was-validated .form-check-input:invalid:checked,
.form-check-input.is-invalid:checked {
  background-color: #dc3545;
}

.was-validated .form-check-input:invalid:focus,
.form-check-input.is-invalid:focus {
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated .form-check-input:invalid~.form-check-label,
.form-check-input.is-invalid~.form-check-label {
  color: #dc3545;
}

.form-check-inline .form-check-input~.invalid-feedback {
  margin-left: .5em;
}

.search-field .search-field__actor {
  background-color: #fff;
}

.search-field__arrow-down {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center;
  background-repeat: no-repeat;
  background-size: 16px 12px;
  cursor: pointer;
}

.filters-container {
  border: 0.125rem solid #e4e4e4;
  padding: 1rem 1.25rem;
}

.search-field__input-wrapper {
  position: relative;
}

.search-field__input-wrapper::after {
  content: '';
  display: block;
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(calc(-50% + 2px));
  transform: translateY(calc(-50% + 2px));
  right: 1rem;
  transform: translateY(-50%);
  width: 1rem;
  height: 1rem;
  background: transparent url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cg clip-path='url%28%23clip0_137_2221%29'%3e%3cpath d='M7.04606 0C3.16097 0 0 3.16097 0 7.04606C0 10.9314 3.16097 14.0921 7.04606 14.0921C10.9314 14.0921 14.0921 10.9314 14.0921 7.04606C14.0921 3.16097 10.9314 0 7.04606 0ZM7.04606 12.7913C3.87816 12.7913 1.30081 10.214 1.30081 7.04609C1.30081 3.87819 3.87816 1.30081 7.04606 1.30081C10.214 1.30081 12.7913 3.87816 12.7913 7.04606C12.7913 10.214 10.214 12.7913 7.04606 12.7913Z' fill='%23767676'/%3e%3cpath d='M15.8095 14.8897L12.0805 11.1607C11.8264 10.9066 11.4149 10.9066 11.1608 11.1607C10.9067 11.4146 10.9067 11.8265 11.1608 12.0804L14.8898 15.8094C15.0168 15.9364 15.1831 16 15.3496 16C15.5159 16 15.6824 15.9364 15.8095 15.8094C16.0636 15.5555 16.0636 15.1436 15.8095 14.8897Z' fill='%23767676'/%3e%3c/g%3e%3cdefs%3e%3cclipPath id='clip0_137_2221'%3e%3crect width='16' height='16' fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e") center/1rem auto no-repeat;
}

.search-field__input {
  width: 100%;
  outline: none;
}

.search-suggestion {
  margin: 0.375rem 0;
}

.search-suggestion__item {
  width: 100%;
  padding: 0.5rem 0;
  color: #767676;
  cursor: pointer;
}

.search-suggestion__item:hover {
  color: #3b3b3b;
}

.progress_uomo {
  height: 0.625rem;
  border-radius: 0.625rem;
  background-color: #e4e4e4;
  overflow: visible;
}

.progress_uomo_small {
  height: 0.25rem;
}

.progress_uomo_medium {
  height: 0.375rem;
}

.progress_uomo .progress-bar {
  position: relative;
  border-radius: 0.625rem;
  overflow: visible;
}

.progress_uomo .progress-bar::before {
  content: attr(aria-valuenow);
  display: block;
  position: absolute;
  top: -2em;
  right: 0;
  transform: translateX(50%);
  color: #222222;
  font-size: 0.875rem;
}

.categories-nav__title {
  margin: 0;
  padding-left: 1.8rem;
  padding-right: 1.8rem;
  border-radius: 4px 4px 0 0;
  background-color: #EBB73F;
  color: #ffffff;
  font-size: 0.875rem;
  line-height: 2em;
  text-transform: uppercase;
}

@media (min-width: 1500px) {
  .categories-nav__title {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.categories-nav__list {
  padding: 1.25rem 1.8rem;
  border: 1px solid #e4e4e4;
  border-top: 0;
  border-radius: 0 0 4px 4px;
}

@media (min-width: 1500px) {
  .categories-nav__list {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.categories-nav__item {
  padding: .6875rem 0;
  font-weight: 500;
  line-height: 2em;
  text-decoration: none;
}

.product-card {
  position: relative;
  overflow: hidden;
}

.product-card .hover-container::before {
  content: '';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: all 0.2s ease;
  background-color: rgba(234, 234, 234, 0.9);
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .pc__img-next,
.product-card:hover .pc__img-prev,
.product-card:hover .pc__img-second {
  opacity: 1;
}

.product-card:hover .hover-container::before {
  opacity: 1;
  visibility: visible;
}

.pc__img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.pc__img-wrapper {
  display: block;
  position: relative;
  height: 0;
  padding-top: 121.212122%;
  overflow: hidden;
}

.pc__img-wrapper .pc__btn-wl {
  top: 1rem;
  right: 1rem;
  width: 2rem;
  height: 2rem;
  padding: 0.625rem .5rem 0.375rem;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.pc__img-wrapper .pc__btn-wl .flaticon-heart {
  line-height: 1;
}

@media (min-width: 768px) {
  .pc__img-wrapper .pc__btn-wl {
    top: 1.25rem;
    right: 1.25rem;
    width: 2.5rem;
    height: 2.5rem;
    padding: 0.8125rem 0.75rem 0.6875rem;
  }
}

.pc-wide__img-wrapper {
  padding-top: 60.606061%;
}

.pc__img-wrapper_wide2 {
  padding-top: 90.9091%;
}

.pc__img-wrapper_wide3 {
  padding-top: 78.43137%;
}

.pc__img-second {
  opacity: 0;
  transition: opacity 0.3s linear;
}

.pc__img-next,
.pc__img-prev {
  position: absolute;
  top: 50%;
  margin-top: -0.5rem;
  color: #767676;
  font-size: 1rem;
  opacity: 0;
  z-index: 1;
  transition: opacity 0.35s;
  width: 1rem;
  text-align: center;
}

.pc__img-next>svg,
.pc__img-prev>svg {
  height: auto;
  width: 0.625rem;
}

.pc__img-next {
  right: 1.25rem;
}

.pc__img-prev {
  left: 1.25rem;
}

.pc__info {
  margin-top: 1rem;
}

.pc__info.hover__content {
  margin-top: 0;
  min-width: auto;
  height: 100%;
  transform: translateY(1.125rem);
  -webkit-transform: translateY(1.125rem);
  background: transparent;
}

.pc__info.hover__content .pc__atc {
  max-width: 19.375rem;
}

.product-card:hover .pc__info.hover__content {
  transform: translateY(0);
  -webkit-transform: translateY(0);
}

.product-label {
  position: absolute;
  left: 0;
  top: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.3125rem;
  padding: 0.1875rem 0.625rem;
  line-height: 1.5rem;
  font-size: 0.875rem;
}

.pc__category {
  margin: 0;
  margin-bottom: .25rem;
  color: #767676;
  font-weight: 400;
  line-height: 1.7143;
}

.pc__title {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
}

.price {
  font-size: 1rem;
}

.price-sale {
  color: #d6001c;
}

.price-old {
  margin-right: .625rem;
  color: #767676;
  text-decoration: line-through;
}

.review-star {
  width: 9px;
  height: 9px;
  margin-right: .25rem;
  fill: #ffc78b;
}

.pc__btn-wl {
  color: #767676;
}

.pc__btn-wl2 {
  color: #76767600;
}

.js-add-wishlist.active {
  color: #193174 !important;
}

.js-add-wishlist.active.btn-hover-red {
  color: #fff !important;
  background-color: #193174 !important;
}

.js-add-wishlist.active.btn-hover-primary {
  color: #fff !important;
  background-color: #222222 !important;
}

.js-add-wishlist.active.theme-bg-color.text-white {
  color: #193174 !important;
  background-color: #fff !important;
}

.js-add-wishlist.active.bg-transparent.text-white {
  color: #193174 !important;
  background-color: #fff !important;
}

.js-add-wishlist.active.bg-black.text-white {
  color: #fff !important;
  background-color: #193174 !important;
}

.pc__btn-wl .flaticon,
.btn-link .flaticon {
  display: block;
  font-size: 1rem;
  line-height: 1.7143;
}

.pc__atc {
  left: 0.625rem;
  width: calc(100% - 1.25rem);
  padding-right: 0.625rem;
  padding-left: 0.625rem;
  white-space: nowrap;
}

.pc__atc:hover {
  filter: brightness(0.95);
}

@media (max-width: 767.98px) {
  .pc__atc {
    padding-top: .625rem;
    padding-bottom: .375rem;
    font-size: .75rem;
  }
}

.pc__swatch-color {
  display: block;
  position: relative;
  width: 1.25rem;
  height: 1.25rem;
  margin-right: .375rem;
  margin-bottom: .375rem;
  border-radius: 50%;
}

.pc__swatch-color:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
  border-radius: 100%;
  background-color: currentColor;
  color: inherit;
  content: '';
}

.pc__swatch-color.swatch_active {
  border: 2px solid #222222;
}

.pc-labels {
  padding: 0.625rem;
  z-index: 3;
}

.pc-label {
  padding: 0.25rem 0.625rem 0.125rem;
  font-size: .75rem;
}

@media (min-width: 768px) {
  .pc-label {
    font-size: 0.875rem;
  }
}

.pc-label_sale {
  background-color: #d6001c;
}

.pc-label_sale-text {
  background-color: #222222;
  color: #fff;
}

.product-card_style3 .pc__img-wrapper {
  border-radius: 0.625rem;
}

.product-card_style6 {
  transition: all 0.2s ease;
  overflow: initial;
}

.product-card_style6 .pc__info {
  margin: 0;
  padding: 0.875rem 1.125rem;
  transition: all 0.2s ease;
  z-index: 1;
}

.product-card_style6 .hover__content {
  min-width: auto;
  box-shadow: none;
}

@media (max-width: 575.98px) {
  .product-card_style6 .hover__content {
    position: relative;
    opacity: 1;
    visibility: visible;
  }
}

.product-card_style6:hover,
.product-card_style6:active {
  box-shadow: 0 8px 15px 0 rgba(140, 152, 164, 0.1);
}

.product-card_style6:hover .pc__info,
.product-card_style6:active .pc__info {
  margin-top: -2.5rem;
}

.product-card_style6:hover .pc__info:after,
.product-card_style6:active .pc__info:after {
  content: '';
  position: absolute;
  bottom: -2.5rem;
  left: 0;
  width: 100%;
  height: 2.5rem;
  z-index: 1;
}

.product-card_style8 {
  border: 1px solid transparent;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.product-card_style8.border-1 {
  border-color: #eee;
}

.product-card_style8 .pc__info {
  margin: 0.875rem .5rem .625rem;
}

@media (min-width: 768px) {
  .product-card_style8 .pc__info {
    margin: 0.875rem 1.25rem 1.5rem;
  }
}

.product-card_style8 .pc__title {
  font-size: 0.9375rem;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  line-height: 1.5;
}

.product-card_style8 .reviews-note {
  font-size: 0.8125rem;
}

.product-card_style8 .product-card__price {
  margin-top: 0.625rem;
  color: #0046be;
}

.product-card_style8:hover {
  border-color: #0046be;
  box-shadow: 0 0 20px 0 rgba(0, 70, 190, 0.1);
}

.product-card_style8 .js-add-wishlist,
.product-card_style8 .js-add-cart,
.product-card_style8 .js-quick-view {
  color: #0046be;
}

.product-card_style9 {
  transition: all 0.2s ease;
  border: 1px solid transparent;
  border-radius: 0.25rem;
}

.product-card_style9 .pc__info {
  margin: 0.875rem .5rem .625rem;
}

@media (min-width: 768px) {
  .product-card_style9 .pc__info {
    margin: 0.875rem 1.25rem 0.8125rem;
  }
}

.product-card_style9 .pc__title {
  font-size: 0.9375rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-card_style9 .reviews-note {
  font-size: 0.8125rem;
}

.product-card_style9 .product-card__price {
  margin-top: 0.625rem;
  color: #86bc42;
}

.product-card_style9:hover {
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.1);
}

.product-card_style9:hover .anim_appear-bottom {
  bottom: 0;
}

.product-card_style9 .js-add-wishlist,
.product-card_style9 .js-add-cart,
.product-card_style9 .js-quick-view {
  background-color: #f3e8d6;
  color: #074e37;
}

.product-card_style9 .js-add-wishlist:hover,
.product-card_style9 .js-add-cart:hover,
.product-card_style9 .js-quick-view:hover {
  background-color: #86bc42;
  color: #fff;
}

.product-card_style9.type2 {
  border: 0;
  border-radius: 0;
}

.product-card_style9.type2 .pc__title {
  font-size: 1rem;
  white-space: initial;
  overflow: initial;
  text-overflow: initial;
  line-height: 1.5;
}

.product-card_style9.type2 .pc__title a {
  color: #193174;
}

.product-card_style9.type2:hover {
  box-shadow: none;
}

.product-card_style9.type2 .js-add-wishlist,
.product-card_style9.type2 .js-add-cart,
.product-card_style9.type2 .js-quick-view {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #E4F5F2;
  color: #193174;
}

.product-card_style9.type2 .js-add-wishlist:hover,
.product-card_style9.type2 .js-add-cart:hover,
.product-card_style9.type2 .js-quick-view:hover {
  background-color: #193174;
  color: #fff;
}

.product-card_style9.type2 .product-card__price {
  color: #193174;
  font-size: 1rem;
}

.product-card_style10 {
  transition: background-color .3s ease;
}

.product-card_style10:hover {
  background-color: #F7F7F7;
}

.product-card__actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: #fff;
  white-space: nowrap;
}

.product-card__actions>* {
  display: none;
}

@media (min-width: 1200px) {
  .product-card__actions>* {
    display: block;
  }
}

.product-card__actions>*:first-child {
  display: block;
}

.product-card:hover .anim_appear-bottom.product-card__actions {
  bottom: 0;
}

.aside {
  position: fixed;
  top: 0;
  width: 26.25rem;
  max-width: 100%;
  height: 100vh;
  height: -webkit-fill-available;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
  background-color: #ffffff;
  opacity: .7;
  z-index: 1050;
}

@media (min-width: 576px) {
  .aside {
    padding: 0 1.25rem;
  }
}

.aside_visible {
  opacity: 1;
}

.aside_left {
  left: -26.25rem;
}

.aside_left.aside_visible {
  left: 0;
}

.aside_right {
  right: -26.25rem;
}

.aside_right.aside_visible {
  right: 0;
}

.aside-header {
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  padding: 2.125rem 2.5rem 1.75rem;
  background-color: #faf9f8;
}

.aside-content {
  margin: 1.875rem 0;
  padding: 0 1.25rem;
}

.customer-forms__wrapper {
  left: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.customer__login,
.customer__register {
  min-width: 100%;
}

.search-field__actor svg {
  transition: opacity 0.15s linear;
}

@media (prefers-reduced-motion: reduce) {
  .search-field__actor svg {
    transition: none;
  }
}

.search-field__actor .btn-close-lg {
  position: absolute;
  top: 3px;
  left: 3px;
  padding: 0;
  transition: opacity 0.15s linear;
  opacity: 0;
  visibility: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .search-field__actor .btn-close-lg {
    transition: none;
  }
}

.js-content_visible .search-field__actor svg {
  opacity: 0;
  visibility: hidden;
}

.js-content_visible .search-field__actor .btn-close-lg {
  opacity: 1;
  visibility: visible;
}

.search-popup {
  top: 100%;
  left: 0;
  padding-top: 2.625rem;
  padding-bottom: 2.45rem;
  border-top: 1px solid #e4e4e4;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
}

@media (min-width: 1200px) {
  .search-popup {
    padding-top: 3.75rem;
    padding-bottom: 3.5rem;
  }
}

.search-popup .search-suggestion {
  transition: all 0.28s;
}

.search-popup__reset,
.search-popup__submit {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  position: absolute;
  right: 0;
  bottom: 0;
  height: 100%;
  padding: 0;
  padding-bottom: 0.625rem;
  transition: opacity 0.15s linear;
  color: #767676;
  outline: none;
}

@media (prefers-reduced-motion: reduce) {

  .search-popup__reset,
  .search-popup__submit {
    transition: none;
  }
}

.search-popup__reset {
  opacity: 0;
  visibility: hidden;
}

.search-popup__input {
  padding-bottom: 0.625rem;
  border: 0;
  border-bottom: 2px solid #767676;
  outline: none;
}

.search-field__focused .search-popup__input {
  border-bottom-color: #222222;
}

.search-field__focused .search-popup__reset,
.search-field__focused .search-popup__submit {
  color: #222222;
}

.search-field__focused .search-popup__submit {
  opacity: 0;
  visibility: hidden;
}

.search-field__focused .search-popup__reset {
  opacity: 1;
  visibility: visible;
}

.search-field__focused .search-result {
  position: relative;
  width: auto;
  margin-top: 0;
  transition: all 0.28s;
  opacity: 1;
  visibility: visible;
}

.search-field__focused .search-suggestion {
  position: absolute;
  margin-top: -.5rem;
  opacity: 0;
  visibility: hidden;
}

.search-popup__results {
  margin-top: 1.75rem;
}

.search-result {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 14.25rem;
  margin-top: .5rem;
  padding-bottom: 1.2rem;
  opacity: 0;
  visibility: hidden;
}

.search-result .product-card {
  --bs-gutter-x: 1.75rem;
}

.search-result .pc__img-wrapper {
  padding-top: 10.125rem;
}

@media (min-width: 1200px) {
  .search-result {
    min-height: 19rem;
    padding-bottom: 1.6rem;
  }

  .search-result .pc__img-wrapper {
    padding-top: 15rem;
  }
}

@media (min-width: 1500px) {
  .search-result {
    min-height: 23.75rem;
    padding-bottom: 2rem;
  }

  .search-result .pc__img-wrapper {
    padding-top: 18.75rem;
  }
}

.cart-drawer {
  padding-bottom: 22.5rem;
}

.cart-drawer-items-list {
  max-height: 27.675rem;
  overflow-y: auto;
  height: 100%;
}

.cart-drawer-item {
  max-height: 7.5rem;
  overflow: hidden;
}

.cart-drawer-item._removed {
  max-height: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.cart-drawer-item__img {
  width: 7.5rem;
  height: 7.5rem;
  object-fit: cover;
}

.cart-drawer-item__info {
  margin-left: 1.25rem;
}

.cart-drawer-item__title {
  margin: 2px 0 4px;
}

.cart-drawer-item__option {
  margin: 0;
}

.cart-drawer-item__price {
  font-size: 1.125rem;
}

.qty-control {
  width: 3.375rem;
}

.qty-control input::-webkit-outer-spin-button,
.qty-control input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.qty-control__number {
  padding: 0;
  width: 100%;
  background-color: #ffffff;
  outline: none;
  -moz-appearance: textfield;
}

.qty-control__reduce,
.qty-control__increase {
  position: absolute;
  top: 0;
  width: .75rem;
  padding: 0;
  cursor: pointer;
  user-select: none;
  -ms-user-select: none;
}

.qty-control__reduce {
  left: 0;
}

.qty-control__increase {
  right: 0;
}

.cart-drawer-divider {
  margin: 1.25rem 0;
  color: #e4e4e4;
  opacity: 1;
}

.cart-drawer-divider._removed {
  height: 0;
  margin: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.cart-drawer-actions {
  background-color: #ffffff;
  padding-right: 1.25rem;
  padding-bottom: 1.25rem;
  padding-left: 1.25rem;
}

@media (min-width: 576px) {
  .cart-drawer-actions {
    padding-right: 2.5rem;
    padding-bottom: 2.5rem;
    padding-left: 2.5rem;
  }
}

.star-rating__star-icon {
  cursor: pointer;
  transition: all .1s ease;
  fill: #ccc;
}

.star-rating__star-icon path {
  pointer-events: none;
}

.star-rating__star-icon.is-selected {
  fill: #eeba36;
}

.star-rating__star-icon.is-overed {
  fill: #eeba36;
}

.star-rating__star-icon.is-overed~.star-rating__star-icon:not(.is-overed):not(.is-selected) {
  fill: #ccc;
}

.star-rating__star-icon.is-overed~.star-rating__star-icon.is-selected:not(.is-overed) {
  fill: #ffe296;
}

.size-guide.modal-dialog {
  width: 60rem;
  max-width: calc(100% - 1rem);
}

.size-guide .modal-header {
  background-color: #FAF9F8;
  border-bottom: 0;
  padding: 1.75rem 2.5rem;
  text-transform: uppercase;
}

.size-guide .modal-header .modal-title {
  font-size: 1rem;
}

.size-guide .modal-body {
  padding: 2.5rem;
}

.size-guide__wrapper {
  display: flex;
  gap: 2.6875rem;
}

@media (max-width: 767.98px) {
  .size-guide__wrapper {
    flex-direction: column;
  }
}

.size-guide__image {
  flex: 0 0 42%;
  max-width: 42%;
}

@media (max-width: 767.98px) {
  .size-guide__image {
    flex: 0 0 100%;
    max-width: 100%;
  }
}

.size-guide__detail {
  flex: 1;
}

.size-guide__detail>h5,
.size-guide__detail>.h5 {
  margin-bottom: 1.875rem;
}

.size-guide__detail table {
  font-size: 0.875rem;
  margin-bottom: 1.875rem;
  width: 100%;
}

.size-guide__detail table thead th {
  color: #767676;
  padding-bottom: 0.8125rem;
}

.size-guide__detail table tbody td {
  line-height: 2.1875rem;
}

.delivery-modal.modal-dialog {
  width: 37.5rem;
  max-width: calc(100% - 1rem);
}

.delivery-modal .modal-header {
  background-color: #FAF9F8;
  border-bottom: 0;
  padding: 1.75rem 2.5rem;
  text-transform: uppercase;
}

.delivery-modal .modal-header .modal-title {
  font-size: 1rem;
}

.delivery-modal .modal-body {
  padding: 2.5rem;
}

.delivery-modal .modal-body p {
  line-height: 1.875rem;
  margin-right: 3.875rem;
  margin-bottom: 1.875rem;
}

.cookieConsentContainer {
  position: fixed;
  right: 1.25rem;
  bottom: 1.25rem;
  width: 18.75rem;
  max-width: calc(100% - 2.5rem);
  background-color: #222;
  color: #fff;
  padding: 1.875rem;
  z-index: 1050;
}

.cookieConsentContainer .cookieButton a {
  background-color: #5c5c5c;
  color: #fff;
  height: 2.5rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.cookieConsentContainer .cookieDesc p {
  font-size: 0.8125rem;
}

@-webkit-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-moz-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-ms-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-o-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-moz-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-ms-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-o-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-webkit-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-moz-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-ms-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-o-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-webkit-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-moz-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-ms-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-o-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-webkit-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-moz-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-ms-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-o-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-webkit-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-moz-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-ms-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-o-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-webkit-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-moz-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-ms-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-o-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-webkit-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-moz-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-ms-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-o-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

.effect {
  position: relative;
}

.effect:before,
.effect:after {
  pointer-events: none;
}

.normal-effect::before {
  position: absolute;
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .normal-effect::before {
    transition: none;
  }
}

.normal-effect:hover::before {
  opacity: .3;
}

.normal-effect.dark-bg::before {
  background-color: #000;
}

.plus-zoom::before,
.plus-zoom::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  margin: auto;
  width: 100%;
  height: 100%;
  transition: all 0.5s ease;
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {

  .plus-zoom::before,
  .plus-zoom::after {
    transition: none;
  }
}

.plus-zoom:hover::before {
  width: 0;
  background-color: rgba(255, 255, 255, 0.5);
}

.plus-zoom:hover::after {
  height: 0;
  background-color: rgba(255, 255, 255, 0.5);
}

.overlay-plus::before,
.overlay-plus::after,
.overlay-cross::before,
.overlay-cross::after,
.overlay-horizontal::before,
.overlay-horizontal::after,
.overlay-vertical::before,
.overlay-vertical::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.15);
}

@media (prefers-reduced-motion: reduce) {

  .overlay-plus::before,
  .overlay-plus::after,
  .overlay-cross::before,
  .overlay-cross::after,
  .overlay-horizontal::before,
  .overlay-horizontal::after,
  .overlay-vertical::before,
  .overlay-vertical::after {
    transition: none;
  }
}

.overlay-plus.overlay-dark::before,
.overlay-plus.overlay-dark::after,
.overlay-cross.overlay-dark::before,
.overlay-cross.overlay-dark::after,
.overlay-horizontal.overlay-dark::before,
.overlay-horizontal.overlay-dark::after,
.overlay-vertical.overlay-dark::before,
.overlay-vertical.overlay-dark::after {
  background-color: rgba(0, 0, 0, 0.15);
}

.overlay-plus::before,
.overlay-plus::after {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.overlay-plus:not(:hover)::before {
  width: 0;
}

.overlay-plus:not(:hover)::after {
  height: 0;
}

.overlay-cross::before {
  top: 0;
  left: 0;
}

.overlay-cross::after {
  bottom: 0;
  right: 0;
}

.overlay-cross:not(:hover)::before,
.overlay-cross:not(:hover)::after {
  width: 0;
  height: 0;
}

.overlay-horizontal::before {
  top: 0;
  left: 0;
  bottom: 0;
}

.overlay-horizontal::after {
  top: 0;
  right: 0;
  bottom: 0;
}

.overlay-horizontal:not(:hover)::before,
.overlay-horizontal:not(:hover)::after {
  width: 0;
}

.overlay-vertical::before {
  top: 0;
  left: 0;
  right: 0;
}

.overlay-vertical::after {
  left: 0;
  right: 0;
  bottom: 0;
}

.overlay-vertical:not(:hover)::before,
.overlay-vertical:not(:hover)::after {
  height: 0;
}

.overlay-fade::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.3);
}

@media (prefers-reduced-motion: reduce) {
  .overlay-fade::before {
    transition: none;
  }
}

.overlay-fade.overlay-dark::before {
  background-color: rgba(0, 0, 0, 0.3);
}

.overlay-fade:not(:hover)::before {
  opacity: 0;
  visibility: hidden;
}

.overlay-scale-left-top::before,
.overlay-scale-right-top::before,
.overlay-scale-left-bottom::before,
.overlay-scale-right-bottom::before,
.overlay-scale-left::before,
.overlay-scale-right::before,
.overlay-scale-top::before,
.overlay-scale-bottom::before,
.overlay-scale-center::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.3);
}

@media (prefers-reduced-motion: reduce) {

  .overlay-scale-left-top::before,
  .overlay-scale-right-top::before,
  .overlay-scale-left-bottom::before,
  .overlay-scale-right-bottom::before,
  .overlay-scale-left::before,
  .overlay-scale-right::before,
  .overlay-scale-top::before,
  .overlay-scale-bottom::before,
  .overlay-scale-center::before {
    transition: none;
  }
}

.overlay-scale-left-top.overlay-dark::before,
.overlay-scale-right-top.overlay-dark::before,
.overlay-scale-left-bottom.overlay-dark::before,
.overlay-scale-right-bottom.overlay-dark::before,
.overlay-scale-left.overlay-dark::before,
.overlay-scale-right.overlay-dark::before,
.overlay-scale-top.overlay-dark::before,
.overlay-scale-bottom.overlay-dark::before,
.overlay-scale-center.overlay-dark::before {
  background-color: rgba(0, 0, 0, 0.3);
}

.overlay-scale-left-top::before {
  top: 0;
  left: 0;
}

.overlay-scale-left-top:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-right-top::before {
  top: 0;
  right: 0;
}

.overlay-scale-right-top:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-left-bottom::before {
  bottom: 0;
  left: 0;
}

.overlay-scale-left-bottom:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-right-bottom::before {
  bottom: 0;
  right: 0;
}

.overlay-scale-right-bottom:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-center::before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: auto;
  height: auto;
}

.overlay-scale-center:not(:hover)::before {
  top: 50%;
  left: 50%;
  right: 50%;
  bottom: 50%;
}

.overlay-scale-left::before {
  top: 0;
  left: 0;
  bottom: 0;
}

.overlay-scale-left:not(:hover)::before {
  width: 0;
}

.overlay-scale-right::before {
  top: 0;
  right: 0;
  bottom: 0;
}

.overlay-scale-right:not(:hover)::before {
  width: 0;
}

.overlay-scale-top::before {
  top: 0;
  left: 0;
  right: 0;
}

.overlay-scale-top:not(:hover)::before {
  height: 0;
}

.overlay-scale-bottom::before {
  bottom: 0;
  left: 0;
  right: 0;
}

.overlay-scale-bottom:not(:hover)::before {
  height: 0;
}

.border-zoom {
  overflow: hidden;
}

.border-zoom::before,
.border-zoom::after {
  position: absolute;
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  transition: all 0.5s ease;
  z-index: 2;
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {

  .border-zoom::before,
  .border-zoom::after {
    transition: none;
  }
}

.border-zoom::before {
  background-color: #000;
}

.border-zoom::after {
  top: -15px;
  bottom: -15px;
  left: -15px;
  right: -15px;
  border: 2px solid #fff;
}

.border-zoom:hover::before {
  opacity: .3;
}

.border-zoom:hover::after {
  top: 15px;
  bottom: 15px;
  left: 15px;
  right: 15px;
  opacity: 1;
}

.border-plus,
.border-scale {
  background-color: #000;
}

.border-plus .image-effect,
.border-plus img,
.border-scale .image-effect,
.border-scale img {
  transition: all 0.3s ease;
}

@media (prefers-reduced-motion: reduce) {

  .border-plus .image-effect,
  .border-plus img,
  .border-scale .image-effect,
  .border-scale img {
    transition: none;
  }
}

.border-plus:hover .image-effect,
.border-plus:hover img,
.border-scale:hover .image-effect,
.border-scale:hover img {
  opacity: .7;
}

.border-plus::before,
.border-plus::after,
.border-scale::before,
.border-scale::after {
  content: '';
  position: absolute;
  z-index: 2;
  border: solid #fff;
  top: 15px;
  bottom: 15px;
  left: 15px;
  right: 15px;
  margin: auto;
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .border-plus::before,
  .border-plus::after,
  .border-scale::before,
  .border-scale::after {
    transition: none;
  }
}

.border-plus::before,
.border-scale::before {
  border-width: 2px 0;
}

.border-plus::after,
.border-scale::after {
  border-width: 0 2px;
}

.border-plus.s2::before,
.border-scale.s2::before {
  top: 30px;
  bottom: 30px;
}

.border-plus.s2::after,
.border-scale.s2::after {
  left: 30px;
  right: 30px;
}

.border-scale:not(:hover)::before {
  left: 50%;
  right: 50%;
}

.border-scale:not(:hover)::after {
  top: 50%;
  bottom: 50%;
}

.border-plus:not(:hover)::before {
  top: 30%;
  bottom: 30%;
  opacity: 0;
}

.border-plus:not(:hover)::after {
  left: 30%;
  right: 30%;
  opacity: 0;
}

.flashlight::before,
.flashlight::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  background-color: #000;
  z-index: 2;
}

.flashlight::before {
  left: 0;
  width: 100%;
}

.flashlight::after {
  right: 0;
  width: 0;
  opacity: .5;
}

.flashlight:hover::before {
  width: 0;
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {
  .flashlight:hover::before {
    transition: none;
  }
}

.flashlight:hover::after {
  width: 100%;
  transition: all 0.8s ease;
}

@media (prefers-reduced-motion: reduce) {
  .flashlight:hover::after {
    transition: none;
  }
}

.bounce-in:hover .image-effect,
.bounce-in:hover img {
  -webkit-animation: bounceIn 0.5s ease;
  -moz-animation: bounceIn 0.5s ease;
  -ms-animation: bounceIn 0.5s ease;
  -o-animation: bounceIn 0.5s ease;
  animation: bounceIn 0.5s ease;
}

.faded-in .image-effect,
.faded-in img {
  transition: opacity 0.2s ease;
}

@media (prefers-reduced-motion: reduce) {

  .faded-in .image-effect,
  .faded-in img {
    transition: none;
  }
}

.faded-in:not(:hover) .image-effect,
.faded-in:not(:hover) img {
  opacity: 0.3;
}

.background-zoom {
  overflow: hidden;
}

.background-zoom .image-effect,
.background-zoom img {
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-zoom .image-effect,
  .background-zoom img {
    transition: none;
  }
}

.background-zoom.slow .image-effect,
.background-zoom.slow img {
  transition: all 10s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-zoom.slow .image-effect,
  .background-zoom.slow img {
    transition: none;
  }
}

.background-zoom:hover .image-effect,
.background-zoom:hover img {
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
  transform: scale(1.1);
}

.background-slide {
  overflow: hidden;
}

.background-slide .image-effect,
.background-slide img {
  position: relative;
  width: calc(100% + 60px);
  max-width: calc(100% + 60px);
  left: 50%;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  transition: all 0.4s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-slide .image-effect,
  .background-slide img {
    transition: none;
  }
}

.background-slide:hover .image-effect,
.background-slide:hover img {
  margin-left: 30px;
}

.grayscale {
  overflow: hidden;
}

.grayscale .image-effect,
.grayscale img {
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .grayscale .image-effect,
  .grayscale img {
    transition: none;
  }
}

.grayscale.slow .image-effect,
.grayscale.slow img {
  transition: all 10s ease;
}

@media (prefers-reduced-motion: reduce) {

  .grayscale.slow .image-effect,
  .grayscale.slow img {
    transition: none;
  }
}

.grayscale:hover .image-effect,
.grayscale:hover img {
  -webkit-filter: grayscale(0);
  -moz-filter: grayscale(0);
  -ms-filter: grayscale(0);
  -o-filter: grayscale(0);
  filter: grayscale(0);
}

.grayscale.revert .image-effect,
.grayscale.revert img {
  -webkit-filter: grayscale(0);
  -moz-filter: grayscale(0);
  -ms-filter: grayscale(0);
  -o-filter: grayscale(0);
  filter: grayscale(0);
}

.grayscale.revert:hover .image-effect,
.grayscale.revert:hover img {
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
}

.rotate-left,
.rotate-right {
  overflow: hidden;
}

.rotate-left .image-effect,
.rotate-left img,
.rotate-right .image-effect,
.rotate-right img {
  transition: all 0.7s ease;
}

@media (prefers-reduced-motion: reduce) {

  .rotate-left .image-effect,
  .rotate-left img,
  .rotate-right .image-effect,
  .rotate-right img {
    transition: none;
  }
}

.rotate-left:hover .image-effect,
.rotate-left:hover img {
  -webkit-transform: scale(1.2) rotate(-5deg);
  -moz-transform: scale(1.2) rotate(-5deg);
  -ms-transform: scale(1.2) rotate(-5deg);
  -o-transform: scale(1.2) rotate(-5deg);
  transform: scale(1.2) rotate(-5deg);
}

.rotate-right:hover .image-effect,
.rotate-right:hover img {
  -webkit-transform: scale(1.2) rotate(5deg);
  -moz-transform: scale(1.2) rotate(5deg);
  -ms-transform: scale(1.2) rotate(5deg);
  -o-transform: scale(1.2) rotate(5deg);
  transform: scale(1.2) rotate(5deg);
}

.navigation__list {
  margin-bottom: 0;
}

@media (min-width: 992px) {
  .navigation__item {
    margin: 0 5px;
  }

  .navigation__item:hover::before {
    display: block;
    position: absolute;
    top: 0;
    width: 7.5rem;
    height: 100%;
    background-color: transparent;
    content: '';
  }
}

.navigation__link {
  display: inline-block;
  position: relative;
  padding-top: 2px;
  padding-bottom: 2px;
  color: #222222;
  font-weight: 500;
  line-height: 1.5rem;
  text-decoration: none;
  text-transform: uppercase;
}

.navigation__link:after {
  content: '';
  display: block;
  position: absolute;
  top: 100%;
  left: 0.7rem;
  width: 0;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.navigation__link:hover:after {
  width: 2em;
}

@media (min-width: 992px) {
  .navigation__link {
    padding-right: 0.7rem;
    padding-left: 0.7rem;
  }
}

@media (min-width: 1200px) {
  .navigation__link {
    padding-right: 1rem;
    padding-left: 1rem;
  }

  .navigation__link:after {
    left: 1rem;
  }
}

.sub-menu__title {
  display: block;
  margin-bottom: .75rem;
  color: #767676;
  font-weight: 500;
  text-transform: uppercase;
}

.menu-link {
  display: inline-block;
  position: relative;
  padding: 0.5em 0;
  color: #222222;
  line-height: 1.5em;
}

.menu-link_us-s:after {
  content: '';
  display: block;
  position: absolute;
  top: 2em;
  left: 0;
  width: 0;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.menu-link_us-s:hover:after,
.menu-link_us-s.menu-link_active:after {
  width: 2em;
}

.default-menu {
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 16.25rem;
  padding: 1.5rem 1.875rem 1rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .default-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.box-menu {
  display: flex;
  display: -ms-flexbox;
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 49.6875rem;
  padding: 2.5rem 3.75rem 2rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .box-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.mega-menu {
  border-top: 1px solid #e4e4e4;
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 100%;
  padding: 2.5rem 0 2.75rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .mega-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.sub-menu__list+.sub-menu__title {
  margin-top: 1.875rem;
}

.mega-menu__media {
  flex: 2 0 0;
  max-width: 25.625rem;
}

.mega-menu__img {
  max-width: 100%;
}

.sitemap {
  height: 100vh;
  background-color: #ffffff;
  z-index: 1030;
}

.sitemap__bg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.sitemap__links .modal-header {
  background: #faf9f8;
  border: 0;
}

.sitemap__links .modal-body ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  background-color: #ffffff;
}

.sitemap__links .modal-body ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #e4e4e4;
}

.sitemap__links .nav {
  padding-left: calc(var(--bs-gutter-x) / 2);
}

.sitemap__links .nav-link_rline {
  padding-left: 0;
  font-size: 1.25rem;
  line-height: 1.5em;
}

.header {
  display: none;
  position: relative;
  background-color: #ffffff;
  z-index: 2;
}

.header .form-select {
  border: 0;
  box-shadow: none;
  height: 2.5rem;
  padding: 0.375rem 2.025rem 0.3rem 1.125rem;
  background-image: url('data:image/svg+xml,%3csvg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"%3e%3cg clip-path="url%28%23clip0_34_1038%29"%3e%3cpath d="M5.57201 9.11914C5.8052 9.35233 6.1948 9.35233 6.42858 9.11914L11.8229 3.73866C12.059 3.50248 12.059 3.11947 11.8229 2.88389C11.5867 2.64771 11.2031 2.64771 10.9669 2.88389L6.00002 7.83695L1.03375 2.88329C0.796978 2.64711 0.413959 2.64711 0.177183 2.88329C-0.0589957 3.11947 -0.0589957 3.50248 0.177183 3.73806L5.57201 9.11914Z" fill="%23222222"/%3e%3c/g%3e%3cdefs%3e%3cclipPath id="clip0_34_1038"%3e%3crect width="12" height="12" fill="white" transform="translate%2812 12%29 rotate%28-180%29"/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e');
}

.header .form-select.color-white {
  background-image: url('data:image/svg+xml,%3csvg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"%3e%3cg clip-path="url%28%23clip0_34_1038%29"%3e%3cpath d="M5.57201 9.11914C5.8052 9.35233 6.1948 9.35233 6.42858 9.11914L11.8229 3.73866C12.059 3.50248 12.059 3.11947 11.8229 2.88389C11.5867 2.64771 11.2031 2.64771 10.9669 2.88389L6.00002 7.83695L1.03375 2.88329C0.796978 2.64711 0.413959 2.64711 0.177183 2.88329C-0.0589957 3.11947 -0.0589957 3.50248 0.177183 3.73806L5.57201 9.11914Z" fill="white"/%3e%3c/g%3e%3cdefs%3e%3cclipPath id="clip0_34_1038"%3e%3crect width="12" height="12" fill="white" transform="translate%2812 12%29 rotate%28-180%29"/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e');
}

.header .form-select option {
  color: #222222;
}

@media (min-width: 992px) {
  .header {
    display: block;
  }
}

.header.header-transparent-bg:not(.header_sticky-active) {
  background: transparent;
}

.header.header_dark {
  background-color: #222222;
}

.header.header_dark .navigation__link {
  color: #fff;
}

.header.header_dark .header-tools__item {
  color: #fff;
}

.header-desk {
  display: flex;
  align-items: center;
}

.header-fullwidth {
  padding: 0 1.75rem;
  width: 100%;
}

@media (min-width: 1500px) {
  .header-fullwidth {
    padding: 0 3.75rem;
  }
}

.header-fullwidth .header-top {
  margin: 0 -1.75rem;
  padding: 0 1.75rem;
}

@media (min-width: 1500px) {
  .header-fullwidth .header-top {
    margin: 0 -3.75rem;
    padding: 0 3.75rem;
  }
}

.logo__image {
  max-width: 100%;
  max-height: 120px;
}

.logo__image2 {
  max-width: 90%;
}

.tifsu_logo_footer {
  max-width: 293px;
  border-radius: 7px;
}

.header-tools {
  margin-right: -0.5rem;
}

.header-tools__item {
  display: flex;
  padding: 0.25rem 0.5rem;
  text-decoration: none;
  color: #222222;
}

.header-tools__item .flaticon::before {
  display: block;
  line-height: 1;
}

.header-tools__item:last-child {
  margin-right: 0;
}

@media (min-width: 1200px) {
  .header-tools__item {
    margin-right: 1rem;
  }
}

.header-tools__cart {
  position: relative;
}

.header-tools__cart .cart-amount {
  top: calc(0.25rem + 1em);
  left: calc(0.5rem + 1.4em);
  width: 1rem;
  height: 1rem;
  border-radius: 100%;
  background: #b9a16b;
  color: #ffffff;
  font-size: 0.625rem;
  line-height: 1rem;
  text-align: center;
}

.header-search {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.25rem 0.625rem 0.875rem;
  border: 1px solid #e4e4e4;
  border-radius: 3px;
  background-color: #ffffff;
}

.header-search> :first-child {
  padding-left: 0;
}

.header-search> :last-child {
  margin-left: 1.25rem;
}

.header-search .hover-container {
  display: none;
}

@media (min-width: 1200px) {
  .header-search .hover-container {
    display: block;
  }
}

.header-search__input {
  padding: 0 0 0 1.25rem;
  border: 0;
  background-color: transparent;
  color: #222222;
  outline: none;
}

.header-search__btn {
  padding: 0;
  border: 0;
  line-height: 1;
}

.header-search__category {
  padding-right: 12px;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23222222' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0 center;
  background-size: 12px;
  color: #222222;
  outline: none;
}

.header-search__category::placeholder {
  color: #6c757d;
}

.header-search__category-list {
  right: calc(-1.25rem - 1px);
  width: calc(100% + 1.875rem + 1px);
  padding: 0 0.625rem;
  border: 1px solid #e4e4e4;
}

.header_sticky-bg_dark a {
  color: #fff;
}

.header_sticky-bg_dark svg {
  opacity: 1;
}

.header_sticky-bg_dark .btn-close-lg {
  background-image: url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.414336 14.1421L14.5565 0L15.9707 1.41421L1.82855 15.5563L0.414336 14.1421Z' fill='%23fff'/%3e%3cpath d='M1.41421 0.142113L15.5563 14.2842L14.1421 15.6985L0 1.55633L1.41421 0.142113Z' fill='%23fff'/%3e%3c/svg%3e");
}

.header_sticky-bg_dark .mega-menu a,
.header_sticky-bg_dark .box-menu a,
.header_sticky-bg_dark .default-menu a {
  color: #222222;
}

.header-top.bordered {
  border-bottom: 1px solid #e4e4e4;
}

.header-top.bordered-20per {
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.header_transparent {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: transparent;
}

.header-desk_type_1 {
  padding: 1.875rem 0 1.5rem 0;
}

.header-desk_type_1 .logo {
  margin-right: 2.1875rem;
}

.header-desk_type_1 .header-tools {
  margin-left: auto;
  margin-right: -0.5rem;
}

.header-fullwidth .header-desk_type_1 {
  padding: 1.25rem 0;
}

.header-fullwidth .header-desk_type_1 .header-search {
  padding-top: 0.6125rem;
  padding-bottom: 0.5rem;
  width: 21.5625rem;
}

.header-desk_type_2 {
  padding: 1.75rem 0;
}

.header-desk_type_2 .logo {
  margin: 0 auto;
  padding: 0 1rem;
}

.header-desk_type_2 .navigation {
  flex: 1;
}

.header-desk_type_2 .header-tools {
  flex: 1;
  justify-content: flex-end;
}

@media (min-width: 992px) and (max-width: 1499.98px) {
  .header-desk_type_2 .navigation__link {
    padding: 2px 0.5rem;
  }

  .header-desk_type_2 .navigation__link:after {
    left: 0.5rem;
  }
}

@media (min-width: 1500px) {
  .header-desk_type_2 {
    padding: 1.875rem 0;
  }
}

.header-desk_type_3 {
  padding: 2.625rem 0 1.5rem 0;
}

.header-desk_type_3 .logo {
  margin-right: 2.375rem;
}

.header-desk_type_3 .header-tools {
  margin-left: auto;
  margin-right: -0.5rem;
}

.header-desk_type_4 {
  padding: 1.875rem 0 1.5rem 0;
}

.header-desk_type_4.header-desk_sm {
  padding: 1.375rem 0;
}

.header-desk_type_4 .navigation {
  margin: 0 auto;
}

.header-desk_type_5 {
  padding: 1.25rem 0;
}

.header-desk_type_5 .logo {
  margin-right: 2.75rem;
}

.header-desk_type_5 .header-search {
  width: 26.625rem;
  margin-right: auto;
}

.header-desk_type_6 {
  border-bottom: 1px solid #e4e4e4;
}

.header-desk_type_6 .header-middle {
  padding: 1.25rem 0;
  border-bottom: 1px solid #e4e4e4;
}

.header-desk_type_6 .logo {
  width: 20.5rem;
  margin-right: 0.9375rem;
}

.header-desk_type_6 .navigation {
  margin: 0 -0.7rem;
  padding: 1.125rem 0 0.75rem 0.9375rem;
}

@media (min-width: 1200px) {
  .header-desk_type_6 .navigation {
    margin: -1rem;
  }
}

.header-desk_type_6 .navigation__item:first-child {
  margin-left: 0;
}

.header-desk_type_6 .navigation__item:last-child {
  margin-right: 0;
}

.header-desk_type_6 .header-search {
  flex-grow: 1;
  margin-left: 0.9375rem;
  margin-right: 0.5rem;
}

@media (min-width: 1200px) {
  .header-desk_type_6 .header-search {
    margin-right: 1.5rem;
  }
}

.header-desk_type_6 .categories-nav {
  width: 13.325rem;
  max-width: 20.5rem;
  margin-right: 0.9375rem;
}

@media (min-width: 1500px) {
  .header-desk_type_6 .categories-nav {
    width: 20.5rem;
  }
}

.header-desk_type_6 .categories-nav__list {
  position: absolute;
  width: 100%;
  left: 0;
  top: 100%;
  background-color: #ffffff;
  transition: all .3s ease;
}

.header-desk_type_6 .categories-nav__title {
  padding: 1.125rem 0 0.75rem 0.9375rem;
  padding-left: 1.8rem;
  padding-right: 1.8rem;
}

@media (min-width: 1500px) {
  .header-desk_type_6 .categories-nav__title {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.header-desk_type_6.style2 .header-search {
  padding-left: 1.75rem;
  padding-right: 1.75rem;
}

.header-desk_type_6.style2 .header-bottom {
  background-color: #193174;
}

.header-desk_type_6.style2 .header-bottom .navigation__list>.navigation__item>span {
  color: #ffffff;
}

.header-desk_type_6.style2 .header-bottom .navigation__list>.navigation__item>.navigation__link {
  color: #ffffff;
}

.header-desk_type_6.style2 .navigation {
  margin-right: 0;
}

.header-desk_type_6.style2 .categories-nav__title {
  padding-left: 0;
  padding-right: 0;
  cursor: pointer;
  background-color: #193174;
}

.header-desk_type_6.style2 .categories-nav__title+.categories-nav__list {
  opacity: 0;
  visibility: hidden;
  transition: all .3s ease;
}

.header-desk_type_6.style2 .categories-nav:hover>.categories-nav__list {
  opacity: 1;
  visibility: visible;
}

.header_sticky-active .header-desk_type_6 .categories-nav__list {
  opacity: 0;
  visibility: hidden;
}

.header_sticky-active .header-desk_type_6 .categories-nav:hover .categories-nav__list {
  opacity: 1;
  visibility: visible;
}

.header-desk_type_7 .header-top {
  padding: 1.25rem 0;
  color: #ffffff;
  background-color: #222222;
}

.header-desk_type_7 .header-bottom {
  padding: 1.25rem 0 0.75rem;
  color: #ffffff;
  background-color: #767676;
}

.header-desk_type_7 .logo {
  margin-right: 2.75rem;
}

.header-desk_type_7 .header-search {
  width: 26.625rem;
  margin-right: auto;
}

.header-desk_type_7 .navigation {
  width: 100%;
}

.header-desk_type_7 .navigation__link,
.header-desk_type_7 .header-tools__item {
  color: inherit;
}

.header-desk_type_7 .navigation__item:first-child {
  margin-left: 0;
}

.header-desk_type_7 .navigation__item:first-child .navigation__link {
  padding-left: 0;
}

.header-desk_type_7 .navigation__item:last-child {
  margin-right: 0;
}

.header-desk_type_7 .navigation__item:last-child .navigation__link {
  padding-right: 0;
}

.header-mobile {
  height: 3.75rem;
  min-height: 3.75rem;
  background-color: #ffffff;
  z-index: 1030;
}

.header-mobile .logo {
  margin: 0 auto;
}

.header-mobile .logo__image {
  max-height: 3rem;
}

@media (min-width: 992px) {
  .header-mobile {
    display: none;
  }
}

.header-mobile_sticky {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 8px 25px 0 rgba(140, 152, 164, 0.15);
}

.header-mobile__navigation {
  display: flex;
  flex-direction: column;
  height: 0;
  max-height: 0;
  transition: max-height .35s, height .35s;
  z-index: 1030;
}

.header-mobile__navigation .search-field__input {
  padding: 0.625rem 0.875rem 0.375rem;
}

.header-mobile__navigation .search-result {
  max-height: 30rem;
  overflow: auto;
  background-color: #ffffff;
  z-index: 1;
}

.header-mobile__navigation .search-result .product-card {
  display: flex;
  margin: 0.625rem 0;
}

.header-mobile__navigation .search-result .pc__img-wrapper {
  width: 40%;
  margin-right: 0.875rem;
}

.header-mobile__navigation .navigation__link {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
  font-size: 1rem;
}

.header-mobile__navigation .navigation__link .flaticon {
  font-size: 0.75rem;
}

.header-mobile__navigation .navigation__link:after {
  top: auto;
  bottom: 0.5rem;
  left: 0;
}

.header-mobile__navigation .form-select-sm {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.mobile-nav-activator .nav-icon,
.mobile-nav-activator .btn-close-lg {
  transition: all .24s;
}

.mobile-nav-activator .btn-close-lg {
  transform: rotate(-90deg);
  opacity: 0;
  visibility: hidden;
}

.mobile-menu-opened {
  overflow: hidden;
}

.mobile-menu-opened .header-mobile {
  z-index: 1050;
}

.mobile-menu-opened .header-mobile__navigation {
  height: calc(100vh - 100%);
  max-height: calc(100vh - 100%);
  transition: max-height .35s, height .35s;
  border-top: 1px solid #e4e4e4;
}

.mobile-menu-opened .navigation__list {
  left: 0;
  transition: all .18s ease-in;
}

.mobile-menu-opened .mobile-nav-activator .nav-icon {
  opacity: 0;
  visibility: hidden;
}

.mobile-menu-opened .mobile-nav-activator .btn-close-lg {
  transform: rotate(0);
  opacity: 1;
  visibility: visible;
}

.header_sticky {
  top: 0;
  left: 0;
  width: 100%;
  max-width: 100%;
  z-index: 9;
  transition: all .3s ease;
}

.header_sticky-active {
  position: fixed;
  animation: moveDown .5s;
  background-color: #ffffff;
  box-shadow: 0 8px 25px 0 rgba(140, 152, 164, 0.15);
  z-index: 1020;
}

.header_sticky-active.header_sticky-bg_dark {
  background-color: #222222;
}

.header_sticky-active .header-desk_type_3 {
  padding-top: 1.5rem;
}

.footer-top {
  padding-top: 6.2rem;
}

.footer-top .block-newsletter {
  max-width: 47rem;
  margin: 0 auto;
  text-align: center;
}

.footer-middle {
  padding-top: 3.125rem;
  padding-bottom: 1.625rem;
}

.footer-middle .logo {
  margin-bottom: 2.75rem;
}

@media (min-width: 768px) {
  .footer-middle {
    padding-top: 3.75rem;
    padding-bottom: 2.85rem;
  }
}

@media (min-width: 992px) {
  .footer-middle {
    padding-top: 6.25rem;
    padding-bottom: 4.75rem;
  }
}

.footer-column {
  flex-grow: 1;
}

.footer-address {
  margin-bottom: 0.875rem;
}

.footer__social-link {
  padding: 0.5rem 1rem;
  color: inherit;
}

.footer__social-link .svg-icon {
  fill: currentColor;
}

.footer-newsletter__form .btn-link {
  padding-right: 0.9375rem;
}

.footer-bottom {
  padding-top: 1.25rem;
  padding-bottom: 1rem;
  border-top: 1px solid #cfcdcd;
}

.footer {
  background-color: #e4e4e4;
  color: #222222;
}

.footer .sub-menu__title {
  margin-bottom: 0.875rem;
  color: inherit;
}

@media (min-width: 992px) {
  .footer .sub-menu__title {
    margin-bottom: 1.875rem;
  }
}

.footer .menu-link {
  margin-top: 3px;
  margin-bottom: 2px;
}

.footer .social-links {
  margin-left: -1rem;
}

.footer .form-select {
  color: inherit;
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23222222'/%3e%3c/svg%3e");
}

.footer .form-select:focus {
  box-shadow: none;
  border-color: transparent;
}

@media (max-width: 767.98px) {
  .footer .form-select {
    padding-left: 0;
  }
}

.footer .form-select.color-white {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='white'/%3e%3c/svg%3e");
}

.footer .form-select.color-white option {
  color: #222222;
}

.footer .service-promotion.horizontal {
  border-bottom: 1px solid #cfcdcd;
}

.footer_type_2 {
  background-color: #ffffff;
  color: #c0bfbf;
}

.footer_type_2 .form-select {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23767676'/%3e%3c/svg%3e");
}

.footer_type_2 .footer-select__option {
  background-color: #ffffff;
}

.footer_type_2 .footer-bottom {
  border-color: #e4e4e4;
}

.footer_type_2 .sub-menu__title {
  color: #222222;
}

.footer_type_2.dark {
  background-color: #222222;
  color: #c0bfbf;
}

.footer_type_2.dark .sub-menu__title {
  color: inherit;
}

.footer_type_2.dark .menu-link {
  color: #e4e4e4;
}

.footer_type_2.dark .form-select {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23ffffff'/%3e%3c/svg%3e");
}

.footer_type_2.dark .footer-select__option {
  background-color: #222222;
}

.footer_type_2.dark .footer-bottom {
  border-color: rgba(255, 255, 255, 0.15);
}

.footer_type_2.dark .footer__social-link:hover {
  color: #767676;
}

.footer_type_2.bordered {
  border-top: 1px solid #e4e4e4;
}

.footer_type_3 {
  background-color: #fff;
}

.footer_type_3 .footer-middle {
  padding: 0.875rem 0;
  border-top: 1px solid #cfcdcd;
}

.app-download-link {
  background: #767676;
  display: flex;
  width: 14.1875rem;
  height: 4.375rem;
  border-radius: 0.25rem;
  color: #ffffff;
  align-items: center;
  padding: 0.875rem;
  line-height: 1.4;
  gap: 1.5rem;
  transition: all .3s ease;
}

.app-download-link .app-download-text {
  display: flex;
  flex-direction: column;
  font-size: 0.8125rem;
}

.app-download-link .app-download-text strong {
  font-size: 1rem;
  font-weight: 400;
}

.app-download-link:hover {
  color: #ffffff;
  background-color: #222222;
}

.app-download-link.no-bg {
  width: auto;
  height: auto;
  border-radius: 0;
  color: #222222;
  background-color: transparent;
  padding: 0;
  gap: 1rem;
}

@media (min-width: 992px) {
  .footer-store-info {
    width: 24%;
  }

  .footer-menu {
    width: 17%;
  }

  .footer-menu2 {
    width: 1%;
  }

  .footer-newsletter {
    width: 25%;
  }
}

.footer-mobile {
  max-width: 100%;
  padding-top: 0.625rem;
  padding-bottom: 0.125rem;
  z-index: 1000;
  opacity: 0;
  bottom: -6.25rem;
  transition: all .32s;
}

.footer-mobile .flaticon {
  font-size: 1.125rem;
}

.footer-mobile .cart-amount,
.footer-mobile .wishlist-amount {
  top: -5px;
  left: calc(100% - 5px);
  width: 1rem;
  height: 1rem;
  border-radius: 100%;
  background: #b9a16b;
  color: #ffffff;
  font-size: 0.625rem;
  line-height: 1rem;
  text-align: center;
}

.footer-mobile.position-fixed {
  opacity: 1;
}

.footer-mobile.footer-mobile_initialized {
  bottom: 0;
  transition: all .32s;
}

.footer-mobile__link {
  font-size: 0.8125rem;
}

.slideshow {
  height: 34.5rem;
}

.slideshow.type3 {
  height: 26.25rem;
}

.slideshow.type4 {
  height: 26.25rem;
}

@media (min-width: 992px) {
  .slideshow {
    height: 50rem;
  }

  .slideshow.type2 {
    height: 56rem;
  }

  .slideshow.type3 {
    height: 35rem;
  }

  .slideshow.type4 {
    height: 37.5rem;
  }

  .slideshow.slideshow-lg {
    height: 47.5rem;
  }

  .slideshow.slideshow-md {
    height: 43.75rem;
  }
}

@media (max-width: 575.98px) {
  .slideshow.h-xs-25rem {
    height: 25rem;
  }
}

@media (max-width: 991.98px) {
  .slideshow.minh-100 {
    min-height: calc(100vh - 4rem);
  }
}

@media (max-width: 767.98px) {
  .slideshow.minh-100 {
    min-height: calc(100vh - 7rem);
  }
}

.slideshow_small {
  height: 20rem;
}

@media (min-width: 992px) {
  .slideshow_small {
    height: 28.125rem;
  }
}

.swiper-slide {
  overflow: hidden;
}

.slideshow-bg {
  height: 100%;
}

.slideshow-bg__img {
  width: 100%;
  height: 100%;
}

.slideshow-character__img {
  max-height: 555px;
}

@media (min-width: 992px) {
  .slideshow-character__img {
    max-height: 733px;
  }
}

.slideshow_small .slideshow-character__img {
  max-height: 20rem;
}

@media (min-width: 992px) {
  .slideshow_small .slideshow-character__img {
    max-height: 28.125rem;
  }
}

.character_bg {
  max-width: 140%;
  width: 43.125rem;
  margin-top: -10%;
}

.slideshow-pagination {
  z-index: 10;
}

.slideshow-pagination.type2 .swiper-pagination-bullet::after {
  color: #767676;
}

.slideshow-pagination.type2 .swiper-pagination-bullet-active {
  border-color: transparent;
}

.slideshow-pagination.type2 .swiper-pagination-bullet-active::after {
  color: #222222;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
}

.slideshow-pagination.position-left-center {
  position: absolute;
  left: 50%;
  top: auto;
  bottom: 1rem;
  transform: translateX(-50%);
  display: flex;
  width: auto;
}

@media (min-width: 1700px) {
  .slideshow-pagination.position-left-center {
    left: 3.75rem;
    top: 50%;
    bottom: auto;
    transform: translateY(-50%);
    flex-direction: column;
  }
}

.slideshow-pagination.position-right-center {
  position: absolute;
  left: auto;
  right: 50%;
  top: auto;
  bottom: 1rem;
  transform: translateX(50%);
  display: flex;
  width: auto;
}

@media (min-width: 1500px) {
  .slideshow-pagination.position-right-center {
    right: 3.75rem;
    top: 50%;
    bottom: auto;
    transform: translateY(-50%);
    flex-direction: column;
  }

  .slideshow-pagination.position-right-center.position-right-2 {
    right: 2.6875rem;
  }
}

.lookbook-container .slideshow-pagination.position-right-center {
  position: static;
  align-items: center;
  justify-content: center;
  margin-top: 1rem;
}

@media (min-width: 1500px) {
  .lookbook-container .slideshow-pagination.position-right-center {
    position: absolute;
    right: -3.75rem;
  }

  .lookbook-container .slideshow-pagination.position-right-center.position-right-2 {
    right: -2.6875rem;
  }

  .lookbook-container .slideshow-pagination.position-right-center.position-right-2 .swiper-pagination-bullet {
    margin: 0.25rem 0;
  }
}

.blog-pagination,
.testimonial-pagination,
.products-pagination,
.slideshow-pagination {
  z-index: 10;
}

.blog-pagination.type2 .swiper-pagination-bullet-active,
.testimonial-pagination.type2 .swiper-pagination-bullet-active,
.products-pagination.type2 .swiper-pagination-bullet-active,
.slideshow-pagination.type2 .swiper-pagination-bullet-active {
  border-color: transparent;
}

.blog-pagination.type2 .swiper-pagination-bullet-active::after,
.testimonial-pagination.type2 .swiper-pagination-bullet-active::after,
.products-pagination.type2 .swiper-pagination-bullet-active::after,
.slideshow-pagination.type2 .swiper-pagination-bullet-active::after {
  color: #222222;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
}

.blog-pagination.active-white .swiper-pagination-bullet::after,
.testimonial-pagination.active-white .swiper-pagination-bullet::after,
.products-pagination.active-white .swiper-pagination-bullet::after,
.slideshow-pagination.active-white .swiper-pagination-bullet::after {
  color: #767676;
}

.blog-pagination.active-white .swiper-pagination-bullet-active::after,
.testimonial-pagination.active-white .swiper-pagination-bullet-active::after,
.products-pagination.active-white .swiper-pagination-bullet-active::after,
.slideshow-pagination.active-white .swiper-pagination-bullet-active::after {
  color: #ffffff;
}

.blog-pagination.color-white .swiper-pagination-bullet::after,
.testimonial-pagination.color-white .swiper-pagination-bullet::after,
.products-pagination.color-white .swiper-pagination-bullet::after,
.slideshow-pagination.color-white .swiper-pagination-bullet::after {
  color: #ffffff;
}

.blog-pagination.color-white .swiper-pagination-bullet-active::after,
.testimonial-pagination.color-white .swiper-pagination-bullet-active::after,
.products-pagination.color-white .swiper-pagination-bullet-active::after,
.slideshow-pagination.color-white .swiper-pagination-bullet-active::after {
  color: #ffffff;
}

.slideshow-number-pagination .swiper-pagination-bullet {
  width: auto;
  height: auto;
  border: 0;
  color: #767676;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.slideshow-number-pagination .swiper-pagination-bullet:before {
  content: '';
  border-top: 1px solid #767676;
  width: 2.3125rem;
  display: block;
}

.slideshow-number-pagination .swiper-pagination-bullet:after {
  display: none;
}

.slideshow-number-pagination .swiper-pagination-bullet:first-child:before {
  display: none;
}

.slideshow-number-pagination .swiper-pagination-bullet-active {
  color: #222222;
}

@media (min-width: 1500px) {
  .slideshow-number-pagination.position-xxl-right-center {
    right: 0 !important;
    top: 50% !important;
    bottom: auto !important;
    left: auto !important;
    transform: translateY(-50%);
    flex-direction: column;
    margin: 0 1.125rem;
  }

  .slideshow-number-pagination.position-xxl-right-center .swiper-pagination-bullet {
    flex-direction: column;
  }

  .slideshow-number-pagination.position-xxl-right-center .swiper-pagination-bullet:before {
    border-top: 0;
    border-left: 1px solid #767676;
    width: 1px;
    height: 2.3125rem;
  }
}

.slideshow-navigation {
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.slideshow-navigation .slideshow__prev,
.slideshow-navigation .slideshow__next {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  color: #767676;
  font-weight: 500;
  width: auto;
  opacity: 1;
}

.slideshow-navigation .slideshow__prev:after {
  content: '';
  display: block;
  width: 1.875rem;
  border-bottom: 2px solid;
  transition: all .3s ease;
}

.slideshow-navigation .slideshow__prev:hover {
  color: #222222;
}

.slideshow-navigation .slideshow__prev:hover:after {
  width: 3.125rem;
}

.slideshow-navigation .slideshow__next:before {
  content: '';
  display: block;
  width: 1.875rem;
  border-bottom: 2px solid;
  transition: all .3s ease;
}

.slideshow-navigation .slideshow__next:hover {
  color: #222222;
}

.slideshow-navigation .slideshow__next:hover:before {
  width: 3.125rem;
}

.slideshow__prev,
.slideshow__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  z-index: 1;
  outline: none;
}

.slideshow__prev .flaticon,
.slideshow__next .flaticon {
  font-size: 10px;
}

@media (min-width: 1530px) {

  .slideshow__prev,
  .slideshow__next {
    width: 25px;
    height: 25px;
    margin-top: -0.875rem;
    border: 0;
    transition: opacity .32s;
    opacity: 0.5;
  }

  .slideshow__prev .flaticon,
  .slideshow__next .flaticon {
    font-size: 25px;
  }

  .slideshow__prev:hover,
  .slideshow__next:hover {
    opacity: 1;
  }
}

.slideshow__prev {
  left: 1rem;
}

@media (min-width: 1530px) {
  .slideshow__prev {
    left: 3.5rem;
  }
}

.slideshow__next {
  right: 1rem;
}

@media (min-width: 1530px) {
  .slideshow__next {
    right: 3.5rem;
  }
}

.slideshow-navigation-white-sm .slideshow__prev,
.slideshow-navigation-white-sm .slideshow__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  z-index: 1;
  outline: none;
  background-color: #ffffff;
  display: none !important;
}

@media (min-width: 768px) {

  .slideshow-navigation-white-sm .slideshow__prev,
  .slideshow-navigation-white-sm .slideshow__next {
    display: flex !important;
  }
}

.slideshow-navigation-white-sm .slideshow__prev .flaticon,
.slideshow-navigation-white-sm .slideshow__next .flaticon {
  font-size: 10px;
}

@media (max-width: 767.98px) {
  .slideshow_split {
    height: auto;
  }
}

.slide-split_text {
  flex: 2 2 40%;
}

@media (max-width: 1499.98px) {
  .slide-split_text {
    flex: 2 2 50%;
  }
}

.slide-split_media {
  flex: 1 1 60%;
}

@media (max-width: 1499.98px) {
  .slide-split_media {
    flex: 2 2 50%;
  }
}

.slideshow-social-follow {
  width: 3.75rem;
  z-index: 1;
}

.slideshow-social-follow__title {
  transform: rotate(-90deg);
  white-space: nowrap;
}

.slideshow-scroll {
  width: 3.75rem;
  transform: rotate(-90deg) translateX(30%);
  white-space: nowrap;
  z-index: 3;
}

.slideshow-boxed-right>.slideshow {
  height: 26.25rem;
  background-color: #eee;
  border-radius: 4px;
}

@media (min-width: 992px) {
  .slideshow-boxed-right>.slideshow {
    height: 31.875rem;
    width: 44rem;
    margin-left: auto;
    margin-right: 0;
    margin-top: 1.875rem;
  }
}

@media (min-width: 1200px) {
  .slideshow-boxed-right>.slideshow {
    width: 54rem;
  }
}

@media (min-width: 1500px) {
  .slideshow-boxed-right>.slideshow {
    width: 65.625rem;
  }
}

@media (min-width: 992px) {
  .collections-grid_masonry {
    height: 30rem;
  }
}

@media (min-width: 1500px) {
  .collections-grid_masonry {
    height: 37.5rem;
  }
}

.collections-grid_masonry .collection-grid__item {
  height: 17.8125rem;
}

@media (min-width: 992px) {
  .collections-grid_masonry .collection-grid__item {
    height: auto;
  }
}

.collection-grid__item {
  margin-bottom: 0.9375rem;
}

@media (min-width: 992px) {
  .collection-grid__item {
    margin-bottom: 0;
  }
}

.grid-banner__item_rect {
  min-height: 19.375rem;
}

@media (min-width: 992px) {
  .grid-banner__item_rect {
    min-height: 24.875rem;
  }
}

@media (min-width: 992px) {
  .grid-banner__item_rect_2 {
    min-height: 31.25rem;
  }

  .grid-banner__item_rect_2 .content_abs {
    --content-space: 4.5625rem;
  }
}

.products-grid .row {
  --bs-gutter-x: 0.875rem;
}

@media (min-width: 768px) {
  .products-grid .row {
    --bs-gutter-x: 1.5rem;
  }
}

@media (min-width: 992px) {
  .products-grid .row {
    --bs-gutter-x: 1.875rem;
  }
}

.products-grid .nav {
  margin-left: -var(--bs-gutter-x);
  margin-right: -var(--bs-gutter-x);
}

@media (min-width: 992px) {
  .products-masonry {
    height: 480px;
  }

  .products-masonry .pc__img-wrapper {
    height: 100%;
  }
}

@media (min-width: 1200px) {
  .products-masonry {
    height: 640px;
  }
}

@media (min-width: 1500px) {
  .products-masonry {
    height: 730px;
  }
}

.deal-timer {
  --countdown-space: 1.125rem;
  min-height: 19.375rem;
  margin: 0 0.9375rem;
  padding: 2rem 1rem;
}

.deal-timer .countdown-unit {
  position: relative;
  min-width: 4.375rem;
  padding-right: calc(var(--countdown-space) * 2);
  font-size: 1.125rem;
  line-height: 1;
}

.deal-timer .countdown-word {
  font-size: 0.875rem;
}

.deal-timer .day:after,
.deal-timer .hour:after,
.deal-timer .min:after {
  content: ':';
  display: block;
  position: absolute;
  top: 0;
  right: var(--countdown-space);
}

@media (min-width: 768px) {
  .deal-timer {
    min-height: 25rem;
  }

  .deal-timer .countdown-unit {
    font-size: 1.5rem;
  }
}

@media (min-width: 992px) {
  .deal-timer {
    min-height: 31.25rem;
    padding: 2.5rem 0;
  }

  .deal-timer .countdown-unit {
    min-width: 6.25rem;
    font-size: 1.875rem;
  }

  .deal-timer .countdown-word {
    font-size: 1rem;
  }
}

@media (min-width: 1500px) {
  .deal-timer {
    --countdown-space: 1.375rem;
    min-height: 37.5rem;
    margin: 0 3.75rem;
  }
}

.hot-deals {
  --countdown-space: 0.875rem;
}

.hot-deals .countdown-unit {
  position: relative;
  padding-right: calc(var(--countdown-space) * 2);
  line-height: 1;
  font-size: 1.125rem;
}

.hot-deals .countdown-word {
  font-size: 0.875rem;
}

.hot-deals .day:after,
.hot-deals .hour:after,
.hot-deals .min:after {
  content: ':';
  display: block;
  position: absolute;
  top: 0;
  right: var(--countdown-space);
}

.swiper-slide.product-card {
  width: 50%;
}

@media (min-width: 768px) {
  .swiper-slide.product-card {
    width: 33.33333%;
  }
}

@media (min-width: 992px) {
  .swiper-slide.product-card {
    width: 25%;
  }
}

.products-carousel__prev,
.products-carousel__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  background-color: #ffffff;
  z-index: 1;
  outline: none;
}

.products-carousel__prev svg,
.products-carousel__next svg {
  color: #767676;
  width: 10px;
  height: auto;
}

.products-carousel__prev.type2,
.products-carousel__next.type2 {
  background-color: #eee;
}

.products-carousel__prev.type2 svg,
.products-carousel__next.type2 svg {
  width: 0.75rem;
}

@media (min-width: 1530px) {

  .products-carousel__prev:not(.navigation-sm),
  .products-carousel__next:not(.navigation-sm) {
    width: 25px;
    height: 25px;
    margin-top: -0.875rem;
    border: 0;
    transition: opacity .32s;
    opacity: 0.5;
  }

  .products-carousel__prev:not(.navigation-sm) svg,
  .products-carousel__next:not(.navigation-sm) svg {
    width: 25px;
  }

  .products-carousel__prev:not(.navigation-sm):hover,
  .products-carousel__next:not(.navigation-sm):hover {
    opacity: 1;
  }

  .products-carousel__prev:not(.navigation-sm).type2,
  .products-carousel__next:not(.navigation-sm).type2 {
    width: 2.8125rem;
    height: 2.8125rem;
  }
}

.products-carousel__prev {
  left: -0.625rem;
}

@media (min-width: 1530px) {
  .products-carousel__prev {
    left: -3rem;
  }

  .products-carousel__prev.type2 {
    left: -4.5rem;
  }
}

.products-carousel__next {
  right: -0.625rem;
}

@media (min-width: 1530px) {
  .products-carousel__next {
    right: -3rem;
  }

  .products-carousel__next.type2 {
    right: -4.5rem;
  }
}

.products-carousel-with-banner .products-carousel__prev svg,
.products-carousel-with-banner .products-carousel__next svg {
  width: 0.9375rem;
  height: auto;
}

.products-carousel-with-banner__category {
  position: absolute;
  right: 0;
  top: 0;
  transform: rotate(-90deg);
  transform-origin: right top;
}

.instagram__img {
  width: 100%;
  max-width: 100%;
  height: 100%;
  object-fit: cover;
}

.instagram .row {
  margin: -7px;
}

@media (min-width: 768px) {
  .instagram .row {
    margin: -3px;
  }
}

.instagram__tile {
  padding: 7px;
}

@media (min-width: 768px) {
  .instagram__tile {
    padding: 3px;
  }
}

.service-promotion__icon .flaticon {
  font-size: 3.25rem;
}

.service-promotion__content {
  font-size: 0.9375rem;
}

.service-promotion.horizontal {
  padding-top: 2.9375rem;
  padding-bottom: 2.3rem;
}

.service-promotion.horizontal .service-promotion__icon .flaticon {
  font-size: 2.8125rem;
}

.shop-banner {
  min-height: 18.5rem;
}

@media (min-width: 1200px) {
  .shop-banner {
    min-height: 21.5rem;
  }
}

@media (min-width: 1200px) {
  .shop-banner {
    min-height: 26.25rem;
  }
}

.shop-acs__select {
  padding-right: 0.9375rem;
  background-position: right center;
  cursor: pointer;
  padding-left: 0;
  box-shadow: none !important;
  text-transform: uppercase;
  font-weight: 500;
}

.shop-asc__seprator {
  width: 2px;
  height: 22px;
}

.aside-filters {
  overflow-x: hidden;
  overflow-y: auto;
}

.shop-acs .multi-select__actor {
  padding-right: 2.8125rem;
}

.shop-acs .filters-container {
  border: 1px solid #e4e4e4;
}

.shop-pages .flaticon {
  font-size: 0.625rem;
}

.shop-sidebar {
  width: 18.75rem;
  min-width: 18.75rem;
}

.aside-filters .accordion-button__icon,
.shop-sidebar .accordion-button__icon {
  width: 0.625rem;
  height: 0.625rem;
}

.shop-list {
  max-width: 100%;
}

@media (min-width: 992px) {
  .shop-list {
    max-width: calc(100% - 22.5rem);
  }
}

.side-sticky {
  position: fixed;
  top: 0;
  right: -26.25rem;
  left: auto;
  width: 26.25rem;
  max-width: 100%;
  height: 100vh;
  padding: 0 1.25rem 1.75rem;
  transition: left .35s, right .35s;
  overflow-x: hidden;
  overflow-y: auto;
  z-index: 1050;
}

.side-sticky.aside_visible {
  right: 0;
}

.side-sticky .accordion {
  padding-left: 1.25rem;
  padding-right: 1.25rem;
}

@media (min-width: 992px) {
  .side-sticky {
    position: sticky;
    top: 0;
    right: auto;
    left: 0;
    width: 18.75rem;
    height: 100%;
    padding: .375rem 0 0;
    margin-right: 3.75rem;
    z-index: 1;
  }

  .side-sticky .accordion {
    padding-left: 0;
    padding-right: 0;
  }
}

.shop-categories {
  --item-space: 0.9375rem;
  padding: calc(var(--item-space) * 2) var(--item-space);
}

@media (min-width: 992px) {
  .shop-categories {
    --item-space: 1.875rem;
    padding: var(--item-space);
  }
}

@media (min-width: 1500px) {
  .shop-categories {
    --item-space: 3.75rem;
  }
}

.shop-categories__list {
  margin: 0 calc(var(--item-space) * -1 / 2);
}

.shop-categories__item,
.shop-categories__item_sm {
  margin-right: calc(var(--item-space) / 2);
  margin-left: calc(var(--item-space) / 2);
  transition: filter .2s;
}

.shop-categories__item:hover,
.shop-categories__item_sm:hover {
  filter: brightness(0.97);
}

.shop-categories__item-img {
  width: 5rem;
  height: 5rem;
  background-color: #e4e4e4;
}

@media (min-width: 992px) {
  .shop-categories__item-img {
    width: 6.25rem;
    height: 6.25rem;
  }
}

@media (min-width: 1500px) {
  .shop-categories__item-img {
    width: 7.5rem;
    height: 7.5rem;
  }

  .shop-categories__item_sm .shop-categories__item-img {
    width: 6.25rem;
    height: 6.25rem;
  }
}

@media (min-width: 576px) {
  .block-newsletter {
    padding: 0 1rem;
  }
}

.block-newsletter .block__title {
  color: #222222;
  margin-bottom: 1.125rem;
}

.block-newsletter p {
  margin-bottom: 1.5rem;
}

.block-newsletter .block-newsletter__form {
  display: flex;
  gap: 1.25rem;
}

.block-newsletter .form-control {
  border-width: 1px;
  border-color: #e4e4e4;
}

.block-newsletter .btn {
  font-size: 0.875rem;
  background-color: #222222;
}

.block-newsletter.dark .block__title {
  color: inherit;
}

.block-newsletter.dark .form-control {
  border-color: #353535;
  background-color: #353535;
  color: #ffffff;
}

.block-newsletter.dark .form-control::placeholder {
  color: #e4e4e4;
}

.block-newsletter.dark .btn {
  border-color: #5C5C5C;
  background-color: #5C5C5C;
  color: #ffffff;
}

.newsletter-popup {
  width: 56.25rem;
  max-width: calc(100% - 1rem);
}

.newsletter-popup .modal-content {
  overflow: hidden;
}

.newsletter-popup .modal-content .btn-close {
  position: absolute;
  right: 0.75rem;
  top: 1rem;
}

.newsletter-popup .block-newsletter {
  padding: 1.875rem 1.25rem;
}

@media (min-width: 768px) {
  .newsletter-popup .block-newsletter {
    padding: 3.5rem 2.5rem;
  }
}

@media (min-width: 1200px) {
  .product-single>.row {
    --bs-gutter-x: 3.75rem;
  }
}

.product-single__media {
  display: flex;
  width: 100%;
  margin: 0 -0.3125rem;
  position: relative;
  flex-direction: column;
  margin-bottom: 3rem;
}

@media (min-width: 992px) {
  .product-single__media {
    flex-direction: row;
    margin-bottom: 0;
  }
}

.product-single__media .swiper-container {
  width: 100%;
  height: 100%;
}

.product-single__media .swiper-button-prev,
.product-single__media .swiper-button-next {
  width: 2.1875rem;
  height: 2.1875rem;
  background-color: #fff;
  border-radius: 2rem;
  font-size: 0.875rem;
  color: #222222;
}

.product-single__media .swiper-button-prev:hover,
.product-single__media .swiper-button-next:hover {
  background-color: #e4e4e4;
}

.product-single__media .swiper-button-prev:after,
.product-single__media .swiper-button-next:after {
  display: none;
}

@media (min-width: 576px) {

  .product-single__media .swiper-button-prev,
  .product-single__media .swiper-button-next {
    width: 2.8125rem;
    height: 2.8125rem;
  }
}

.product-single__media .swiper-button-prev {
  left: 1rem;
  z-index: 1;
}

@media (min-width: 576px) {
  .product-single__media .swiper-button-prev {
    left: 2rem;
  }
}

.product-single__media .swiper-button-next {
  right: 1rem;
  z-index: 1;
}

@media (min-width: 576px) {
  .product-single__media .swiper-button-next {
    right: 2rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image {
  flex: 0 0 85.7142%;
  max-width: 85.7142%;
}

@media (max-width: 991.98px) {
  .product-single__media.vertical-thumbnail .product-single__image {
    flex: 0 0 100%;
    max-width: 100%;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 0.3125rem;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a,
.product-single__media.vertical-thumbnail .product-single__image-item>button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a:hover,
.product-single__media.vertical-thumbnail .product-single__image-item>button:hover {
  background-color: #e4e4e4;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a svg,
.product-single__media.vertical-thumbnail .product-single__image-item>button svg {
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a,
  .product-single__media.vertical-thumbnail .product-single__image-item>button {
    width: 2.1875rem;
    height: 2.1875rem;
    right: 1rem;
    bottom: 1rem;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a svg,
  .product-single__media.vertical-thumbnail .product-single__image-item>button svg {
    width: 0.7775rem;
    height: 0.7775rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.view-video,
.product-single__media.vertical-thumbnail .product-single__image-item>button.view-video {
  bottom: 6rem;
  border: 0;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.view-video .flaticon,
.product-single__media.vertical-thumbnail .product-single__image-item>button.view-video .flaticon {
  font-size: 1rem;
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a.view-video,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.view-video {
    bottom: 4rem;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a.view-video .flaticon,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.view-video .flaticon {
    font-size: 0.75rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree,
.product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree {
  left: 1.875rem;
  top: 1.875rem;
  right: auto;
  bottom: auto;
  background-color: transparent;
  width: auto;
  height: auto;
  padding-top: 0.5rem;
  padding-right: 0.5rem;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree .flaticon,
.product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree .flaticon {
  font-size: 2.5rem;
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree {
    left: 1rem;
    top: 1rem;
    right: auto;
    bottom: auto;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree .flaticon,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree .flaticon {
    font-size: 1.5rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image img {
  width: 100%;
}

.product-single__media.vertical-thumbnail .product-single__thumbnail {
  flex: 0 0 100%;
  max-width: 1000%;
  order: 1;
}

@media (min-width: 992px) {
  .product-single__media.vertical-thumbnail .product-single__thumbnail {
    flex: 0 0 14.2857%;
    max-width: 14.2857%;
    order: -1;
  }
}

.product-single__media.vertical-thumbnail .product-single__thumbnail .swiper-slide {
  cursor: pointer;
  opacity: .5;
  border: 0;
}

.product-single__media.vertical-thumbnail .product-single__thumbnail .swiper-slide.swiper-slide-thumb-active {
  opacity: 1;
}

.product-single__media.horizontal-thumbnail {
  flex-direction: column;
}

.product-single__media.horizontal-thumbnail .product-single__image {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 0.3125rem;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a:hover {
  background-color: #e4e4e4;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a svg {
  pointer-events: none;
}

.product-single__media.horizontal-thumbnail .product-single__image img {
  width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail .swiper-slide {
  cursor: pointer;
  opacity: .5;
  border: 0;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail .swiper-slide.swiper-slide-thumb-active {
  opacity: 1;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot {
    padding-left: 5.375rem;
  }
}

.product-single__media.vertical-dot .product-single__image {
  flex: 0 0 100%;
  max-width: 100%;
  margin: 0;
  position: static;
}

.product-single__media.vertical-dot .product-single__image .swiper-container {
  position: static;
}

.product-single__media.vertical-dot .product-single__image .swiper-wrapper {
  margin-bottom: 1rem;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot .product-single__image .swiper-wrapper {
    margin-bottom: 0;
  }
}

.product-single__media.vertical-dot .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 1rem;
}

@media (min-width: 576px) {
  .product-single__media.vertical-dot .product-single__image-item {
    padding: 10%;
  }
}

.product-single__media.vertical-dot .product-single__image-item>a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.vertical-dot .product-single__image-item>a:hover {
  background-color: #e4e4e4;
}

.product-single__media.vertical-dot .product-single__image img {
  width: 100%;
}

.product-single__media.vertical-dot .product-single__image .swiper-pagination {
  position: static;
  transform: none;
  flex-direction: row;
  justify-content: center;
  left: 0;
  top: 50%;
  display: flex;
  gap: 0.5rem;
  width: auto;
  bottom: auto;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot .product-single__image .swiper-pagination {
    position: absolute;
    transform: translateY(-50%);
    flex-direction: column;
  }
}

.product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet:first-child {
  margin-left: 4px;
}

.product-single__media .product-label {
  position: absolute;
  left: auto;
  right: 1rem;
  top: 1rem;
  width: 4.5625rem;
  height: 4.5625rem;
  border-radius: 3rem;
  background-color: #D6001C;
  color: #fff;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  padding: 0.5rem;
  text-align: center;
  line-height: 1.4;
  z-index: 1;
}

@media (min-width: 768px) {
  .product-single__media .product-label {
    right: -1.125rem;
    top: 1.875rem;
  }
}

.product-single__prev-next {
  gap: 1.875rem;
  display: none !important;
}

@media (min-width: 992px) {
  .product-single__prev-next {
    display: flex !important;
  }
}

.product-single__prev-next>a {
  display: flex;
  align-items: center;
  gap: 0.625rem;
}

.product-single__prev-next>a .flaticon {
  font-size: 0.75rem;
}

.product-single__prev-next>a.disabled {
  opacity: .5;
  pointer-events: none;
}

.product-single__name {
  font-size: 1.625rem;
}

.product-single__rating {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  margin-bottom: 0.625rem;
}

.product-single__price {
  font-size: 1.375rem;
  font-weight: 500;
  margin-bottom: 1.6875rem;
}

.product-single__price span.old-price {
  font-size: 1rem;
  color: #767676;
  font-weight: 400;
  text-decoration: line-through;
}

.product-single__price .special-price {
  color: #D6001C;
  margin-left: 0.5rem;
}

.product-single__short-desc {
  margin-bottom: 2.1875rem;
}

.product-single__addtocart {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 2.1875rem;
  flex-wrap: wrap;
}

.product-single__addtocart .qty-control {
  min-width: 7.25rem;
}

.product-single__addtocart .qty-control__number {
  border: 2px solid #E4E4E4;
  height: 3.75rem;
  padding: 0 2rem;
  min-width: 6.5rem;
}

.product-single__addtocart .qty-control__reduce,
.product-single__addtocart .qty-control__increase {
  font-size: 1rem;
  text-align: center;
  top: 50%;
  transform: translateY(-50%);
  width: 2rem;
}

.product-single__addtocart .qty-control__reduce {
  padding-left: 1.25rem;
}

.product-single__addtocart .qty-control__increase {
  padding-right: 1.25rem;
}

.product-single__addtocart .btn-addtocart {
  height: 3.75rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  width: 17.5rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.product-single__addtocart .btn-addtocart.btn-outofstock {
  border: 2px solid #D6001C;
  color: #D6001C;
  background-color: #fff;
  cursor: default;
  pointer-events: none;
}

.product-single__addtocart.product-single__grouped {
  flex-direction: column;
  align-items: normal;
  gap: 0;
}

.product-single__addtocart.product-single__grouped .grouped-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  border-top: 1px solid #e4e4e4;
  padding: 1.25rem 0;
}

.product-single__addtocart.product-single__grouped .grouped-item:first-child {
  border-top: 0;
  padding-top: 0;
}

.product-single__addtocart.product-single__grouped .grouped-item__name {
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-single__addtocart.product-single__grouped .grouped-item__price {
  margin-left: auto;
  font-weight: 500;
}

.product-single__addtocart.product-single__grouped>div:not(.grouped-item) {
  margin-top: 1.2rem;
}

.product-single__addtolinks {
  font-size: 0.8125rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
}

.product-single__addtolinks>a,
.product-single__addtolinks>.share-button>button {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding: 0 0 0.625rem;
  text-transform: uppercase;
  border: 0;
  background-color: transparent;
  font-weight: 500;
}

.product-single__addtolinks>a:hover:after,
.product-single__addtolinks>.share-button>button:hover:after {
  width: 50%;
}

.product-single__addtolinks>a .flaticon,
.product-single__addtolinks>.share-button>button .flaticon {
  font-size: 1rem;
}

.product-single__addtolinks>.add-to-wishlist.active svg {
  color: #193174;
}

.product-single__meta-info {
  font-size: 0.8125rem;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.product-single__meta-info label {
  color: #767676;
  text-transform: uppercase;
}

.product-single__details-tab {
  margin: 6.25rem auto 2.375rem;
  max-width: 58.125rem;
}

.product-single__details-tab>.nav-tabs {
  justify-content: center;
  text-transform: uppercase;
}

@media (max-width: 575.98px) {
  .product-single__details-tab>.nav-tabs {
    flex-direction: column;
  }

  .product-single__details-tab>.nav-tabs .nav-link {
    width: max-content;
  }
}

.product-single__details-tab>.tab-content {
  padding: 3.125rem 0;
}

.product-single__description * {
  line-height: 1.875rem;
}

.product-single__addtional-info>.item {
  margin-bottom: 1.875rem;
}

.product-single__addtional-info>.item label {
  min-width: 8.75rem;
  margin: 0;
}

.product-single__reviews-title {
  font-size: 1.125rem;
  margin-bottom: 1.75rem;
}

.product-single__reviews-list {
  display: flex;
  flex-direction: column;
  gap: 1.87rem;
  margin-bottom: 2.375rem;
}

.product-single__reviews-item {
  display: flex;
  gap: 1.875rem;
  border-bottom: 1px solid #e4e4e4;
}

.product-single__reviews-item:last-child {
  border-bottom: 0;
}

.product-single__reviews-item .customer-avatar {
  flex: 0 0 3.75rem;
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 2rem;
  overflow: hidden;
}

.product-single__reviews-item .customer-avatar>img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-single__reviews-item .customer-review .customer-name {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.product-single__reviews-item .customer-review .customer-name>h6,
.product-single__reviews-item .customer-review .customer-name>.h6 {
  margin: 0;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
}

.product-single__reviews-item .customer-review .review-date {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.25rem;
}

.product-single__reviews-item .customer-review .review-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.5rem;
}

.product-single__review-form form>h5,
.product-single__review-form form>.h5 {
  font-size: 1.125rem;
  margin-bottom: 0.375rem;
}

.product-single__review-form form>p {
  font-size: 0.875rem;
  color: #767676;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.product-single__review-form form .select-star-rating {
  margin-bottom: 2rem;
}

.product-single__review-form form button {
  text-transform: uppercase;
  font-size: 0.875rem;
  min-width: 12.5rem;
}

.product-single__swatches .product-swatch {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 2.5rem;
  margin-bottom: 1.875rem;
}

@media (max-width: 1499.98px) {
  .product-single__swatches .product-swatch {
    gap: 1rem;
  }
}

.product-single__swatches .product-swatch>label {
  font-size: 0.875rem;
  font-weight: 500;
  min-width: 3rem;
  text-transform: uppercase;
}

.product-single__swatches .product-swatch .swatch-list {
  display: flex;
  align-items: center;
  gap: 0.625rem;
}

.product-single__swatches .product-swatch .swatch-list>input[type="radio"] {
  display: none;
}

.product-single__swatches .product-swatch .sizeguide-link {
  margin-left: auto;
  font-size: 0.8125rem;
  font-weight: 500;
  text-transform: uppercase;
  line-height: 1.875rem;
  position: relative;
}

@media (max-width: 1499.98px) {
  .product-single__swatches .product-swatch .sizeguide-link {
    margin-left: 0;
  }
}

.product-single__swatches .product-swatch .sizeguide-link:before {
  content: '';
  border-bottom: 2px solid;
  display: block;
  width: 0;
  transition: all .3s ease;
  position: absolute;
  left: 0;
  bottom: 0;
}

.product-single__swatches .product-swatch .sizeguide-link:hover:before {
  width: 100%;
}

.product-single__swatches .product-swatch .swatch {
  transition: all .3s ease;
}

.product-single__swatches .product-swatch.text-swatches .swatch {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 1.875rem;
  border: 1px solid #e4e4e4;
  padding: 0 0.8125rem;
}

.product-single__swatches .product-swatch.text-swatches .swatch.swatch_active,
.product-single__swatches .product-swatch.text-swatches .swatch:hover {
  border-color: #222222;
}

.product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches .swatch-color {
  margin: 0;
  border: 2px solid transparent;
}

.product-single__swatches .product-swatch.color-swatches .swatch-color.swatch_active,
.product-single__swatches .product-swatch.color-swatches .swatch-color:hover {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-color {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image {
  width: 3.875rem;
  height: 3.875rem;
  border: 1px solid transparent;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image.swatch_active,
.product-single__swatches .product-swatch.color-swatches .swatch-image:hover {
  border-color: #e4e4e4;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image img {
  pointer-events: none;
}

.product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-image {
  border-color: #e4e4e4;
}

.product-single__additional-info {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.product-single__additional-info>a {
  font-size: 0.8125rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  width: max-content;
}

.product-single__additional-info>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__additional-info>a:hover:before {
  width: 100%;
}

@media (min-width: 576px) {
  .product-single__additional-info {
    flex-direction: row;
    align-items: center;
    gap: 1.875rem;
  }
}

@media (min-width: 992px) {
  .product-single__additional-info {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }
}

@media (min-width: 1500px) {
  .product-single__additional-info {
    flex-direction: row;
    align-items: center;
    gap: 1.875rem;
  }
}

.product-single__type-2 .product-single__top-background {
  background-color: #e0e0e0;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch {
  border-color: #222222;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch:hover,
.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch.swatch_active {
  box-shadow: 0 0 0 1px inset #222222;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  box-shadow: 0 0 0 1px inset #222222;
  border-color: #222222;
}

.product-single__type-2 .product-single__addtocart .qty-control__number {
  border-color: #222222;
  background-color: transparent;
}

.product-single__type-3 .breadcrumb .menu-link {
  color: #767676;
}

.product-single__type-3 .breadcrumb .menu-link:hover {
  color: #767676;
}

.product-single__type-3 .product-single {
  color: #fff;
}

.product-single__type-3 .product-single__top-background {
  background-color: #222222;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image-item {
  padding: 0;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet:after {
  color: #fff;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet-active {
  border-color: #fff;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet-active:after {
  color: #fff;
}

.product-single__type-3 .product-single__prev-next a,
.product-single__type-3 .product-single__prev-next .menu-link {
  color: #767676;
}

.product-single__type-3 .product-single__name {
  color: #fff;
}

.product-single__type-3 .product-single__rating .reviews-note {
  color: #fff !important;
}

.product-single__type-3 .product-single__price {
  color: #fff;
}

.product-single__type-3 .product-single__short-desc {
  color: #e4e4e4;
}

.product-single__type-3 .product-single__swatches label {
  color: #767676;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch {
  border-color: #fff;
  color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch:hover,
.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch.swatch_active {
  box-shadow: 0 0 0 1px inset #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  box-shadow: 0 0 0 1px inset #fff;
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.color-swatches .swatch-color.swatch_active,
.product-single__type-3 .product-single__swatches .product-swatch.color-swatches .swatch-color:hover {
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-color {
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch .sizeguide-link {
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .qty-control__number {
  background: transparent;
  border-color: #767676;
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .qty-control__reduce,
.product-single__type-3 .product-single__addtocart .qty-control__increase {
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .btn-addtocart {
  background-color: #fff;
  color: #222222;
}

.product-single__type-3 .product-single__addtolinks>a {
  color: #fff;
}

.product-single__type-3 .product-single__meta-info label {
  color: #767676;
}

.product-single__type-3 .product-single__meta-info span {
  color: #fff;
}

.product-single__type-3 .product-single__additional-info>a {
  color: #fff;
}

.product-single__type-4 .product-single__media:before {
  content: '';
  height: 100%;
  width: 100vw;
  background-color: #e6e6e6;
  position: absolute;
  right: 0;
  z-index: -1;
}

@media (max-width: 991.98px) {
  .product-single__type-4 .product-single__media:before {
    right: -9.5rem;
    width: calc(100% + 19rem);
  }
}

.product-single__type-4 .product-single__image {
  width: 100%;
  position: relative;
  background-color: #e6e6e6;
}

.product-single__type-4 .product-single__image-item {
  padding-top: 6.25rem;
  height: 100vh;
  scroll-snap-align: center;
}

.product-single__type-4 .product-single__image-item img {
  height: 100%;
  width: 100%;
  object-fit: contain;
}

.product-single__type-5 {
  margin-bottom: 6.25rem;
}

.product-single__type-5 .product-single__image-item img {
  width: 100%;
}

.product-single__type-5 .product-single__swatches .product-swatch {
  gap: 0.5rem;
}

.product-single__type-5 .product-single__swatches .product-swatch>label {
  flex: 0 0 100%;
}

.product-single__type-5 .product-single__additional-info {
  flex-wrap: wrap;
  row-gap: 0.5rem;
}

.product-single__type-6 {
  margin-bottom: 6.25rem;
}

.product-single__type-7 {
  margin-bottom: 6.25rem;
}

.product-single__type-7 .product-single__media {
  margin-bottom: 1.25rem;
}

.product-single__type-7 .product-single__image {
  display: flex;
  flex-wrap: wrap;
  gap: 0.625rem;
}

.product-single__type-7 .product-single__image-item {
  flex: 0 0 calc(50% - 0.3125rem);
  max-width: calc(50% - 0.3125rem);
}

.product-single__type-7 .product-single__image-item:first-child {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__type-7 .product-single__details {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 1.875rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.product-single__type-7 .product-single__details>a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  color: #767676;
  transition: all .3s ease;
  white-space: nowrap;
}

.product-single__type-7 .product-single__details>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__type-7 .product-single__details>a:hover {
  color: #222222;
}

.product-single__type-7 .product-single__details>a:hover:before {
  width: 100%;
}

@media (max-width: 575.98px) {
  .product-single__type-7 .product-single__details {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }

  .product-single__type-7 .product-single__details>a {
    width: max-content;
  }
}

.product-single__type-9 {
  margin-bottom: 6.25rem;
}

.product-single__type-9 .product-single__details {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 1.875rem;
  margin-bottom: 1rem;
}

.product-single__type-9 .product-single__details>a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  color: #767676;
  transition: all .3s ease;
}

.product-single__type-9 .product-single__details>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__type-9 .product-single__details>a:hover {
  color: #222222;
}

.product-single__type-9 .product-single__details>a:hover:before {
  width: 100%;
}

@media (max-width: 575.98px) {
  .product-single__type-9 .product-single__details {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }

  .product-single__type-9 .product-single__details>a {
    width: max-content;
  }
}

.product-single__aside {
  width: 37.5rem;
  right: -37.5rem;
}

.product-single__aside .aside-content {
  height: calc(100% - 9rem);
  overflow-y: auto;
}

.product-single__details-accordion {
  margin-bottom: 6rem;
}

.product-single__details-accordion .accordion-item {
  margin-bottom: 1.25rem;
}

.product-single__details-accordion .accordion-button {
  text-transform: uppercase;
  border: 0;
  border-bottom: 1px solid #e4e4e4;
  padding: 0.625rem 0;
  color: #767676;
}

.product-single__details-accordion .accordion-collapse {
  border: 0;
}

.product-single__details-accordion .accordion-body {
  padding: 1.5rem 0;
}

.product-single__details-list {
  width: 65.3125rem;
  max-width: 100%;
  margin-top: 1.375rem;
}

.product-single__details-list__title {
  font-size: 1rem;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 3.4375rem;
}

.product-single__details-list__title:after {
  content: '';
  display: block;
  width: 2.5rem;
  border-bottom: 2px solid;
}

.product-single__details-list__content {
  padding-left: 7.1875rem;
  margin-bottom: 6.25rem;
}

@media (max-width: 575.98px) {
  .product-single__details-list__content {
    padding-left: 2.1875rem;
  }
}

.header_transparent~main {
  padding-top: 0 !important;
  overflow: hidden;
}

html.snap {
  scroll-snap-type: y mandatory;
  -webkit-overflow-scrolling: touch;
  scroll-snap-points-y: repeat(100%);
}

button.js-add-wishlist.active .flaticon.flaticon-heart,
a.add-to-wishlist.active .flaticon.flaticon-heart {
  color: #d6001c;
}

.quick-view {
  width: 73.125rem;
  max-width: calc(100% - 1rem);
}

.quick-view .product-single {
  display: flex;
  flex-wrap: wrap;
}

.quick-view .product-single__media {
  flex: 0 0 100%;
  max-width: 100%;
}

.quick-view .product-single__media img {
  width: 100%;
}

@media (min-width: 768px) {
  .quick-view .product-single__media {
    flex: 0 0 47%;
    max-width: 47%;
  }
}

.quick-view .product-single__detail {
  flex: 0 0 100%;
  max-width: 100%;
  padding: 1.875rem 1.25rem;
}

@media (min-width: 768px) {
  .quick-view .product-single__detail {
    flex: 0 0 53%;
    max-width: 53%;
    padding: 3.5rem 2.5rem;
  }
}

.quick-view .modal-content {
  overflow: hidden;
}

.quick-view .modal-content .btn-close {
  position: absolute;
  right: 0.75rem;
  top: 1rem;
}

.shop-checkout .page-title {
  font-size: 2.1875rem;
  margin-bottom: 3.125rem;
  text-transform: uppercase;
}

.shop-checkout .checkout-steps {
  display: flex;
  border-bottom: 2px solid #e4e4e4;
}

.shop-checkout .checkout-steps__item {
  flex-grow: 1;
  display: flex;
  gap: 0.75rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
}

.shop-checkout .checkout-steps__item-number {
  font-size: 1.125rem;
  font-weight: 500;
}

.shop-checkout .checkout-steps__item-title {
  display: flex;
  flex-direction: column;
}

.shop-checkout .checkout-steps__item-title>span {
  font-size: 1.125rem;
  font-weight: 500;
  text-transform: uppercase;
}

.shop-checkout .checkout-steps__item-title>em {
  font-size: 0.875rem;
  font-weight: 400;
  font-style: normal;
  color: #767676;
}

.shop-checkout .checkout-steps__item.active {
  border-color: #222222;
}

@media (max-width: 991.98px) {
  .shop-checkout .checkout-steps {
    border-bottom: 0;
    border-left: 2px solid #e4e4e4;
    flex-direction: column;
  }

  .shop-checkout .checkout-steps__item {
    border-left: 2px solid transparent;
    margin-left: -2px;
    border-bottom: 0;
    margin-bottom: 0;
    padding: 0.5rem 1rem;
  }
}

.shopping-cart {
  display: flex;
  flex-direction: column;
  gap: 3.625rem;
}

@media (min-width: 1200px) {
  .shopping-cart {
    flex-direction: row;
  }
}

.shopping-cart .cart-table__wrapper {
  padding-top: 3.125rem;
  flex-grow: 1;
}

.shopping-cart__totals-wrapper .sticky-content {
  padding-top: 3.125rem;
}

.shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .button-wrapper:not(.fixed-btn) {
  padding: 0;
}

.shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
  position: fixed;
  left: var(--bs-gutter-x, 0.9375rem);
  right: var(--bs-gutter-x, 0.9375rem);
  bottom: 4rem;
  width: auto;
}

@media (min-width: 768px) {
  .shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
    bottom: 1rem;
  }
}

@media (min-width: 992px) {
  .shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
    position: static;
  }
}

.shopping-cart__totals-wrapper .btn-checkout {
  width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

.shopping-cart__totals {
  border: 1px solid #222;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 0.5rem;
  max-width: 100%;
}

@media (min-width: 1200px) {
  .shopping-cart__totals {
    width: 26.25rem;
  }
}

.shopping-cart__totals>h3,
.shopping-cart__totals>.h3 {
  font-size: 1rem;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.shopping-cart__totals table {
  width: 100%;
}

.shopping-cart__totals table th,
.shopping-cart__totals table td {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.shopping-cart__totals table th {
  text-transform: uppercase;
  vertical-align: baseline;
}

.shopping-cart__totals table tr:last-child th,
.shopping-cart__totals table tr:last-child td {
  border-bottom: 0;
}

.shopping-cart .cart-table {
  width: 100%;
}

@media (min-width: 768px) {

  .shopping-cart .cart-table th,
  .shopping-cart .cart-table td {
    border-bottom: 1px solid #e4e4e4;
  }
}

.shopping-cart .cart-table thead {
  display: none;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table thead {
    display: table-header-group;
  }
}

.shopping-cart .cart-table thead th {
  font-size: 0.875rem;
  text-transform: uppercase;
  font-weight: 500;
  padding: 0 0 0.625rem;
}

.shopping-cart .cart-table tbody tr {
  position: relative;
  display: block;
  padding: 1.25rem 0;
  border-bottom: 1px solid #e4e4e4;
  transition: all .3s ease;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr {
    display: table-row;
    padding: 0;
    border: 0;
  }
}

.shopping-cart .cart-table tbody tr:first-child {
  border-top: 1px solid #e4e4e4;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr:first-child {
    border: 0;
  }
}

.shopping-cart .cart-table tbody tr:after {
  content: '';
  display: block;
  clear: both;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr:after {
    display: none;
  }
}

.shopping-cart .cart-table tbody tr td {
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.shopping-cart .cart-table tbody tr td>* {
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
  overflow: hidden;
  max-height: 12rem;
}

.shopping-cart .cart-table tbody tr._removed td {
  padding-top: 0;
  padding-bottom: 0;
}

.shopping-cart .cart-table tbody tr._removed td>* {
  max-height: 0;
}

.shopping-cart .cart-table tbody td {
  display: block;
  margin-left: 9.375rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td {
    padding: 1.875rem 0;
    display: table-cell;
    margin: 0;
  }
}

.shopping-cart .cart-table tbody td:first-child {
  width: 9.375rem;
  float: left;
  margin-left: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td:first-child {
    float: none;
  }
}

.shopping-cart .cart-table tbody td .shopping-cart__product-price {
  display: none;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .shopping-cart__product-price {
    display: block;
  }
}

.shopping-cart .cart-table tbody td .shopping-cart__subtotal {
  float: right;
  display: block;
  margin-top: -2.2rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .shopping-cart__subtotal {
    float: none;
    margin: 0;
  }
}

.shopping-cart .cart-table tbody td .remove-cart {
  position: absolute;
  right: 0;
  top: 1rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .remove-cart {
    position: static;
  }
}

.shopping-cart .cart-table .qty-control {
  margin: 0.5rem 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control {
    width: 7.25rem;
    margin: 0;
  }
}

.shopping-cart .cart-table .qty-control__number {
  border: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__number {
    border: 2px solid #e4e4e4;
    height: 3.125rem;
    padding: 0 2rem;
    min-width: 6.875rem;
  }
}

.shopping-cart .cart-table .qty-control__reduce,
.shopping-cart .cart-table .qty-control__increase {
  font-size: 1rem;
  text-align: center;
  top: 50%;
  transform: translateY(-50%);
}

.shopping-cart .cart-table .qty-control__reduce {
  left: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__reduce {
    left: 1.25rem;
  }
}

.shopping-cart .cart-table .qty-control__increase {
  right: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__increase {
    right: 1.25rem;
  }
}

.shopping-cart .cart-table-footer {
  display: flex;
  justify-content: space-between;
  padding-top: 1.875rem;
  gap: 1.875rem;
  flex-wrap: wrap;
}

.shopping-cart .cart-table-footer form {
  max-width: 100%;
}

.shopping-cart .cart-table-footer .form-control {
  width: 23.125rem;
  max-width: 100%;
  height: 3.875rem;
}

.shopping-cart .cart-table-footer button {
  height: 3.875rem;
}

.shopping-cart__product-item {
  display: flex;
  align-items: center;
  gap: 1.875rem;
}

.shopping-cart__product-item img {
  width: 7.5rem;
  height: auto;
}

.shopping-cart__product-item__detail h4,
.shopping-cart__product-item__detail .h4 {
  font-size: 1rem;
  font-weight: 400;
  margin-bottom: 0;
}

.shopping-cart__product-item__options {
  list-style: none;
  padding: 0;
  margin: 0;
  margin-top: 0.5rem;
}

.shopping-cart__product-item__options li {
  font-size: 0.875rem;
  color: #767676;
}

.shopping-cart__product-price {
  font-size: 1rem;
  color: #767676;
}

.shopping-cart__subtotal {
  font-size: 1rem;
  font-weight: 500;
}

.checkout-form {
  display: flex;
  gap: 3.625rem;
}

@media (max-width: 1199.98px) {
  .checkout-form {
    flex-direction: column;
  }
}

.checkout-form .billing-info__wrapper {
  padding-top: 3.125rem;
  flex-grow: 1;
}

.checkout-form .billing-info__wrapper .form-floating>label,
.checkout-form .billing-info__wrapper .form-label-fixed>.form-label {
  color: #767676;
}

.checkout-form .checkout__totals-wrapper .sticky-content {
  padding-top: 3.125rem;
}

.checkout-form .checkout__totals-wrapper .btn-checkout {
  width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

.checkout-form .checkout__payment-methods {
  border: 1px solid #e4e4e4;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 1.5rem;
  width: 26.25rem;
}

@media (max-width: 1199.98px) {
  .checkout-form .checkout__payment-methods {
    width: 100%;
  }
}

.checkout-form .checkout__payment-methods label {
  font-size: 1rem;
  line-height: 1.5rem;
}

.checkout-form .checkout__payment-methods label .option-detail {
  font-size: 0.875rem;
  margin: 0.625rem 0 0;
  display: none;
}

.checkout-form .checkout__payment-methods .form-check-input:checked~label .option-detail {
  display: block;
}

.checkout-form .checkout__payment-methods .policy-text {
  font-size: 0.75rem;
  line-height: 1.5rem;
}

.checkout-form .checkout__payment-methods .policy-text>a {
  color: #c32929;
}

.checkout__totals {
  border: 1px solid #222;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 0.5rem;
  width: 26.25rem;
}

@media (max-width: 1199.98px) {
  .checkout__totals {
    width: 100%;
  }
}

.checkout__totals>h3,
.checkout__totals>.h3 {
  font-size: 1rem;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.checkout__totals table {
  width: 100%;
}

.checkout__totals .checkout-cart-items thead th {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.checkout__totals .checkout-cart-items tbody td {
  padding: 0.40625rem 0;
  color: #767676;
}

.checkout__totals .checkout-cart-items tbody tr:first-child td {
  padding-top: 0.8125rem;
}

.checkout__totals .checkout-cart-items tbody tr:last-child td {
  padding-bottom: 0.8125rem;
  border-bottom: 1px solid #e4e4e4;
}

.checkout__totals .checkout-totals th,
.checkout__totals .checkout-totals td {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.checkout__totals .checkout-totals tr:last-child th,
.checkout__totals .checkout-totals tr:last-child td {
  border-bottom: 0;
}

.order-complete {
  width: 56.25rem;
  max-width: 100%;
  margin: 3.125rem auto;
  display: flex;
  flex-direction: column;
  gap: 2.25rem;
}

.order-complete__message {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.order-complete__message svg {
  margin-bottom: 1.25rem;
}

.order-complete__message h3,
.order-complete__message .h3 {
  font-size: 2.1875rem;
  text-align: center;
}

.order-complete__message p {
  color: #767676;
  margin-bottom: 0;
  text-align: center;
}

.order-complete .order-info {
  width: 100%;
  border: 2px dashed #767676;
  padding: 2.5rem;
  display: flex;
  gap: 1rem;
}

@media (max-width: 767.98px) {
  .order-complete .order-info {
    flex-direction: column;
  }
}

.order-complete .order-info__item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex-grow: 1;
}

.order-complete .order-info__item label {
  font-size: 0.875rem;
  font-weight: 400;
  color: #767676;
}

.order-complete .order-info__item span {
  font-size: 1rem;
  font-weight: 500;
}

.order-complete .checkout__totals {
  width: 100%;
}

.order-complete .checkout__totals .checkout-cart-items thead th:last-child {
  text-align: right;
}

.order-tracking {
  width: 31.25rem;
  max-width: 100%;
  margin: 0 auto;
  text-align: center;
}

.order-tracking .btn-track {
  height: 3.75rem;
  font-size: 0.875rem;
}

.my-account .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
}

.my-account .account-nav {
  list-style: none;
  padding: 0;
  padding-top: 2.5rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  font-weight: 500;
}

.my-account .account-nav .menu-link.menu-link_active {
  pointer-events: none;
  color: #c32929;
}

.my-account .page-content {
  padding-top: 2.5rem;
}

.my-account__dashboard p {
  width: 43.125rem;
  max-width: 100%;
}

.my-account__dashboard .unerline-link {
  text-decoration: underline;
}

.my-account__orders-list {
  overflow-x: auto;
  width: 100%;
}

.my-account .orders-table {
  border: 1px solid #e4e4e4;
  width: 100%;
}

.my-account .orders-table thead th {
  background-color: #e4e4e4;
  padding: 1rem 1.875rem;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.my-account .orders-table tbody td {
  border-top: 1px solid #e4e4e4;
  padding: 1.875rem;
}

.my-account .orders-table tbody td:first-child {
  text-decoration: underline;
}

.my-account .orders-table tbody td:last-child {
  width: 12.5rem;
}

.my-account .orders-table tbody td .btn {
  height: 3.125rem;
  font-size: 0.875rem;
}

.my-account__address .notice {
  margin-bottom: 3.75rem;
}

.my-account__address-list {
  display: flex;
  gap: 5.625rem;
}

@media (max-width: 767.98px) {
  .my-account__address-list {
    flex-direction: column;
  }
}

.my-account__address-item {
  flex-grow: 1;
}

.my-account__address-item__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  line-height: 1.5rem;
  text-transform: uppercase;
  margin-bottom: 0.875rem;
  font-weight: 500;
}

.my-account__address-item__title h5,
.my-account__address-item__title .h5 {
  font-size: 1.125rem;
  margin: 0;
}

.my-account__address-item__title a {
  font-size: 0.8125rem;
  border-bottom: 2px solid;
}

.my-account__address-item__detail {
  line-height: 1.5rem;
}

.my-account__address-item__detail p {
  margin: 0;
}

.my-account__edit .btn-primary {
  width: 18.75rem;
  height: 3.75rem;
  max-width: 100%;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.my-account__wishlist .btn-remove-from-wishlist {
  position: absolute;
  left: 1.25rem;
  top: 1.25rem;
  z-index: 2;
  border: 0;
  background-color: #fff;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all .3s ease;
  box-shadow: 0 0 1px rgba(0, 0, 0, 0.1);
  opacity: 0;
  visibility: hidden;
}

.my-account__wishlist .product-card:hover .btn-remove-from-wishlist {
  opacity: 1;
  visibility: visible;
}

.blog-page-title {
  width: 112.5rem;
  height: 16rem;
  max-width: calc(100% - 1.875rem);
  border: 2px solid #e4e4e4;
  margin: 0 auto;
  background-size: cover;
  position: relative;
  display: flex;
  align-items: center;
  padding: 1.25rem;
}

.blog-page-title .page-title {
  font-size: calc(1.5rem + 3vw);
  font-weight: 700;
  text-transform: uppercase;
}

@media (min-width: 1200px) {
  .blog-page-title .page-title {
    font-size: 3.75rem;
  }
}

.blog-page-title .title-bg {
  display: block;
  position: absolute;
  left: 0.5rem;
  right: 0.5rem;
  top: 0.5rem;
  bottom: 0.5rem;
  z-index: -1;
}

.blog-page-title .title-bg img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (min-width: 576px) {
  .blog-page-title {
    height: 27.5rem;
    padding: 0;
  }
}

.blog-page .flaticon {
  font-size: 0.625rem;
}

.blog__filter {
  display: flex;
  gap: 1rem;
  row-gap: 0;
  flex-wrap: wrap;
}

.blog__filter>a {
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: 500;
}

.blog-grid__item {
  margin-bottom: 2.75rem;
}

.blog-grid__item-image {
  margin-bottom: 1.25rem;
}

.blog-grid__item-image img {
  display: block;
  width: 100%;
}

.blog-grid__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 0.25rem;
  white-space: nowrap;
}

.blog-grid__item-title {
  font-size: 1.625rem;
  margin-bottom: 1.875rem;
  line-height: 1.5;
}

@media (max-width: 991.98px) {
  .blog-grid__item-title {
    font-size: 1.125rem;
    margin-bottom: 1.25rem;
  }
}

.blog-grid__item-content p {
  margin-bottom: 0.625rem;
}

.blog-grid__item-content .readmore-link {
  text-transform: uppercase;
  position: relative;
  display: inline-block;
  font-weight: 500;
}

.blog-grid__item-content .readmore-link:after {
  content: '';
  display: block;
  width: 70%;
  border-bottom: 2px solid;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.blog-grid__item-content .readmore-link:hover:after {
  width: 100%;
}

.blog-grid.row-cols-xl-3 .blog-grid__item-title {
  font-size: 1.125rem;
  margin-bottom: 1.25rem;
}

.blog-list {
  margin-bottom: 3.125rem;
}

@media (min-width: 992px) {
  .blog-list {
    margin-bottom: 6.25rem;
  }
}

.blog-list__item {
  margin-bottom: 1.875rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1.25rem;
}

@media (min-width: 992px) {
  .blog-list__item {
    flex-direction: row;
    align-items: center;
    gap: 3.125rem;
  }
}

.blog-list__item-image {
  flex: 0 0 100%;
  width: 100%;
}

@media (min-width: 992px) {
  .blog-list__item-image {
    flex: 0 0 calc(50% - 1.5625rem);
  }
}

.blog-list__item-image img {
  display: block;
  width: 100%;
}

.blog-list__item-detail {
  flex: 0 0 100%;
  padding: 0;
}

@media (min-width: 992px) {
  .blog-list__item-detail {
    flex: 0 0 calc(50% - 1.5625rem);
    padding: 1.875rem 0;
  }
}

.blog-list__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 0.25rem;
}

.blog-list__item-title {
  font-size: 1.125rem;
  margin-bottom: 1.25rem;
  line-height: 1.5;
}

@media (min-width: 992px) {
  .blog-list__item-title {
    font-size: 1.625rem;
    margin-bottom: 1.875rem;
  }
}

.blog-list__item-content p {
  margin-bottom: 0.625rem;
}

.blog-list__item-content .readmore-link {
  text-transform: uppercase;
  position: relative;
  display: inline-block;
  font-weight: 500;
}

.blog-list__item-content .readmore-link:after {
  content: '';
  display: block;
  width: 70%;
  border-bottom: 2px solid;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.blog-list__item-content .readmore-link:hover:after {
  width: 100%;
}

.blog-single .page-title {
  margin-bottom: 0.875rem;
}

.blog-single__reviews-title {
  font-size: 1.125rem;
  margin-bottom: 1.75rem;
}

.blog-single__reviews-list {
  display: flex;
  flex-direction: column;
  gap: 1.87rem;
  margin-bottom: 2.375rem;
}

.blog-single__reviews-item {
  display: flex;
  gap: 1.875rem;
  border-bottom: 1px solid #e4e4e4;
}

.blog-single__reviews-item:last-child {
  border-bottom: 0;
}

.blog-single__reviews-item .customer-avatar {
  flex: 0 0 3.75rem;
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 2rem;
  overflow: hidden;
}

.blog-single__reviews-item .customer-avatar>img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.blog-single__reviews-item .customer-review .customer-name {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.blog-single__reviews-item .customer-review .customer-name>h6,
.blog-single__reviews-item .customer-review .customer-name>.h6 {
  margin: 0;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
}

.blog-single__reviews-item .customer-review .review-date {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.25rem;
}

.blog-single__reviews-item .customer-review .review-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.5rem;
}

.blog-single__review-form form>h5,
.blog-single__review-form form>.h5 {
  font-size: 1.125rem;
  margin-bottom: 0.375rem;
}

.blog-single__review-form form>p {
  font-size: 0.875rem;
  color: #767676;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.blog-single__review-form form .select-star-rating {
  margin-bottom: 2rem;
}

.blog-single__review-form form button {
  text-transform: uppercase;
  font-size: 0.875rem;
  min-width: 12.5rem;
  height: 3.75rem;
}

.blog-single__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 2.625rem;
}

.blog-single__item-pagination {
  padding-top: 2.8125rem;
  border-top: 1px solid #e4e4e4;
  border-bottom: 1px solid #e4e4e4;
  margin-bottom: 3.125rem;
}

.blog-single__item-pagination p {
  margin-bottom: 2.625rem !important;
}

.blog-single__item-pagination a {
  color: #767676;
}

.blog-single p {
  margin-bottom: 1.875rem;
}

.blog-single p img {
  margin-bottom: 3.25rem;
}

.blog-single h5,
.blog-single .h5 {
  margin-bottom: 1.875rem;
}

.blog-single .text-list {
  margin-bottom: 1.875rem;
}

.blog-single .text-list__item {
  line-height: 1.875rem;
}

.blog-single__item-share {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 3.125rem;
  flex-direction: column;
}

@media (min-width: 992px) {
  .blog-single__item-share {
    flex-direction: row;
  }
}

.blog-single .btn-share {
  width: 13.75rem;
  height: 3.125rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.875rem;
  color: #fff;
  padding: 0;
}

.blog-single .btn-share.btn-facebook {
  background-color: #306199;
}

.blog-single .btn-share.btn-twitter {
  background-color: #26C4F1;
}

.blog-single .btn-share.btn-pinterest {
  background-color: #E82B2D;
}

.blog-single .btn-share.btn-more {
  background-color: #222222;
  font-size: 1.5625rem;
  padding: 0;
  width: 3.125rem;
}

.about-us .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.about-us__content {
  line-height: 1.875rem;
}

.brands-carousel .swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
}

.google-map__wrapper {
  height: 34.375rem;
  position: relative;
}

.google-map__wrapper>div {
  height: 100%;
}

.google-map__marker-detail {
  position: absolute;
  left: 10rem;
  top: 50%;
  transform: translateY(-50%);
  padding: 1.6875rem 1.875rem 1.25rem;
  width: auto;
  height: auto !important;
  background-color: #fff;
  border-radius: 4px;
  transition: all .3s ease;
}

@media (max-width: 767.98px) {
  .google-map__marker-detail {
    display: none;
  }
}

.google-map__marker-detail.hide {
  opacity: 0;
  visibility: hidden;
}

.google-map__marker-detail .btn-close {
  background: none;
  padding: 0;
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
}

.google-map__marker-detail__content a {
  display: none;
}

.contact-us .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.contact-us__form input.form-control {
  height: 3.4375rem;
}

.contact-us__form .btn {
  min-width: 12.5rem;
  height: 3.75rem;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.lookbook .page-title {
  font-size: calc(1.34375rem + 1.125vw);
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

@media (min-width: 1200px) {
  .lookbook .page-title {
    font-size: 2.1875rem;
  }
}

.lookbook-collection__item {
  display: block;
  padding-top: 57.68%;
}

.lookbook-collection__item.size-lg {
  padding-top: 119.7%;
}

.lookbook-collection__item-image {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.lookbook-collection__item-image img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popover-point {
  padding: 1rem;
  border: 0;
  background-color: transparent;
}

.popover-point>span {
  display: block;
  width: 1.5rem;
  height: 1.5rem;
  border: 0.3rem solid #fff;
  background-color: #b9a16b;
  border-radius: 1rem;
}

.popover-point.type2 {
  padding: 0.2rem;
}

@media (min-width: 768px) {
  .popover-point.type2 {
    padding: 1rem;
  }
}

.popover-point.type2>span {
  background-color: #ffffff;
  border-radius: 3rem;
  border: 0;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 0.625rem;
  height: 0.625rem;
  box-shadow: 0 0 0 0.2625rem rgba(255, 255, 255, 0.3);
  font-size: 0.5625rem;
  padding-bottom: 0.05rem;
}

@media (min-width: 768px) {
  .popover-point.type2>span {
    width: 2.625rem;
    height: 2.625rem;
    box-shadow: 0 0 0 0.5625rem rgba(255, 255, 255, 0.3);
    font-size: 1.5625rem;
    padding-bottom: 0.2rem;
  }
}

.popover-point.type3 {
  padding: 0.2rem;
}

@media (min-width: 768px) {
  .popover-point.type3 {
    padding: 1rem;
  }
}

.popover-point.type3>span {
  background-color: #ffffff;
  border-radius: 3rem;
  border: 0;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 0.625rem;
  height: 0.625rem;
  box-shadow: 0 0 0 0.2625rem rgba(255, 255, 255, 0.3);
  font-size: 0.5625rem;
  padding-bottom: 0.05rem;
}

@media (min-width: 768px) {
  .popover-point.type3>span {
    width: 1.75rem;
    height: 1.75rem;
    box-shadow: 0 0 0 0.375rem rgba(255, 255, 255, 0.3);
    font-size: 1.5625rem;
    padding-bottom: 0.2rem;
  }
}

.lookbook-products>h2,
.lookbook-products>.h2 {
  pointer-events: none;
}

.store-location .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.store-location__search {
  position: relative;
  width: 100%;
}

.store-location__search-input {
  padding: 1.25rem 3.875rem 1rem 1.25rem;
  height: 3.75rem;
  border: 1px solid #e4e4e4;
  font-size: 0.875rem;
  width: 100%;
}

.store-location__search-btn {
  position: absolute;
  right: 1.25rem;
  top: 50%;
  transform: translateY(-50%);
  padding: 0;
}

.store-location__search-result__item {
  padding: 1.875rem 0;
  border-top: 1px solid #e4e4e4;
}

.store-location__search-result__item:first-child {
  border-top: 0;
}

.store-location__search-result__item h5,
.store-location__search-result__item .h5 {
  margin-bottom: 0.8125rem;
}

.store-location__search-result__item a {
  font-size: 0.8125rem;
  line-height: 1.5rem;
  display: inline-block;
  position: relative;
  text-transform: uppercase;
  font-weight: 500;
}

.store-location__search-result__item a:after {
  content: '';
  display: block;
  border-bottom: 2px solid;
  width: 0;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.store-location__search-result__item a:hover:after {
  width: 75%;
}

.store-location .google-map__wrapper {
  height: 46.875rem;
  max-height: 100vh;
}

.login-register {
  width: 40.625rem;
  max-width: 100%;
  padding: 0 4.6875rem;
}

@media (max-width: 767.98px) {
  .login-register {
    padding: 0 1rem;
  }
}

.login-register .nav-tabs {
  justify-content: center;
  text-transform: uppercase;
}

.login-register .btn {
  font-size: 0.875rem;
  height: 3.75rem;
  font-weight: 500;
}

.login-register p {
  color: #767676;
}

body.not-found-page {
  background: url(../../images/pattern_bg.png) center no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

body.not-found-page .header {
  background: transparent;
}

.page-not-found {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5rem;
}

.page-not-found .content {
  width: 31.25rem;
  max-width: 100%;
  text-align: center;
}

.page-not-found .content h2,
.page-not-found .content .h2 {
  font-size: calc(1.75rem + 6vw);
  font-weight: 700;
}

@media (min-width: 1200px) {

  .page-not-found .content h2,
  .page-not-found .content .h2 {
    font-size: 6.25rem;
  }
}

.page-not-found .content .btn {
  width: 21.25rem;
  max-width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

body.coming-soon-page {
  background: url(../../images/pattern_bg.png) center no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

body.coming-soon-page .header {
  background: transparent;
}

.coming-soon {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5rem;
}

.coming-soon .content {
  width: 46.875rem;
  max-width: 100%;
  text-align: center;
}

.coming-soon .content h2,
.coming-soon .content .h2 {
  font-size: calc(1.75rem + 6vw);
  font-weight: 700;
  letter-spacing: -0.05em;
}

@media (min-width: 1200px) {

  .coming-soon .content h2,
  .coming-soon .content .h2 {
    font-size: 6.25rem;
  }
}

.coming-soon .content p {
  width: 29.75rem;
  max-width: 100%;
  margin: 0 auto;
}

.coming-soon .js-countdown {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

@media (min-width: 768px) {
  .coming-soon .js-countdown {
    gap: 3.625rem;
  }
}

.coming-soon .js-countdown .countdown-num {
  font-size: 1.875rem;
}

.coming-soon .js-countdown .countdown-word {
  font-size: 1rem;
}

.coming-soon .js-countdown .countdown-unit {
  position: relative;
  min-width: 3.625rem;
}

.coming-soon .js-countdown .countdown-unit:before {
  content: ':';
  display: block;
  position: absolute;
  font-size: 1.875rem;
  left: -1rem;
}

@media (min-width: 768px) {
  .coming-soon .js-countdown .countdown-unit:before {
    left: -2rem;
  }
}

.coming-soon .js-countdown .countdown-unit:first-child:before {
  display: none;
}

.coming-soon .block-newsletter .block-newsletter__form {
  height: 3.75rem;
}

.coming-soon .block-newsletter .block-newsletter__form button {
  font-weight: 400;
  font-size: 0.875rem;
}

.image-banner {
  position: relative;
  min-height: 18.75rem;
  display: flex;
  align-items: center;
}

@media (min-width: 576px) {
  .image-banner {
    min-height: 30rem;
  }
}

@media (min-width: 992px) {
  .image-banner {
    min-height: 43.75rem;
  }
}

.image-banner__content {
  position: relative;
  z-index: 1;
  text-align: center;
}

.image-banner__content h2,
.image-banner__content .h2 {
  font-size: calc(1.5rem + 3vw);
  font-weight: 700;
  text-transform: uppercase;
}

@media (min-width: 1200px) {

  .image-banner__content h2,
  .image-banner__content .h2 {
    font-size: 3.75rem;
  }
}

.category-banner__item {
  position: relative;
}

.category-banner__item-content {
  position: absolute;
  left: 12.2%;
  right: 12.2%;
  bottom: -2.3125rem;
  background-color: white;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1.5rem 2rem;
}

@media (min-width: 1200px) {
  .category-banner__item-content {
    padding: 2.6875rem 2rem 1.625rem;
  }
}

.category-banner__item-content h2,
.category-banner__item-content .h2 {
  margin: 0;
}

.category-banner__item-mark {
  background: #d6001c;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  text-transform: uppercase;
  color: #fff;
  padding: 0.75rem 1rem 0.5rem;
  text-align: center;
  line-height: 1.5;
  position: absolute;
  font-size: 0.9375rem;
  width: 6.25rem;
  height: 6.25rem;
  border-radius: 6.25rem;
  right: 1.875rem;
  top: 1.875rem;
}

.category-masonry__title {
  font-size: calc(1.4375rem + 2.25vw);
  line-height: 1.5;
}

@media (min-width: 1200px) {
  .category-masonry__title {
    font-size: 3.125rem;
  }
}

.category-masonry__item {
  position: relative;
}

.category-masonry__item-category {
  position: absolute;
  left: 0;
  top: 0;
  transform: rotate(-90deg) translate(-100%, -100%);
  transform-origin: left top;
}

.video-banner {
  height: 100vh;
  max-height: 43.75rem;
}

.video-banner:before {
  content: '';
  display: block;
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.btn-video-player {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.5rem;
  height: 2.5rem;
  border: 0.125rem solid;
  border-radius: 4rem;
  padding-left: 0.125rem;
  transition: all .3s ease;
  background-color: transparent;
}

.btn-video-player:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.btn-video-player .flaticon {
  font-size: 1rem;
}

@media (min-width: 768px) {
  .btn-video-player {
    width: 4.375rem;
    height: 4.375rem;
    border: 0.25rem solid;
    padding-left: 0.25rem;
  }

  .btn-video-player .flaticon {
    font-size: 1.25rem;
  }
}

.btn-video-player svg {
  display: block;
}

.btn-video-player svg.btn-pause {
  display: none;
}

.btn-video-player svg.btn-play {
  margin-left: 0.3rem;
}

.btn-video-player.playing svg.btn-play {
  display: none;
}

.btn-video-player.playing svg.btn-pause {
  display: block;
}

/* Style the custom dropdown container */
.custom-dropdown {
  position: relative;
  display: inline-block;
  z-index: 3; /* Set a higher z-index to ensure it appears above other elements */
  text-align: center; /* Center the content horizontally */
}

/* Style the selected option */
.selected-option {
  display: inline-block;
  padding: 15px 15px; /* Adjust the padding as needed */
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 1px;
  cursor: pointer;
  font-size: 14px; /* Adjust the font size as needed */
  white-space: nowrap; /* Prevent text wrapping */
  height: 35px; /* Set a fixed height to maintain consistency */
  line-height: 5px; /* Adjust line-height for vertical centering */
  width: 140px;
}


/* Style the dropdown list */
.dropdown-list {
  list-style: none;
  font-size: 13px; /* Adjust the font size as needed */
  padding: 15px;
  margin: 0;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 1px 1px;
  display: none;
}

/* Style the dropdown list items */
.dropdown-list li {
  padding: 1px;
  cursor: pointer;
}

/* Add a hover effect to the dropdown list items */
.dropdown-list li:hover {
  background-color: #f0f0f0;
}

/* Show the dropdown list on hover */
.custom-dropdown:hover .dropdown-list {
  display: block;
}

/* Brands */
.text-above-image {
  position: relative;
  z-index: 2;
}

.brandimage {
  position: relative;
  z-index: 1;
}

.large-heading {
  font-size: 36px; /* Adjust the font size as needed */
  display: inline;
}

.vision-heading {
  display: inline;
}

.section-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.section-content {
  flex-grow: 1;
  margin-right: 20px; /* Adjust this value as needed */
}

.image-container {
  flex-shrink: 0;
  width: 200px; /* Adjust the width of the image container as needed */
}

.section-image {
  max-width: 100%;
  height: auto;
}
"""

css_block2 = """/*!
 * Bootstrap v5.0.0-beta1 (https://getbootstrap.com/)
 * Copyright 2011-2020 The Bootstrap Authors
 * Copyright 2011-2020 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/main/LICENSE)
 */
/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
:root {
  --bs-blue: #0d6efd;
  --bs-indigo: #6610f2;
  --bs-purple: #6f42c1;
  --bs-pink: #d63384;
  --bs-red: #dc3545;
  --bs-orange: #fd7e14;
  --bs-yellow: #ffc107;
  --bs-green: #198754;
  --bs-teal: #20c997;
  --bs-cyan: #0dcaf0;
  --bs-white: #fff;
  --bs-gray: #6c757d;
  --bs-gray-dark: #343a40;
  --bs-primary: #222222;
  --bs-secondary: #767676;
  --bs-success: #def2d7;
  --bs-info: #cde9f6;
  --bs-warning: #f7f3d7;
  --bs-danger: #ecc8c5;
  --bs-light: #e4e4e4;
  --bs-lighter: #faf9f8;
  --bs-dark: #222222;
  --bs-red: #c32929;
  --bs-beige: #b9a16b;
  --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Liberation Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  --bs-gradient: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

@media (prefers-reduced-motion: no-preference) {
  :root {
    scroll-behavior: smooth;
  }
}

body {
  margin: 0;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

[tabindex="-1"]:focus:not(:focus-visible) {
  outline: 0 !important;
}

hr {
  margin: 1rem 0;
  color: inherit;
  background-color: currentColor;
  border: 0;
  opacity: 0.25;
}

hr:not([size]) {
  height: 1px;
}

h1,
.h1,
h2,
.h2,
h3,
.h3,
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-weight: 500;
  line-height: 1.2;
}

h1,
.h1 {
  font-size: calc(1.5625rem + 3.75vw);
}

@media (min-width: 1200px) {

  h1,
  .h1 {
    font-size: 4.375rem;
  }
}

h2,
.h2 {
  font-size: calc(1.3rem + 0.6vw);
}

@media (min-width: 1200px) {

  h2,
  .h2 {
    font-size: 1.75rem;
  }
}

h3,
.h3 {
  font-size: calc(1.2875rem + 0.45vw);
}

@media (min-width: 1200px) {

  h3,
  .h3 {
    font-size: 1.625rem;
  }
}

h4,
.h4 {
  font-size: 1.25rem;
}

h5,
.h5 {
  font-size: 1.125rem;
}

h6,
.h6 {
  font-size: 1rem;
}

p {
  margin-top: 0;
  margin-bottom: 1rem;
}

abbr[title],
abbr[data-bs-original-title] {
  text-decoration: underline;
  text-decoration: underline dotted;
  cursor: help;
  text-decoration-skip-ink: none;
}

address {
  margin-bottom: 1rem;
  font-style: normal;
  line-height: inherit;
}

ol,
ul {
  padding-left: 2rem;
}

ol,
ul,
dl {
  margin-top: 0;
  margin-bottom: 1rem;
}

ol ol,
ul ul,
ol ul,
ul ol {
  margin-bottom: 0;
}

dt {
  font-weight: 700;
}

dd {
  margin-bottom: .5rem;
  margin-left: 0;
}

blockquote {
  margin: 0 0 1rem;
}

b,
strong {
  font-weight: bolder;
}

small,
.small {
  font-size: 0.875em;
}

mark,
.mark {
  padding: 0.2em;
  background-color: #fcf8e3;
}

sub,
sup {
  position: relative;
  font-size: 0.75em;
  line-height: 0;
  vertical-align: baseline;
}

sub {
  bottom: -.25em;
}

sup {
  top: -.5em;
}

a {
  color: #222222;
  text-decoration: none;
}

a:hover {
  color: #1b1b1b;
}

a:not([href]):not([class]),
a:not([href]):not([class]):hover {
  color: inherit;
  text-decoration: none;
}

pre,
code,
kbd,
samp {
  font-family: var(--bs-font-monospace);
  font-size: 1em;
  direction: ltr
    /* rtl:ignore */
  ;
  unicode-bidi: bidi-override;
}

pre {
  display: block;
  margin-top: 0;
  margin-bottom: 1rem;
  overflow: auto;
  font-size: 0.875em;
}

pre code {
  font-size: inherit;
  color: inherit;
  word-break: normal;
}

code {
  font-size: 0.875em;
  color: #d63384;
  word-wrap: break-word;
}

a>code {
  color: inherit;
}

kbd {
  padding: 0.2rem 0.4rem;
  font-size: 0.875em;
  color: #fff;
  background-color: #222222;
  border-radius: 0.2rem;
}

kbd kbd {
  padding: 0;
  font-size: 1em;
  font-weight: 700;
}

figure {
  margin: 0 0 1rem;
}

img,
svg {
  vertical-align: middle;
}

table {
  caption-side: bottom;
  border-collapse: collapse;
}

caption {
  padding-top: 1.53125rem;
  padding-bottom: 1.53125rem;
  color: #6c757d;
  text-align: left;
}

th {
  font-weight: 500;
  text-align: inherit;
  text-align: -webkit-match-parent;
}

thead,
tbody,
tfoot,
tr,
td,
th {
  border-color: inherit;
  border-style: solid;
  border-width: 0;
}

label {
  display: inline-block;
}

button {
  border-radius: 0;
}

button:focus {
  outline: 0;
}

input,
button,
select,
optgroup,
textarea {
  margin: 0;
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}

button,
select {
  text-transform: none;
}

[role="button"] {
  cursor: pointer;
}

select {
  word-wrap: normal;
}

[list]::-webkit-calendar-picker-indicator {
  display: none;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
  -webkit-appearance: button;
}

button:not(:disabled),
[type="button"]:not(:disabled),
[type="reset"]:not(:disabled),
[type="submit"]:not(:disabled) {
  cursor: pointer;
}

::-moz-focus-inner {
  padding: 0;
  border-style: none;
}

textarea {
  resize: vertical;
}

fieldset {
  min-width: 0;
  padding: 0;
  margin: 0;
  border: 0;
}

legend {
  float: left;
  width: 100%;
  padding: 0;
  margin-bottom: 0.5rem;
  font-size: calc(1.275rem + 0.3vw);
  line-height: inherit;
}

@media (min-width: 1200px) {
  legend {
    font-size: 1.5rem;
  }
}

legend+* {
  clear: left;
}

::-webkit-datetime-edit-fields-wrapper,
::-webkit-datetime-edit-text,
::-webkit-datetime-edit-minute,
::-webkit-datetime-edit-hour-field,
::-webkit-datetime-edit-day-field,
::-webkit-datetime-edit-month-field,
::-webkit-datetime-edit-year-field {
  padding: 0;
}

::-webkit-inner-spin-button {
  height: auto;
}

[type="search"] {
  outline-offset: -2px;
  -webkit-appearance: textfield;
}

/* rtl:raw:
[type="tel"],
[type="url"],
[type="email"],
[type="number"] {
  direction: ltr;
}
*/
::-webkit-search-decoration {
  -webkit-appearance: none;
}

::-webkit-color-swatch-wrapper {
  padding: 0;
}

::file-selector-button {
  font: inherit;
}

::-webkit-file-upload-button {
  font: inherit;
  -webkit-appearance: button;
}

output {
  display: inline-block;
}

iframe {
  border: 0;
}

summary {
  display: list-item;
  cursor: pointer;
}

progress {
  vertical-align: baseline;
}

[hidden] {
  display: none !important;
}

.lead {
  font-size: 1.25rem;
  font-weight: 300;
}

.display-1 {
  font-size: calc(1.625rem + 4.5vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-1 {
    font-size: 5rem;
  }
}

.display-2 {
  font-size: calc(1.575rem + 3.9vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-2 {
    font-size: 4.5rem;
  }
}

.display-3 {
  font-size: calc(1.525rem + 3.3vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-3 {
    font-size: 4rem;
  }
}

.display-4 {
  font-size: calc(1.475rem + 2.7vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-4 {
    font-size: 3.5rem;
  }
}

.display-5 {
  font-size: calc(1.425rem + 2.1vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-5 {
    font-size: 3rem;
  }
}

.display-6 {
  font-size: calc(1.375rem + 1.5vw);
  font-weight: 300;
  line-height: 1.2;
}

@media (min-width: 1200px) {
  .display-6 {
    font-size: 2.5rem;
  }
}

.list-unstyled {
  padding-left: 0;
  list-style: none;
}

.list-inline {
  padding-left: 0;
  list-style: none;
}

.list-inline-item {
  display: inline-block;
}

.list-inline-item:not(:last-child) {
  margin-right: 0.5rem;
}

.initialism {
  font-size: 0.875em;
  text-transform: uppercase;
}

.blockquote {
  margin-bottom: 1rem;
  font-size: 1rem;
}

.blockquote> :last-child {
  margin-bottom: 0;
}

.blockquote-footer {
  margin-top: -1rem;
  margin-bottom: 1rem;
  font-size: 0.875rem;
  color: #6c757d;
}

.blockquote-footer::before {
  content: "\2014\00A0";
}

.img-fluid {
  max-width: 100%;
  height: auto;
}

.img-thumbnail {
  padding: 0.25rem;
  background-color: #fff;
  border: 1px solid #dee2e6;
  border-radius: 0.25rem;
  max-width: 100%;
  height: auto;
}

.figure {
  display: inline-block;
}

.figure-img {
  margin-bottom: 0.5rem;
  line-height: 1;
}

.figure-caption {
  font-size: 0.875em;
  color: #6c757d;
}

.container,
.container-fluid,
.container-sm,
.container-md,
.container-lg,
.container-xl,
.container-xxl {
  width: 100%;
  padding-right: var(--bs-gutter-x, 0.9375rem);
  padding-left: var(--bs-gutter-x, 0.9375rem);
  margin-right: auto;
  margin-left: auto;
}

@media (min-width: 576px) {

  .container,
  .container-sm {
    max-width: 540px;
  }
}

@media (min-width: 768px) {

  .container,
  .container-sm,
  .container-md {
    max-width: 720px;
  }
}

@media (min-width: 992px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg {
    max-width: 960px;
  }
}

@media (min-width: 1200px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl {
    max-width: 1140px;
  }
}

@media (min-width: 1500px) {

  .container,
  .container-sm,
  .container-md,
  .container-lg,
  .container-xl,
  .container-xxl {
    max-width: 1440px;
  }
}

.fade {
  transition: opacity 0.15s linear;
}

@media (prefers-reduced-motion: reduce) {
  .fade {
    transition: none;
  }
}

.fade:not(.show) {
  opacity: 0;
}

.collapse:not(.show) {
  display: none;
}

.collapsing {
  height: 0;
  overflow: hidden;
  transition: height 0.35s ease;
}

@media (prefers-reduced-motion: reduce) {
  .collapsing {
    transition: none;
  }
}

.dropup,
.dropend,
.dropdown,
.dropstart {
  position: relative;
}

.dropdown-toggle {
  white-space: nowrap;
}

.dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid;
  border-right: 0.3em solid transparent;
  border-bottom: 0;
  border-left: 0.3em solid transparent;
}

.dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  min-width: 10rem;
  padding: 0.5rem 0;
  margin: 0.125rem 0 0;
  font-size: 1rem;
  color: #222222;
  text-align: left;
  list-style: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem;
}

.dropdown-menu[style] {
  right: auto !important;
}

.dropdown-menu-start {
  --bs-position: start;
  right: auto
    /* rtl:ignore */
  ;
  left: 0
    /* rtl:ignore */
  ;
}

.dropdown-menu-end {
  --bs-position: end;
  right: 0
    /* rtl:ignore */
  ;
  left: auto
    /* rtl:ignore */
  ;
}

@media (min-width: 576px) {
  .dropdown-menu-sm-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-sm-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 768px) {
  .dropdown-menu-md-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-md-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 992px) {
  .dropdown-menu-lg-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-lg-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1200px) {
  .dropdown-menu-xl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1500px) {
  .dropdown-menu-xxl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xxl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

@media (min-width: 1700px) {
  .dropdown-menu-xxxl-start {
    --bs-position: start;
    right: auto
      /* rtl:ignore */
    ;
    left: 0
      /* rtl:ignore */
    ;
  }

  .dropdown-menu-xxxl-end {
    --bs-position: end;
    right: 0
      /* rtl:ignore */
    ;
    left: auto
      /* rtl:ignore */
    ;
  }
}

.dropup .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-top: 0;
  margin-bottom: 0.125rem;
}

.dropup .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0;
  border-right: 0.3em solid transparent;
  border-bottom: 0.3em solid;
  border-left: 0.3em solid transparent;
}

.dropup .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropend .dropdown-menu {
  top: 0;
  right: auto;
  left: 100%;
  margin-top: 0;
  margin-left: 0.125rem;
}

.dropend .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0;
  border-bottom: 0.3em solid transparent;
  border-left: 0.3em solid;
}

.dropend .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropend .dropdown-toggle::after {
  vertical-align: 0;
}

.dropstart .dropdown-menu {
  top: 0;
  right: 100%;
  left: auto;
  margin-top: 0;
  margin-right: 0.125rem;
}

.dropstart .dropdown-toggle::after {
  display: inline-block;
  margin-left: 0.255em;
  vertical-align: 0.255em;
  content: "";
}

.dropstart .dropdown-toggle::after {
  display: none;
}

.dropstart .dropdown-toggle::before {
  display: inline-block;
  margin-right: 0.255em;
  vertical-align: 0.255em;
  content: "";
  border-top: 0.3em solid transparent;
  border-right: 0.3em solid;
  border-bottom: 0.3em solid transparent;
}

.dropstart .dropdown-toggle:empty::after {
  margin-left: 0;
}

.dropstart .dropdown-toggle::before {
  vertical-align: 0;
}

.dropdown-divider {
  height: 0;
  margin: 0.5rem 0;
  overflow: hidden;
  border-top: 1px solid rgba(0, 0, 0, 0.15);
}

.dropdown-item {
  display: block;
  width: 100%;
  padding: 0.25rem 1rem;
  clear: both;
  font-weight: 400;
  color: #222222;
  text-align: inherit;
  white-space: nowrap;
  background-color: transparent;
  border: 0;
}

.dropdown-item:hover,
.dropdown-item:focus {
  color: #1f1f1f;
  background-color: #f8f9fa;
}

.dropdown-item.active,
.dropdown-item:active {
  color: #fff;
  text-decoration: none;
  background-color: #222222;
}

.dropdown-item.disabled,
.dropdown-item:disabled {
  color: #6c757d;
  pointer-events: none;
  background-color: transparent;
}

.dropdown-menu.show {
  display: block;
}

.dropdown-header {
  display: block;
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  color: #6c757d;
  white-space: nowrap;
}

.dropdown-item-text {
  display: block;
  padding: 0.25rem 1rem;
  color: #222222;
}

.dropdown-menu-dark {
  color: #dee2e6;
  background-color: #343a40;
  border-color: rgba(0, 0, 0, 0.15);
}

.dropdown-menu-dark .dropdown-item {
  color: #dee2e6;
}

.dropdown-menu-dark .dropdown-item:hover,
.dropdown-menu-dark .dropdown-item:focus {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.15);
}

.dropdown-menu-dark .dropdown-item.active,
.dropdown-menu-dark .dropdown-item:active {
  color: #fff;
  background-color: #222222;
}

.dropdown-menu-dark .dropdown-item.disabled,
.dropdown-menu-dark .dropdown-item:disabled {
  color: #adb5bd;
}

.dropdown-menu-dark .dropdown-divider {
  border-color: rgba(0, 0, 0, 0.15);
}

.dropdown-menu-dark .dropdown-item-text {
  color: #dee2e6;
}

.dropdown-menu-dark .dropdown-header {
  color: #adb5bd;
}

.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-flex;
  vertical-align: middle;
}

.btn-group>.btn,
.btn-group-vertical>.btn {
  position: relative;
  flex: 1 1 auto;
}

.btn-group>.btn-check:checked+.btn,
.btn-group>.btn-check:focus+.btn,
.btn-group>.btn:hover,
.btn-group>.btn:focus,
.btn-group>.btn:active,
.btn-group>.btn.active,
.btn-group-vertical>.btn-check:checked+.btn,
.btn-group-vertical>.btn-check:focus+.btn,
.btn-group-vertical>.btn:hover,
.btn-group-vertical>.btn:focus,
.btn-group-vertical>.btn:active,
.btn-group-vertical>.btn.active {
  z-index: 1;
}

.btn-toolbar {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.btn-toolbar .input-group {
  width: auto;
}

.btn-group>.btn:not(:first-child),
.btn-group>.btn-group:not(:first-child) {
  margin-left: -1px;
}

.btn-group>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group>.btn-group:not(:last-child)>.btn {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.btn-group>.btn:nth-child(n + 3),
.btn-group> :not(.btn-check)+.btn,
.btn-group>.btn-group:not(:first-child)>.btn {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.dropdown-toggle-split {
  padding-right: 2.34375rem;
  padding-left: 2.34375rem;
}

.dropdown-toggle-split::after,
.dropup .dropdown-toggle-split::after,
.dropend .dropdown-toggle-split::after {
  margin-left: 0;
}

.dropstart .dropdown-toggle-split::before {
  margin-right: 0;
}

.btn-sm+.dropdown-toggle-split,
.btn-group-sm>.btn+.dropdown-toggle-split {
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
}

.btn-lg+.dropdown-toggle-split,
.btn-group-lg>.btn+.dropdown-toggle-split {
  padding-right: 0.9375rem;
  padding-left: 0.9375rem;
}

.btn-group-vertical {
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.btn-group-vertical>.btn,
.btn-group-vertical>.btn-group {
  width: 100%;
}

.btn-group-vertical>.btn:not(:first-child),
.btn-group-vertical>.btn-group:not(:first-child) {
  margin-top: -1px;
}

.btn-group-vertical>.btn:not(:last-child):not(.dropdown-toggle),
.btn-group-vertical>.btn-group:not(:last-child)>.btn {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.btn-group-vertical>.btn~.btn,
.btn-group-vertical>.btn-group:not(:first-child)>.btn {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.navbar {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.navbar>.container,
.navbar>.container-fluid,
.navbar>.container-sm,
.navbar>.container-md,
.navbar>.container-lg,
.navbar>.container-xl,
.navbar>.container-xxl {
  display: flex;
  flex-wrap: inherit;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  padding-top: 0.3125rem;
  padding-bottom: 0.3125rem;
  margin-right: 1rem;
  font-size: 1.25rem;
  white-space: nowrap;
}

.navbar-nav {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.navbar-nav .nav-link {
  padding-right: 0;
  padding-left: 0;
}

.navbar-nav .dropdown-menu {
  position: static;
}

.navbar-text {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.navbar-collapse {
  align-items: center;
  width: 100%;
}

.navbar-toggler {
  padding: 0.25rem 0.75rem;
  font-size: 1.25rem;
  line-height: 1;
  background-color: transparent;
  border: 1px solid transparent;
  border-radius: 0.25rem;
  transition: box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .navbar-toggler {
    transition: none;
  }
}

.navbar-toggler:hover {
  text-decoration: none;
}

.navbar-toggler:focus {
  text-decoration: none;
  outline: 0;
  box-shadow: 0 0 0 0.25rem;
}

.navbar-toggler-icon {
  display: inline-block;
  width: 1.5em;
  height: 1.5em;
  vertical-align: middle;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100%;
}

@media (min-width: 576px) {
  .navbar-expand-sm {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-sm .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-sm .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-sm .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-sm .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-sm .navbar-toggler {
    display: none;
  }
}

@media (min-width: 768px) {
  .navbar-expand-md {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-md .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-md .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-md .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-md .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-md .navbar-toggler {
    display: none;
  }
}

@media (min-width: 992px) {
  .navbar-expand-lg {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-lg .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-lg .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-lg .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-lg .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-lg .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1200px) {
  .navbar-expand-xl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xl .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1500px) {
  .navbar-expand-xxl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xxl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xxl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xxl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xxl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xxl .navbar-toggler {
    display: none;
  }
}

@media (min-width: 1700px) {
  .navbar-expand-xxxl {
    flex-wrap: nowrap;
    justify-content: flex-start;
  }

  .navbar-expand-xxxl .navbar-nav {
    flex-direction: row;
  }

  .navbar-expand-xxxl .navbar-nav .dropdown-menu {
    position: absolute;
  }

  .navbar-expand-xxxl .navbar-nav .nav-link {
    padding-right: 0.5rem;
    padding-left: 0.5rem;
  }

  .navbar-expand-xxxl .navbar-collapse {
    display: flex !important;
  }

  .navbar-expand-xxxl .navbar-toggler {
    display: none;
  }
}

.navbar-expand {
  flex-wrap: nowrap;
  justify-content: flex-start;
}

.navbar-expand .navbar-nav {
  flex-direction: row;
}

.navbar-expand .navbar-nav .dropdown-menu {
  position: absolute;
}

.navbar-expand .navbar-nav .nav-link {
  padding-right: 0.5rem;
  padding-left: 0.5rem;
}

.navbar-expand .navbar-collapse {
  display: flex !important;
}

.navbar-expand .navbar-toggler {
  display: none;
}

.navbar-light .navbar-brand {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-brand:hover,
.navbar-light .navbar-brand:focus {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-nav .nav-link {
  color: rgba(0, 0, 0, 0.55);
}

.navbar-light .navbar-nav .nav-link:hover,
.navbar-light .navbar-nav .nav-link:focus {
  color: rgba(0, 0, 0, 0.7);
}

.navbar-light .navbar-nav .nav-link.disabled {
  color: rgba(0, 0, 0, 0.3);
}

.navbar-light .navbar-nav .show>.nav-link,
.navbar-light .navbar-nav .nav-link.active {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-light .navbar-toggler {
  color: rgba(0, 0, 0, 0.55);
  border-color: rgba(0, 0, 0, 0.1);
}

.navbar-light .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%280, 0, 0, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-light .navbar-text {
  color: rgba(0, 0, 0, 0.55);
}

.navbar-light .navbar-text a,
.navbar-light .navbar-text a:hover,
.navbar-light .navbar-text a:focus {
  color: rgba(0, 0, 0, 0.9);
}

.navbar-dark .navbar-brand {
  color: #fff;
}

.navbar-dark .navbar-brand:hover,
.navbar-dark .navbar-brand:focus {
  color: #fff;
}

.navbar-dark .navbar-nav .nav-link {
  color: rgba(255, 255, 255, 0.55);
}

.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus {
  color: rgba(255, 255, 255, 0.75);
}

.navbar-dark .navbar-nav .nav-link.disabled {
  color: rgba(255, 255, 255, 0.25);
}

.navbar-dark .navbar-nav .show>.nav-link,
.navbar-dark .navbar-nav .nav-link.active {
  color: #fff;
}

.navbar-dark .navbar-toggler {
  color: rgba(255, 255, 255, 0.55);
  border-color: rgba(255, 255, 255, 0.1);
}

.navbar-dark .navbar-toggler-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28255, 255, 255, 0.55%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-dark .navbar-text {
  color: rgba(255, 255, 255, 0.55);
}

.navbar-dark .navbar-text a,
.navbar-dark .navbar-text a:hover,
.navbar-dark .navbar-text a:focus {
  color: #fff;
}

.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}

.card>hr {
  margin-right: 0;
  margin-left: 0;
}

.card>.list-group {
  border-top: inherit;
  border-bottom: inherit;
}

.card>.list-group:first-child {
  border-top-width: 0;
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.card>.list-group:last-child {
  border-bottom-width: 0;
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card>.card-header+.list-group,
.card>.list-group+.card-footer {
  border-top: 0;
}

.card-body {
  flex: 1 1 auto;
  padding: 1rem 1rem;
}

.card-title {
  margin-bottom: 0.5rem;
}

.card-subtitle {
  margin-top: -0.25rem;
  margin-bottom: 0;
}

.card-text:last-child {
  margin-bottom: 0;
}

.card-link:hover {
  text-decoration: none;
}

.card-link+.card-link {
  margin-left: 1rem
    /* rtl:ignore */
  ;
}

.card-header {
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  background-color: rgba(0, 0, 0, 0.03);
  border-bottom: 1px solid rgba(0, 0, 0, 0.125);
}

.card-header:first-child {
  border-radius: calc(0.25rem - 1px) calc(0.25rem - 1px) 0 0;
}

.card-footer {
  padding: 0.5rem 1rem;
  background-color: rgba(0, 0, 0, 0.03);
  border-top: 1px solid rgba(0, 0, 0, 0.125);
}

.card-footer:last-child {
  border-radius: 0 0 calc(0.25rem - 1px) calc(0.25rem - 1px);
}

.card-header-tabs {
  margin-right: -0.5rem;
  margin-bottom: -0.5rem;
  margin-left: -0.5rem;
  border-bottom: 0;
}

.card-header-pills {
  margin-right: -0.5rem;
  margin-left: -0.5rem;
}

.card-img-overlay {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  padding: 1rem;
  border-radius: calc(0.25rem - 1px);
}

.card-img,
.card-img-top,
.card-img-bottom {
  width: 100%;
}

.card-img,
.card-img-top {
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.card-img,
.card-img-bottom {
  border-bottom-right-radius: calc(0.25rem - 1px);
  border-bottom-left-radius: calc(0.25rem - 1px);
}

.card-group>.card {
  margin-bottom: 0.75rem;
}

@media (min-width: 576px) {
  .card-group {
    display: flex;
    flex-flow: row wrap;
  }

  .card-group>.card {
    flex: 1 0 0%;
    margin-bottom: 0;
  }

  .card-group>.card+.card {
    margin-left: 0;
    border-left: 0;
  }

  .card-group>.card:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  .card-group>.card:not(:last-child) .card-img-top,
  .card-group>.card:not(:last-child) .card-header {
    border-top-right-radius: 0;
  }

  .card-group>.card:not(:last-child) .card-img-bottom,
  .card-group>.card:not(:last-child) .card-footer {
    border-bottom-right-radius: 0;
  }

  .card-group>.card:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  .card-group>.card:not(:first-child) .card-img-top,
  .card-group>.card:not(:first-child) .card-header {
    border-top-left-radius: 0;
  }

  .card-group>.card:not(:first-child) .card-img-bottom,
  .card-group>.card:not(:first-child) .card-footer {
    border-bottom-left-radius: 0;
  }
}

.accordion-button {
  position: relative;
  display: flex;
  align-items: center;
  width: 100%;
  border-radius: 0;
  overflow-anchor: none;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out, border-radius 0.15s ease;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button {
    transition: none;
  }
}

.accordion-button::after {
  flex-shrink: 0;
  margin-left: auto;
  content: "";
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
  transform: rotate(90deg);
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button::after {
    transition: none;
  }
}

.accordion-button.collapsed {
  border-bottom-width: 0;
}

.accordion-button:hover {
  z-index: 2;
}

.accordion-button:focus {
  z-index: 3;
  outline: 0;
}

.accordion-header {
  margin-bottom: 0;
}

.accordion-item:last-of-type .accordion-button.collapsed {
  border-bottom-width: 1px;
}

.accordion-item:last-of-type .accordion-collapse {
  border-bottom-width: 1px;
}

.accordion-collapse {
  border: solid #eeeeee;
  border-width: 0 1px;
}

.accordion-flush .accordion-button {
  border-right: 0;
  border-left: 0;
  border-radius: 0;
}

.accordion-flush .accordion-collapse {
  border-width: 0;
}

.accordion-flush .accordion-item:first-of-type .accordion-button {
  border-top-width: 0;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.accordion-flush .accordion-item:last-of-type .accordion-button.collapsed {
  border-bottom-width: 0;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  padding: 0 0;
  margin-bottom: 1rem;
  list-style: none;
}

.breadcrumb-item+.breadcrumb-item {
  padding-left: 0.5rem;
}

.breadcrumb-item+.breadcrumb-item::before {
  float: left;
  padding-right: 0.5rem;
  color: #6c757d;
  content: var(--bs-breadcrumb-divider, "/")
    /* rtl: var(--bs-breadcrumb-divider, "/") */
  ;
}

.breadcrumb-item.active {
  color: #6c757d;
}

.pagination {
  display: flex;
  padding-left: 0;
  list-style: none;
}

.page-link {
  position: relative;
  display: block;
  color: #222222;
  background-color: #fff;
  border: 1px solid #dee2e6;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .page-link {
    transition: none;
  }
}

.page-link:hover {
  z-index: 2;
  color: #1b1b1b;
  background-color: #e9ecef;
  border-color: #dee2e6;
}

.page-link:focus {
  z-index: 3;
  color: #1b1b1b;
  background-color: #e9ecef;
  outline: 0;
  box-shadow: none;
}

.page-item:not(:first-child) .page-link {
  margin-left: -1px;
}

.page-item.active .page-link {
  z-index: 3;
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.page-item.disabled .page-link {
  color: #6c757d;
  pointer-events: none;
  background-color: #fff;
  border-color: #dee2e6;
}

.page-link {
  padding: 0.375rem 0.75rem;
}

.page-item:first-child .page-link {
  border-top-left-radius: 0.25rem;
  border-bottom-left-radius: 0.25rem;
}

.page-item:last-child .page-link {
  border-top-right-radius: 0.25rem;
  border-bottom-right-radius: 0.25rem;
}

.pagination-lg .page-link {
  padding: 0.75rem 1.5rem;
  font-size: 1.25rem;
}

.pagination-lg .page-item:first-child .page-link {
  border-top-left-radius: 0.3rem;
  border-bottom-left-radius: 0.3rem;
}

.pagination-lg .page-item:last-child .page-link {
  border-top-right-radius: 0.3rem;
  border-bottom-right-radius: 0.3rem;
}

.pagination-sm .page-link {
  padding: 0.25rem 0.5rem;
  font-size: 0.875rem;
}

.pagination-sm .page-item:first-child .page-link {
  border-top-left-radius: 0.2rem;
  border-bottom-left-radius: 0.2rem;
}

.pagination-sm .page-item:last-child .page-link {
  border-top-right-radius: 0.2rem;
  border-bottom-right-radius: 0.2rem;
}

.badge {
  display: inline-block;
  padding: 0.35em 0.65em;
  font-size: 0.75em;
  font-weight: 700;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: 0.25rem;
}

.badge:empty {
  display: none;
}

.btn .badge {
  position: relative;
  top: -1px;
}

@keyframes progress-bar-stripes {
  0% {
    background-position-x: 1rem;
  }
}

.progress {
  display: flex;
  height: 1rem;
  overflow: hidden;
  font-size: 0.875rem;
  background-color: #e9ecef;
  border-radius: 0.25rem;
}

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  background-color: #222222;
  transition: width 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
  .progress-bar {
    transition: none;
  }
}

.progress-bar-striped {
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 1rem 1rem;
}

.progress-bar-animated {
  animation: 1s linear infinite progress-bar-stripes;
}

@media (prefers-reduced-motion: reduce) {
  .progress-bar-animated {
    animation: none;
  }
}

.list-group {
  display: flex;
  flex-direction: column;
  padding-left: 0;
  margin-bottom: 0;
  border-radius: 0.25rem;
}

.list-group-item-action {
  width: 100%;
  color: #495057;
  text-align: inherit;
}

.list-group-item-action:hover,
.list-group-item-action:focus {
  z-index: 1;
  color: #495057;
  text-decoration: none;
  background-color: #f8f9fa;
}

.list-group-item-action:active {
  color: #222222;
  background-color: #e9ecef;
}

.list-group-item {
  position: relative;
  display: block;
  padding: 0.5rem 1rem;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.125);
}

.list-group-item:first-child {
  border-top-left-radius: inherit;
  border-top-right-radius: inherit;
}

.list-group-item:last-child {
  border-bottom-right-radius: inherit;
  border-bottom-left-radius: inherit;
}

.list-group-item.disabled,
.list-group-item:disabled {
  color: #6c757d;
  pointer-events: none;
  background-color: #fff;
}

.list-group-item.active {
  z-index: 2;
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.list-group-item+.list-group-item {
  border-top-width: 0;
}

.list-group-item+.list-group-item.active {
  margin-top: -1px;
  border-top-width: 1px;
}

.list-group-horizontal {
  flex-direction: row;
}

.list-group-horizontal>.list-group-item:first-child {
  border-bottom-left-radius: 0.25rem;
  border-top-right-radius: 0;
}

.list-group-horizontal>.list-group-item:last-child {
  border-top-right-radius: 0.25rem;
  border-bottom-left-radius: 0;
}

.list-group-horizontal>.list-group-item.active {
  margin-top: 0;
}

.list-group-horizontal>.list-group-item+.list-group-item {
  border-top-width: 1px;
  border-left-width: 0;
}

.list-group-horizontal>.list-group-item+.list-group-item.active {
  margin-left: -1px;
  border-left-width: 1px;
}

@media (min-width: 576px) {
  .list-group-horizontal-sm {
    flex-direction: row;
  }

  .list-group-horizontal-sm>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-sm>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-sm>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-sm>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-sm>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 768px) {
  .list-group-horizontal-md {
    flex-direction: row;
  }

  .list-group-horizontal-md>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-md>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-md>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-md>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-md>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 992px) {
  .list-group-horizontal-lg {
    flex-direction: row;
  }

  .list-group-horizontal-lg>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-lg>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-lg>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-lg>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-lg>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1200px) {
  .list-group-horizontal-xl {
    flex-direction: row;
  }

  .list-group-horizontal-xl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1500px) {
  .list-group-horizontal-xxl {
    flex-direction: row;
  }

  .list-group-horizontal-xxl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xxl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xxl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xxl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xxl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

@media (min-width: 1700px) {
  .list-group-horizontal-xxxl {
    flex-direction: row;
  }

  .list-group-horizontal-xxxl>.list-group-item:first-child {
    border-bottom-left-radius: 0.25rem;
    border-top-right-radius: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item:last-child {
    border-top-right-radius: 0.25rem;
    border-bottom-left-radius: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item.active {
    margin-top: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item+.list-group-item {
    border-top-width: 1px;
    border-left-width: 0;
  }

  .list-group-horizontal-xxxl>.list-group-item+.list-group-item.active {
    margin-left: -1px;
    border-left-width: 1px;
  }
}

.list-group-flush {
  border-radius: 0;
}

.list-group-flush>.list-group-item {
  border-width: 0 0 1px;
}

.list-group-flush>.list-group-item:last-child {
  border-bottom-width: 0;
}

.list-group-item-primary {
  color: #141414;
  background-color: lightgray;
}

.list-group-item-primary.list-group-item-action:hover,
.list-group-item-primary.list-group-item-action:focus {
  color: #141414;
  background-color: #bebebe;
}

.list-group-item-primary.list-group-item-action.active {
  color: #fff;
  background-color: #141414;
  border-color: #141414;
}

.list-group-item-secondary {
  color: #474747;
  background-color: #e4e4e4;
}

.list-group-item-secondary.list-group-item-action:hover,
.list-group-item-secondary.list-group-item-action:focus {
  color: #474747;
  background-color: #cdcdcd;
}

.list-group-item-secondary.list-group-item-action.active {
  color: #fff;
  background-color: #474747;
  border-color: #474747;
}

.list-group-item-success {
  color: #596156;
  background-color: #f8fcf7;
}

.list-group-item-success.list-group-item-action:hover,
.list-group-item-success.list-group-item-action:focus {
  color: #596156;
  background-color: #dfe3de;
}

.list-group-item-success.list-group-item-action.active {
  color: #fff;
  background-color: #596156;
  border-color: #596156;
}

.list-group-item-info {
  color: #525d62;
  background-color: #f5fbfd;
}

.list-group-item-info.list-group-item-action:hover,
.list-group-item-info.list-group-item-action:focus {
  color: #525d62;
  background-color: #dde2e4;
}

.list-group-item-info.list-group-item-action.active {
  color: #fff;
  background-color: #525d62;
  border-color: #525d62;
}

.list-group-item-warning {
  color: #636156;
  background-color: #fdfdf7;
}

.list-group-item-warning.list-group-item-action:hover,
.list-group-item-warning.list-group-item-action:focus {
  color: #636156;
  background-color: #e4e4de;
}

.list-group-item-warning.list-group-item-action.active {
  color: #fff;
  background-color: #636156;
  border-color: #636156;
}

.list-group-item-danger {
  color: #5e504f;
  background-color: #fbf4f3;
}

.list-group-item-danger.list-group-item-action:hover,
.list-group-item-danger.list-group-item-action:focus {
  color: #5e504f;
  background-color: #e2dcdb;
}

.list-group-item-danger.list-group-item-action.active {
  color: #fff;
  background-color: #5e504f;
  border-color: #5e504f;
}

.list-group-item-light {
  color: #5b5b5b;
  background-color: #fafafa;
}

.list-group-item-light.list-group-item-action:hover,
.list-group-item-light.list-group-item-action:focus {
  color: #5b5b5b;
  background-color: #e1e1e1;
}

.list-group-item-light.list-group-item-action.active {
  color: #fff;
  background-color: #5b5b5b;
  border-color: #5b5b5b;
}

.list-group-item-lighter {
  color: #646463;
  background-color: #fefefe;
}

.list-group-item-lighter.list-group-item-action:hover,
.list-group-item-lighter.list-group-item-action:focus {
  color: #646463;
  background-color: #e5e5e5;
}

.list-group-item-lighter.list-group-item-action.active {
  color: #fff;
  background-color: #646463;
  border-color: #646463;
}

.list-group-item-dark {
  color: #141414;
  background-color: lightgray;
}

.list-group-item-dark.list-group-item-action:hover,
.list-group-item-dark.list-group-item-action:focus {
  color: #141414;
  background-color: #bebebe;
}

.list-group-item-dark.list-group-item-action.active {
  color: #fff;
  background-color: #141414;
  border-color: #141414;
}

.list-group-item-red {
  color: #751919;
  background-color: #f3d4d4;
}

.list-group-item-red.list-group-item-action:hover,
.list-group-item-red.list-group-item-action:focus {
  color: #751919;
  background-color: #dbbfbf;
}

.list-group-item-red.list-group-item-action.active {
  color: #fff;
  background-color: #751919;
  border-color: #751919;
}

.list-group-item-beige {
  color: #6f6140;
  background-color: #f1ece1;
}

.list-group-item-beige.list-group-item-action:hover,
.list-group-item-beige.list-group-item-action:focus {
  color: #6f6140;
  background-color: #d9d4cb;
}

.list-group-item-beige.list-group-item-action.active {
  color: #fff;
  background-color: #6f6140;
  border-color: #6f6140;
}

.toast {
  width: 350px;
  max-width: 100%;
  font-size: 0.875rem;
  pointer-events: auto;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.1);
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  border-radius: 0.25rem;
}

.toast:not(.showing):not(.show) {
  opacity: 0;
}

.toast.hide {
  display: none;
}

.toast-container {
  width: max-content;
  max-width: 100%;
  pointer-events: none;
}

.toast-container> :not(:last-child) {
  margin-bottom: 0.75rem;
}

.toast-header {
  display: flex;
  align-items: center;
  padding: 0.5rem 0.75rem;
  color: #6c757d;
  background-color: rgba(255, 255, 255, 0.85);
  background-clip: padding-box;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  border-top-left-radius: calc(0.25rem - 1px);
  border-top-right-radius: calc(0.25rem - 1px);
}

.toast-header .btn-close {
  margin-right: -0.375rem;
  margin-left: 0.75rem;
}

.toast-body {
  padding: 0.75rem;
}

.modal-open {
  overflow: hidden;
}

.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  display: none;
  width: 100%;
  height: 100%;
  overflow: hidden;
  outline: 0;
}

.modal-dialog {
  position: relative;
  width: auto;
  margin: 0.5rem;
  pointer-events: none;
}

.modal.fade .modal-dialog {
  transition: transform 0.3s ease-out;
  transform: translate(0, -50px);
}

@media (prefers-reduced-motion: reduce) {
  .modal.fade .modal-dialog {
    transition: none;
  }
}

.modal.show .modal-dialog {
  transform: none;
}

.modal.modal-static .modal-dialog {
  transform: scale(1.02);
}

.modal-dialog-scrollable {
  height: calc(100% - 1rem);
}

.modal-dialog-scrollable .modal-content {
  max-height: 100%;
  overflow: hidden;
}

.modal-dialog-scrollable .modal-body {
  overflow-y: auto;
}

.modal-dialog-centered {
  display: flex;
  align-items: center;
  min-height: calc(100% - 1rem);
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  pointer-events: auto;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
  outline: 0;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1040;
  width: 100vw;
  height: 100vh;
  background-color: #000;
}

.modal-backdrop.fade {
  opacity: 0;
}

.modal-backdrop.show {
  opacity: 0.5;
}

.modal-header {
  display: flex;
  flex-shrink: 0;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 2.5rem;
  border-bottom: 1px solid #dee2e6;
  border-top-left-radius: calc(0.3rem - 1px);
  border-top-right-radius: calc(0.3rem - 1px);
}

.modal-header .btn-close {
  padding: 0.75rem 1.25rem;
  margin: -0.75rem -1.25rem -0.75rem auto;
}

.modal-title {
  margin-bottom: 0;
  line-height: 1.5;
}

.modal-body {
  position: relative;
  flex: 1 1 auto;
  padding: 1.875rem 2.5rem;
}

.modal-footer {
  display: flex;
  flex-wrap: wrap;
  flex-shrink: 0;
  align-items: center;
  justify-content: flex-end;
  padding: 1.875rem 2.5rem-0.25rem;
  border-top: 1px solid #dee2e6;
  border-bottom-right-radius: calc(0.3rem - 1px);
  border-bottom-left-radius: calc(0.3rem - 1px);
}

.modal-footer>* {
  margin: 0.25rem;
}

.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 500px;
    margin: 1.75rem auto;
  }

  .modal-dialog-scrollable {
    height: calc(100% - 3.5rem);
  }

  .modal-dialog-centered {
    min-height: calc(100% - 3.5rem);
  }

  .modal-sm {
    max-width: 300px;
  }
}

@media (min-width: 992px) {

  .modal-lg,
  .modal-xl {
    max-width: 800px;
  }
}

@media (min-width: 1200px) {
  .modal-xl {
    max-width: 1140px;
  }
}

.modal-fullscreen {
  width: 100vw;
  max-width: none;
  height: 100%;
  margin: 0;
}

.modal-fullscreen .modal-content {
  height: 100%;
  border: 0;
  border-radius: 0;
}

.modal-fullscreen .modal-header {
  border-radius: 0;
}

.modal-fullscreen .modal-body {
  overflow-y: auto;
}

.modal-fullscreen .modal-footer {
  border-radius: 0;
}

@media (max-width: 575.98px) {
  .modal-fullscreen-sm-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-sm-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-sm-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-sm-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-sm-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 767.98px) {
  .modal-fullscreen-md-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-md-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-md-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-md-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-md-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 991.98px) {
  .modal-fullscreen-lg-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-lg-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-lg-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-lg-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-lg-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1199.98px) {
  .modal-fullscreen-xl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xl-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1499.98px) {
  .modal-fullscreen-xxl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xxl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xxl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xxl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xxl-down .modal-footer {
    border-radius: 0;
  }
}

@media (max-width: 1699.98px) {
  .modal-fullscreen-xxxl-down {
    width: 100vw;
    max-width: none;
    height: 100%;
    margin: 0;
  }

  .modal-fullscreen-xxxl-down .modal-content {
    height: 100%;
    border: 0;
    border-radius: 0;
  }

  .modal-fullscreen-xxxl-down .modal-header {
    border-radius: 0;
  }

  .modal-fullscreen-xxxl-down .modal-body {
    overflow-y: auto;
  }

  .modal-fullscreen-xxxl-down .modal-footer {
    border-radius: 0;
  }
}

.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  margin: 0;
  font-family: "Jost", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.7143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.8125rem;
  word-wrap: break-word;
  opacity: 0;
}

.tooltip.show {
  opacity: 1;
}

.tooltip .tooltip-arrow {
  position: absolute;
  display: block;
  width: 0.8rem;
  height: 0.4rem;
}

.tooltip .tooltip-arrow::before {
  position: absolute;
  content: "";
  border-color: transparent;
  border-style: solid;
}

.bs-tooltip-top,
.bs-tooltip-auto[data-popper-placement^="top"] {
  padding: 0.4rem 0;
}

.bs-tooltip-top .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="top"] .tooltip-arrow {
  bottom: 0;
}

.bs-tooltip-top .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="top"] .tooltip-arrow::before {
  top: -1px;
  border-width: 0.4rem 0.4rem 0;
  border-top-color: #000;
}

.bs-tooltip-end,
.bs-tooltip-auto[data-popper-placement^="right"] {
  padding: 0 0.4rem;
}

.bs-tooltip-end .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="right"] .tooltip-arrow {
  left: 0;
  width: 0.4rem;
  height: 0.8rem;
}

.bs-tooltip-end .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="right"] .tooltip-arrow::before {
  right: -1px;
  border-width: 0.4rem 0.4rem 0.4rem 0;
  border-right-color: #000;
}

.bs-tooltip-bottom,
.bs-tooltip-auto[data-popper-placement^="bottom"] {
  padding: 0.4rem 0;
}

.bs-tooltip-bottom .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-arrow {
  top: 0;
}

.bs-tooltip-bottom .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-arrow::before {
  bottom: -1px;
  border-width: 0 0.4rem 0.4rem;
  border-bottom-color: #000;
}

.bs-tooltip-start,
.bs-tooltip-auto[data-popper-placement^="left"] {
  padding: 0 0.4rem;
}

.bs-tooltip-start .tooltip-arrow,
.bs-tooltip-auto[data-popper-placement^="left"] .tooltip-arrow {
  right: 0;
  width: 0.4rem;
  height: 0.8rem;
}

.bs-tooltip-start .tooltip-arrow::before,
.bs-tooltip-auto[data-popper-placement^="left"] .tooltip-arrow::before {
  left: -1px;
  border-width: 0.4rem 0 0.4rem 0.4rem;
  border-left-color: #000;
}

.tooltip-inner {
  max-width: 200px;
  padding: 0.25rem 0.5rem;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 0.25rem;
}

.popover {
  position: absolute;
  top: 0;
  left: 0
    /* rtl:ignore */
  ;
  z-index: 1060;
  display: block;
  max-width: 276px;
  font-family: "Jost", sans-serif;
  font-style: normal;
  font-weight: 400;
  line-height: 1.7143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  letter-spacing: normal;
  word-break: normal;
  word-spacing: normal;
  white-space: normal;
  line-break: auto;
  font-size: 0.875rem;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 0.3rem;
}

.popover .popover-arrow {
  position: absolute;
  display: block;
  width: 1rem;
  height: 0.5rem;
  margin: 0 0.3rem;
}

.popover .popover-arrow::before,
.popover .popover-arrow::after {
  position: absolute;
  display: block;
  content: "";
  border-color: transparent;
  border-style: solid;
}

.bs-popover-top,
.bs-popover-auto[data-popper-placement^="top"] {
  margin-bottom: 0.5rem !important;
}

.bs-popover-top>.popover-arrow,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow {
  bottom: calc(-0.5rem - 1px);
}

.bs-popover-top>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow::before {
  bottom: 0;
  border-width: 0.5rem 0.5rem 0;
  border-top-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-top>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="top"]>.popover-arrow::after {
  bottom: 1px;
  border-width: 0.5rem 0.5rem 0;
  border-top-color: #fff;
}

.bs-popover-end,
.bs-popover-auto[data-popper-placement^="right"] {
  margin-left: 0.5rem !important;
}

.bs-popover-end>.popover-arrow,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow {
  left: calc(-0.5rem - 1px);
  width: 0.5rem;
  height: 1rem;
  margin: 0.3rem 0;
}

.bs-popover-end>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow::before {
  left: 0;
  border-width: 0.5rem 0.5rem 0.5rem 0;
  border-right-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-end>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow::after {
  left: 1px;
  border-width: 0.5rem 0.5rem 0.5rem 0;
  border-right-color: #fff;
}

.bs-popover-bottom,
.bs-popover-auto[data-popper-placement^="bottom"] {
  margin-top: 0.5rem !important;
}

.bs-popover-bottom>.popover-arrow,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow {
  top: calc(-0.5rem - 1px);
}

.bs-popover-bottom>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow::before {
  top: 0;
  border-width: 0 0.5rem 0.5rem 0.5rem;
  border-bottom-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-bottom>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="bottom"]>.popover-arrow::after {
  top: 1px;
  border-width: 0 0.5rem 0.5rem 0.5rem;
  border-bottom-color: #fff;
}

.bs-popover-bottom .popover-header::before,
.bs-popover-auto[data-popper-placement^="bottom"] .popover-header::before {
  position: absolute;
  top: 0;
  left: 50%;
  display: block;
  width: 1rem;
  margin-left: -0.5rem;
  content: "";
  border-bottom: 1px solid #f0f0f0;
}

.bs-popover-start,
.bs-popover-auto[data-popper-placement^="left"] {
  margin-right: 0.5rem !important;
}

.bs-popover-start>.popover-arrow,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow {
  right: calc(-0.5rem - 1px);
  width: 0.5rem;
  height: 1rem;
  margin: 0.3rem 0;
}

.bs-popover-start>.popover-arrow::before,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow::before {
  right: 0;
  border-width: 0.5rem 0 0.5rem 0.5rem;
  border-left-color: rgba(0, 0, 0, 0.25);
}

.bs-popover-start>.popover-arrow::after,
.bs-popover-auto[data-popper-placement^="left"]>.popover-arrow::after {
  right: 1px;
  border-width: 0.5rem 0 0.5rem 0.5rem;
  border-left-color: #fff;
}

.popover-header {
  padding: 0.5rem 1rem;
  margin-bottom: 0;
  font-size: 0.875rem;
  background-color: #f0f0f0;
  border-bottom: 1px solid #d8d8d8;
  border-top-left-radius: calc(0.3rem - 1px);
  border-top-right-radius: calc(0.3rem - 1px);
}

.popover-header:empty {
  display: none;
}

.popover-body {
  padding: 1rem 1rem;
  color: #222222;
}

.carousel {
  position: relative;
}

.carousel.pointer-event {
  touch-action: pan-y;
}

.carousel-inner {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.carousel-inner::after {
  display: block;
  clear: both;
  content: "";
}

.carousel-item {
  position: relative;
  display: none;
  float: left;
  width: 100%;
  margin-right: -100%;
  backface-visibility: hidden;
  transition: transform 0.6s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .carousel-item {
    transition: none;
  }
}

.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
  display: block;
}

/* rtl:begin:ignore */
.carousel-item-next:not(.carousel-item-start),
.active.carousel-item-end {
  transform: translateX(100%);
}

.carousel-item-prev:not(.carousel-item-end),
.active.carousel-item-start {
  transform: translateX(-100%);
}

/* rtl:end:ignore */
.carousel-fade .carousel-item {
  opacity: 0;
  transition-property: opacity;
  transform: none;
}

.carousel-fade .carousel-item.active,
.carousel-fade .carousel-item-next.carousel-item-start,
.carousel-fade .carousel-item-prev.carousel-item-end {
  z-index: 1;
  opacity: 1;
}

.carousel-fade .active.carousel-item-start,
.carousel-fade .active.carousel-item-end {
  z-index: 0;
  opacity: 0;
  transition: opacity 0s 0.6s;
}

@media (prefers-reduced-motion: reduce) {

  .carousel-fade .active.carousel-item-start,
  .carousel-fade .active.carousel-item-end {
    transition: none;
  }
}

.carousel-control-prev,
.carousel-control-next {
  position: absolute;
  top: 0;
  bottom: 0;
  z-index: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 15%;
  color: #fff;
  text-align: center;
  opacity: 0.5;
  transition: opacity 0.15s ease;
}

@media (prefers-reduced-motion: reduce) {

  .carousel-control-prev,
  .carousel-control-next {
    transition: none;
  }
}

.carousel-control-prev:hover,
.carousel-control-prev:focus,
.carousel-control-next:hover,
.carousel-control-next:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  opacity: 0.9;
}

.carousel-control-prev {
  left: 0;
}

.carousel-control-next {
  right: 0;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  background-repeat: no-repeat;
  background-position: 50%;
  background-size: 100% 100%;
}

/* rtl:options: {
  "autoRename": true,
  "stringMap":[ {
    "name"    : "prev-next",
    "search"  : "prev",
    "replace" : "next"
  } ]
} */
.carousel-control-prev-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z'/%3e%3c/svg%3e");
}

.carousel-control-next-icon {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23fff'%3e%3cpath d='M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z'/%3e%3c/svg%3e");
}

.carousel-indicators {
  position: absolute;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 2;
  display: flex;
  justify-content: center;
  padding-left: 0;
  margin-right: 15%;
  margin-left: 15%;
  list-style: none;
}

.carousel-indicators li {
  box-sizing: content-box;
  flex: 0 1 auto;
  width: 30px;
  height: 3px;
  margin-right: 3px;
  margin-left: 3px;
  text-indent: -999px;
  cursor: pointer;
  background-color: #fff;
  background-clip: padding-box;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  opacity: 0.5;
  transition: opacity 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
  .carousel-indicators li {
    transition: none;
  }
}

.carousel-indicators .active {
  opacity: 1;
}

.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 1.25rem;
  left: 15%;
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
  color: #fff;
  text-align: center;
}

.carousel-dark .carousel-control-prev-icon,
.carousel-dark .carousel-control-next-icon {
  filter: invert(1) grayscale(100);
}

.carousel-dark .carousel-indicators li {
  background-color: #000;
}

.carousel-dark .carousel-caption {
  color: #000;
}

@keyframes spinner-border {
  to {
    transform: rotate(360deg)
      /* rtl:ignore */
    ;
  }
}

.spinner-border {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  border: 0.25em solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: 0.75s linear infinite spinner-border;
}

.spinner-border-sm {
  width: 1rem;
  height: 1rem;
  border-width: 0.2em;
}

@keyframes spinner-grow {
  0% {
    transform: scale(0);
  }

  50% {
    opacity: 1;
    transform: none;
  }
}

.spinner-grow {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  background-color: currentColor;
  border-radius: 50%;
  opacity: 0;
  animation: 0.75s linear infinite spinner-grow;
}

.spinner-grow-sm {
  width: 1rem;
  height: 1rem;
}

@media (prefers-reduced-motion: reduce) {

  .spinner-border,
  .spinner-grow {
    animation-duration: 1.5s;
  }
}

.clearfix::after {
  display: block;
  clear: both;
  content: "";
}

.link-primary {
  color: #222222;
}

.link-primary:hover,
.link-primary:focus {
  color: #1b1b1b;
}

.link-secondary {
  color: #767676;
}

.link-secondary:hover,
.link-secondary:focus {
  color: #5e5e5e;
}

.link-success {
  color: #def2d7;
}

.link-success:hover,
.link-success:focus {
  color: #e5f5df;
}

.link-info {
  color: #cde9f6;
}

.link-info:hover,
.link-info:focus {
  color: #d7edf8;
}

.link-warning {
  color: #f7f3d7;
}

.link-warning:hover,
.link-warning:focus {
  color: #f9f5df;
}

.link-danger {
  color: #ecc8c5;
}

.link-danger:hover,
.link-danger:focus {
  color: #f0d3d1;
}

.link-light {
  color: #e4e4e4;
}

.link-light:hover,
.link-light:focus {
  color: #e9e9e9;
}

.link-lighter {
  color: #faf9f8;
}

.link-lighter:hover,
.link-lighter:focus {
  color: #fbfaf9;
}

.link-dark {
  color: #222222;
}

.link-dark:hover,
.link-dark:focus {
  color: #1b1b1b;
}

.link-red {
  color: #c32929;
}

.link-red:hover,
.link-red:focus {
  color: #9c2121;
}

.link-beige {
  color: #b9a16b;
}

.link-beige:hover,
.link-beige:focus {
  color: #c7b489;
}

.ratio {
  position: relative;
  width: 100%;
}

.ratio::before {
  display: block;
  padding-top: var(--aspect-ratio);
  content: "";
}

.ratio>* {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.ratio-1x1 {
  --aspect-ratio: 100%;
}

.ratio-4x3 {
  --aspect-ratio: calc(3 / 4 * 100%);
}

.ratio-16x9 {
  --aspect-ratio: calc(9 / 16 * 100%);
}

.ratio-21x9 {
  --aspect-ratio: calc(9 / 21 * 100%);
}

.fixed-top {
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  z-index: 1030;
}

.fixed-bottom {
  position: fixed;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1030;
}

.sticky-top {
  position: sticky;
  top: 0;
  z-index: 1020;
}

@media (min-width: 576px) {
  .sticky-sm-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 768px) {
  .sticky-md-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 992px) {
  .sticky-lg-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1200px) {
  .sticky-xl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1500px) {
  .sticky-xxl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

@media (min-width: 1700px) {
  .sticky-xxxl-top {
    position: sticky;
    top: 0;
    z-index: 1020;
  }
}

.visually-hidden,
.visually-hidden-focusable:not(:focus) {
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  padding: 0 !important;
  margin: -1px !important;
  overflow: hidden !important;
  clip: rect(0, 0, 0, 0) !important;
  white-space: nowrap !important;
  border: 0 !important;
}

.stretched-link::after {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1;
  content: "";
}

.text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.align-baseline {
  vertical-align: baseline !important;
}

.align-top {
  vertical-align: top !important;
}

.align-middle {
  vertical-align: middle !important;
}

.align-bottom {
  vertical-align: bottom !important;
}

.align-text-bottom {
  vertical-align: text-bottom !important;
}

.align-text-top {
  vertical-align: text-top !important;
}

.float-start {
  float: left !important;
}

.float-end {
  float: right !important;
}

.float-none {
  float: none !important;
}

.overflow-auto {
  overflow: auto !important;
}

.overflow-hidden {
  overflow: hidden !important;
}

.overflow-visible {
  overflow: visible !important;
}

.overflow-scroll {
  overflow: scroll !important;
}

.d-inline {
  display: inline !important;
}

.d-inline-block {
  display: inline-block !important;
}

.d-block {
  display: block !important;
}

.d-grid {
  display: grid !important;
}

.d-table {
  display: table !important;
}

.d-table-row {
  display: table-row !important;
}

.d-table-cell {
  display: table-cell !important;
}

.d-flex {
  display: flex !important;
}

.d-inline-flex {
  display: inline-flex !important;
}

.d-none {
  display: none !important;
}

.shadow {
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05) !important;
}

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075) !important;
}

.shadow-lg {
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.175) !important;
}

.shadow-none {
  box-shadow: none !important;
}

.position-static {
  position: static !important;
}

.position-relative {
  position: relative !important;
}

.position-absolute {
  position: absolute !important;
}

.position-fixed {
  position: fixed !important;
}

.position-sticky {
  position: sticky !important;
}

.top-0 {
  top: 0 !important;
}

.top-50 {
  top: 50% !important;
}

.top-100 {
  top: 100% !important;
}

.bottom-0 {
  bottom: 0 !important;
}

.bottom-50 {
  bottom: 50% !important;
}

.bottom-100 {
  bottom: 100% !important;
}

.start-0 {
  left: 0 !important;
}

.start-50 {
  left: 50% !important;
}

.start-100 {
  left: 100% !important;
}

.end-0 {
  right: 0 !important;
}

.end-50 {
  right: 50% !important;
}

.end-100 {
  right: 100% !important;
}

.translate-middle {
  transform: translate(-50%, -50%) !important;
}

.translate-middle-x {
  transform: translateX(-50%) !important;
}

.translate-middle-y {
  transform: translateY(-50%) !important;
}

.border {
  border: 1px solid #e4e4e4 !important;
}

.border-0 {
  border: 0 !important;
}

.border-top {
  border-top: 1px solid #e4e4e4 !important;
}

.border-top-0 {
  border-top: 0 !important;
}

.border-end {
  border-right: 1px solid #e4e4e4 !important;
}

.border-end-0 {
  border-right: 0 !important;
}

.border-bottom {
  border-bottom: 1px solid #e4e4e4 !important;
}

.border-bottom-0 {
  border-bottom: 0 !important;
}

.border-start {
  border-left: 1px solid #e4e4e4 !important;
}

.border-start-0 {
  border-left: 0 !important;
}

.border-primary {
  border-color: #222222 !important;
}

.border-secondary {
  border-color: #767676 !important;
}

.border-success {
  border-color: #def2d7 !important;
}

.border-info {
  border-color: #cde9f6 !important;
}

.border-warning {
  border-color: #f7f3d7 !important;
}

.border-danger {
  border-color: #ecc8c5 !important;
}

.border-light {
  border-color: #e4e4e4 !important;
}

.border-lighter {
  border-color: #faf9f8 !important;
}

.border-dark {
  border-color: #222222 !important;
}

.border-red {
  border-color: #c32929 !important;
}

.border-beige {
  border-color: #b9a16b !important;
}

.border-white {
  border-color: #fff !important;
}

.border-0 {
  border-width: 0 !important;
}

.border-1 {
  border-width: 1px !important;
}

.border-2 {
  border-width: 2px !important;
}

.border-3 {
  border-width: 3px !important;
}

.border-4 {
  border-width: 4px !important;
}

.border-5 {
  border-width: 5px !important;
}

.w-25 {
  width: 25% !important;
}

.w-50 {
  width: 50% !important;
}

.w-75 {
  width: 75% !important;
}

.w-100 {
  width: 100% !important;
}

.w-auto {
  width: auto !important;
}

.mw-100 {
  max-width: 100% !important;
}

.vw-100 {
  width: 100vw !important;
}

.min-vw-100 {
  min-width: 100vw !important;
}

.h-25 {
  height: 25% !important;
}

.h-50 {
  height: 50% !important;
}

.h-75 {
  height: 75% !important;
}

.h-100 {
  height: 100% !important;
}

.h-auto {
  height: auto !important;
}

.mh-100 {
  max-height: 100% !important;
}

.vh-100 {
  height: 100vh !important;
}

.min-vh-100 {
  min-height: 100vh !important;
}

.flex-fill {
  flex: 1 1 auto !important;
}

.flex-row {
  flex-direction: row !important;
}

.flex-column {
  flex-direction: column !important;
}

.flex-row-reverse {
  flex-direction: row-reverse !important;
}

.flex-column-reverse {
  flex-direction: column-reverse !important;
}

.flex-grow-0 {
  flex-grow: 0 !important;
}

.flex-grow-1 {
  flex-grow: 1 !important;
}

.flex-shrink-0 {
  flex-shrink: 0 !important;
}

.flex-shrink-1 {
  flex-shrink: 1 !important;
}

.flex-wrap {
  flex-wrap: wrap !important;
}

.flex-nowrap {
  flex-wrap: nowrap !important;
}

.flex-wrap-reverse {
  flex-wrap: wrap-reverse !important;
}

.gap-0 {
  gap: 0 !important;
}

.gap-1 {
  gap: 0.25rem !important;
}

.gap-2 {
  gap: 0.5rem !important;
}

.gap-3 {
  gap: 1rem !important;
}

.gap-4 {
  gap: 1.5rem !important;
}

.gap-5 {
  gap: 3rem !important;
}

.justify-content-start {
  justify-content: flex-start !important;
}

.justify-content-end {
  justify-content: flex-end !important;
}

.justify-content-center {
  justify-content: center !important;
}

.justify-content-between {
  justify-content: space-between !important;
}

.justify-content-around {
  justify-content: space-around !important;
}

.justify-content-evenly {
  justify-content: space-evenly !important;
}

.align-items-start {
  align-items: flex-start !important;
}

.align-items-end {
  align-items: flex-end !important;
}

.align-items-center {
  align-items: center !important;
}

.align-items-baseline {
  align-items: baseline !important;
}

.align-items-stretch {
  align-items: stretch !important;
}

.align-content-start {
  align-content: flex-start !important;
}

.align-content-end {
  align-content: flex-end !important;
}

.align-content-center {
  align-content: center !important;
}

.align-content-between {
  align-content: space-between !important;
}

.align-content-around {
  align-content: space-around !important;
}

.align-content-stretch {
  align-content: stretch !important;
}

.align-self-auto {
  align-self: auto !important;
}

.align-self-start {
  align-self: flex-start !important;
}

.align-self-end {
  align-self: flex-end !important;
}

.align-self-center {
  align-self: center !important;
}

.align-self-baseline {
  align-self: baseline !important;
}

.align-self-stretch {
  align-self: stretch !important;
}

.order-first {
  order: -1 !important;
}

.order-0 {
  order: 0 !important;
}

.order-1 {
  order: 1 !important;
}

.order-2 {
  order: 2 !important;
}

.order-3 {
  order: 3 !important;
}

.order-4 {
  order: 4 !important;
}

.order-5 {
  order: 5 !important;
}

.order-last {
  order: 6 !important;
}

.m-0 {
  margin: 0 !important;
}

.m-1 {
  margin: 0.25rem !important;
}

.m-2 {
  margin: 0.5rem !important;
}

.m-3 {
  margin: 1rem !important;
}

.m-4 {
  margin: 1.5rem !important;
}

.m-5 {
  margin: 3rem !important;
}

.m-auto {
  margin: auto !important;
}

.mx-0 {
  margin-right: 0 !important;
  margin-left: 0 !important;
}

.mx-1 {
  margin-right: 0.25rem !important;
  margin-left: 0.25rem !important;
}

.mx-2 {
  margin-right: 0.5rem !important;
  margin-left: 0.5rem !important;
}

.mx-3 {
  margin-right: 1rem !important;
  margin-left: 1rem !important;
}

.mx-4 {
  margin-right: 1.5rem !important;
  margin-left: 1.5rem !important;
}

.mx-5 {
  margin-right: 3rem !important;
  margin-left: 3rem !important;
}

.mx-auto {
  margin-right: auto !important;
  margin-left: auto !important;
}

.my-0 {
  margin-top: 0 !important;
  margin-bottom: 0 !important;
}

.my-1 {
  margin-top: 0.25rem !important;
  margin-bottom: 0.25rem !important;
}

.my-2 {
  margin-top: 0.5rem !important;
  margin-bottom: 0.5rem !important;
}

.my-3 {
  margin-top: 1rem !important;
  margin-bottom: 1rem !important;
}

.my-4 {
  margin-top: 1.5rem !important;
  margin-bottom: 1.5rem !important;
}

.my-5 {
  margin-top: 3rem !important;
  margin-bottom: 3rem !important;
}

.my-auto {
  margin-top: auto !important;
  margin-bottom: auto !important;
}

.mt-0 {
  margin-top: 0 !important;
}

.mt-1 {
  margin-top: 0.25rem !important;
}

.mt-2 {
  margin-top: 0.5rem !important;
}

.mt-3 {
  margin-top: 1rem !important;
}

.mt-4 {
  margin-top: 1.5rem !important;
}

.mt-5 {
  margin-top: 3rem !important;
}

.mt-auto {
  margin-top: auto !important;
}

.me-0 {
  margin-right: 0 !important;
}

.me-1 {
  margin-right: 0.25rem !important;
}

.me-2 {
  margin-right: 0.5rem !important;
}

.me-3 {
  margin-right: 1rem !important;
}

.me-4 {
  margin-right: 1.5rem !important;
}

.me-5 {
  margin-right: 3rem !important;
}

.me-auto {
  margin-right: auto !important;
}

.mb-0 {
  margin-bottom: 0 !important;
}

.mb-1 {
  margin-bottom: 0.25rem !important;
}

.mb-2 {
  margin-bottom: 0.5rem !important;
}

.mb-3 {
  margin-bottom: 1rem !important;
}

.mb-4 {
  margin-bottom: 1.5rem !important;
}

.mb-5 {
  margin-bottom: 3rem !important;
}

.mb-auto {
  margin-bottom: auto !important;
}

.ms-0 {
  margin-left: 0 !important;
}

.ms-1 {
  margin-left: 0.25rem !important;
}

.ms-2 {
  margin-left: 0.5rem !important;
}

.ms-3 {
  margin-left: 1rem !important;
}

.ms-4 {
  margin-left: 1.5rem !important;
}

.ms-5 {
  margin-left: 3rem !important;
}

.ms-auto {
  margin-left: auto !important;
}

.p-0 {
  padding: 0 !important;
}

.p-1 {
  padding: 0.25rem !important;
}

.p-2 {
  padding: 0.5rem !important;
}

.p-3 {
  padding: 1rem !important;
}

.p-4 {
  padding: 1.5rem !important;
}

.p-5 {
  padding: 3rem !important;
}

.px-0 {
  padding-right: 0 !important;
  padding-left: 0 !important;
}

.px-1 {
  padding-right: 0.25rem !important;
  padding-left: 0.25rem !important;
}

.px-2 {
  padding-right: 0.5rem !important;
  padding-left: 0.5rem !important;
}

.px-3 {
  padding-right: 1rem !important;
  padding-left: 1rem !important;
}

.px-4 {
  padding-right: 1.5rem !important;
  padding-left: 1.5rem !important;
}

.px-5 {
  padding-right: 3rem !important;
  padding-left: 3rem !important;
}

.py-0 {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}

.py-1 {
  padding-top: 0.25rem !important;
  padding-bottom: 0.25rem !important;
}

.py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}

.py-3 {
  padding-top: 1rem !important;
  padding-bottom: 1rem !important;
}

.py-4 {
  padding-top: 1.5rem !important;
  padding-bottom: 1.5rem !important;
}

.py-5 {
  padding-top: 3rem !important;
  padding-bottom: 3rem !important;
}

.pt-0 {
  padding-top: 0 !important;
}

.pt-1 {
  padding-top: 0.25rem !important;
}

.pt-2 {
  padding-top: 0.5rem !important;
}

.pt-3 {
  padding-top: 1rem !important;
}

.pt-4 {
  padding-top: 1.5rem !important;
}

.pt-5 {
  padding-top: 3rem !important;
}

.pe-0 {
  padding-right: 0 !important;
}

.pe-1 {
  padding-right: 0.25rem !important;
}

.pe-2 {
  padding-right: 0.5rem !important;
}

.pe-3 {
  padding-right: 1rem !important;
}

.pe-4 {
  padding-right: 1.5rem !important;
}

.pe-5 {
  padding-right: 3rem !important;
}

.pb-0 {
  padding-bottom: 0 !important;
}

.pb-1 {
  padding-bottom: 0.25rem !important;
}

.pb-2 {
  padding-bottom: 0.5rem !important;
}

.pb-3 {
  padding-bottom: 1rem !important;
}

.pb-4 {
  padding-bottom: 1.5rem !important;
}

.pb-5 {
  padding-bottom: 3rem !important;
}

.ps-0 {
  padding-left: 0 !important;
}

.ps-1 {
  padding-left: 0.25rem !important;
}

.ps-2 {
  padding-left: 0.5rem !important;
}

.ps-3 {
  padding-left: 1rem !important;
}

.ps-4 {
  padding-left: 1.5rem !important;
}

.ps-5 {
  padding-left: 3rem !important;
}

.fs-1 {
  font-size: calc(1.625rem + 4.5vw) !important;
}

.fs-2 {
  font-size: calc(1.325rem + 0.9vw) !important;
}

.fs-3 {
  font-size: calc(1.2875rem + 0.45vw) !important;
}

.fs-4 {
  font-size: 1.25rem !important;
}

.fs-5 {
  font-size: 1.125rem !important;
}

.fs-6 {
  font-size: 1rem !important;
}

.fst-italic {
  font-style: italic !important;
}

.fst-normal {
  font-style: normal !important;
}

.fw-light {
  font-weight: 300 !important;
}

.fw-lighter {
  font-weight: lighter !important;
}

.fw-normal {
  font-weight: 400 !important;
}

.fw-medium {
  font-weight: 500 !important;
}

.fw-bold {
  font-weight: 700 !important;
}

.fw-bolder {
  font-weight: bolder !important;
}

.text-lowercase {
  text-transform: lowercase !important;
}

.text-uppercase {
  text-transform: uppercase !important;
}

.text-capitalize {
  text-transform: capitalize !important;
}

.text-start {
  text-align: left !important;
}

.text-end {
  text-align: right !important;
}

.text-center {
  text-align: center !important;
}

.text-primary {
  color: #222222 !important;
}

.text-secondary {
  color: #767676 !important;
}

.text-success {
  color: #def2d7 !important;
}

.text-info {
  color: #cde9f6 !important;
}

.text-warning {
  color: #f7f3d7 !important;
}

.text-danger {
  color: #ecc8c5 !important;
}

.text-light {
  color: #e4e4e4 !important;
}

.text-lighter {
  color: #faf9f8 !important;
}

.text-dark {
  color: #222222 !important;
}

.text-red {
  color: #c32929 !important;
}

.text-beige {
  color: #b9a16b !important;
}

.text-white {
  color: #fff !important;
}

.text-body {
  color: #222222 !important;
}

.text-muted {
  color: #6c757d !important;
}

.text-black-50 {
  color: rgba(0, 0, 0, 0.5) !important;
}

.text-white-50 {
  color: rgba(255, 255, 255, 0.5) !important;
}

.text-reset {
  color: inherit !important;
}

.lh-1 {
  line-height: 1 !important;
}

.lh-sm {
  line-height: 1.25 !important;
}

.lh-base {
  line-height: 1.7143 !important;
}

.lh-lg {
  line-height: 2 !important;
}

.bg-primary {
  background-color: #222222 !important;
}

.bg-secondary {
  background-color: #767676 !important;
}

.bg-success {
  background-color: #def2d7 !important;
}

.bg-info {
  background-color: #cde9f6 !important;
}

.bg-warning {
  background-color: #f7f3d7 !important;
}

.bg-danger {
  background-color: #ecc8c5 !important;
}

.bg-light {
  background-color: #e4e4e4 !important;
}

.bg-lighter {
  background-color: #faf9f8 !important;
}

.bg-dark {
  background-color: #222222 !important;
}

.bg-red {
  background-color: #c32929 !important;
}

.bg-beige {
  background-color: #b9a16b !important;
}

.bg-body {
  background-color: #ffffff !important;
}

.bg-white {
  background-color: #fff !important;
}

.bg-transparent {
  background-color: transparent !important;
}

.bg-gradient {
  background-image: var(--bs-gradient) !important;
}

.text-wrap {
  white-space: normal !important;
}

.text-nowrap {
  white-space: nowrap !important;
}

.text-decoration-none {
  text-decoration: none !important;
}

.text-decoration-underline {
  text-decoration: underline !important;
}

.text-decoration-line-through {
  text-decoration: line-through !important;
}

/* rtl:begin:remove */
.text-break {
  word-wrap: break-word !important;
  word-break: break-word !important;
}

/* rtl:end:remove */
.font-monospace {
  font-family: var(--bs-font-monospace) !important;
}

.user-select-all {
  user-select: all !important;
}

.user-select-auto {
  user-select: auto !important;
}

.user-select-none {
  user-select: none !important;
}

.pe-none {
  pointer-events: none !important;
}

.pe-auto {
  pointer-events: auto !important;
}

.rounded {
  border-radius: 0 !important;
}

.rounded-0 {
  border-radius: 0 !important;
}

.rounded-1 {
  border-radius: 0.2rem !important;
}

.rounded-2 {
  border-radius: 0 !important;
}

.rounded-3 {
  border-radius: 0.3rem !important;
}

.rounded-circle {
  border-radius: 50% !important;
}

.rounded-pill {
  border-radius: 50rem !important;
}

.rounded-top {
  border-top-left-radius: 0 !important;
  border-top-right-radius: 0 !important;
}

.rounded-end {
  border-top-right-radius: 0 !important;
  border-bottom-right-radius: 0 !important;
}

.rounded-bottom {
  border-bottom-right-radius: 0 !important;
  border-bottom-left-radius: 0 !important;
}

.rounded-start {
  border-bottom-left-radius: 0 !important;
  border-top-left-radius: 0 !important;
}

.visible {
  visibility: visible !important;
}

.invisible {
  visibility: hidden !important;
}

@media (min-width: 576px) {
  .float-sm-start {
    float: left !important;
  }

  .float-sm-end {
    float: right !important;
  }

  .float-sm-none {
    float: none !important;
  }

  .d-sm-inline {
    display: inline !important;
  }

  .d-sm-inline-block {
    display: inline-block !important;
  }

  .d-sm-block {
    display: block !important;
  }

  .d-sm-grid {
    display: grid !important;
  }

  .d-sm-table {
    display: table !important;
  }

  .d-sm-table-row {
    display: table-row !important;
  }

  .d-sm-table-cell {
    display: table-cell !important;
  }

  .d-sm-flex {
    display: flex !important;
  }

  .d-sm-inline-flex {
    display: inline-flex !important;
  }

  .d-sm-none {
    display: none !important;
  }

  .flex-sm-fill {
    flex: 1 1 auto !important;
  }

  .flex-sm-row {
    flex-direction: row !important;
  }

  .flex-sm-column {
    flex-direction: column !important;
  }

  .flex-sm-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-sm-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-sm-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-sm-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-sm-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-sm-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-sm-wrap {
    flex-wrap: wrap !important;
  }

  .flex-sm-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-sm-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-sm-0 {
    gap: 0 !important;
  }

  .gap-sm-1 {
    gap: 0.25rem !important;
  }

  .gap-sm-2 {
    gap: 0.5rem !important;
  }

  .gap-sm-3 {
    gap: 1rem !important;
  }

  .gap-sm-4 {
    gap: 1.5rem !important;
  }

  .gap-sm-5 {
    gap: 3rem !important;
  }

  .justify-content-sm-start {
    justify-content: flex-start !important;
  }

  .justify-content-sm-end {
    justify-content: flex-end !important;
  }

  .justify-content-sm-center {
    justify-content: center !important;
  }

  .justify-content-sm-between {
    justify-content: space-between !important;
  }

  .justify-content-sm-around {
    justify-content: space-around !important;
  }

  .justify-content-sm-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-sm-start {
    align-items: flex-start !important;
  }

  .align-items-sm-end {
    align-items: flex-end !important;
  }

  .align-items-sm-center {
    align-items: center !important;
  }

  .align-items-sm-baseline {
    align-items: baseline !important;
  }

  .align-items-sm-stretch {
    align-items: stretch !important;
  }

  .align-content-sm-start {
    align-content: flex-start !important;
  }

  .align-content-sm-end {
    align-content: flex-end !important;
  }

  .align-content-sm-center {
    align-content: center !important;
  }

  .align-content-sm-between {
    align-content: space-between !important;
  }

  .align-content-sm-around {
    align-content: space-around !important;
  }

  .align-content-sm-stretch {
    align-content: stretch !important;
  }

  .align-self-sm-auto {
    align-self: auto !important;
  }

  .align-self-sm-start {
    align-self: flex-start !important;
  }

  .align-self-sm-end {
    align-self: flex-end !important;
  }

  .align-self-sm-center {
    align-self: center !important;
  }

  .align-self-sm-baseline {
    align-self: baseline !important;
  }

  .align-self-sm-stretch {
    align-self: stretch !important;
  }

  .order-sm-first {
    order: -1 !important;
  }

  .order-sm-0 {
    order: 0 !important;
  }

  .order-sm-1 {
    order: 1 !important;
  }

  .order-sm-2 {
    order: 2 !important;
  }

  .order-sm-3 {
    order: 3 !important;
  }

  .order-sm-4 {
    order: 4 !important;
  }

  .order-sm-5 {
    order: 5 !important;
  }

  .order-sm-last {
    order: 6 !important;
  }

  .m-sm-0 {
    margin: 0 !important;
  }

  .m-sm-1 {
    margin: 0.25rem !important;
  }

  .m-sm-2 {
    margin: 0.5rem !important;
  }

  .m-sm-3 {
    margin: 1rem !important;
  }

  .m-sm-4 {
    margin: 1.5rem !important;
  }

  .m-sm-5 {
    margin: 3rem !important;
  }

  .m-sm-auto {
    margin: auto !important;
  }

  .mx-sm-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-sm-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-sm-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-sm-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-sm-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-sm-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-sm-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-sm-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-sm-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-sm-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-sm-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-sm-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-sm-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-sm-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-sm-0 {
    margin-top: 0 !important;
  }

  .mt-sm-1 {
    margin-top: 0.25rem !important;
  }

  .mt-sm-2 {
    margin-top: 0.5rem !important;
  }

  .mt-sm-3 {
    margin-top: 1rem !important;
  }

  .mt-sm-4 {
    margin-top: 1.5rem !important;
  }

  .mt-sm-5 {
    margin-top: 3rem !important;
  }

  .mt-sm-auto {
    margin-top: auto !important;
  }

  .me-sm-0 {
    margin-right: 0 !important;
  }

  .me-sm-1 {
    margin-right: 0.25rem !important;
  }

  .me-sm-2 {
    margin-right: 0.5rem !important;
  }

  .me-sm-3 {
    margin-right: 1rem !important;
  }

  .me-sm-4 {
    margin-right: 1.5rem !important;
  }

  .me-sm-5 {
    margin-right: 3rem !important;
  }

  .me-sm-auto {
    margin-right: auto !important;
  }

  .mb-sm-0 {
    margin-bottom: 0 !important;
  }

  .mb-sm-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-sm-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-sm-3 {
    margin-bottom: 1rem !important;
  }

  .mb-sm-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-sm-5 {
    margin-bottom: 3rem !important;
  }

  .mb-sm-auto {
    margin-bottom: auto !important;
  }

  .ms-sm-0 {
    margin-left: 0 !important;
  }

  .ms-sm-1 {
    margin-left: 0.25rem !important;
  }

  .ms-sm-2 {
    margin-left: 0.5rem !important;
  }

  .ms-sm-3 {
    margin-left: 1rem !important;
  }

  .ms-sm-4 {
    margin-left: 1.5rem !important;
  }

  .ms-sm-5 {
    margin-left: 3rem !important;
  }

  .ms-sm-auto {
    margin-left: auto !important;
  }

  .p-sm-0 {
    padding: 0 !important;
  }

  .p-sm-1 {
    padding: 0.25rem !important;
  }

  .p-sm-2 {
    padding: 0.5rem !important;
  }

  .p-sm-3 {
    padding: 1rem !important;
  }

  .p-sm-4 {
    padding: 1.5rem !important;
  }

  .p-sm-5 {
    padding: 3rem !important;
  }

  .px-sm-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-sm-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-sm-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-sm-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-sm-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-sm-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-sm-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-sm-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-sm-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-sm-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-sm-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-sm-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-sm-0 {
    padding-top: 0 !important;
  }

  .pt-sm-1 {
    padding-top: 0.25rem !important;
  }

  .pt-sm-2 {
    padding-top: 0.5rem !important;
  }

  .pt-sm-3 {
    padding-top: 1rem !important;
  }

  .pt-sm-4 {
    padding-top: 1.5rem !important;
  }

  .pt-sm-5 {
    padding-top: 3rem !important;
  }

  .pe-sm-0 {
    padding-right: 0 !important;
  }

  .pe-sm-1 {
    padding-right: 0.25rem !important;
  }

  .pe-sm-2 {
    padding-right: 0.5rem !important;
  }

  .pe-sm-3 {
    padding-right: 1rem !important;
  }

  .pe-sm-4 {
    padding-right: 1.5rem !important;
  }

  .pe-sm-5 {
    padding-right: 3rem !important;
  }

  .pb-sm-0 {
    padding-bottom: 0 !important;
  }

  .pb-sm-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-sm-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-sm-3 {
    padding-bottom: 1rem !important;
  }

  .pb-sm-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-sm-5 {
    padding-bottom: 3rem !important;
  }

  .ps-sm-0 {
    padding-left: 0 !important;
  }

  .ps-sm-1 {
    padding-left: 0.25rem !important;
  }

  .ps-sm-2 {
    padding-left: 0.5rem !important;
  }

  .ps-sm-3 {
    padding-left: 1rem !important;
  }

  .ps-sm-4 {
    padding-left: 1.5rem !important;
  }

  .ps-sm-5 {
    padding-left: 3rem !important;
  }

  .text-sm-start {
    text-align: left !important;
  }

  .text-sm-end {
    text-align: right !important;
  }

  .text-sm-center {
    text-align: center !important;
  }
}

@media (min-width: 768px) {
  .float-md-start {
    float: left !important;
  }

  .float-md-end {
    float: right !important;
  }

  .float-md-none {
    float: none !important;
  }

  .d-md-inline {
    display: inline !important;
  }

  .d-md-inline-block {
    display: inline-block !important;
  }

  .d-md-block {
    display: block !important;
  }

  .d-md-grid {
    display: grid !important;
  }

  .d-md-table {
    display: table !important;
  }

  .d-md-table-row {
    display: table-row !important;
  }

  .d-md-table-cell {
    display: table-cell !important;
  }

  .d-md-flex {
    display: flex !important;
  }

  .d-md-inline-flex {
    display: inline-flex !important;
  }

  .d-md-none {
    display: none !important;
  }

  .flex-md-fill {
    flex: 1 1 auto !important;
  }

  .flex-md-row {
    flex-direction: row !important;
  }

  .flex-md-column {
    flex-direction: column !important;
  }

  .flex-md-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-md-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-md-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-md-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-md-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-md-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-md-wrap {
    flex-wrap: wrap !important;
  }

  .flex-md-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-md-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-md-0 {
    gap: 0 !important;
  }

  .gap-md-1 {
    gap: 0.25rem !important;
  }

  .gap-md-2 {
    gap: 0.5rem !important;
  }

  .gap-md-3 {
    gap: 1rem !important;
  }

  .gap-md-4 {
    gap: 1.5rem !important;
  }

  .gap-md-5 {
    gap: 3rem !important;
  }

  .justify-content-md-start {
    justify-content: flex-start !important;
  }

  .justify-content-md-end {
    justify-content: flex-end !important;
  }

  .justify-content-md-center {
    justify-content: center !important;
  }

  .justify-content-md-between {
    justify-content: space-between !important;
  }

  .justify-content-md-around {
    justify-content: space-around !important;
  }

  .justify-content-md-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-md-start {
    align-items: flex-start !important;
  }

  .align-items-md-end {
    align-items: flex-end !important;
  }

  .align-items-md-center {
    align-items: center !important;
  }

  .align-items-md-baseline {
    align-items: baseline !important;
  }

  .align-items-md-stretch {
    align-items: stretch !important;
  }

  .align-content-md-start {
    align-content: flex-start !important;
  }

  .align-content-md-end {
    align-content: flex-end !important;
  }

  .align-content-md-center {
    align-content: center !important;
  }

  .align-content-md-between {
    align-content: space-between !important;
  }

  .align-content-md-around {
    align-content: space-around !important;
  }

  .align-content-md-stretch {
    align-content: stretch !important;
  }

  .align-self-md-auto {
    align-self: auto !important;
  }

  .align-self-md-start {
    align-self: flex-start !important;
  }

  .align-self-md-end {
    align-self: flex-end !important;
  }

  .align-self-md-center {
    align-self: center !important;
  }

  .align-self-md-baseline {
    align-self: baseline !important;
  }

  .align-self-md-stretch {
    align-self: stretch !important;
  }

  .order-md-first {
    order: -1 !important;
  }

  .order-md-0 {
    order: 0 !important;
  }

  .order-md-1 {
    order: 1 !important;
  }

  .order-md-2 {
    order: 2 !important;
  }

  .order-md-3 {
    order: 3 !important;
  }

  .order-md-4 {
    order: 4 !important;
  }

  .order-md-5 {
    order: 5 !important;
  }

  .order-md-last {
    order: 6 !important;
  }

  .m-md-0 {
    margin: 0 !important;
  }

  .m-md-1 {
    margin: 0.25rem !important;
  }

  .m-md-2 {
    margin: 0.5rem !important;
  }

  .m-md-3 {
    margin: 1rem !important;
  }

  .m-md-4 {
    margin: 1.5rem !important;
  }

  .m-md-5 {
    margin: 3rem !important;
  }

  .m-md-auto {
    margin: auto !important;
  }

  .mx-md-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-md-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-md-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-md-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-md-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-md-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-md-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-md-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-md-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-md-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-md-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-md-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-md-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-md-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-md-0 {
    margin-top: 0 !important;
  }

  .mt-md-1 {
    margin-top: 0.25rem !important;
  }

  .mt-md-2 {
    margin-top: 0.5rem !important;
  }

  .mt-md-3 {
    margin-top: 1rem !important;
  }

  .mt-md-4 {
    margin-top: 1.5rem !important;
  }

  .mt-md-5 {
    margin-top: 3rem !important;
  }

  .mt-md-auto {
    margin-top: auto !important;
  }

  .me-md-0 {
    margin-right: 0 !important;
  }

  .me-md-1 {
    margin-right: 0.25rem !important;
  }

  .me-md-2 {
    margin-right: 0.5rem !important;
  }

  .me-md-3 {
    margin-right: 1rem !important;
  }

  .me-md-4 {
    margin-right: 1.5rem !important;
  }

  .me-md-5 {
    margin-right: 3rem !important;
  }

  .me-md-auto {
    margin-right: auto !important;
  }

  .mb-md-0 {
    margin-bottom: 0 !important;
  }

  .mb-md-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-md-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-md-3 {
    margin-bottom: 1rem !important;
  }

  .mb-md-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-md-5 {
    margin-bottom: 3rem !important;
  }

  .mb-md-auto {
    margin-bottom: auto !important;
  }

  .ms-md-0 {
    margin-left: 0 !important;
  }

  .ms-md-1 {
    margin-left: 0.25rem !important;
  }

  .ms-md-2 {
    margin-left: 0.5rem !important;
  }

  .ms-md-3 {
    margin-left: 1rem !important;
  }

  .ms-md-4 {
    margin-left: 1.5rem !important;
  }

  .ms-md-5 {
    margin-left: 3rem !important;
  }

  .ms-md-auto {
    margin-left: auto !important;
  }

  .p-md-0 {
    padding: 0 !important;
  }

  .p-md-1 {
    padding: 0.25rem !important;
  }

  .p-md-2 {
    padding: 0.5rem !important;
  }

  .p-md-3 {
    padding: 1rem !important;
  }

  .p-md-4 {
    padding: 1.5rem !important;
  }

  .p-md-5 {
    padding: 3rem !important;
  }

  .px-md-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-md-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-md-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-md-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-md-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-md-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-md-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-md-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-md-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-md-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-md-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-md-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-md-0 {
    padding-top: 0 !important;
  }

  .pt-md-1 {
    padding-top: 0.25rem !important;
  }

  .pt-md-2 {
    padding-top: 0.5rem !important;
  }

  .pt-md-3 {
    padding-top: 1rem !important;
  }

  .pt-md-4 {
    padding-top: 1.5rem !important;
  }

  .pt-md-5 {
    padding-top: 3rem !important;
  }

  .pe-md-0 {
    padding-right: 0 !important;
  }

  .pe-md-1 {
    padding-right: 0.25rem !important;
  }

  .pe-md-2 {
    padding-right: 0.5rem !important;
  }

  .pe-md-3 {
    padding-right: 1rem !important;
  }

  .pe-md-4 {
    padding-right: 1.5rem !important;
  }

  .pe-md-5 {
    padding-right: 3rem !important;
  }

  .pb-md-0 {
    padding-bottom: 0 !important;
  }

  .pb-md-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-md-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-md-3 {
    padding-bottom: 1rem !important;
  }

  .pb-md-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-md-5 {
    padding-bottom: 3rem !important;
  }

  .ps-md-0 {
    padding-left: 0 !important;
  }

  .ps-md-1 {
    padding-left: 0.25rem !important;
  }

  .ps-md-2 {
    padding-left: 0.5rem !important;
  }

  .ps-md-3 {
    padding-left: 1rem !important;
  }

  .ps-md-4 {
    padding-left: 1.5rem !important;
  }

  .ps-md-5 {
    padding-left: 3rem !important;
  }

  .text-md-start {
    text-align: left !important;
  }

  .text-md-end {
    text-align: right !important;
  }

  .text-md-center {
    text-align: center !important;
  }
}

@media (min-width: 992px) {
  .float-lg-start {
    float: left !important;
  }

  .float-lg-end {
    float: right !important;
  }

  .float-lg-none {
    float: none !important;
  }

  .d-lg-inline {
    display: inline !important;
  }

  .d-lg-inline-block {
    display: inline-block !important;
  }

  .d-lg-block {
    display: block !important;
  }

  .d-lg-grid {
    display: grid !important;
  }

  .d-lg-table {
    display: table !important;
  }

  .d-lg-table-row {
    display: table-row !important;
  }

  .d-lg-table-cell {
    display: table-cell !important;
  }

  .d-lg-flex {
    display: flex !important;
  }

  .d-lg-inline-flex {
    display: inline-flex !important;
  }

  .d-lg-none {
    display: none !important;
  }

  .flex-lg-fill {
    flex: 1 1 auto !important;
  }

  .flex-lg-row {
    flex-direction: row !important;
  }

  .flex-lg-column {
    flex-direction: column !important;
  }

  .flex-lg-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-lg-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-lg-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-lg-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-lg-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-lg-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-lg-wrap {
    flex-wrap: wrap !important;
  }

  .flex-lg-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-lg-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-lg-0 {
    gap: 0 !important;
  }

  .gap-lg-1 {
    gap: 0.25rem !important;
  }

  .gap-lg-2 {
    gap: 0.5rem !important;
  }

  .gap-lg-3 {
    gap: 1rem !important;
  }

  .gap-lg-4 {
    gap: 1.5rem !important;
  }

  .gap-lg-5 {
    gap: 3rem !important;
  }

  .justify-content-lg-start {
    justify-content: flex-start !important;
  }

  .justify-content-lg-end {
    justify-content: flex-end !important;
  }

  .justify-content-lg-center {
    justify-content: center !important;
  }

  .justify-content-lg-between {
    justify-content: space-between !important;
  }

  .justify-content-lg-around {
    justify-content: space-around !important;
  }

  .justify-content-lg-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-lg-start {
    align-items: flex-start !important;
  }

  .align-items-lg-end {
    align-items: flex-end !important;
  }

  .align-items-lg-center {
    align-items: center !important;
  }

  .align-items-lg-baseline {
    align-items: baseline !important;
  }

  .align-items-lg-stretch {
    align-items: stretch !important;
  }

  .align-content-lg-start {
    align-content: flex-start !important;
  }

  .align-content-lg-end {
    align-content: flex-end !important;
  }

  .align-content-lg-center {
    align-content: center !important;
  }

  .align-content-lg-between {
    align-content: space-between !important;
  }

  .align-content-lg-around {
    align-content: space-around !important;
  }

  .align-content-lg-stretch {
    align-content: stretch !important;
  }

  .align-self-lg-auto {
    align-self: auto !important;
  }

  .align-self-lg-start {
    align-self: flex-start !important;
  }

  .align-self-lg-end {
    align-self: flex-end !important;
  }

  .align-self-lg-center {
    align-self: center !important;
  }

  .align-self-lg-baseline {
    align-self: baseline !important;
  }

  .align-self-lg-stretch {
    align-self: stretch !important;
  }

  .order-lg-first {
    order: -1 !important;
  }

  .order-lg-0 {
    order: 0 !important;
  }

  .order-lg-1 {
    order: 1 !important;
  }

  .order-lg-2 {
    order: 2 !important;
  }

  .order-lg-3 {
    order: 3 !important;
  }

  .order-lg-4 {
    order: 4 !important;
  }

  .order-lg-5 {
    order: 5 !important;
  }

  .order-lg-last {
    order: 6 !important;
  }

  .m-lg-0 {
    margin: 0 !important;
  }

  .m-lg-1 {
    margin: 0.25rem !important;
  }

  .m-lg-2 {
    margin: 0.5rem !important;
  }

  .m-lg-3 {
    margin: 1rem !important;
  }

  .m-lg-4 {
    margin: 1.5rem !important;
  }

  .m-lg-5 {
    margin: 3rem !important;
  }

  .m-lg-auto {
    margin: auto !important;
  }

  .mx-lg-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-lg-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-lg-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-lg-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-lg-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-lg-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-lg-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-lg-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-lg-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-lg-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-lg-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-lg-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-lg-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-lg-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-lg-0 {
    margin-top: 0 !important;
  }

  .mt-lg-1 {
    margin-top: 0.25rem !important;
  }

  .mt-lg-2 {
    margin-top: 0.5rem !important;
  }

  .mt-lg-3 {
    margin-top: 1rem !important;
  }

  .mt-lg-4 {
    margin-top: 1.5rem !important;
  }

  .mt-lg-5 {
    margin-top: 3rem !important;
  }

  .mt-lg-auto {
    margin-top: auto !important;
  }

  .me-lg-0 {
    margin-right: 0 !important;
  }

  .me-lg-1 {
    margin-right: 0.25rem !important;
  }

  .me-lg-2 {
    margin-right: 0.5rem !important;
  }

  .me-lg-3 {
    margin-right: 1rem !important;
  }

  .me-lg-4 {
    margin-right: 1.5rem !important;
  }

  .me-lg-5 {
    margin-right: 3rem !important;
  }

  .me-lg-auto {
    margin-right: auto !important;
  }

  .mb-lg-0 {
    margin-bottom: 0 !important;
  }

  .mb-lg-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-lg-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-lg-3 {
    margin-bottom: 1rem !important;
  }

  .mb-lg-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-lg-5 {
    margin-bottom: 3rem !important;
  }

  .mb-lg-auto {
    margin-bottom: auto !important;
  }

  .ms-lg-0 {
    margin-left: 0 !important;
  }

  .ms-lg-1 {
    margin-left: 0.25rem !important;
  }

  .ms-lg-2 {
    margin-left: 0.5rem !important;
  }

  .ms-lg-3 {
    margin-left: 1rem !important;
  }

  .ms-lg-4 {
    margin-left: 1.5rem !important;
  }

  .ms-lg-5 {
    margin-left: 3rem !important;
  }

  .ms-lg-auto {
    margin-left: auto !important;
  }

  .p-lg-0 {
    padding: 0 !important;
  }

  .p-lg-1 {
    padding: 0.25rem !important;
  }

  .p-lg-2 {
    padding: 0.5rem !important;
  }

  .p-lg-3 {
    padding: 1rem !important;
  }

  .p-lg-4 {
    padding: 1.5rem !important;
  }

  .p-lg-5 {
    padding: 3rem !important;
  }

  .px-lg-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-lg-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-lg-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-lg-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-lg-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-lg-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-lg-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-lg-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-lg-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-lg-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-lg-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-lg-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-lg-0 {
    padding-top: 0 !important;
  }

  .pt-lg-1 {
    padding-top: 0.25rem !important;
  }

  .pt-lg-2 {
    padding-top: 0.5rem !important;
  }

  .pt-lg-3 {
    padding-top: 1rem !important;
  }

  .pt-lg-4 {
    padding-top: 1.5rem !important;
  }

  .pt-lg-5 {
    padding-top: 3rem !important;
  }

  .pe-lg-0 {
    padding-right: 0 !important;
  }

  .pe-lg-1 {
    padding-right: 0.25rem !important;
  }

  .pe-lg-2 {
    padding-right: 0.5rem !important;
  }

  .pe-lg-3 {
    padding-right: 1rem !important;
  }

  .pe-lg-4 {
    padding-right: 1.5rem !important;
  }

  .pe-lg-5 {
    padding-right: 3rem !important;
  }

  .pb-lg-0 {
    padding-bottom: 0 !important;
  }

  .pb-lg-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-lg-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-lg-3 {
    padding-bottom: 1rem !important;
  }

  .pb-lg-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-lg-5 {
    padding-bottom: 3rem !important;
  }

  .ps-lg-0 {
    padding-left: 0 !important;
  }

  .ps-lg-1 {
    padding-left: 0.25rem !important;
  }

  .ps-lg-2 {
    padding-left: 0.5rem !important;
  }

  .ps-lg-3 {
    padding-left: 1rem !important;
  }

  .ps-lg-4 {
    padding-left: 1.5rem !important;
  }

  .ps-lg-5 {
    padding-left: 3rem !important;
  }

  .text-lg-start {
    text-align: left !important;
  }

  .text-lg-end {
    text-align: right !important;
  }

  .text-lg-center {
    text-align: center !important;
  }
}

@media (min-width: 1200px) {
  .float-xl-start {
    float: left !important;
  }

  .float-xl-end {
    float: right !important;
  }

  .float-xl-none {
    float: none !important;
  }

  .d-xl-inline {
    display: inline !important;
  }

  .d-xl-inline-block {
    display: inline-block !important;
  }

  .d-xl-block {
    display: block !important;
  }

  .d-xl-grid {
    display: grid !important;
  }

  .d-xl-table {
    display: table !important;
  }

  .d-xl-table-row {
    display: table-row !important;
  }

  .d-xl-table-cell {
    display: table-cell !important;
  }

  .d-xl-flex {
    display: flex !important;
  }

  .d-xl-inline-flex {
    display: inline-flex !important;
  }

  .d-xl-none {
    display: none !important;
  }

  .flex-xl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xl-row {
    flex-direction: row !important;
  }

  .flex-xl-column {
    flex-direction: column !important;
  }

  .flex-xl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xl-0 {
    gap: 0 !important;
  }

  .gap-xl-1 {
    gap: 0.25rem !important;
  }

  .gap-xl-2 {
    gap: 0.5rem !important;
  }

  .gap-xl-3 {
    gap: 1rem !important;
  }

  .gap-xl-4 {
    gap: 1.5rem !important;
  }

  .gap-xl-5 {
    gap: 3rem !important;
  }

  .justify-content-xl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xl-center {
    justify-content: center !important;
  }

  .justify-content-xl-between {
    justify-content: space-between !important;
  }

  .justify-content-xl-around {
    justify-content: space-around !important;
  }

  .justify-content-xl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xl-start {
    align-items: flex-start !important;
  }

  .align-items-xl-end {
    align-items: flex-end !important;
  }

  .align-items-xl-center {
    align-items: center !important;
  }

  .align-items-xl-baseline {
    align-items: baseline !important;
  }

  .align-items-xl-stretch {
    align-items: stretch !important;
  }

  .align-content-xl-start {
    align-content: flex-start !important;
  }

  .align-content-xl-end {
    align-content: flex-end !important;
  }

  .align-content-xl-center {
    align-content: center !important;
  }

  .align-content-xl-between {
    align-content: space-between !important;
  }

  .align-content-xl-around {
    align-content: space-around !important;
  }

  .align-content-xl-stretch {
    align-content: stretch !important;
  }

  .align-self-xl-auto {
    align-self: auto !important;
  }

  .align-self-xl-start {
    align-self: flex-start !important;
  }

  .align-self-xl-end {
    align-self: flex-end !important;
  }

  .align-self-xl-center {
    align-self: center !important;
  }

  .align-self-xl-baseline {
    align-self: baseline !important;
  }

  .align-self-xl-stretch {
    align-self: stretch !important;
  }

  .order-xl-first {
    order: -1 !important;
  }

  .order-xl-0 {
    order: 0 !important;
  }

  .order-xl-1 {
    order: 1 !important;
  }

  .order-xl-2 {
    order: 2 !important;
  }

  .order-xl-3 {
    order: 3 !important;
  }

  .order-xl-4 {
    order: 4 !important;
  }

  .order-xl-5 {
    order: 5 !important;
  }

  .order-xl-last {
    order: 6 !important;
  }

  .m-xl-0 {
    margin: 0 !important;
  }

  .m-xl-1 {
    margin: 0.25rem !important;
  }

  .m-xl-2 {
    margin: 0.5rem !important;
  }

  .m-xl-3 {
    margin: 1rem !important;
  }

  .m-xl-4 {
    margin: 1.5rem !important;
  }

  .m-xl-5 {
    margin: 3rem !important;
  }

  .m-xl-auto {
    margin: auto !important;
  }

  .mx-xl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xl-0 {
    margin-top: 0 !important;
  }

  .mt-xl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xl-3 {
    margin-top: 1rem !important;
  }

  .mt-xl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xl-5 {
    margin-top: 3rem !important;
  }

  .mt-xl-auto {
    margin-top: auto !important;
  }

  .me-xl-0 {
    margin-right: 0 !important;
  }

  .me-xl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xl-3 {
    margin-right: 1rem !important;
  }

  .me-xl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xl-5 {
    margin-right: 3rem !important;
  }

  .me-xl-auto {
    margin-right: auto !important;
  }

  .mb-xl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xl-auto {
    margin-bottom: auto !important;
  }

  .ms-xl-0 {
    margin-left: 0 !important;
  }

  .ms-xl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xl-3 {
    margin-left: 1rem !important;
  }

  .ms-xl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xl-5 {
    margin-left: 3rem !important;
  }

  .ms-xl-auto {
    margin-left: auto !important;
  }

  .p-xl-0 {
    padding: 0 !important;
  }

  .p-xl-1 {
    padding: 0.25rem !important;
  }

  .p-xl-2 {
    padding: 0.5rem !important;
  }

  .p-xl-3 {
    padding: 1rem !important;
  }

  .p-xl-4 {
    padding: 1.5rem !important;
  }

  .p-xl-5 {
    padding: 3rem !important;
  }

  .px-xl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xl-0 {
    padding-top: 0 !important;
  }

  .pt-xl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xl-3 {
    padding-top: 1rem !important;
  }

  .pt-xl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xl-5 {
    padding-top: 3rem !important;
  }

  .pe-xl-0 {
    padding-right: 0 !important;
  }

  .pe-xl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xl-3 {
    padding-right: 1rem !important;
  }

  .pe-xl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xl-5 {
    padding-right: 3rem !important;
  }

  .pb-xl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xl-0 {
    padding-left: 0 !important;
  }

  .ps-xl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xl-3 {
    padding-left: 1rem !important;
  }

  .ps-xl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xl-5 {
    padding-left: 3rem !important;
  }

  .text-xl-start {
    text-align: left !important;
  }

  .text-xl-end {
    text-align: right !important;
  }

  .text-xl-center {
    text-align: center !important;
  }
}

@media (min-width: 1500px) {
  .float-xxl-start {
    float: left !important;
  }

  .float-xxl-end {
    float: right !important;
  }

  .float-xxl-none {
    float: none !important;
  }

  .d-xxl-inline {
    display: inline !important;
  }

  .d-xxl-inline-block {
    display: inline-block !important;
  }

  .d-xxl-block {
    display: block !important;
  }

  .d-xxl-grid {
    display: grid !important;
  }

  .d-xxl-table {
    display: table !important;
  }

  .d-xxl-table-row {
    display: table-row !important;
  }

  .d-xxl-table-cell {
    display: table-cell !important;
  }

  .d-xxl-flex {
    display: flex !important;
  }

  .d-xxl-inline-flex {
    display: inline-flex !important;
  }

  .d-xxl-none {
    display: none !important;
  }

  .flex-xxl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xxl-row {
    flex-direction: row !important;
  }

  .flex-xxl-column {
    flex-direction: column !important;
  }

  .flex-xxl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xxl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xxl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xxl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xxl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xxl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xxl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xxl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xxl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xxl-0 {
    gap: 0 !important;
  }

  .gap-xxl-1 {
    gap: 0.25rem !important;
  }

  .gap-xxl-2 {
    gap: 0.5rem !important;
  }

  .gap-xxl-3 {
    gap: 1rem !important;
  }

  .gap-xxl-4 {
    gap: 1.5rem !important;
  }

  .gap-xxl-5 {
    gap: 3rem !important;
  }

  .justify-content-xxl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xxl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xxl-center {
    justify-content: center !important;
  }

  .justify-content-xxl-between {
    justify-content: space-between !important;
  }

  .justify-content-xxl-around {
    justify-content: space-around !important;
  }

  .justify-content-xxl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xxl-start {
    align-items: flex-start !important;
  }

  .align-items-xxl-end {
    align-items: flex-end !important;
  }

  .align-items-xxl-center {
    align-items: center !important;
  }

  .align-items-xxl-baseline {
    align-items: baseline !important;
  }

  .align-items-xxl-stretch {
    align-items: stretch !important;
  }

  .align-content-xxl-start {
    align-content: flex-start !important;
  }

  .align-content-xxl-end {
    align-content: flex-end !important;
  }

  .align-content-xxl-center {
    align-content: center !important;
  }

  .align-content-xxl-between {
    align-content: space-between !important;
  }

  .align-content-xxl-around {
    align-content: space-around !important;
  }

  .align-content-xxl-stretch {
    align-content: stretch !important;
  }

  .align-self-xxl-auto {
    align-self: auto !important;
  }

  .align-self-xxl-start {
    align-self: flex-start !important;
  }

  .align-self-xxl-end {
    align-self: flex-end !important;
  }

  .align-self-xxl-center {
    align-self: center !important;
  }

  .align-self-xxl-baseline {
    align-self: baseline !important;
  }

  .align-self-xxl-stretch {
    align-self: stretch !important;
  }

  .order-xxl-first {
    order: -1 !important;
  }

  .order-xxl-0 {
    order: 0 !important;
  }

  .order-xxl-1 {
    order: 1 !important;
  }

  .order-xxl-2 {
    order: 2 !important;
  }

  .order-xxl-3 {
    order: 3 !important;
  }

  .order-xxl-4 {
    order: 4 !important;
  }

  .order-xxl-5 {
    order: 5 !important;
  }

  .order-xxl-last {
    order: 6 !important;
  }

  .m-xxl-0 {
    margin: 0 !important;
  }

  .m-xxl-1 {
    margin: 0.25rem !important;
  }

  .m-xxl-2 {
    margin: 0.5rem !important;
  }

  .m-xxl-3 {
    margin: 1rem !important;
  }

  .m-xxl-4 {
    margin: 1.5rem !important;
  }

  .m-xxl-5 {
    margin: 3rem !important;
  }

  .m-xxl-auto {
    margin: auto !important;
  }

  .mx-xxl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xxl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xxl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xxl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xxl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xxl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xxl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xxl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xxl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xxl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xxl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xxl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xxl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xxl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xxl-0 {
    margin-top: 0 !important;
  }

  .mt-xxl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xxl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xxl-3 {
    margin-top: 1rem !important;
  }

  .mt-xxl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xxl-5 {
    margin-top: 3rem !important;
  }

  .mt-xxl-auto {
    margin-top: auto !important;
  }

  .me-xxl-0 {
    margin-right: 0 !important;
  }

  .me-xxl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xxl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xxl-3 {
    margin-right: 1rem !important;
  }

  .me-xxl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xxl-5 {
    margin-right: 3rem !important;
  }

  .me-xxl-auto {
    margin-right: auto !important;
  }

  .mb-xxl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xxl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xxl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xxl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xxl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xxl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xxl-auto {
    margin-bottom: auto !important;
  }

  .ms-xxl-0 {
    margin-left: 0 !important;
  }

  .ms-xxl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xxl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xxl-3 {
    margin-left: 1rem !important;
  }

  .ms-xxl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xxl-5 {
    margin-left: 3rem !important;
  }

  .ms-xxl-auto {
    margin-left: auto !important;
  }

  .p-xxl-0 {
    padding: 0 !important;
  }

  .p-xxl-1 {
    padding: 0.25rem !important;
  }

  .p-xxl-2 {
    padding: 0.5rem !important;
  }

  .p-xxl-3 {
    padding: 1rem !important;
  }

  .p-xxl-4 {
    padding: 1.5rem !important;
  }

  .p-xxl-5 {
    padding: 3rem !important;
  }

  .px-xxl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xxl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xxl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xxl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xxl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xxl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xxl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xxl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xxl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xxl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xxl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xxl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xxl-0 {
    padding-top: 0 !important;
  }

  .pt-xxl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xxl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xxl-3 {
    padding-top: 1rem !important;
  }

  .pt-xxl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xxl-5 {
    padding-top: 3rem !important;
  }

  .pe-xxl-0 {
    padding-right: 0 !important;
  }

  .pe-xxl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xxl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xxl-3 {
    padding-right: 1rem !important;
  }

  .pe-xxl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xxl-5 {
    padding-right: 3rem !important;
  }

  .pb-xxl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xxl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xxl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xxl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xxl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xxl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xxl-0 {
    padding-left: 0 !important;
  }

  .ps-xxl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xxl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xxl-3 {
    padding-left: 1rem !important;
  }

  .ps-xxl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xxl-5 {
    padding-left: 3rem !important;
  }

  .text-xxl-start {
    text-align: left !important;
  }

  .text-xxl-end {
    text-align: right !important;
  }

  .text-xxl-center {
    text-align: center !important;
  }
}

@media (min-width: 1700px) {
  .float-xxxl-start {
    float: left !important;
  }

  .float-xxxl-end {
    float: right !important;
  }

  .float-xxxl-none {
    float: none !important;
  }

  .d-xxxl-inline {
    display: inline !important;
  }

  .d-xxxl-inline-block {
    display: inline-block !important;
  }

  .d-xxxl-block {
    display: block !important;
  }

  .d-xxxl-grid {
    display: grid !important;
  }

  .d-xxxl-table {
    display: table !important;
  }

  .d-xxxl-table-row {
    display: table-row !important;
  }

  .d-xxxl-table-cell {
    display: table-cell !important;
  }

  .d-xxxl-flex {
    display: flex !important;
  }

  .d-xxxl-inline-flex {
    display: inline-flex !important;
  }

  .d-xxxl-none {
    display: none !important;
  }

  .flex-xxxl-fill {
    flex: 1 1 auto !important;
  }

  .flex-xxxl-row {
    flex-direction: row !important;
  }

  .flex-xxxl-column {
    flex-direction: column !important;
  }

  .flex-xxxl-row-reverse {
    flex-direction: row-reverse !important;
  }

  .flex-xxxl-column-reverse {
    flex-direction: column-reverse !important;
  }

  .flex-xxxl-grow-0 {
    flex-grow: 0 !important;
  }

  .flex-xxxl-grow-1 {
    flex-grow: 1 !important;
  }

  .flex-xxxl-shrink-0 {
    flex-shrink: 0 !important;
  }

  .flex-xxxl-shrink-1 {
    flex-shrink: 1 !important;
  }

  .flex-xxxl-wrap {
    flex-wrap: wrap !important;
  }

  .flex-xxxl-nowrap {
    flex-wrap: nowrap !important;
  }

  .flex-xxxl-wrap-reverse {
    flex-wrap: wrap-reverse !important;
  }

  .gap-xxxl-0 {
    gap: 0 !important;
  }

  .gap-xxxl-1 {
    gap: 0.25rem !important;
  }

  .gap-xxxl-2 {
    gap: 0.5rem !important;
  }

  .gap-xxxl-3 {
    gap: 1rem !important;
  }

  .gap-xxxl-4 {
    gap: 1.5rem !important;
  }

  .gap-xxxl-5 {
    gap: 3rem !important;
  }

  .justify-content-xxxl-start {
    justify-content: flex-start !important;
  }

  .justify-content-xxxl-end {
    justify-content: flex-end !important;
  }

  .justify-content-xxxl-center {
    justify-content: center !important;
  }

  .justify-content-xxxl-between {
    justify-content: space-between !important;
  }

  .justify-content-xxxl-around {
    justify-content: space-around !important;
  }

  .justify-content-xxxl-evenly {
    justify-content: space-evenly !important;
  }

  .align-items-xxxl-start {
    align-items: flex-start !important;
  }

  .align-items-xxxl-end {
    align-items: flex-end !important;
  }

  .align-items-xxxl-center {
    align-items: center !important;
  }

  .align-items-xxxl-baseline {
    align-items: baseline !important;
  }

  .align-items-xxxl-stretch {
    align-items: stretch !important;
  }

  .align-content-xxxl-start {
    align-content: flex-start !important;
  }

  .align-content-xxxl-end {
    align-content: flex-end !important;
  }

  .align-content-xxxl-center {
    align-content: center !important;
  }

  .align-content-xxxl-between {
    align-content: space-between !important;
  }

  .align-content-xxxl-around {
    align-content: space-around !important;
  }

  .align-content-xxxl-stretch {
    align-content: stretch !important;
  }

  .align-self-xxxl-auto {
    align-self: auto !important;
  }

  .align-self-xxxl-start {
    align-self: flex-start !important;
  }

  .align-self-xxxl-end {
    align-self: flex-end !important;
  }

  .align-self-xxxl-center {
    align-self: center !important;
  }

  .align-self-xxxl-baseline {
    align-self: baseline !important;
  }

  .align-self-xxxl-stretch {
    align-self: stretch !important;
  }

  .order-xxxl-first {
    order: -1 !important;
  }

  .order-xxxl-0 {
    order: 0 !important;
  }

  .order-xxxl-1 {
    order: 1 !important;
  }

  .order-xxxl-2 {
    order: 2 !important;
  }

  .order-xxxl-3 {
    order: 3 !important;
  }

  .order-xxxl-4 {
    order: 4 !important;
  }

  .order-xxxl-5 {
    order: 5 !important;
  }

  .order-xxxl-last {
    order: 6 !important;
  }

  .m-xxxl-0 {
    margin: 0 !important;
  }

  .m-xxxl-1 {
    margin: 0.25rem !important;
  }

  .m-xxxl-2 {
    margin: 0.5rem !important;
  }

  .m-xxxl-3 {
    margin: 1rem !important;
  }

  .m-xxxl-4 {
    margin: 1.5rem !important;
  }

  .m-xxxl-5 {
    margin: 3rem !important;
  }

  .m-xxxl-auto {
    margin: auto !important;
  }

  .mx-xxxl-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
  }

  .mx-xxxl-1 {
    margin-right: 0.25rem !important;
    margin-left: 0.25rem !important;
  }

  .mx-xxxl-2 {
    margin-right: 0.5rem !important;
    margin-left: 0.5rem !important;
  }

  .mx-xxxl-3 {
    margin-right: 1rem !important;
    margin-left: 1rem !important;
  }

  .mx-xxxl-4 {
    margin-right: 1.5rem !important;
    margin-left: 1.5rem !important;
  }

  .mx-xxxl-5 {
    margin-right: 3rem !important;
    margin-left: 3rem !important;
  }

  .mx-xxxl-auto {
    margin-right: auto !important;
    margin-left: auto !important;
  }

  .my-xxxl-0 {
    margin-top: 0 !important;
    margin-bottom: 0 !important;
  }

  .my-xxxl-1 {
    margin-top: 0.25rem !important;
    margin-bottom: 0.25rem !important;
  }

  .my-xxxl-2 {
    margin-top: 0.5rem !important;
    margin-bottom: 0.5rem !important;
  }

  .my-xxxl-3 {
    margin-top: 1rem !important;
    margin-bottom: 1rem !important;
  }

  .my-xxxl-4 {
    margin-top: 1.5rem !important;
    margin-bottom: 1.5rem !important;
  }

  .my-xxxl-5 {
    margin-top: 3rem !important;
    margin-bottom: 3rem !important;
  }

  .my-xxxl-auto {
    margin-top: auto !important;
    margin-bottom: auto !important;
  }

  .mt-xxxl-0 {
    margin-top: 0 !important;
  }

  .mt-xxxl-1 {
    margin-top: 0.25rem !important;
  }

  .mt-xxxl-2 {
    margin-top: 0.5rem !important;
  }

  .mt-xxxl-3 {
    margin-top: 1rem !important;
  }

  .mt-xxxl-4 {
    margin-top: 1.5rem !important;
  }

  .mt-xxxl-5 {
    margin-top: 3rem !important;
  }

  .mt-xxxl-auto {
    margin-top: auto !important;
  }

  .me-xxxl-0 {
    margin-right: 0 !important;
  }

  .me-xxxl-1 {
    margin-right: 0.25rem !important;
  }

  .me-xxxl-2 {
    margin-right: 0.5rem !important;
  }

  .me-xxxl-3 {
    margin-right: 1rem !important;
  }

  .me-xxxl-4 {
    margin-right: 1.5rem !important;
  }

  .me-xxxl-5 {
    margin-right: 3rem !important;
  }

  .me-xxxl-auto {
    margin-right: auto !important;
  }

  .mb-xxxl-0 {
    margin-bottom: 0 !important;
  }

  .mb-xxxl-1 {
    margin-bottom: 0.25rem !important;
  }

  .mb-xxxl-2 {
    margin-bottom: 0.5rem !important;
  }

  .mb-xxxl-3 {
    margin-bottom: 1rem !important;
  }

  .mb-xxxl-4 {
    margin-bottom: 1.5rem !important;
  }

  .mb-xxxl-5 {
    margin-bottom: 3rem !important;
  }

  .mb-xxxl-auto {
    margin-bottom: auto !important;
  }

  .ms-xxxl-0 {
    margin-left: 0 !important;
  }

  .ms-xxxl-1 {
    margin-left: 0.25rem !important;
  }

  .ms-xxxl-2 {
    margin-left: 0.5rem !important;
  }

  .ms-xxxl-3 {
    margin-left: 1rem !important;
  }

  .ms-xxxl-4 {
    margin-left: 1.5rem !important;
  }

  .ms-xxxl-5 {
    margin-left: 3rem !important;
  }

  .ms-xxxl-auto {
    margin-left: auto !important;
  }

  .p-xxxl-0 {
    padding: 0 !important;
  }

  .p-xxxl-1 {
    padding: 0.25rem !important;
  }

  .p-xxxl-2 {
    padding: 0.5rem !important;
  }

  .p-xxxl-3 {
    padding: 1rem !important;
  }

  .p-xxxl-4 {
    padding: 1.5rem !important;
  }

  .p-xxxl-5 {
    padding: 3rem !important;
  }

  .px-xxxl-0 {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .px-xxxl-1 {
    padding-right: 0.25rem !important;
    padding-left: 0.25rem !important;
  }

  .px-xxxl-2 {
    padding-right: 0.5rem !important;
    padding-left: 0.5rem !important;
  }

  .px-xxxl-3 {
    padding-right: 1rem !important;
    padding-left: 1rem !important;
  }

  .px-xxxl-4 {
    padding-right: 1.5rem !important;
    padding-left: 1.5rem !important;
  }

  .px-xxxl-5 {
    padding-right: 3rem !important;
    padding-left: 3rem !important;
  }

  .py-xxxl-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
  }

  .py-xxxl-1 {
    padding-top: 0.25rem !important;
    padding-bottom: 0.25rem !important;
  }

  .py-xxxl-2 {
    padding-top: 0.5rem !important;
    padding-bottom: 0.5rem !important;
  }

  .py-xxxl-3 {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
  }

  .py-xxxl-4 {
    padding-top: 1.5rem !important;
    padding-bottom: 1.5rem !important;
  }

  .py-xxxl-5 {
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
  }

  .pt-xxxl-0 {
    padding-top: 0 !important;
  }

  .pt-xxxl-1 {
    padding-top: 0.25rem !important;
  }

  .pt-xxxl-2 {
    padding-top: 0.5rem !important;
  }

  .pt-xxxl-3 {
    padding-top: 1rem !important;
  }

  .pt-xxxl-4 {
    padding-top: 1.5rem !important;
  }

  .pt-xxxl-5 {
    padding-top: 3rem !important;
  }

  .pe-xxxl-0 {
    padding-right: 0 !important;
  }

  .pe-xxxl-1 {
    padding-right: 0.25rem !important;
  }

  .pe-xxxl-2 {
    padding-right: 0.5rem !important;
  }

  .pe-xxxl-3 {
    padding-right: 1rem !important;
  }

  .pe-xxxl-4 {
    padding-right: 1.5rem !important;
  }

  .pe-xxxl-5 {
    padding-right: 3rem !important;
  }

  .pb-xxxl-0 {
    padding-bottom: 0 !important;
  }

  .pb-xxxl-1 {
    padding-bottom: 0.25rem !important;
  }

  .pb-xxxl-2 {
    padding-bottom: 0.5rem !important;
  }

  .pb-xxxl-3 {
    padding-bottom: 1rem !important;
  }

  .pb-xxxl-4 {
    padding-bottom: 1.5rem !important;
  }

  .pb-xxxl-5 {
    padding-bottom: 3rem !important;
  }

  .ps-xxxl-0 {
    padding-left: 0 !important;
  }

  .ps-xxxl-1 {
    padding-left: 0.25rem !important;
  }

  .ps-xxxl-2 {
    padding-left: 0.5rem !important;
  }

  .ps-xxxl-3 {
    padding-left: 1rem !important;
  }

  .ps-xxxl-4 {
    padding-left: 1.5rem !important;
  }

  .ps-xxxl-5 {
    padding-left: 3rem !important;
  }

  .text-xxxl-start {
    text-align: left !important;
  }

  .text-xxxl-end {
    text-align: right !important;
  }

  .text-xxxl-center {
    text-align: center !important;
  }
}

@media (min-width: 1200px) {
  .fs-1 {
    font-size: 5rem !important;
  }

  .fs-2 {
    font-size: 2rem !important;
  }

  .fs-3 {
    font-size: 1.625rem !important;
  }

  .fs-sm-1 {
    font-size: 5rem !important;
  }

  .fs-sm-2 {
    font-size: 2rem !important;
  }

  .fs-sm-3 {
    font-size: 1.625rem !important;
  }

  .fs-md-1 {
    font-size: 5rem !important;
  }

  .fs-md-2 {
    font-size: 2rem !important;
  }

  .fs-md-3 {
    font-size: 1.625rem !important;
  }

  .fs-lg-1 {
    font-size: 5rem !important;
  }

  .fs-lg-2 {
    font-size: 2rem !important;
  }

  .fs-lg-3 {
    font-size: 1.625rem !important;
  }
}

@media print {
  .d-print-inline {
    display: inline !important;
  }

  .d-print-inline-block {
    display: inline-block !important;
  }

  .d-print-block {
    display: block !important;
  }

  .d-print-grid {
    display: grid !important;
  }

  .d-print-table {
    display: table !important;
  }

  .d-print-table-row {
    display: table-row !important;
  }

  .d-print-table-cell {
    display: table-cell !important;
  }

  .d-print-flex {
    display: flex !important;
  }

  .d-print-inline-flex {
    display: inline-flex !important;
  }

  .d-print-none {
    display: none !important;
  }
}

/*! =========================================================
 * bootstrap-slider.js
 *
 * Maintainers:
 *    Kyle Kemp
 *      - Twitter: @seiyria
 *      - Github:  seiyria
 *    Rohit Kalkur
 *      - Twitter: @Rovolutionary
 *      - Github:  rovolution
 *
 * =========================================================
 *
 * bootstrap-slider is released under the MIT License
 * Copyright (c) 2019 Kyle Kemp, Rohit Kalkur, and contributors
 * 
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * ========================================================= */
/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
.slider {
  display: inline-block;
  vertical-align: middle;
  position: relative;
}

.slider.slider-horizontal {
  width: 100%;
  height: 18px;
}

.slider.slider-horizontal .slider-track {
  height: 6px;
  width: 100%;
  margin-top: 6px;
  top: 0;
  left: 0;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
}

.slider.slider-horizontal .slider-selection,
.slider.slider-horizontal .slider-track-low,
.slider.slider-horizontal .slider-track-high {
  height: 100%;
  top: 0;
  bottom: 0;
}

.slider.slider-horizontal .slider-tick,
.slider.slider-horizontal .slider-handle {
  margin-left: -9px;
}

.slider.slider-horizontal .slider-tick.triangle,
.slider.slider-horizontal .slider-handle.triangle {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  border-width: 0 9px 9px 9px;
  width: 0;
  height: 0;
  border-bottom-color: #151515;
  margin-top: 0;
}

.slider.slider-horizontal .slider-handle.min-slider-handle {
  margin-left: 0;
}

.slider.slider-horizontal .slider-handle.max-slider-handle {
  margin-left: -18px;
}

.slider.slider-horizontal .slider-tick-container {
  white-space: nowrap;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
}

.slider.slider-horizontal .slider-tick-label-container {
  white-space: nowrap;
  margin-top: 18px;
}

.slider.slider-horizontal .slider-tick-label-container .slider-tick-label {
  display: inline-block;
  text-align: center;
}

.slider.slider-horizontal.slider-rtl .slider-track {
  left: initial;
  right: 0;
}

.slider.slider-horizontal.slider-rtl .slider-tick,
.slider.slider-horizontal.slider-rtl .slider-handle {
  margin-left: initial;
  margin-right: -9px;
}

.slider.slider-horizontal.slider-rtl .slider-tick-container {
  left: initial;
  right: 0;
}

.slider.slider-vertical {
  height: 210px;
  width: 18px;
}

.slider.slider-vertical .slider-track {
  width: 9px;
  height: 100%;
  left: 25%;
  top: 0;
}

.slider.slider-vertical .slider-selection {
  width: 100%;
  left: 0;
  top: 0;
  bottom: 0;
}

.slider.slider-vertical .slider-track-low,
.slider.slider-vertical .slider-track-high {
  width: 100%;
  left: 0;
  right: 0;
}

.slider.slider-vertical .slider-tick,
.slider.slider-vertical .slider-handle {
  margin-top: -6px;
}

.slider.slider-vertical .slider-tick.triangle,
.slider.slider-vertical .slider-handle.triangle {
  border-width: 9px 0 9px 9px;
  width: 1px;
  height: 1px;
  border-left-color: #151515;
  margin-left: 0;
}

.slider.slider-vertical .slider-tick-label-container {
  white-space: nowrap;
}

.slider.slider-vertical .slider-tick-label-container .slider-tick-label {
  padding-left: 3.6px;
}

.slider.slider-vertical.slider-rtl .slider-track {
  left: initial;
  right: 25%;
}

.slider.slider-vertical.slider-rtl .slider-selection {
  left: initial;
  right: 0;
}

.slider.slider-vertical.slider-rtl .slider-tick.triangle,
.slider.slider-vertical.slider-rtl .slider-handle.triangle {
  border-width: 9px 9px 9px 0;
}

.slider.slider-vertical.slider-rtl .slider-tick-label-container .slider-tick-label {
  padding-left: initial;
  padding-right: 3.6px;
}

.slider.slider-disabled .slider-handle {
  background-color: #cfcfcf;
  background-image: -moz-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#DFDFDF), to(#BEBEBE));
  background-image: -webkit-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: -o-linear-gradient(top, #DFDFDF, #BEBEBE);
  background-image: linear-gradient(to bottom, #DFDFDF, #BEBEBE);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#DFDFDF', endColorstr='#BEBEBE', GradientType=0);
}

.slider.slider-disabled .slider-track {
  background-color: #e7e7e7;
  background-image: -moz-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#E5E5E5), to(#E9E9E9));
  background-image: -webkit-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: -o-linear-gradient(top, #E5E5E5, #E9E9E9);
  background-image: linear-gradient(to bottom, #E5E5E5, #E9E9E9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#E5E5E5', endColorstr='#E9E9E9', GradientType=0);
  cursor: not-allowed;
}

.slider input {
  display: none;
}

.slider .tooltip-inner {
  white-space: nowrap;
  max-width: none;
  border: 1px solid #e7e7ec;
  border-radius: 0;
  background-color: #fff;
  color: #222222;
  box-shadow: 0 8px 15px 0 rgba(140, 152, 164, 0.1);
}

.slider .bs-tooltip-top .tooltip-inner,
.slider .bs-tooltip-auto[data-popper-placement^="top"] .tooltip-inner,
.slider .bs-tooltip-bottom .tooltip-inner,
.slider .bs-tooltip-auto[data-popper-placement^="bottom"] .tooltip-inner {
  position: relative;
  left: -50%;
}

.slider.bs-tooltip-left .tooltip-inner,
.slider.bs-tooltip-right .tooltip-inner {
  position: relative;
  top: -100%;
}

.slider .tooltip {
  pointer-events: none;
}

.slider .tooltip.bs-tooltip-top .arrow,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="top"] .arrow,
.slider .tooltip.bs-tooltip-bottom .arrow,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="bottom"] .arrow {
  left: -.4rem;
}

.slider .tooltip.bs-tooltip-top,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="top"] {
  margin-top: -44px;
}

.slider .tooltip.bs-tooltip-bottom,
.slider .tooltip.bs-tooltip-auto[data-popper-placement^="bottom"] {
  margin-top: 2px;
}

.slider .tooltip.bs-tooltip-left,
.slider .tooltip.bs-tooltip-right {
  margin-top: -14px;
}

.slider .tooltip.bs-tooltip-left .arrow,
.slider .tooltip.bs-tooltip-right .arrow {
  top: 8px;
}

.slider .tooltip.tooltip-min {
  transform: translateX(50%);
}

.slider .tooltip.tooltip-max {
  transform: translateX(-50%);
}

.slider .hide {
  display: none;
}

.slider-track {
  position: absolute;
  background-color: #e4e4e4;
  cursor: pointer;
}

.slider-selection {
  position: absolute;
  background-color: #222222;
}

.slider-selection.tick-slider-selection {
  background-color: #6f5858;
  background-image: -moz-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#7e5454), to(#5f5b5b));
  background-image: -webkit-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -o-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: linear-gradient(to bottom, #7e5454, #5f5b5b);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#7e5454', endColorstr='#5f5b5b', GradientType=0);
}

.slider-track-low,
.slider-track-high {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  border-radius: 10px;
  position: absolute;
  background: transparent;
}

.slider-handle {
  position: absolute;
  top: 0;
  width: 18px;
  height: 18px;
  background-color: #ffffff;
  border: 0.125rem solid #222222;
}

.slider-handle:hover {
  cursor: pointer;
}

.slider-handle.round {
  -webkit-border-radius: 18px;
  -moz-border-radius: 18px;
  border-radius: 18px;
}

.slider-handle.triangle {
  background: transparent none;
}

.slider-handle.custom {
  background: transparent none;
}

.slider-handle.custom::before {
  line-height: 18px;
  font-size: 20px;
  content: '\2605';
  color: #726204;
}

.slider-tick {
  background-color: #f7f7f7;
  background-image: -moz-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#F5F5F5), to(#F9F9F9));
  background-image: -webkit-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: -o-linear-gradient(top, #F5F5F5, #F9F9F9);
  background-image: linear-gradient(to bottom, #F5F5F5, #F9F9F9);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#F5F5F5', endColorstr='#F9F9F9', GradientType=0);
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -moz-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  position: absolute;
  cursor: pointer;
  width: 18px;
  height: 18px;
  filter: none;
  opacity: 0.8;
  border: 0px solid transparent;
}

.slider-tick.round {
  border-radius: 50%;
}

.slider-tick.triangle {
  background: transparent none;
}

.slider-tick.custom {
  background: transparent none;
}

.slider-tick.custom::before {
  line-height: 18px;
  font-size: 20px;
  content: '\2605';
  color: #726204;
}

.slider-tick.in-selection {
  background-color: #6f5858;
  background-image: -moz-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#7e5454), to(#5f5b5b));
  background-image: -webkit-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: -o-linear-gradient(top, #7e5454, #5f5b5b);
  background-image: linear-gradient(to bottom, #7e5454, #5f5b5b);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#7e5454', endColorstr='#5f5b5b', GradientType=0);
  opacity: 1;
}

/*-----------------------------------------------*/
/*------------------ Base Colors ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Typography -----------------*/
/*-----------------------------------------------*/
/*------------------ Page Title -----------------*/
/*---------------- Section Title ----------------*/
/*----------------- Block Title -----------------*/
/*------------------ Tab Title ------------------*/
/*----------------- Text content ----------------*/
/*----------------- Blockquote ------------------*/
/*------------------ List style -----------------*/
/*-----------------------------------------------*/
/*-------------------- Layout -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Compontents ----------------*/
/*-----------------------------------------------*/
/*-------------------- Table --------------------*/
/*-------------------- Alert --------------------*/
/*-------------------- Buttons --------------------*/
/*---------------------- List ---------------------*/
/*---------------------- Form ---------------------*/
/*------------------ Accordions -----------------*/
/*--------------------- Tabs --------------------*/
/*----------------- Range Slider ----------------*/
/*----------------- Progressbar -----------------*/
/*-----------------------------------------------*/
/*-------------------- Header -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*--------------------- Menu --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Footer -------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Aside Popup -----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*-------------------- Modal --------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*----------------- Text content ----------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Swatches ------------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------- Rating Stars --------------*/
/*-----------------------------------------------*/
/*-----------------------------------------------*/
/*------------------ Shop Checkout --------------*/
/*-----------------------------------------------*/
body {
  background-color: #ffffff;
}

.flex-1 {
  flex: 1 !important;
}

.bg-black {
  background-color: #222222 !important;
}

.bg-grey-faf9f8 {
  background-color: #FAF9F8 !important;
}

.bg-grey-eeeeee {
  background-color: #EEE !important;
}

.bg-grey-f7f5ee {
  background-color: #f7f5ee !important;
}

.bg-yellow {
  background-color: #F3EDDF !important;
}

.bg-yellow-ffd35b {
  background-color: #FFD35B !important;
}

.bg-light-green-e4f5f2 {
  background-color: #e4f5f2 !important;
}

.color-white {
  color: #fff !important;
}

.color-gray-5a5a5a {
  color: #5a5a5a !important;
}

.bottom-3 {
  bottom: 3rem !important;
}

.object-fit-cover {
  object-fit: cover;
}

.object-position-top {
  object-position: top;
}

.background-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center center;
}

.background-img_overlay::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(34, 34, 34, 0.4);
}

.hover__content,
.js-hidden-content {
  position: absolute;
  top: 100%;
  width: 100%;
  min-width: 16rem;
  transition: all 0.2s ease;
  background-color: #ffffff;
  box-shadow: 0 0 1.5625rem 0 rgba(34, 34, 34, 0.05);
  opacity: 0;
  visibility: hidden;
  z-index: 1000;
}

.hover-container:hover .hover__content,
.hover-container.js-content_visible .js-hidden-content {
  opacity: 1;
  visibility: visible;
}

.content_abs {
  position: absolute;
  --content-space: 1.875rem;
}

.content_center {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.content_top {
  top: var(--content-space);
  padding-bottom: var(--content-space);
}

.content_right {
  right: var(--content-space);
  padding-left: var(--content-space);
}

.content_bottom {
  bottom: var(--content-space);
  padding-top: var(--content-space);
}

.content_left {
  left: var(--content-space);
  padding-right: var(--content-space);
}

@media (min-width: 768px) {
  .content_top-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_right-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_bottom-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 768px) {
  .content_left-lg {
    --content-space: 2.5rem;
  }
}

@media (min-width: 1200px) {
  .content_top-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_right-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_bottom-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 1200px) {
  .content_left-xl {
    --content-space: 3.125rem;
  }
}

@media (min-width: 992px) {
  .h-md-100 {
    height: 100% !important;
  }
}

.pos_right-center {
  left: 50%;
}

.pos_right-center-71 {
  left: 71%;
}

@media (min-width: 992px) {
  .pos_right-center {
    left: 60%;
  }

  .pos_right-center-70 {
    left: 70%;
  }
}

.scrollbar-gray ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  height: .25rem;
  background-color: #eeeeee;
}

.scrollbar-gray ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #767676;
}

.sticky-content {
  position: sticky;
  top: 0;
  padding-bottom: 1px;
}

.border-circle {
  border-radius: 10rem !important;
}

.border-radius-0 {
  border-radius: 0 !important;
}

.border-radius-4 {
  border-radius: 4px !important;
}

.border-radius-8 {
  border-radius: 8px !important;
}

.border-radius-10 {
  border-radius: 10px !important;
}

.swiper-scrollbar {
  height: 4px;
}

.left-auto {
  left: auto !important;
}

.right-auto {
  right: auto !important;
}

.left-0 {
  left: 0 !important;
}

.right-0 {
  right: 0 !important;
}

.position-center {
  left: 50% !important;
  top: 50% !important;
  transform: translate(-50%, -50%) !important;
}

.position-top-center {
  left: 50% !important;
  top: 0;
  transform: translateX(-50%) !important;
}

.position-right-center {
  left: auto !important;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  max-width: 50%;
}

.position-right-bottom {
  left: auto !important;
  right: 0;
  top: auto;
  bottom: 0;
  max-width: 50%;
}

.left-50 {
  left: 50%;
  transform: translateX(-50%);
}

@media (min-width: 1200px) {
  .row-cols-xl-8>* {
    flex: 0 0 auto;
    width: 12.5% !important;
  }
}

.minh-100 {
  min-height: 100vh;
}

.minh-240 {
  min-height: 16rem;
}

.rect-circle {
  width: 100%;
  padding-top: 100%;
  position: relative;
  border-radius: 10rem;
}

.bg-image {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.bg-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bg-video {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: -1;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-video {
  position: absolute;
  left: 0.3125rem;
  right: 0.3125rem;
  top: 0.3125rem;
  bottom: 0.3125rem;
  z-index: -1;
  width: calc(100% - 0.625rem);
  height: calc(100% - 0.625rem);
  object-fit: cover;
}

.border-left-0 {
  border-left: 0;
}

@media (min-width: 992px) {
  .border-left-lg-1 {
    border-left: 1px solid #eee;
  }
}

.border-top-1 {
  border-top: 1px solid #eee;
}

@media (min-width: 992px) {
  .border-top-lg-0 {
    border-top: 0;
  }
}

.border-1 {
  border: 1px solid #eee !important;
}

.border-white {
  border-color: #fff !important;
}

.object-position-right {
  object-position: 90% center;
}

.popover {
  border: 0;
  box-shadow: 0 0 1rem rgba(0, 0, 0, 0.1);
  border-radius: 0;
}

.popover img {
  width: 170px;
}

.bs-popover-end>.popover-arrow,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow {
  margin: 0;
}

.bs-popover-end>.popover-arrow:before,
.bs-popover-auto[data-popper-placement^="right"]>.popover-arrow:before {
  border-color: transparent;
}

.text-yellow-bg-rounded {
  display: inline-block;
  background-color: #FFD35B;
  padding: 0.5125rem 1rem 0.3125rem;
  border-radius: 2rem;
}

.mb--1 {
  margin-bottom: -1px;
}

.mb-1px {
  margin-bottom: 1px;
}

.body-color {
  color: #222222 !important;
}

.body-color-secondary {
  color: #767676 !important;
}

.theme-color {
  color: #193174 !important;
}

.theme-bg-color {
  background-color: #193174 !important;
}

.theme-color-secondary {
  color: #EBB73F !important;
}

.theme-bg-color-secondary {
  background-color: #EBB73F !important;
}

.theme-color-third {
  color: #86BC42 !important;
}

.theme-bg-color-third {
  background-color: #86BC42 !important;
}

.text-shadow-white {
  text-shadow: 0 0 0.1rem #ffffff;
}

.text-outline-white {
  color: #222222; /* Fill color of the text */
  text-shadow: 
  -1px -1px 0 1px #afafaf,  
  1px -1px 0 1px #afafaf,
  -1px 1px 0 1px #afafaf,
  1px 1px 0 1px #afafaf; /* Width and color of the outline */
}


@media (min-width: 768px) {
  .h-md-100 {
    height: 100% !important;
  }
}

@media (min-width: 576px) {
  .h-sm-100 {
    height: 100% !important;
  }
}

svg.flaticon {
  display: block;
}

.transparent-bg {
  background-color: transparent !important;
}

.bg-white-overlay {
  background-color: rgba(255, 255, 255, 0.9);
}

.pt-100per {
  padding-top: 100% !important;
}

@media (min-width: 768px) {
  .text-md-right {
    text-align: right !important;
  }

  .order-md-12 {
    order: 12;
  }
}

@media (min-width: 992px) {
  .order-lg--1 {
    order: -1;
  }
}

@media (min-width: 992px) {
  .mt-lg--5 {
    margin-top: -13rem !important;
  }
}

.mt--3 {
  margin-top: -3rem !important;
}

.swiper-scrollbar-drag {
  background-color: rgba(0, 0, 0, 0.5);
}

@font-face {
  font-family: 'SofiaProBold';
  src: url(../fonts/SofiaProBold.woff);
}

body {
  color: #222222;
  font-family: "Jost", sans-serif;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
}

/*============================================*/
/*================= Headings =================*/
/*============================================*/
h1,
.h1,
h2,
.h2,
h3,
.h3,
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  color: #222222;
  font-family: "Jost", sans-serif;
  font-weight: 500;
}

.font-special {
  font-family: "Allura", cursive;
}

.font-courgette {
  font-family: Courgette;
}

.fs-base,
.form-title {
  font-size: 0.875rem !important;
}

.font-sofia {
  font-family: 'SofiaProBold';
}

.third-color {
  color: #b9a16b !important;
}

.white-color {
  color: #fff !important;
}

.mark-grey-color {
  -webkit-text-stroke-color: #c2c2c2;
}

.page-title {
  font-weight: 700;
}

@media (min-width: 992px) {
  .page-title {
    font-size: 3.125rem;
  }
}

.section-title {
  font-size: 1.625rem;
}

@media (min-width: 992px) {
  .section-title {
    font-size: 2.1875rem;
  }
}

.lh-30 {
  line-height: 1.875rem !important;
}

.lh-2rem {
  line-height: 2rem !important;
}

.block-title {
  margin-bottom: 1rem;
  font-size: 1rem;
}

/*============================================*/
/*=================== Texts ==================*/
/*============================================*/
.character_markup {
  display: none;
}

@media (min-width: 1500px) {
  .character_markup {
    display: block;
    position: absolute;
    bottom: 5rem;
    margin-left: -1.5em;
    -webkit-text-stroke-width: 3px;
    -webkit-text-stroke-color: #ffffff;
    color: transparent;
    font-size: 7.5rem;
    transform: rotate(90deg);
    transform-origin: bottom right;
    opacity: 0.8;
  }

  .character_markup.type2 {
    transform: none;
    font-size: 15.625rem;
    -webkit-text-stroke-color: #767676;
    font-weight: 700;
    bottom: 0;
    line-height: 1;
    left: auto;
    margin: 0;
    right: 0;
    opacity: 0.3;
    letter-spacing: 0.05em;
    z-index: -1;
  }
}

.content {
  margin-bottom: 1.5rem;
  font-size: 0.875rem;
  line-height: 1.7143;
}

.blockquote {
  padding: calc(1.4rem + 1.8vw) calc(1.3625rem + 1.35vw) calc(1.35625rem + 1.275vw) calc(1.4875rem + 2.85vw);
  background-color: #faf9f8;
}

@media (min-width: 1200px) {
  .blockquote {
    padding: 2.75rem 2.375rem 2.3125rem 3.625rem;
  }
}

.blockquote__content {
  margin-bottom: 0;
  font-size: 1rem;
  font-style: italic;
  font-weight: 500;
  line-height: 1.375;
}

.blockquote__footer {
  margin-top: 1.5rem;
  color: #767676;
  font-size: 0.875rem;
}

.text-list {
  padding-left: 1.25em;
}

.text-list__item {
  line-height: 3.143;
}

.list_dot_darkgray ::marker {
  color: #767676;
  font-size: 1rem;
}

.list-style_checkbox {
  display: flex;
  align-items: center;
}

.text_dash {
  position: relative;
  padding-left: 3.25rem;
}

.text_dash::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 2.5rem;
  height: 2px;
  margin-top: -1px;
  background-color: currentColor;
  color: inherit;
}

.text_dash_half {
  position: relative;
  padding-left: 2rem;
}

.text_dash_half::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  width: 1.25rem;
  height: 2px;
  margin-top: -1px;
  background-color: currentColor;
  color: inherit;
}

.stroke-text {
  --stroke-color: #222222;
  --stroke-width: 1px;
  color: #eeeeee;
  font-size: 2.25rem;
  opacity: 0.4;
  text-shadow: var(--stroke-width) 0 0 var(--stroke-color), calc(var(--stroke-width) * -1) 0 0 var(--stroke-color), 0 var(--stroke-width) 0 var(--stroke-color), 0 calc(var(--stroke-width) * -1) 0 var(--stroke-color);
}

@media (min-width: 992px) {
  .stroke-text {
    --stroke-width: 2px;
    font-size: 3.375rem;
  }
}

@media (min-width: 1200px) {
  .stroke-text {
    font-size: 5.625rem;
  }
}

.smooth-16 {
  text-shadow: calc(var(--stroke-width) * 1) calc(var(--stroke-width) * 0) 0 var(--stroke-color), calc(var(--stroke-width) * 0.9239) calc(var(--stroke-width) * 0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * 0.7071) calc(var(--stroke-width) * 0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * 0.3827) calc(var(--stroke-width) * 0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0) calc(var(--stroke-width) * 1) 0 var(--stroke-color), calc(var(--stroke-width) * -0.3827) calc(var(--stroke-width) * 0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * -0.7071) calc(var(--stroke-width) * 0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * -0.9239) calc(var(--stroke-width) * 0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * -1) calc(var(--stroke-width) * 0) 0 var(--stroke-color), calc(var(--stroke-width) * -0.9239) calc(var(--stroke-width) * -0.3827) 0 var(--stroke-color), calc(var(--stroke-width) * -0.7071) calc(var(--stroke-width) * -0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * -0.3827) calc(var(--stroke-width) * -0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0) calc(var(--stroke-width) * -1) 0 var(--stroke-color), calc(var(--stroke-width) * 0.3827) calc(var(--stroke-width) * -0.9239) 0 var(--stroke-color), calc(var(--stroke-width) * 0.7071) calc(var(--stroke-width) * -0.7071) 0 var(--stroke-color), calc(var(--stroke-width) * 0.9239) calc(var(--stroke-width) * -0.3827) 0 var(--stroke-color);
}

@media (min-width: 992px) {
  .text-lg-right {
    text-align: right !important;
  }
}

.fs-12 {
  font-size: 0.75rem !important;
}

.fs-13 {
  font-size: 0.8125rem !important;
}

.fs-15 {
  font-size: 0.9375rem !important;
}

.fs-18 {
  font-size: 1.125rem !important;
}

.fs-20 {
  font-size: 1.25rem;
}

.fs-22 {
  font-size: calc(1.2625rem + 0.15vw);
}

@media (min-width: 1200px) {
  .fs-22 {
    font-size: 1.375rem;
  }
}

.fs-25 {
  font-size: calc(1.28125rem + 0.375vw);
}

@media (min-width: 1200px) {
  .fs-25 {
    font-size: 1.5625rem;
  }
}

.fs-30 {
  font-size: calc(1.3125rem + 0.75vw);
}

@media (min-width: 1200px) {
  .fs-30 {
    font-size: 1.875rem;
  }
}

.fs-35 {
  font-size: calc(1.34375rem + 1.125vw);
}

@media (min-width: 1200px) {
  .fs-35 {
    font-size: 2.1875rem;
  }
}

.fs-40 {
  font-size: calc(1.375rem + 1.5vw);
}

@media (min-width: 1200px) {
  .fs-40 {
    font-size: 2.5rem;
  }
}

.fs-45 {
  font-size: calc(1.40625rem + 1.875vw);
}

@media (min-width: 1200px) {
  .fs-45 {
    font-size: 2.8125rem;
  }
}

.fs-50 {
  font-size: calc(1.4375rem + 2.25vw);
}

@media (min-width: 1200px) {
  .fs-50 {
    font-size: 3.125rem;
  }
}

.fs-70 {
  font-size: calc(1.5625rem + 3.75vw);
}

@media (min-width: 1200px) {
  .fs-70 {
    font-size: 4.375rem;
  }
}

.fs-100 {
  font-size: calc(1.75rem + 6vw);
}

@media (min-width: 1200px) {
  .fs-100 {
    font-size: 6.25rem;
  }
}

.fw-semi-bold {
  font-weight: 600 !important;
}

th[align="right"] {
  text-align: right;
}

@keyframes moveDown {
  0% {
    transform: translateY(-100%);
    -webkit-transform: translateY(-100%);
  }

  100% {
    transform: translateY(0);
    -webkit-transform: translateY(0);
  }
}

.animate {
  transition: all ease-in .5s;
  transition: all cubic-bezier(0.445, 0.05, 0.55, 0.95) 0.5s;
}

.animate_fade {
  opacity: 0;
  visibility: hidden;
}

.animate_rtl {
  position: relative;
  right: -2.5rem;
}

.animate_btt {
  position: relative;
  bottom: -2.5rem;
}

.animate_delay-1 {
  transition-delay: 0.1s;
}

.animate_delay-2 {
  transition-delay: 0.2s;
}

.animate_delay-3 {
  transition-delay: 0.3s;
}

.animate_delay-4 {
  transition-delay: 0.4s;
}

.animate_delay-5 {
  transition-delay: 0.5s;
}

.animate_delay-6 {
  transition-delay: 0.6s;
}

.animate_delay-7 {
  transition-delay: 0.7s;
}

.animate_delay-8 {
  transition-delay: 0.8s;
}

.animate_delay-9 {
  transition-delay: 0.9s;
}

.animate_delay-10 {
  transition-delay: 1s;
}

.swiper-slide-active .animate_fade {
  opacity: 1;
  visibility: visible;
}

.swiper-slide-active .animate_rtl {
  right: 0;
}

.swiper-slide-active .animate_btt {
  bottom: 0;
}

.anim_appear-fade {
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-fade {
  opacity: 1;
  visibility: visible;
}

.anim_appear-bottom {
  bottom: -0.625rem;
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-bottom {
  bottom: 0.625rem;
  opacity: 1;
  visibility: visible;
}

.anim_appear-right {
  right: -0.625rem;
  transition: all 0.2s ease;
  font-size: 0.875rem;
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .anim_appear-right {
  right: 0;
  opacity: 1;
  visibility: visible;
}

.row {
  --bs-gutter-x: 1.875rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(var(--bs-gutter-y) * -1);
  margin-right: calc(var(--bs-gutter-x) / -2);
  margin-left: calc(var(--bs-gutter-x) / -2);
}

.row>* {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) / 2);
  padding-left: calc(var(--bs-gutter-x) / 2);
  margin-top: var(--bs-gutter-y);
}

.col {
  flex: 1 0 0%;
}

.row-cols-auto>* {
  flex: 0 0 auto;
  width: auto;
}

.row-cols-1>* {
  flex: 0 0 auto;
  width: 100%;
}

.row-cols-2>* {
  flex: 0 0 auto;
  width: 50%;
}

.row-cols-3>* {
  flex: 0 0 auto;
  width: 33.3333333333%;
}

.row-cols-4>* {
  flex: 0 0 auto;
  width: 25%;
}

.row-cols-5>* {
  flex: 0 0 auto;
  width: 20%;
}

.row-cols-6>* {
  flex: 0 0 auto;
  width: 16.6666666667%;
}

.col-auto {
  flex: 0 0 auto;
  width: auto;
}

.col-1 {
  flex: 0 0 auto;
  width: 8.3333333333%;
}

.col-2 {
  flex: 0 0 auto;
  width: 16.6666666667%;
}

.col-3 {
  flex: 0 0 auto;
  width: 25%;
}

.col-4 {
  flex: 0 0 auto;
  width: 33.3333333333%;
}

.col-5 {
  flex: 0 0 auto;
  width: 41.6666666667%;
}

.col-6 {
  flex: 0 0 auto;
  width: 50%;
}

.col-7 {
  flex: 0 0 auto;
  width: 58.3333333333%;
}

.col-8 {
  flex: 0 0 auto;
  width: 66.6666666667%;
}

.col-9 {
  flex: 0 0 auto;
  width: 75%;
}

.col-10 {
  flex: 0 0 auto;
  width: 83.3333333333%;
}

.col-11 {
  flex: 0 0 auto;
  width: 91.6666666667%;
}

.col-12 {
  flex: 0 0 auto;
  width: 100%;
}

.offset-1 {
  margin-left: 8.3333333333%;
}

.offset-2 {
  margin-left: 16.6666666667%;
}

.offset-3 {
  margin-left: 25%;
}

.offset-4 {
  margin-left: 33.3333333333%;
}

.offset-5 {
  margin-left: 41.6666666667%;
}

.offset-6 {
  margin-left: 50%;
}

.offset-7 {
  margin-left: 58.3333333333%;
}

.offset-8 {
  margin-left: 66.6666666667%;
}

.offset-9 {
  margin-left: 75%;
}

.offset-10 {
  margin-left: 83.3333333333%;
}

.offset-11 {
  margin-left: 91.6666666667%;
}

.g-0,
.gx-0 {
  --bs-gutter-x: 0;
}

.g-0,
.gy-0 {
  --bs-gutter-y: 0;
}

.g-1,
.gx-1 {
  --bs-gutter-x: 0.25rem;
}

.g-1,
.gy-1 {
  --bs-gutter-y: 0.25rem;
}

.g-2,
.gx-2 {
  --bs-gutter-x: 0.5rem;
}

.g-2,
.gy-2 {
  --bs-gutter-y: 0.5rem;
}

.g-3,
.gx-3 {
  --bs-gutter-x: 1rem;
}

.g-3,
.gy-3 {
  --bs-gutter-y: 1rem;
}

.g-4,
.gx-4 {
  --bs-gutter-x: 1.5rem;
}

.g-4,
.gy-4 {
  --bs-gutter-y: 1.5rem;
}

.g-5,
.gx-5 {
  --bs-gutter-x: 3rem;
}

.g-5,
.gy-5 {
  --bs-gutter-y: 3rem;
}

@media (min-width: 576px) {
  .col-sm {
    flex: 1 0 0%;
  }

  .row-cols-sm-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-sm-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-sm-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-sm-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-sm-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-sm-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-sm-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-sm-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-sm-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-sm-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-sm-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-sm-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-sm-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-sm-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-sm-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-sm-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-sm-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-sm-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-sm-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-sm-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-sm-0 {
    margin-left: 0;
  }

  .offset-sm-1 {
    margin-left: 8.3333333333%;
  }

  .offset-sm-2 {
    margin-left: 16.6666666667%;
  }

  .offset-sm-3 {
    margin-left: 25%;
  }

  .offset-sm-4 {
    margin-left: 33.3333333333%;
  }

  .offset-sm-5 {
    margin-left: 41.6666666667%;
  }

  .offset-sm-6 {
    margin-left: 50%;
  }

  .offset-sm-7 {
    margin-left: 58.3333333333%;
  }

  .offset-sm-8 {
    margin-left: 66.6666666667%;
  }

  .offset-sm-9 {
    margin-left: 75%;
  }

  .offset-sm-10 {
    margin-left: 83.3333333333%;
  }

  .offset-sm-11 {
    margin-left: 91.6666666667%;
  }

  .g-sm-0,
  .gx-sm-0 {
    --bs-gutter-x: 0;
  }

  .g-sm-0,
  .gy-sm-0 {
    --bs-gutter-y: 0;
  }

  .g-sm-1,
  .gx-sm-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-sm-1,
  .gy-sm-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-sm-2,
  .gx-sm-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-sm-2,
  .gy-sm-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-sm-3,
  .gx-sm-3 {
    --bs-gutter-x: 1rem;
  }

  .g-sm-3,
  .gy-sm-3 {
    --bs-gutter-y: 1rem;
  }

  .g-sm-4,
  .gx-sm-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-sm-4,
  .gy-sm-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-sm-5,
  .gx-sm-5 {
    --bs-gutter-x: 3rem;
  }

  .g-sm-5,
  .gy-sm-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 768px) {
  .col-md {
    flex: 1 0 0%;
  }

  .row-cols-md-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-md-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-md-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-md-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-md-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-md-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-md-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-md-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-md-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-md-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-md-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-md-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-md-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-md-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-md-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-md-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-md-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-md-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-md-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-md-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-md-0 {
    margin-left: 0;
  }

  .offset-md-1 {
    margin-left: 8.3333333333%;
  }

  .offset-md-2 {
    margin-left: 16.6666666667%;
  }

  .offset-md-3 {
    margin-left: 25%;
  }

  .offset-md-4 {
    margin-left: 33.3333333333%;
  }

  .offset-md-5 {
    margin-left: 41.6666666667%;
  }

  .offset-md-6 {
    margin-left: 50%;
  }

  .offset-md-7 {
    margin-left: 58.3333333333%;
  }

  .offset-md-8 {
    margin-left: 66.6666666667%;
  }

  .offset-md-9 {
    margin-left: 75%;
  }

  .offset-md-10 {
    margin-left: 83.3333333333%;
  }

  .offset-md-11 {
    margin-left: 91.6666666667%;
  }

  .g-md-0,
  .gx-md-0 {
    --bs-gutter-x: 0;
  }

  .g-md-0,
  .gy-md-0 {
    --bs-gutter-y: 0;
  }

  .g-md-1,
  .gx-md-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-md-1,
  .gy-md-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-md-2,
  .gx-md-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-md-2,
  .gy-md-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-md-3,
  .gx-md-3 {
    --bs-gutter-x: 1rem;
  }

  .g-md-3,
  .gy-md-3 {
    --bs-gutter-y: 1rem;
  }

  .g-md-4,
  .gx-md-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-md-4,
  .gy-md-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-md-5,
  .gx-md-5 {
    --bs-gutter-x: 3rem;
  }

  .g-md-5,
  .gy-md-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 992px) {
  .col-lg {
    flex: 1 0 0%;
  }

  .row-cols-lg-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-lg-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-lg-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-lg-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-lg-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-lg-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-lg-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-lg-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-lg-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-lg-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-lg-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-lg-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-lg-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-lg-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-lg-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-lg-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-lg-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-lg-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-lg-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-lg-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-lg-0 {
    margin-left: 0;
  }

  .offset-lg-1 {
    margin-left: 8.3333333333%;
  }

  .offset-lg-2 {
    margin-left: 16.6666666667%;
  }

  .offset-lg-3 {
    margin-left: 25%;
  }

  .offset-lg-4 {
    margin-left: 33.3333333333%;
  }

  .offset-lg-5 {
    margin-left: 41.6666666667%;
  }

  .offset-lg-6 {
    margin-left: 50%;
  }

  .offset-lg-7 {
    margin-left: 58.3333333333%;
  }

  .offset-lg-8 {
    margin-left: 66.6666666667%;
  }

  .offset-lg-9 {
    margin-left: 75%;
  }

  .offset-lg-10 {
    margin-left: 83.3333333333%;
  }

  .offset-lg-11 {
    margin-left: 91.6666666667%;
  }

  .g-lg-0,
  .gx-lg-0 {
    --bs-gutter-x: 0;
  }

  .g-lg-0,
  .gy-lg-0 {
    --bs-gutter-y: 0;
  }

  .g-lg-1,
  .gx-lg-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-lg-1,
  .gy-lg-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-lg-2,
  .gx-lg-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-lg-2,
  .gy-lg-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-lg-3,
  .gx-lg-3 {
    --bs-gutter-x: 1rem;
  }

  .g-lg-3,
  .gy-lg-3 {
    --bs-gutter-y: 1rem;
  }

  .g-lg-4,
  .gx-lg-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-lg-4,
  .gy-lg-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-lg-5,
  .gx-lg-5 {
    --bs-gutter-x: 3rem;
  }

  .g-lg-5,
  .gy-lg-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1200px) {
  .col-xl {
    flex: 1 0 0%;
  }

  .row-cols-xl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xl-0 {
    margin-left: 0;
  }

  .offset-xl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xl-3 {
    margin-left: 25%;
  }

  .offset-xl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xl-6 {
    margin-left: 50%;
  }

  .offset-xl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xl-9 {
    margin-left: 75%;
  }

  .offset-xl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xl-0,
  .gx-xl-0 {
    --bs-gutter-x: 0;
  }

  .g-xl-0,
  .gy-xl-0 {
    --bs-gutter-y: 0;
  }

  .g-xl-1,
  .gx-xl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xl-1,
  .gy-xl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xl-2,
  .gx-xl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xl-2,
  .gy-xl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xl-3,
  .gx-xl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xl-3,
  .gy-xl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xl-4,
  .gx-xl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xl-4,
  .gy-xl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xl-5,
  .gx-xl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xl-5,
  .gy-xl-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1500px) {
  .col-xxl {
    flex: 1 0 0%;
  }

  .row-cols-xxl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xxl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xxl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xxl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xxl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xxl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xxl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xxl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xxl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xxl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xxl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xxl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xxl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xxl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xxl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xxl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xxl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xxl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xxl-0 {
    margin-left: 0;
  }

  .offset-xxl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xxl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xxl-3 {
    margin-left: 25%;
  }

  .offset-xxl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xxl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xxl-6 {
    margin-left: 50%;
  }

  .offset-xxl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xxl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xxl-9 {
    margin-left: 75%;
  }

  .offset-xxl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xxl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xxl-0,
  .gx-xxl-0 {
    --bs-gutter-x: 0;
  }

  .g-xxl-0,
  .gy-xxl-0 {
    --bs-gutter-y: 0;
  }

  .g-xxl-1,
  .gx-xxl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xxl-1,
  .gy-xxl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xxl-2,
  .gx-xxl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xxl-2,
  .gy-xxl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xxl-3,
  .gx-xxl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xxl-3,
  .gy-xxl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xxl-4,
  .gx-xxl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xxl-4,
  .gy-xxl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xxl-5,
  .gx-xxl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xxl-5,
  .gy-xxl-5 {
    --bs-gutter-y: 3rem;
  }
}

@media (min-width: 1700px) {
  .col-xxxl {
    flex: 1 0 0%;
  }

  .row-cols-xxxl-auto>* {
    flex: 0 0 auto;
    width: auto;
  }

  .row-cols-xxxl-1>* {
    flex: 0 0 auto;
    width: 100%;
  }

  .row-cols-xxxl-2>* {
    flex: 0 0 auto;
    width: 50%;
  }

  .row-cols-xxxl-3>* {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .row-cols-xxxl-4>* {
    flex: 0 0 auto;
    width: 25%;
  }

  .row-cols-xxxl-5>* {
    flex: 0 0 auto;
    width: 20%;
  }

  .row-cols-xxxl-6>* {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxxl-auto {
    flex: 0 0 auto;
    width: auto;
  }

  .col-xxxl-1 {
    flex: 0 0 auto;
    width: 8.3333333333%;
  }

  .col-xxxl-2 {
    flex: 0 0 auto;
    width: 16.6666666667%;
  }

  .col-xxxl-3 {
    flex: 0 0 auto;
    width: 25%;
  }

  .col-xxxl-4 {
    flex: 0 0 auto;
    width: 33.3333333333%;
  }

  .col-xxxl-5 {
    flex: 0 0 auto;
    width: 41.6666666667%;
  }

  .col-xxxl-6 {
    flex: 0 0 auto;
    width: 50%;
  }

  .col-xxxl-7 {
    flex: 0 0 auto;
    width: 58.3333333333%;
  }

  .col-xxxl-8 {
    flex: 0 0 auto;
    width: 66.6666666667%;
  }

  .col-xxxl-9 {
    flex: 0 0 auto;
    width: 75%;
  }

  .col-xxxl-10 {
    flex: 0 0 auto;
    width: 83.3333333333%;
  }

  .col-xxxl-11 {
    flex: 0 0 auto;
    width: 91.6666666667%;
  }

  .col-xxxl-12 {
    flex: 0 0 auto;
    width: 100%;
  }

  .offset-xxxl-0 {
    margin-left: 0;
  }

  .offset-xxxl-1 {
    margin-left: 8.3333333333%;
  }

  .offset-xxxl-2 {
    margin-left: 16.6666666667%;
  }

  .offset-xxxl-3 {
    margin-left: 25%;
  }

  .offset-xxxl-4 {
    margin-left: 33.3333333333%;
  }

  .offset-xxxl-5 {
    margin-left: 41.6666666667%;
  }

  .offset-xxxl-6 {
    margin-left: 50%;
  }

  .offset-xxxl-7 {
    margin-left: 58.3333333333%;
  }

  .offset-xxxl-8 {
    margin-left: 66.6666666667%;
  }

  .offset-xxxl-9 {
    margin-left: 75%;
  }

  .offset-xxxl-10 {
    margin-left: 83.3333333333%;
  }

  .offset-xxxl-11 {
    margin-left: 91.6666666667%;
  }

  .g-xxxl-0,
  .gx-xxxl-0 {
    --bs-gutter-x: 0;
  }

  .g-xxxl-0,
  .gy-xxxl-0 {
    --bs-gutter-y: 0;
  }

  .g-xxxl-1,
  .gx-xxxl-1 {
    --bs-gutter-x: 0.25rem;
  }

  .g-xxxl-1,
  .gy-xxxl-1 {
    --bs-gutter-y: 0.25rem;
  }

  .g-xxxl-2,
  .gx-xxxl-2 {
    --bs-gutter-x: 0.5rem;
  }

  .g-xxxl-2,
  .gy-xxxl-2 {
    --bs-gutter-y: 0.5rem;
  }

  .g-xxxl-3,
  .gx-xxxl-3 {
    --bs-gutter-x: 1rem;
  }

  .g-xxxl-3,
  .gy-xxxl-3 {
    --bs-gutter-y: 1rem;
  }

  .g-xxxl-4,
  .gx-xxxl-4 {
    --bs-gutter-x: 1.5rem;
  }

  .g-xxxl-4,
  .gy-xxxl-4 {
    --bs-gutter-y: 1.5rem;
  }

  .g-xxxl-5,
  .gx-xxxl-5 {
    --bs-gutter-x: 3rem;
  }

  .g-xxxl-5,
  .gy-xxxl-5 {
    --bs-gutter-y: 3rem;
  }
}

body ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  height: .25rem;
  background-color: #ffffff;
}

body ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #e4e4e4;
}

@media (max-width: 991.98px) {
  .snap main {
    overflow-x: hidden;
  }
}

img {
  max-width: 100%;
}

.block {
  margin: 2.125rem 0;
}

.full-width_padding {
  overflow: hidden;
}

@media (min-width: 1500px) {
  .full-width_padding {
    width: 100%;
    padding: 0 3.75rem;
  }
}

.full-width_padding-20 {
  width: 100%;
  padding: 0 1.25rem;
}

@media (max-width: 1499.98px) {
  .full-width_border {
    border: 0 !important;
  }
}

@media (min-width: 1500px) {
  .full-width_border {
    padding: 0.625rem;
    border-style: solid;
  }
}

.page-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  transition: all 0.32s cubic-bezier(0.55, 0.085, 0.68, 0.53);
  background-color: rgba(34, 34, 34, 0.4);
  opacity: 0;
  visibility: hidden;
  z-index: 1040;
}

.page-overlay_visible {
  opacity: 1;
  visibility: visible;
}

#scrollTop {
  position: fixed !important;
  right: 0;
  bottom: 0rem;
  z-index: 1030;
  width: 45px;
  height: 45px;
  background-color: #eeeeee;
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23222222'/%3e%3c/svg%3e");
  background-position: center center;
  background-repeat: no-repeat;
  cursor: pointer;
  clip: auto !important;
  transition: all 0.28s;
}

@media (min-width: 768px) {
  #scrollTop {
    bottom: 0;
  }
}

.mw-1620 {
  width: 1620px !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.mw-1170 {
  width: 1200px !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.mw-930 {
  width: 58.125rem !important;
  max-width: 100% !important;
  margin: 0 auto;
}

.w-740 {
  width: 46.25rem;
  max-width: 100%;
}

.w-100px {
  width: 6.25rem;
}

.h-100px {
  height: 6.25rem;
}

.gradient-bg {
  background-image: url(../../images/home/demo3/slider_bg.jpg);
  background-position: top center;
  background-repeat: no-repeat;
  background-size: 100% auto;
}

.gradient-bg-10 {
  background-image: url(../../images/home/demo10/slider_bg.png);
  background-position: top center;
  background-repeat: no-repeat;
  background-size: auto 84rem;
}

@media (min-width: 992px) {
  .gradient-bg-10 {
    background-size: 100% auto;
  }
}

@media (min-width: 1200px) {
  .col-xl-20per {
    flex: 0 0 auto;
    width: 20%;
  }
}

@media (min-width: 1200px) {
  .col-xl-40per {
    flex: 0 0 auto;
    width: 40%;
  }
}

@media (min-width: 1200px) {
  .col-xl-60per {
    flex: 0 0 auto;
    width: 60%;
  }
}

@media (min-width: 1200px) {
  .col-xl-80per {
    flex: 0 0 auto;
    width: 80%;
  }
}

.gutters-20 .row {
  --bs-gutter-x: 1.25rem;
}

.btn-close,
.btn-close-lg,
.btn-close-xs {
  padding: 0;
  border: 0;
  box-sizing: content-box;
  color: #000;
  border-radius: 0;
  opacity: 1;
}

.btn-close:hover,
.btn-close-lg:hover,
.btn-close-xs:hover {
  color: #000;
  text-decoration: none;
  opacity: 0.75;
}

.btn-close:focus,
.btn-close-lg:focus,
.btn-close-xs:focus {
  outline: none;
  box-shadow: none;
  opacity: 1;
}

.btn-close:disabled,
.btn-close.disabled,
.btn-close-lg:disabled,
.btn-close-lg.disabled,
.btn-close-xs:disabled,
.btn-close-xs.disabled {
  pointer-events: none;
  user-select: none;
  opacity: 0.25;
}

.btn-close {
  width: 1.375rem;
  height: 1.375rem;
  padding: 0.25em 0.25em;
  background: transparent url("data:image/svg+xml,%3csvg width='23' height='22' viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23000'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23000'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.btn-close-lg {
  width: 1rem;
  height: 1rem;
  background: transparent url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.414336 14.1421L14.5565 0L15.9707 1.41421L1.82855 15.5563L0.414336 14.1421Z' fill='%23000'/%3e%3cpath d='M1.41421 0.142113L15.5563 14.2842L14.1421 15.6985L0 1.55633L1.41421 0.142113Z' fill='%23000'/%3e%3c/svg%3e") center/1rem auto no-repeat;
}

.btn-close-xs {
  width: 0.625rem;
  height: 0.625rem;
  padding: 0;
  background: transparent url("data:image/svg+xml,%3csvg width='10' height='10' viewBox='0 0 10 10' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.259435 8.85506L9.11449 0L10 0.885506L1.14494 9.74056L0.259435 8.85506Z' fill='%23767676'/%3e%3cpath d='M0.885506 0.0889838L9.74057 8.94404L8.85506 9.82955L0 0.97449L0.885506 0.0889838Z' fill='%23767676'/%3e%3c/svg%3e") center/0.625rem auto no-repeat;
}

.btn-close-white {
  filter: invert(1) grayscale(100%) brightness(200%);
}

.accordion-item_shadow {
  box-shadow: 0 0 1.5625rem 0 rgba(34, 34, 34, 0.05);
}

.accordion-button {
  padding: 1.75rem 1.875rem 1.125rem;
  border: 1px solid #eeeeee;
  color: #222222;
  background-color: #ffffff;
  font-size: 1.625rem;
  font-weight: 500;
  line-height: 1.375;
  outline: none;
}

.accordion-button::after {
  content: none;
}

.accordion-button.collapsed {
  background-color: transparent;
  color: #222222;
}

.accordion-button.collapsed .accordion-button__icon {
  transform: rotate(0deg);
}

.accordion-button.collapsed .accordion-button__icon .svg-path-horizontal {
  opacity: 1;
}

.accordion-button.collapsed .accordion-button__icon.type2 {
  transform: rotate(180deg);
}

.accordion-button__icon {
  width: 0.875rem;
  height: 0.875rem;
  margin-left: auto;
  fill: #222222;
  transform: rotate(90deg);
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button__icon {
    transition: none;
  }
}

.accordion-button__icon .svg-path-vertical {
  transform: rotate(90deg);
  transform-origin: center;
}

.accordion-button__icon .svg-path-horizontal {
  transition: transform 0.2s ease-in-out, opacity 0.2s ease-in-out;
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .accordion-button__icon .svg-path-horizontal {
    transition: none;
  }
}

.accordion-button__icon.type2 {
  transform: rotate(0deg);
}

.accordion-body {
  padding: 1.5rem 1.875rem 1.75rem;
}

.faq-accordion .accordion-item {
  margin-bottom: 1.25rem;
}

.faq-accordion .accordion-button {
  border: 0;
  border-bottom: 1px solid #e4e4e4;
  padding: 0.625rem 0;
  text-align: left;
}

.faq-accordion .accordion-collapse {
  border: 0;
}

.faq-accordion .accordion-body {
  padding: 1.5rem 0;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.nav-link {
  display: block;
  padding: 0.6875rem 1.75rem 0.4375rem;
  color: #222222;
  font-weight: 500;
  line-height: 1.375;
  outline: none;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .nav-link {
    transition: none;
  }
}

.nav-link.disabled {
  color: #6c757d;
  pointer-events: none;
  cursor: default;
}

@media (min-width: 992px) {
  .nav-link {
    font-size: 1rem;
  }
}

.nav-link_underscore {
  position: relative;
  padding: 0.6875rem 1.5625rem 0.4375rem;
  color: #767676;
}

.nav-link_underscore:after {
  content: '';
  display: block;
  position: absolute;
  bottom: 0;
  left: 1.5625rem;
  width: 0;
  height: 2px;
  background-color: #222222;
  transition: width 0.36s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@media (prefers-reduced-motion: reduce) {
  .nav-link_underscore:after {
    transition: none;
  }
}

.nav-link_underscore.theme-color:after {
  background-color: #193174;
}

.nav-link_underscore:hover,
.nav-link_underscore:focus,
.nav-link_underscore.active,
.nav-item.show .nav-link_underscore {
  color: #222222;
}

.nav-link_underscore:hover:after,
.nav-link_underscore:focus:after,
.nav-link_underscore.active:after,
.nav-item.show .nav-link_underscore:after {
  width: calc(100% - 3.125rem);
}

.nav-link_underscore.underscore-sm:hover:after,
.nav-link_underscore.underscore-sm:focus:after,
.nav-link_underscore.underscore-sm.active:after,
.nav-item.show .nav-link_underscore.underscore-sm:after {
  width: 2rem;
}

.nav-link_underscore.underscore-md:hover:after,
.nav-link_underscore.underscore-md:focus:after,
.nav-link_underscore.underscore-md.active:after,
.nav-item.show .nav-link_underscore.underscore-md:after {
  width: calc((100% - 1.5625rem * 2) * 0.7);
}

.nav-link_underscore.disabled {
  color: #6c757d;
  background-color: transparent;
  border-color: transparent;
}

.nav-link_rline:before {
  content: '';
  position: absolute;
  top: 49%;
  left: 0;
  width: 0px;
  height: 2px;
  background-color: #222222;
  transition: width 0.36s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@media (prefers-reduced-motion: reduce) {
  .nav-link_rline:before {
    transition: none;
  }
}

.nav-link_rline.active:before {
  width: 100%;
}

.rline-content {
  display: inline-block;
  position: relative;
  padding-right: 1.5em;
  background-color: #ffffff;
}

@media (min-width: 768px) {
  .rline-content {
    padding-right: 2.5em;
  }
}

@media (min-width: 1200px) {
  .rline-content {
    padding-right: 3.5em;
  }
}

.nav-pills .nav-link {
  border-radius: 0;
}

.nav-pills .nav-link.active,
.nav-pills .show>.nav-link {
  color: #ffffff;
  background-color: #222222;
}

.nav-fill>.nav-link,
.nav-fill .nav-item {
  flex: 1 1 auto;
  text-align: center;
}

.nav-justified>.nav-link,
.nav-justified .nav-item {
  flex-basis: 0;
  flex-grow: 1;
  text-align: center;
}

.tab-content>.tab-pane {
  display: none;
}

.tab-content>.active {
  display: block;
}

.checkbox__mark {
  display: -ms-inline-flexbox;
  display: inline-flex;
  -ms-flex-align: center;
  align-items: center;
  -ms-flex-pack: center;
  justify-content: center;
  width: 1.125rem;
  height: 1.125rem;
  margin-right: .625rem;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10l3 3l6-6'/%3e%3c/svg%3e");
  background-position: center;
  background-repeat: no-repeat;
  background-size: 66.666667%;
}

.checkbox__mark_gray {
  background-color: #767676;
}

.checkbox__mark_round {
  border-radius: 100%;
}

.table {
  --bs-table-bg: transparent;
  --bs-table-striped-color: #222222;
  --bs-table-striped-bg: #faf9f8;
  --bs-table-active-color: #222222;
  --bs-table-active-bg: rgba(0, 0, 0, 0.1);
  --bs-table-hover-color: #222222;
  --bs-table-hover-bg: rgba(0, 0, 0, 0.075);
  width: 100%;
  margin-bottom: 1rem;
  color: #222222;
  line-height: 1.5;
  vertical-align: top;
  border-color: transparent;
}

.table> :not(caption)>tr>td,
.table> :not(caption)>tr>th {
  background-image: linear-gradient(var(--bs-table-accent-bg), var(--bs-table-accent-bg));
  border-bottom-width: 0;
}

.table> :not(caption)>tr>td {
  padding: 1.53125rem 1.5rem;
  background-color: var(--bs-table-bg);
}

.table> :not(caption)>tr>th {
  padding: 1.625rem 1.5rem 1.25rem;
  background-color: #222222;
  color: #ffffff;
  font-size: 1rem;
  font-weight: 500;
}

.table>tbody {
  vertical-align: inherit;
}

.table>thead {
  vertical-align: bottom;
}

.table> :not(:last-child)>tr:last-child>th,
.table> :not(:last-child)>tr:last-child>td {
  border-bottom-color: currentColor;
}

.caption-top {
  caption-side: top;
}

.table-sm> :not(caption)>tr>th,
.table-sm> :not(caption)>tr>td {
  padding: 0.25rem 0.25rem;
}

.table-bordered> :not(caption)>tr {
  border-width: 0 0;
}

.table-bordered> :not(caption)>tr>th,
.table-bordered> :not(caption)>tr>td {
  border-width: 0 0;
}

.table-borderless> :not(caption)>tr {
  border-bottom-width: 0;
}

.table-striped>tbody>tr:nth-of-type(even) {
  --bs-table-accent-bg: var(--bs-table-striped-bg);
  color: var(--bs-table-striped-color);
}

.table-active {
  --bs-table-accent-bg: var(--bs-table-active-bg);
  color: var(--bs-table-active-color);
}

.table-hover>tbody>tr:hover {
  --bs-table-accent-bg: var(--bs-table-hover-bg);
  color: var(--bs-table-hover-color);
}

.table-primary {
  --bs-table-bg: #ffffff;
  --bs-table-striped-bg: #f2f2f2;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #e6e6e6;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #ececec;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #e6e6e6;
}

.table-secondary {
  --bs-table-bg: #e4e4e4;
  --bs-table-striped-bg: #d9d9d9;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #cdcdcd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: lightgray;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #cdcdcd;
}

.table-success {
  --bs-table-bg: #def2d7;
  --bs-table-striped-bg: #d3e6cc;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #c8dac2;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #cde0c7;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #c8dac2;
}

.table-info {
  --bs-table-bg: #cde9f6;
  --bs-table-striped-bg: #c3ddea;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #b9d2dd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #bed8e4;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #b9d2dd;
}

.table-warning {
  --bs-table-bg: #f7f3d7;
  --bs-table-striped-bg: #ebe7cc;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #dedbc2;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #e4e1c7;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #dedbc2;
}

.table-danger {
  --bs-table-bg: #ecc8c5;
  --bs-table-striped-bg: #e0bebb;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #d4b4b1;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: #dab9b6;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #d4b4b1;
}

.table-light {
  --bs-table-bg: #e4e4e4;
  --bs-table-striped-bg: #d9d9d9;
  --bs-table-striped-color: #000;
  --bs-table-active-bg: #cdcdcd;
  --bs-table-active-color: #000;
  --bs-table-hover-bg: lightgray;
  --bs-table-hover-color: #000;
  color: #000;
  border-color: #cdcdcd;
}

.table-dark {
  --bs-table-bg: #222222;
  --bs-table-striped-bg: #2d2d2d;
  --bs-table-striped-color: #fff;
  --bs-table-active-bg: #383838;
  --bs-table-active-color: #fff;
  --bs-table-hover-bg: #333333;
  --bs-table-hover-color: #fff;
  color: #fff;
  border-color: #383838;
}

.table-responsive {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

@media (max-width: 575.98px) {
  .table-responsive-sm {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 767.98px) {
  .table-responsive-md {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 991.98px) {
  .table-responsive-lg {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1199.98px) {
  .table-responsive-xl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1499.98px) {
  .table-responsive-xxl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

@media (max-width: 1699.98px) {
  .table-responsive-xxxl {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }
}

.table-primary thead>tr>th {
  color: #ffffff;
  font-size: 1rem;
  font-weight: 500;
}

.alert {
  position: relative;
  padding: 1.6875rem 1.875rem 1.375rem;
  margin-bottom: 1rem;
  border: 1px solid transparent;
  font-weight: 500;
  border-radius: 0;
}

.alert-heading {
  color: inherit;
}

.alert-link {
  font-weight: 700;
}

.alert-dismissible {
  padding-right: 3rem;
}

.alert-dismissible .btn-close {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  padding: 1.85625rem 1.875rem 1.375rem;
}

.alert-success {
  color: #5b7052;
  background-color: #def2d7;
  border-color: #def2d7;
}

.alert-success .alert-link {
  color: #495a42;
}

.alert-success .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%235b7052'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%235b7052'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-info {
  color: #4780aa;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.alert-info .alert-link {
  color: #396688;
}

.alert-info .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%234780aa'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%234780aa'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-warning {
  color: #927238;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.alert-warning .alert-link {
  color: #755b2d;
}

.alert-warning .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23927238'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23927238'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.alert-danger {
  color: #ab3331;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.alert-danger .alert-link {
  color: #892927;
}

.alert-danger .btn-close {
  background: transparent url("data:image/svg+xml,%3csvg viewBox='0 0 23 22' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M5.48881 15.5962L16.0954 4.98963L17.5096 6.40384L6.90302 17.0104L5.48881 15.5962Z' fill='%23ab3331'/%3e%3cpath d='M16.0954 17.7176L4.7817 6.40384L6.19592 4.98963L17.5096 16.3033L16.0954 17.7176Z' fill='%23ab3331'/%3e%3c/svg%3e") center/1.375rem auto no-repeat;
}

.btn {
  display: inline-block;
  font-weight: 400;
  line-height: 1.5;
  color: #222222;
  text-align: center;
  vertical-align: middle;
  cursor: pointer;
  user-select: none;
  background-color: #ffffff;
  border: 1px solid transparent;
  padding: 0.375rem 3.125rem;
  font-size: 0.875rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
  font-size: 0.875rem;
  padding-top: 0.703125rem;
  padding-bottom: 0.5625rem;
}

@media (prefers-reduced-motion: reduce) {
  .btn {
    transition: none;
  }
}

@media (max-width: 575.98px) {
  .btn {
    padding-left: 1.125rem;
    padding-right: 1.125rem;
  }
}

.btn:hover {
  color: #222222;
}

.btn-55 {
  height: 3.4375rem;
}

.btn-50 {
  height: 3.125rem;
}

.btn-45 {
  height: 2.8125rem;
}

.btn-40 {
  height: 2.5rem;
}

.btn-check:focus+.btn,
.btn:focus {
  outline: 0;
  box-shadow: none;
}

.btn-check:checked+.btn,
.btn-check:active+.btn,
.btn:active,
.btn.active {
  box-shadow: none;
}

.btn-check:checked+.btn:focus,
.btn-check:active+.btn:focus,
.btn:active:focus,
.btn.active:focus {
  box-shadow: none;
}

.btn:disabled,
.btn.disabled,
fieldset:disabled .btn {
  pointer-events: none;
  opacity: 0.65;
  box-shadow: none;
}

@media (min-width: 1500px) {
  .btn {
    font-size: 1rem;
    padding-top: 0.9375rem;
    padding-bottom: 0.75rem;
  }
}

.btn-primary {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
  box-shadow: none;
}

.btn-primary:hover {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
}

.btn-check:focus+.btn-primary,
.btn-primary:focus {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-check:checked+.btn-primary,
.btn-check:active+.btn-primary,
.btn-primary:active,
.btn-primary.active,
.show>.btn-primary.dropdown-toggle {
  color: #fff;
  background-color: #1b1b1b;
  border-color: #1a1a1a;
}

.btn-check:checked+.btn-primary:focus,
.btn-check:active+.btn-primary:focus,
.btn-primary:active:focus,
.btn-primary.active:focus,
.show>.btn-primary.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-primary:disabled,
.btn-primary.disabled {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-outline-primary {
  color: #222222;
  border-color: #222222;
}

.btn-outline-primary:hover {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:focus+.btn-outline-primary,
.btn-outline-primary:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-primary,
.btn-check:active+.btn-outline-primary,
.btn-outline-primary:active,
.btn-outline-primary.active,
.btn-outline-primary.dropdown-toggle.show {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:checked+.btn-outline-primary:focus,
.btn-check:active+.btn-outline-primary:focus,
.btn-outline-primary:active:focus,
.btn-outline-primary.active:focus,
.btn-outline-primary.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-primary:disabled,
.btn-outline-primary.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-hover-primary:hover {
  background-color: #222222;
  color: #fff;
}

.btn-secondary {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
  box-shadow: none;
}

.btn-secondary:hover {
  color: #fff;
  background-color: #646464;
  border-color: #5e5e5e;
}

.btn-check:focus+.btn-secondary,
.btn-secondary:focus {
  color: #fff;
  background-color: #646464;
  border-color: #5e5e5e;
  box-shadow: 0 0 0 0 rgba(139, 139, 139, 0.5);
}

.btn-check:checked+.btn-secondary,
.btn-check:active+.btn-secondary,
.btn-secondary:active,
.btn-secondary.active,
.show>.btn-secondary.dropdown-toggle {
  color: #fff;
  background-color: #5e5e5e;
  border-color: #595959;
}

.btn-check:checked+.btn-secondary:focus,
.btn-check:active+.btn-secondary:focus,
.btn-secondary:active:focus,
.btn-secondary.active:focus,
.show>.btn-secondary.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(139, 139, 139, 0.5);
}

.btn-secondary:disabled,
.btn-secondary.disabled {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-outline-secondary {
  color: #767676;
  border-color: #767676;
}

.btn-outline-secondary:hover {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-check:focus+.btn-outline-secondary,
.btn-outline-secondary:focus {
  box-shadow: 0 0 0 0 rgba(118, 118, 118, 0.5);
}

.btn-check:checked+.btn-outline-secondary,
.btn-check:active+.btn-outline-secondary,
.btn-outline-secondary:active,
.btn-outline-secondary.active,
.btn-outline-secondary.dropdown-toggle.show {
  color: #fff;
  background-color: #767676;
  border-color: #767676;
}

.btn-check:checked+.btn-outline-secondary:focus,
.btn-check:active+.btn-outline-secondary:focus,
.btn-outline-secondary:active:focus,
.btn-outline-secondary.active:focus,
.btn-outline-secondary.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(118, 118, 118, 0.5);
}

.btn-outline-secondary:disabled,
.btn-outline-secondary.disabled {
  color: #767676;
  background-color: transparent;
}

.btn-hover-secondary:hover {
  background-color: #767676;
  color: #fff;
}

.btn-success {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
  box-shadow: none;
}

.btn-success:hover {
  color: #000;
  background-color: #e3f4dd;
  border-color: #e1f3db;
}

.btn-check:focus+.btn-success,
.btn-success:focus {
  color: #000;
  background-color: #e3f4dd;
  border-color: #e1f3db;
  box-shadow: 0 0 0 0 rgba(189, 206, 183, 0.5);
}

.btn-check:checked+.btn-success,
.btn-check:active+.btn-success,
.btn-success:active,
.btn-success.active,
.show>.btn-success.dropdown-toggle {
  color: #000;
  background-color: #e5f5df;
  border-color: #e1f3db;
}

.btn-check:checked+.btn-success:focus,
.btn-check:active+.btn-success:focus,
.btn-success:active:focus,
.btn-success.active:focus,
.show>.btn-success.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(189, 206, 183, 0.5);
}

.btn-success:disabled,
.btn-success.disabled {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-outline-success {
  color: #def2d7;
  border-color: #def2d7;
}

.btn-outline-success:hover {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-check:focus+.btn-outline-success,
.btn-outline-success:focus {
  box-shadow: 0 0 0 0 rgba(222, 242, 215, 0.5);
}

.btn-check:checked+.btn-outline-success,
.btn-check:active+.btn-outline-success,
.btn-outline-success:active,
.btn-outline-success.active,
.btn-outline-success.dropdown-toggle.show {
  color: #000;
  background-color: #def2d7;
  border-color: #def2d7;
}

.btn-check:checked+.btn-outline-success:focus,
.btn-check:active+.btn-outline-success:focus,
.btn-outline-success:active:focus,
.btn-outline-success.active:focus,
.btn-outline-success.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(222, 242, 215, 0.5);
}

.btn-outline-success:disabled,
.btn-outline-success.disabled {
  color: #def2d7;
  background-color: transparent;
}

.btn-hover-success:hover {
  background-color: #def2d7;
  color: #fff;
}

.btn-info {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
  box-shadow: none;
}

.btn-info:hover {
  color: #000;
  background-color: #d5ecf7;
  border-color: #d2ebf7;
}

.btn-check:focus+.btn-info,
.btn-info:focus {
  color: #000;
  background-color: #d5ecf7;
  border-color: #d2ebf7;
  box-shadow: 0 0 0 0 rgba(174, 198, 209, 0.5);
}

.btn-check:checked+.btn-info,
.btn-check:active+.btn-info,
.btn-info:active,
.btn-info.active,
.show>.btn-info.dropdown-toggle {
  color: #000;
  background-color: #d7edf8;
  border-color: #d2ebf7;
}

.btn-check:checked+.btn-info:focus,
.btn-check:active+.btn-info:focus,
.btn-info:active:focus,
.btn-info.active:focus,
.show>.btn-info.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(174, 198, 209, 0.5);
}

.btn-info:disabled,
.btn-info.disabled {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-outline-info {
  color: #cde9f6;
  border-color: #cde9f6;
}

.btn-outline-info:hover {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-check:focus+.btn-outline-info,
.btn-outline-info:focus {
  box-shadow: 0 0 0 0 rgba(205, 233, 246, 0.5);
}

.btn-check:checked+.btn-outline-info,
.btn-check:active+.btn-outline-info,
.btn-outline-info:active,
.btn-outline-info.active,
.btn-outline-info.dropdown-toggle.show {
  color: #000;
  background-color: #cde9f6;
  border-color: #cde9f6;
}

.btn-check:checked+.btn-outline-info:focus,
.btn-check:active+.btn-outline-info:focus,
.btn-outline-info:active:focus,
.btn-outline-info.active:focus,
.btn-outline-info.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(205, 233, 246, 0.5);
}

.btn-outline-info:disabled,
.btn-outline-info.disabled {
  color: #cde9f6;
  background-color: transparent;
}

.btn-hover-info:hover {
  background-color: #cde9f6;
  color: #fff;
}

.btn-warning {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
  box-shadow: none;
}

.btn-warning:hover {
  color: #000;
  background-color: #f8f5dd;
  border-color: #f8f4db;
}

.btn-check:focus+.btn-warning,
.btn-warning:focus {
  color: #000;
  background-color: #f8f5dd;
  border-color: #f8f4db;
  box-shadow: 0 0 0 0 rgba(210, 207, 183, 0.5);
}

.btn-check:checked+.btn-warning,
.btn-check:active+.btn-warning,
.btn-warning:active,
.btn-warning.active,
.show>.btn-warning.dropdown-toggle {
  color: #000;
  background-color: #f9f5df;
  border-color: #f8f4db;
}

.btn-check:checked+.btn-warning:focus,
.btn-check:active+.btn-warning:focus,
.btn-warning:active:focus,
.btn-warning.active:focus,
.show>.btn-warning.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(210, 207, 183, 0.5);
}

.btn-warning:disabled,
.btn-warning.disabled {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-outline-warning {
  color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-outline-warning:hover {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-check:focus+.btn-outline-warning,
.btn-outline-warning:focus {
  box-shadow: 0 0 0 0 rgba(247, 243, 215, 0.5);
}

.btn-check:checked+.btn-outline-warning,
.btn-check:active+.btn-outline-warning,
.btn-outline-warning:active,
.btn-outline-warning.active,
.btn-outline-warning.dropdown-toggle.show {
  color: #000;
  background-color: #f7f3d7;
  border-color: #f7f3d7;
}

.btn-check:checked+.btn-outline-warning:focus,
.btn-check:active+.btn-outline-warning:focus,
.btn-outline-warning:active:focus,
.btn-outline-warning.active:focus,
.btn-outline-warning.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(247, 243, 215, 0.5);
}

.btn-outline-warning:disabled,
.btn-outline-warning.disabled {
  color: #f7f3d7;
  background-color: transparent;
}

.btn-hover-warning:hover {
  background-color: #f7f3d7;
  color: #fff;
}

.btn-danger {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
  box-shadow: none;
}

.btn-danger:hover {
  color: #000;
  background-color: #efd0ce;
  border-color: #eececb;
}

.btn-check:focus+.btn-danger,
.btn-danger:focus {
  color: #000;
  background-color: #efd0ce;
  border-color: #eececb;
  box-shadow: 0 0 0 0 rgba(201, 170, 167, 0.5);
}

.btn-check:checked+.btn-danger,
.btn-check:active+.btn-danger,
.btn-danger:active,
.btn-danger.active,
.show>.btn-danger.dropdown-toggle {
  color: #000;
  background-color: #f0d3d1;
  border-color: #eececb;
}

.btn-check:checked+.btn-danger:focus,
.btn-check:active+.btn-danger:focus,
.btn-danger:active:focus,
.btn-danger.active:focus,
.show>.btn-danger.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(201, 170, 167, 0.5);
}

.btn-danger:disabled,
.btn-danger.disabled {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-outline-danger {
  color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-outline-danger:hover {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-check:focus+.btn-outline-danger,
.btn-outline-danger:focus {
  box-shadow: 0 0 0 0 rgba(236, 200, 197, 0.5);
}

.btn-check:checked+.btn-outline-danger,
.btn-check:active+.btn-outline-danger,
.btn-outline-danger:active,
.btn-outline-danger.active,
.btn-outline-danger.dropdown-toggle.show {
  color: #000;
  background-color: #ecc8c5;
  border-color: #ecc8c5;
}

.btn-check:checked+.btn-outline-danger:focus,
.btn-check:active+.btn-outline-danger:focus,
.btn-outline-danger:active:focus,
.btn-outline-danger.active:focus,
.btn-outline-danger.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(236, 200, 197, 0.5);
}

.btn-outline-danger:disabled,
.btn-outline-danger.disabled {
  color: #ecc8c5;
  background-color: transparent;
}

.btn-hover-danger:hover {
  background-color: #ecc8c5;
  color: #fff;
}

.btn-dark {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
  box-shadow: none;
}

.btn-dark:hover {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
}

.btn-check:focus+.btn-dark,
.btn-dark:focus {
  color: #fff;
  background-color: #1d1d1d;
  border-color: #1b1b1b;
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-check:checked+.btn-dark,
.btn-check:active+.btn-dark,
.btn-dark:active,
.btn-dark.active,
.show>.btn-dark.dropdown-toggle {
  color: #fff;
  background-color: #1b1b1b;
  border-color: #1a1a1a;
}

.btn-check:checked+.btn-dark:focus,
.btn-check:active+.btn-dark:focus,
.btn-dark:active:focus,
.btn-dark.active:focus,
.show>.btn-dark.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(67, 67, 67, 0.5);
}

.btn-dark:disabled,
.btn-dark.disabled {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-outline-dark {
  color: #222222;
  border-color: #222222;
}

.btn-outline-dark:hover {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:focus+.btn-outline-dark,
.btn-outline-dark:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-dark,
.btn-check:active+.btn-outline-dark,
.btn-outline-dark:active,
.btn-outline-dark.active,
.btn-outline-dark.dropdown-toggle.show {
  color: #fff;
  background-color: #222222;
  border-color: #222222;
}

.btn-check:checked+.btn-outline-dark:focus,
.btn-check:active+.btn-outline-dark:focus,
.btn-outline-dark:active:focus,
.btn-outline-dark.active:focus,
.btn-outline-dark.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-dark:disabled,
.btn-outline-dark.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-hover-dark:hover {
  background-color: #222222;
  color: #fff;
}

.btn-red {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
  box-shadow: none;
}

.btn-red:hover {
  color: #fff;
  background-color: #a62323;
  border-color: #9c2121;
}

.btn-check:focus+.btn-red,
.btn-red:focus {
  color: #fff;
  background-color: #a62323;
  border-color: #9c2121;
  box-shadow: 0 0 0 0 rgba(204, 73, 73, 0.5);
}

.btn-check:checked+.btn-red,
.btn-check:active+.btn-red,
.btn-red:active,
.btn-red.active,
.show>.btn-red.dropdown-toggle {
  color: #fff;
  background-color: #9c2121;
  border-color: #921f1f;
}

.btn-check:checked+.btn-red:focus,
.btn-check:active+.btn-red:focus,
.btn-red:active:focus,
.btn-red.active:focus,
.show>.btn-red.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(204, 73, 73, 0.5);
}

.btn-red:disabled,
.btn-red.disabled {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-outline-red {
  color: #c32929;
  border-color: #c32929;
}

.btn-outline-red:hover {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-check:focus+.btn-outline-red,
.btn-outline-red:focus {
  box-shadow: 0 0 0 0 rgba(195, 41, 41, 0.5);
}

.btn-check:checked+.btn-outline-red,
.btn-check:active+.btn-outline-red,
.btn-outline-red:active,
.btn-outline-red.active,
.btn-outline-red.dropdown-toggle.show {
  color: #fff;
  background-color: #c32929;
  border-color: #c32929;
}

.btn-check:checked+.btn-outline-red:focus,
.btn-check:active+.btn-outline-red:focus,
.btn-outline-red:active:focus,
.btn-outline-red.active:focus,
.btn-outline-red.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(195, 41, 41, 0.5);
}

.btn-outline-red:disabled,
.btn-outline-red.disabled {
  color: #c32929;
  background-color: transparent;
}

.btn-hover-red:hover {
  background-color: #c32929;
  color: #fff;
}

.btn-beige {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
  box-shadow: none;
}

.btn-beige:hover {
  color: #ffffff;
  background-color: #c0aa7a;
  border-color: #c0aa7a;
}

.btn-check:focus+.btn-beige,
.btn-beige:focus {
  color: #ffffff;
  background-color: #c0aa7a;
  border-color: #c0aa7a;
  box-shadow: 0 0 0 0 rgba(196, 175, 129, 0.5);
}

.btn-check:checked+.btn-beige,
.btn-check:active+.btn-beige,
.btn-beige:active,
.btn-beige.active,
.show>.btn-beige.dropdown-toggle {
  color: #000;
  background-color: #948156;
  border-color: #8b7950;
}

.btn-check:checked+.btn-beige:focus,
.btn-check:active+.btn-beige:focus,
.btn-beige:active:focus,
.btn-beige.active:focus,
.show>.btn-beige.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(196, 175, 129, 0.5);
}

.btn-beige:disabled,
.btn-beige.disabled {
  color: #000;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-outline-beige {
  color: #b9a16b;
  border-color: #b9a16b;
}

.btn-outline-beige:hover {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-check:focus+.btn-outline-beige,
.btn-outline-beige:focus {
  box-shadow: 0 0 0 0 rgba(185, 161, 107, 0.5);
}

.btn-check:checked+.btn-outline-beige,
.btn-check:active+.btn-outline-beige,
.btn-outline-beige:active,
.btn-outline-beige.active,
.btn-outline-beige.dropdown-toggle.show {
  color: #ffffff;
  background-color: #b9a16b;
  border-color: #b9a16b;
}

.btn-check:checked+.btn-outline-beige:focus,
.btn-check:active+.btn-outline-beige:focus,
.btn-outline-beige:active:focus,
.btn-outline-beige.active:focus,
.btn-outline-beige.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(185, 161, 107, 0.5);
}

.btn-outline-beige:disabled,
.btn-outline-beige.disabled {
  color: #b9a16b;
  background-color: transparent;
}

.btn-light {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
  box-shadow: none;
}

.btn-light:hover {
  color: #222222;
  background-color: #e7e7e7;
  border-color: #e7e7e7;
}

.btn-check:focus+.btn-light,
.btn-light:focus {
  color: #222222;
  background-color: #e7e7e7;
  border-color: #e7e7e7;
  box-shadow: 0 0 0 0 rgba(199, 199, 199, 0.5);
}

.btn-check:checked+.btn-light,
.btn-check:active+.btn-light,
.btn-light:active,
.btn-light.active,
.show>.btn-light.dropdown-toggle {
  color: #000;
  background-color: #e9e9e9;
  border-color: #e7e7e7;
}

.btn-check:checked+.btn-light:focus,
.btn-check:active+.btn-light:focus,
.btn-light:active:focus,
.btn-light.active:focus,
.show>.btn-light.dropdown-toggle:focus {
  box-shadow: 0 0 0 0 rgba(199, 199, 199, 0.5);
}

.btn-light:disabled,
.btn-light.disabled {
  color: #000;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-outline-light {
  color: #222222;
  border-color: #222222;
  border-color: #e4e4e4;
}

.btn-outline-light:hover {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-check:focus+.btn-outline-light,
.btn-outline-light:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-check:checked+.btn-outline-light,
.btn-check:active+.btn-outline-light,
.btn-outline-light:active,
.btn-outline-light.active,
.btn-outline-light.dropdown-toggle.show {
  color: #222222;
  background-color: #e4e4e4;
  border-color: #e4e4e4;
}

.btn-check:checked+.btn-outline-light:focus,
.btn-check:active+.btn-outline-light:focus,
.btn-outline-light:active:focus,
.btn-outline-light.active:focus,
.btn-outline-light.dropdown-toggle.show:focus {
  box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.btn-outline-light:disabled,
.btn-outline-light.disabled {
  color: #222222;
  background-color: transparent;
}

.btn-link {
  display: inline-block;
  position: relative;
  padding: 0;
  border: 0;
  background-color: transparent;
  color: #222222;
  font-weight: 400;
  text-decoration: none;
}

.btn-link:hover {
  color: #1b1b1b;
}

.btn-link:disabled,
.btn-link.disabled {
  color: #6c757d;
}

.btn-link:after {
  content: '';
  display: block;
  position: absolute;
  top: 100%;
  left: 0;
  width: 0;
  max-width: 100%;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.btn-link:hover:after,
.btn-link.btn-link_active:after {
  width: 3.125rem;
}

.btn-link.default-underline:after {
  width: 3.125rem;
}

.btn-link.default-underline:hover:after {
  width: 100%;
}

.btn-link_lg:hover:after,
.btn-link_lg.btn-link_active:after {
  width: calc(100% - 1rem);
}

.btn-link_lg.default-underline:after {
  width: 86%;
}

.btn-link_lg.default-underline:hover:after {
  width: 100%;
}

.btn-link_md:hover:after,
.btn-link_md.btn-link_active:after {
  width: 70%;
}

.btn-link_md.default-underline:after {
  width: 70%;
}

.btn-link_md.default-underline:hover:after {
  width: 100%;
}

.btn-link_sm:hover:after,
.btn-link_sm.btn-link_active:after {
  width: 45%;
}

.btn-link_sm.default-underline:after {
  width: 45%;
}

.btn-link_sm.default-underline:hover:after {
  width: 100%;
}

.btn-link_f:hover:after,
.btn-link_f.btn-link_active:after {
  width: 100%;
}

.btn-round {
  width: 1.875rem;
  height: 1.875rem;
  padding: 0;
  border-radius: 100%;
}

@media (min-width: 768px) {
  .btn-round {
    width: 2.5rem;
    height: 2.5rem;
  }
}

.btn-round-sm {
  width: 2.1875rem;
  height: 2.1875rem;
  padding: 0;
  border-radius: 100%;
}

.btn-square {
  width: 2.8125rem;
  height: 2.8125rem;
  padding: 0;
}

.btn-lg,
.btn-group-lg>.btn {
  padding: 0.5rem 1.25rem;
  font-size: 0.875rem;
  border-radius: 0;
  line-height: 1.5rem;
}

.btn-sm,
.btn-group-sm>.btn {
  padding: 0.375rem 1.25rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.nav-icon {
  display: block;
  fill: currentColor;
}

.btn-icon {
  border: 0;
  background-color: transparent;
}

.btn-text {
  text-decoration: underline;
}

.swiper-pagination-bullet {
  position: relative;
  width: 1.875rem;
  height: 1.875rem;
  margin: 0 4px;
  border: 2px solid currentColor;
  background-color: transparent;
  color: transparent;
  opacity: 1;
  outline: none;
}

.swiper-pagination-bullet:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0.375rem;
  height: 0.375rem;
  margin-top: -0.1875rem;
  margin-left: -0.1875rem;
  border-radius: 100%;
  background-color: currentColor;
  color: #ddc2bd;
  content: '';
}

.swiper-pagination-bullet:first-child {
  margin-left: 0;
}

.swiper-pagination-bullets.dark-bullet .swiper-pagination-bullet:after {
  color: #222;
}

.swiper-pagination-bullet-active {
  color: #222222;
}

.swiper-pagination-bullet-active:after {
  color: inherit;
}

.swiper-pagination-white .swiper-pagination-bullet-active {
  color: #fff;
}

.swiper-pagination-bullets.theme-color .swiper-pagination-bullet-active {
  color: #193174;
}

.swatch-color {
  display: block;
  position: relative;
  width: 1.75rem;
  height: 1.75rem;
  margin-right: .75rem;
  margin-bottom: .75rem;
  border-radius: 50%;
}

.swatch-color:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 1rem;
  height: 1rem;
  margin-top: -0.5rem;
  margin-left: -0.5rem;
  border-radius: 100%;
  background-color: currentColor;
  color: inherit;
  content: '';
}

.swatch-color.swatch_active {
  border: 2px solid #222222;
}

.hover-container .swatch-color {
  margin: 0;
}

.swatch-size.swatch_active {
  background-color: #e4e4e4;
}

.filter-tag {
  padding: 0 1rem;
  border: 0;
  background-color: #e4e4e4;
  font-size: 11px;
  line-height: 1.875rem;
}

.filter-tag.swatch_active {
  display: none !important;
}

.form-label {
  margin-bottom: 0.5rem;
}

.col-form-label {
  padding-top: 1.0625rem;
  padding-bottom: 1.0625rem;
  margin-bottom: 0;
  font-size: inherit;
  line-height: 1.7143;
}

.col-form-label-lg {
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
  font-size: 1.25rem;
}

.col-form-label-sm {
  padding-top: 0.875rem;
  padding-bottom: 0.875rem;
  font-size: 0.875rem;
}

.form-text {
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #6c757d;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.9375rem 0.9375rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
  color: #222222;
  background-color: #fff;
  background-clip: padding-box;
  border: 0.125rem solid #e4e4e4;
  appearance: none;
  border-radius: 0;
  box-shadow: none;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control {
    transition: none;
  }
}

.form-control[type="file"] {
  overflow: hidden;
}

.form-control[type="file"]:not(:disabled):not([readonly]) {
  cursor: pointer;
}

.form-control:focus {
  color: #222222;
  background-color: #fff;
  border-color: #222222;
  outline: 0;
  box-shadow: none;
}

.form-control::-webkit-date-and-time-value {
  height: 1.7143em;
}

.form-control::placeholder {
  color: #6c757d;
  opacity: 1;
}

.form-control:disabled,
.form-control[readonly] {
  background-color: #fff;
  opacity: 1;
}

.form-control::file-selector-button {
  padding: 0.9375rem 0.9375rem 0.75rem;
  margin: -0.9375rem -0.9375rem;
  margin-inline-end: 0.9375rem;
  color: #222222;
  background-color: #e9ecef;
  pointer-events: none;
  border-color: inherit;
  border-style: solid;
  border-width: 0;
  border-inline-end-width: 0.125rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control::file-selector-button {
    transition: none;
  }
}

.form-control:hover:not(:disabled):not([readonly])::file-selector-button {
  background-color: #dde0e3;
}

.form-control::-webkit-file-upload-button {
  padding: 0.9375rem 0.9375rem 0.75rem;
  margin: -0.9375rem -0.9375rem;
  margin-inline-end: 0.9375rem;
  color: #222222;
  background-color: #e9ecef;
  pointer-events: none;
  border-color: inherit;
  border-style: solid;
  border-width: 0;
  border-inline-end-width: 0.125rem;
  border-radius: 0;
  transition: all 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-control::-webkit-file-upload-button {
    transition: none;
  }
}

.form-control:hover:not(:disabled):not([readonly])::-webkit-file-upload-button {
  background-color: #dde0e3;
}

.form-control[type="password"] {
  font-family: 'Trebuchet MS', sans-serif;
  letter-spacing: 0.18em;
}

.form-control_gray {
  border-color: #e4e4e4;
}

.form-control-plaintext {
  display: block;
  width: 100%;
  padding: 0.9375rem 0;
  margin-bottom: 0;
  line-height: 1.7143;
  color: #222222;
  background-color: transparent;
  border: solid transparent;
  border-width: 0.125rem 0;
}

.form-control-plaintext.form-control-sm,
.form-control-plaintext.form-control-lg {
  padding-right: 0;
  padding-left: 0;
}

.form-control-sm {
  min-height: calc(1.5em + 0.5rem + 2px);
  padding: 0.75rem 1.125rem 0.6rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.form-control-sm::file-selector-button {
  padding: 0.75rem 1.125rem 0.6rem;
  margin: -0.75rem -1.125rem;
  margin-inline-end: 1.125rem;
}

.form-control-sm::-webkit-file-upload-button {
  padding: 0.75rem 1.125rem 0.6rem;
  margin: -0.75rem -1.125rem;
  margin-inline-end: 1.125rem;
}

.form-control-lg {
  min-height: calc(1.5em + 1rem + 2px);
  padding: 1.125rem 1.3125rem 0.9rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.form-control-lg::file-selector-button {
  padding: 1.125rem 1.3125rem 0.9rem;
  margin: -1.125rem -1.3125rem;
  margin-inline-end: 1.3125rem;
}

.form-control-lg::-webkit-file-upload-button {
  padding: 1.125rem 1.3125rem 0.9rem;
  margin: -1.125rem -1.3125rem;
  margin-inline-end: 1.3125rem;
}

textarea.form-control {
  min-height: calc(1.5em + 0.75rem + 2px);
}

textarea.form-control-sm {
  min-height: calc(1.5em + 0.5rem + 2px);
}

textarea.form-control-lg {
  min-height: calc(1.5em + 1rem + 2px);
}

.form-control-color {
  max-width: 3rem;
  height: auto;
  padding: 0.9375rem;
}

.form-control-color:not(:disabled):not([readonly]) {
  cursor: pointer;
}

.form-control-color::-moz-color-swatch {
  height: 1.7143em;
  border-radius: 0;
}

.form-control-color::-webkit-color-swatch {
  height: 1.7143em;
  border-radius: 0;
}

.form-select {
  display: block;
  width: 100%;
  padding: 0.9375rem 0.9375rem 0.75rem;
  padding-right: 2.34375rem;
  font-size: 0.95rem;
  font-weight: 400;
  line-height: 1.7143;
  border: 0.125rem solid #e4e4e4;
  box-shadow: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.9375rem center;
  background-size: 16px 12px;
  color: #222222;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0;
}

/* test */
.custom-select {
  position: relative;
  width: 100%; /* Adjust width as needed */
  z-index: 2;
  display: block;
  padding: 0.9375rem 0.9375rem 0.75rem;
  padding-right: 2.34375rem;
  font-size: 0.95rem;
  font-weight: 400;
  line-height: 1.7143;
  border: 0.125rem solid #e4e4e4;
  box-shadow: none;
  background-color: #fff;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.9375rem center;
  background-size: 16px 12px;
  color: #222222;
  appearance: none;
  border-radius: 0;
}

.custom-select select {
  display: none;
}

.custom-select .select-selected {
  background-color: #fff;
  /* border: 1px solid #ccc;
  padding: 5px 10px; */
  cursor: pointer;
}

.custom-select .select-selected:after {
  position: absolute;
  /* top: 50%;
  right: 10px;
  transform: translateY(-50%); */
}

/* .custom-select .select-items {
  display: none;
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  border-bottom: none; 
  width: 100%;
  max-height: 150px; 
  overflow-y: auto;
  top: 100%; 
} */

/* .custom-select .select-items div {
  padding: 5px 10px;
  cursor: pointer;
} */

/* .custom-select .select-items div:hover {
  background-color: #f2f2f2;
} */


/* test */

.form-select[multiple],
.form-select[size]:not([size="1"]) {
  padding-right: 0.75rem;
  background-image: none;
}

.form-select:disabled {
  color: #6c757d;
  background-color: #e9ecef;
}

.form-select:-moz-focusring {
  color: transparent;
  text-shadow: 0 0 0 #222222;
}

.form-select-sm {
  width: auto;
  padding: 0.75rem 1.125rem 0.6rem;
  padding-right: 2.025rem;
  background-position: right 0.5625rem center;
}

.form-select-lg {
  padding: 1.125rem 1.3125rem 0.9rem;
}

.multi-select .multi-select__actor {
  background-color: #fff;
}

.multi-select__actor {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center;
  background-repeat: no-repeat;
  background-size: 16px 12px;
  cursor: pointer;
}

.multi-select__item {
  display: flex;
  align-items: center;
  position: relative;
  width: 100%;
  padding: 0.5rem 0;
  color: #767676;
  cursor: pointer;
}

.multi-select__item:hover {
  color: #3b3b3b;
}

.multi-select__item:before {
  content: '';
  display: block;
  width: 1rem;
  height: 1rem;
  color: #e4e4e4;
  border: 0.125rem solid currentColor;
  border-radius: 0;
  margin-right: 0.75rem;
}

.multi-select__item:after {
  content: '';
  display: block;
  position: absolute;
  left: 0.25rem;
  top: 50%;
  transform: translateY(-50%);
  width: 0.5rem;
  height: 0.5rem;
  background-color: transparent;
  border-radius: 0;
}

.mult-select__item_selected {
  color: #222222;
}

.mult-select__item_selected:before {
  color: #222222;
}

.mult-select__item_selected:after {
  background-color: #222222;
}

.form-check {
  display: block;
  position: relative;
  min-height: 1.5rem;
  padding-left: 1.625rem;
  margin-bottom: 1rem;
}

.form-check .form-check-input {
  float: left;
  margin-left: -1.625rem;
}

.form-check-input {
  width: 1rem;
  height: 1rem;
  margin-top: 0.25000625rem;
  vertical-align: top;
  background-color: #fff;
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  border: 0.125rem solid #e4e4e4;
  appearance: none;
  color-adjust: exact;
  transition: background-color 0.15s ease-in-out, background-position 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
  .form-check-input {
    transition: none;
  }
}

.form-check-input[type="checkbox"] {
  border-radius: 0;
}

.form-check-input[type="radio"] {
  border-radius: 50%;
}

.form-check-input[type="radio"]:after {
  border-radius: 50%;
}

.form-check-input.form-check-input_fill {
  position: relative;
  border-width: 0.125rem;
}

.form-check-input.form-check-input_fill:after {
  content: '';
  display: block;
  position: absolute;
  left: 0.125rem;
  top: 50%;
  transform: translateY(-50%);
  width: 0.5rem;
  height: 0.5rem;
  background-color: transparent;
}

.form-check-input:focus {
  border-color: #222222;
  outline: 0;
  box-shadow: none;
}

.form-check-input:checked {
  background-color: #222222;
  border-color: #222222;
}

.form-check-input:checked[type="checkbox"] {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10l3 3l6-6'/%3e%3c/svg%3e");
}

.form-check-input:checked[type="radio"] {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='2' fill='%23fff'/%3e%3c/svg%3e");
}

.form-check-input:checked.form-check-input_fill {
  background-image: none;
  background-color: #ffffff;
}

.form-check-input:checked.form-check-input_fill:after {
  background-color: #222222;
}

.form-check-input[type="checkbox"]:indeterminate {
  background-color: #222222;
  border-color: #222222;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3e%3cpath fill='none' stroke='%23fff' stroke-linecap='round' stroke-linejoin='round' stroke-width='3' d='M6 10h8'/%3e%3c/svg%3e");
}

.form-check-input:disabled {
  pointer-events: none;
  opacity: 0.5;
}

.form-check-input[disabled]~.form-check-label,
.form-check-input:disabled~.form-check-label {
  opacity: 0.5;
}

.form-switch {
  min-height: 1.875rem;
  padding-left: 4.625rem;
}

.form-switch .form-check-input {
  width: 3.75rem;
  height: 1.875rem;
  margin-top: 0;
  margin-left: -4.625rem;
  border-radius: 2em;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23767676'/%3e%3c/svg%3e");
  background-position: left center;
}

.form-switch .form-check-input:focus {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23222222'/%3e%3c/svg%3e");
}

.form-switch .form-check-input:checked {
  background-position: right center;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23fff'/%3e%3c/svg%3e");
}

.form-switch .form-check-label {
  line-height: 1.875rem;
}

.form-check-inline {
  display: inline-block;
  margin-right: 1rem;
}

.btn-check {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}

.btn-check[disabled]+.btn,
.btn-check:disabled+.btn {
  pointer-events: none;
  opacity: 0.65;
}

.form-range {
  width: 100%;
  height: 1.5rem;
  padding: 0;
  background-color: transparent;
  appearance: none;
}

.form-range:focus {
  outline: none;
}

.form-range:focus::-webkit-slider-thumb {
  box-shadow: 0 0 0 1px #fff, none;
}

.form-range:focus::-moz-range-thumb {
  box-shadow: 0 0 0 1px #fff, none;
}

.form-range::-moz-focus-outer {
  border: 0;
}

.form-range::-webkit-slider-thumb {
  width: 1rem;
  height: 1rem;
  margin-top: -0.25rem;
  background-color: #222222;
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.1rem 0.25rem rgba(0, 0, 0, 0.1);
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  appearance: none;
}

@media (prefers-reduced-motion: reduce) {
  .form-range::-webkit-slider-thumb {
    transition: none;
  }
}

.form-range::-webkit-slider-thumb:active {
  background-color: #bdbdbd;
}

.form-range::-webkit-slider-runnable-track {
  width: 100%;
  height: 0.5rem;
  color: transparent;
  cursor: pointer;
  background-color: #dee2e6;
  border-color: transparent;
  border-radius: 1rem;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);
}

.form-range::-moz-range-thumb {
  width: 1rem;
  height: 1rem;
  background-color: #222222;
  border: 0;
  border-radius: 1rem;
  box-shadow: 0 0.1rem 0.25rem rgba(0, 0, 0, 0.1);
  transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  appearance: none;
}

@media (prefers-reduced-motion: reduce) {
  .form-range::-moz-range-thumb {
    transition: none;
  }
}

.form-range::-moz-range-thumb:active {
  background-color: #bdbdbd;
}

.form-range::-moz-range-track {
  width: 100%;
  height: 0.5rem;
  color: transparent;
  cursor: pointer;
  background-color: #dee2e6;
  border-color: transparent;
  border-radius: 1rem;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.075);
}

.form-range:disabled {
  pointer-events: none;
}

.form-range:disabled::-webkit-slider-thumb {
  background-color: #adb5bd;
}

.form-range:disabled::-moz-range-thumb {
  background-color: #adb5bd;
}

.form-floating {
  position: relative;
}

.form-floating>.form-control,
.form-floating>.form-select {
  height: calc(3.625rem + 2px);
  padding: 1.125rem 1.3125rem 0.9rem;
}

.form-floating>label {
  position: absolute;
  top: 1rem;
  left: 0.75rem;
  padding: 0 0.5rem;
  pointer-events: none;
  border: 0.125rem solid transparent;
  transform-origin: 0 0;
  transition: opacity 0.1s ease-in-out, transform 0.1s ease-in-out;
  color: #767676;
}

@media (prefers-reduced-motion: reduce) {
  .form-floating>label {
    transition: none;
  }
}

.form-floating>.form-control::placeholder {
  color: transparent;
}

.form-floating>.form-control:-webkit-autofill {
  padding-top: 1.625rem;
  padding-bottom: 0.625rem;
}

.form-floating>.form-select {
  padding-top: 1.625rem;
  padding-bottom: 0.625rem;
}

.form-floating>.form-control:focus~label,
.form-floating>.form-control:not(:placeholder-shown)~label,
.form-floating>.form-select~label {
  background-color: #ffffff;
  color: #222222;
  transform: translateY(-1.9rem);
}

.form-floating>.form-control:-webkit-autofill~label {
  background-color: #ffffff;
  color: #222222;
  transform: translateY(-1.9rem);
}

.form-label-fixed {
  position: relative;
}

.form-label-fixed>.form-label {
  position: absolute;
  top: -1.00000625rem;
  left: 1rem;
  margin: 0;
  padding: 0.25rem 0.5rem 0.25rem 0.5rem;
  background-color: #ffffff;
  color: #222222;
  z-index: 1;
}

.input-group {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.input-group>.form-control,
.input-group>.form-select {
  position: relative;
  flex: 1 1 auto;
  width: 1%;
  min-width: 0;
}

.input-group>.form-control:focus,
.input-group>.form-select:focus {
  z-index: 3;
}

.input-group .btn {
  position: relative;
  z-index: 2;
}

.input-group .btn:focus {
  z-index: 3;
}

.input-group-text {
  display: flex;
  align-items: center;
  padding: 0.375rem 0.75rem;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.7143;
  color: #222222;
  text-align: center;
  white-space: nowrap;
  background-color: #e9ecef;
  border: 0.125rem solid #ced4da;
  border-radius: 0;
}

.input-group-lg>.form-control,
.input-group-lg>.form-select,
.input-group-lg>.input-group-text,
.input-group-lg>.btn {
  padding: 1.125rem 1.3125rem;
  font-size: 1.25rem;
  border-radius: 0;
}

.input-group-sm>.form-control,
.input-group-sm>.form-select,
.input-group-sm>.input-group-text,
.input-group-sm>.btn {
  padding: 0.75rem 1.125rem;
  font-size: 0.875rem;
  border-radius: 0;
}

.input-group-lg>.form-select,
.input-group-sm>.form-select {
  padding-right: 1.75rem;
}

.input-group:not(.has-validation)> :not(:last-child):not(.dropdown-toggle):not(.dropdown-menu),
.input-group:not(.has-validation)>.dropdown-toggle:nth-last-child(n + 3) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.input-group.has-validation> :nth-last-child(n + 3):not(.dropdown-toggle):not(.dropdown-menu),
.input-group.has-validation>.dropdown-toggle:nth-last-child(n + 4) {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.input-group> :not(:first-child):not(.dropdown-menu):not(.valid-tooltip):not(.valid-feedback):not(.invalid-tooltip):not(.invalid-feedback) {
  margin-left: -0.125rem;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.valid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #198754;
}

.valid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  color: #fff;
  background-color: rgba(25, 135, 84, 0.9);
  border-radius: 0.25rem;
}

.was-validated :valid~.valid-feedback,
.was-validated :valid~.valid-tooltip,
.is-valid~.valid-feedback,
.is-valid~.valid-tooltip {
  display: block;
}

.was-validated .form-control:valid,
.form-control.is-valid {
  border-color: #198754;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-control:valid:focus,
.form-control.is-valid:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated textarea.form-control:valid,
textarea.form-control.is-valid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
}

.was-validated .form-select:valid,
.form-select.is-valid {
  border-color: #198754;
  padding-right: calc(0.75em + 2.3125rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e"), url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23198754' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center, center right 1.75rem;
  background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-select:valid:focus,
.form-select.is-valid:focus {
  border-color: #198754;
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated .form-check-input:valid,
.form-check-input.is-valid {
  border-color: #198754;
}

.was-validated .form-check-input:valid:checked,
.form-check-input.is-valid:checked {
  background-color: #198754;
}

.was-validated .form-check-input:valid:focus,
.form-check-input.is-valid:focus {
  box-shadow: 0 0 0 0.25rem rgba(25, 135, 84, 0.25);
}

.was-validated .form-check-input:valid~.form-check-label,
.form-check-input.is-valid~.form-check-label {
  color: #198754;
}

.form-check-inline .form-check-input~.valid-feedback {
  margin-left: .5em;
}

.invalid-feedback {
  display: none;
  width: 100%;
  margin-top: 0.25rem;
  font-size: 0.875em;
  color: #dc3545;
}

.invalid-tooltip {
  position: absolute;
  top: 100%;
  z-index: 5;
  display: none;
  max-width: 100%;
  padding: 0.25rem 0.5rem;
  margin-top: .1rem;
  font-size: 0.875rem;
  color: #fff;
  background-color: rgba(220, 53, 69, 0.9);
  border-radius: 0.25rem;
}

.was-validated :invalid~.invalid-feedback,
.was-validated :invalid~.invalid-tooltip,
.is-invalid~.invalid-feedback,
.is-invalid~.invalid-tooltip {
  display: block;
}

.was-validated .form-control:invalid,
.form-control.is-invalid {
  border-color: #dc3545;
  padding-right: calc(1.5em + 0.75rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right calc(0.375em + 0.1875rem) center;
  background-size: calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-control:invalid:focus,
.form-control.is-invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated textarea.form-control:invalid,
textarea.form-control.is-invalid {
  padding-right: calc(1.5em + 0.75rem);
  background-position: top calc(0.375em + 0.1875rem) right calc(0.375em + 0.1875rem);
}

.was-validated .form-select:invalid,
.form-select.is-invalid {
  border-color: #dc3545;
  padding-right: calc(0.75em + 2.3125rem);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e"), url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12' width='12' height='12' fill='none' stroke='%23dc3545'%3e%3ccircle cx='6' cy='6' r='4.5'/%3e%3cpath stroke-linejoin='round' d='M5.8 3.6h.4L6 6.5z'/%3e%3ccircle cx='6' cy='8.2' r='.6' fill='%23dc3545' stroke='none'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center, center right 1.75rem;
  background-size: 16px 12px, calc(0.75em + 0.375rem) calc(0.75em + 0.375rem);
}

.was-validated .form-select:invalid:focus,
.form-select.is-invalid:focus {
  border-color: #dc3545;
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated .form-check-input:invalid,
.form-check-input.is-invalid {
  border-color: #dc3545;
}

.was-validated .form-check-input:invalid:checked,
.form-check-input.is-invalid:checked {
  background-color: #dc3545;
}

.was-validated .form-check-input:invalid:focus,
.form-check-input.is-invalid:focus {
  box-shadow: 0 0 0 0.25rem rgba(220, 53, 69, 0.25);
}

.was-validated .form-check-input:invalid~.form-check-label,
.form-check-input.is-invalid~.form-check-label {
  color: #dc3545;
}

.form-check-inline .form-check-input~.invalid-feedback {
  margin-left: .5em;
}

.search-field .search-field__actor {
  background-color: #fff;
}

.search-field__arrow-down {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%232F2D51' stroke-linecap='round' stroke-linejoin='round' stroke-width='1' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-position: right 0.9375rem center;
  background-repeat: no-repeat;
  background-size: 16px 12px;
  cursor: pointer;
}

.filters-container {
  border: 0.125rem solid #e4e4e4;
  padding: 1rem 1.25rem;
}

.search-field__input-wrapper {
  position: relative;
}

.search-field__input-wrapper::after {
  content: '';
  display: block;
  position: absolute;
  top: 50%;
  -webkit-transform: translateY(calc(-50% + 2px));
  transform: translateY(calc(-50% + 2px));
  right: 1rem;
  transform: translateY(-50%);
  width: 1rem;
  height: 1rem;
  background: transparent url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cg clip-path='url%28%23clip0_137_2221%29'%3e%3cpath d='M7.04606 0C3.16097 0 0 3.16097 0 7.04606C0 10.9314 3.16097 14.0921 7.04606 14.0921C10.9314 14.0921 14.0921 10.9314 14.0921 7.04606C14.0921 3.16097 10.9314 0 7.04606 0ZM7.04606 12.7913C3.87816 12.7913 1.30081 10.214 1.30081 7.04609C1.30081 3.87819 3.87816 1.30081 7.04606 1.30081C10.214 1.30081 12.7913 3.87816 12.7913 7.04606C12.7913 10.214 10.214 12.7913 7.04606 12.7913Z' fill='%23767676'/%3e%3cpath d='M15.8095 14.8897L12.0805 11.1607C11.8264 10.9066 11.4149 10.9066 11.1608 11.1607C10.9067 11.4146 10.9067 11.8265 11.1608 12.0804L14.8898 15.8094C15.0168 15.9364 15.1831 16 15.3496 16C15.5159 16 15.6824 15.9364 15.8095 15.8094C16.0636 15.5555 16.0636 15.1436 15.8095 14.8897Z' fill='%23767676'/%3e%3c/g%3e%3cdefs%3e%3cclipPath id='clip0_137_2221'%3e%3crect width='16' height='16' fill='white'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e") center/1rem auto no-repeat;
}

.search-field__input {
  width: 100%;
  outline: none;
}

.search-suggestion {
  margin: 0.375rem 0;
}

.search-suggestion__item {
  width: 100%;
  padding: 0.5rem 0;
  color: #767676;
  cursor: pointer;
}

.search-suggestion__item:hover {
  color: #3b3b3b;
}

.progress_uomo {
  height: 0.625rem;
  border-radius: 0.625rem;
  background-color: #e4e4e4;
  overflow: visible;
}

.progress_uomo_small {
  height: 0.25rem;
}

.progress_uomo_medium {
  height: 0.375rem;
}

.progress_uomo .progress-bar {
  position: relative;
  border-radius: 0.625rem;
  overflow: visible;
}

.progress_uomo .progress-bar::before {
  content: attr(aria-valuenow);
  display: block;
  position: absolute;
  top: -2em;
  right: 0;
  transform: translateX(50%);
  color: #222222;
  font-size: 0.875rem;
}

.categories-nav__title {
  margin: 0;
  padding-left: 1.8rem;
  padding-right: 1.8rem;
  border-radius: 4px 4px 0 0;
  background-color: #EBB73F;
  color: #ffffff;
  font-size: 0.875rem;
  line-height: 2em;
  text-transform: uppercase;
}

@media (min-width: 1500px) {
  .categories-nav__title {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.categories-nav__list {
  padding: 1.25rem 1.8rem;
  border: 1px solid #e4e4e4;
  border-top: 0;
  border-radius: 0 0 4px 4px;
}

@media (min-width: 1500px) {
  .categories-nav__list {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.categories-nav__item {
  padding: .6875rem 0;
  font-weight: 500;
  line-height: 2em;
  text-decoration: none;
}

.product-card {
  position: relative;
  overflow: hidden;
}

.product-card .hover-container::before {
  content: '';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: all 0.2s ease;
  background-color: rgba(234, 234, 234, 0.9);
  opacity: 0;
  visibility: hidden;
  z-index: 1;
}

.product-card:hover .pc__img-next,
.product-card:hover .pc__img-prev,
.product-card:hover .pc__img-second {
  opacity: 1;
}

.product-card:hover .hover-container::before {
  opacity: 1;
  visibility: visible;
}

.pc__img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.pc__img-wrapper {
  display: block;
  position: relative;
  height: 0;
  padding-top: 121.212122%;
  overflow: hidden;
}

.pc__img-wrapper .pc__btn-wl {
  top: 1rem;
  right: 1rem;
  width: 2rem;
  height: 2rem;
  padding: 0.625rem .5rem 0.375rem;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

.pc__img-wrapper .pc__btn-wl .flaticon-heart {
  line-height: 1;
}

@media (min-width: 768px) {
  .pc__img-wrapper .pc__btn-wl {
    top: 1.25rem;
    right: 1.25rem;
    width: 2.5rem;
    height: 2.5rem;
    padding: 0.8125rem 0.75rem 0.6875rem;
  }
}

.pc-wide__img-wrapper {
  padding-top: 60.606061%;
}

.pc__img-wrapper_wide2 {
  padding-top: 90.9091%;
}

.pc__img-wrapper_wide3 {
  padding-top: 78.43137%;
}

.pc__img-second {
  opacity: 0;
  transition: opacity 0.3s linear;
}

.pc__img-next,
.pc__img-prev {
  position: absolute;
  top: 50%;
  margin-top: -0.5rem;
  color: #767676;
  font-size: 1rem;
  opacity: 0;
  z-index: 1;
  transition: opacity 0.35s;
  width: 1rem;
  text-align: center;
}

.pc__img-next>svg,
.pc__img-prev>svg {
  height: auto;
  width: 0.625rem;
}

.pc__img-next {
  right: 1.25rem;
}

.pc__img-prev {
  left: 1.25rem;
}

.pc__info {
  margin-top: 1rem;
}

.pc__info.hover__content {
  margin-top: 0;
  min-width: auto;
  height: 100%;
  transform: translateY(1.125rem);
  -webkit-transform: translateY(1.125rem);
  background: transparent;
}

.pc__info.hover__content .pc__atc {
  max-width: 19.375rem;
}

.product-card:hover .pc__info.hover__content {
  transform: translateY(0);
  -webkit-transform: translateY(0);
}

.product-label {
  position: absolute;
  left: 0;
  top: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.3125rem;
  padding: 0.1875rem 0.625rem;
  line-height: 1.5rem;
  font-size: 0.875rem;
}

.pc__category {
  margin: 0;
  margin-bottom: .25rem;
  color: #767676;
  font-weight: 400;
  line-height: 1.7143;
}

.pc__title {
  margin: 0;
  font-size: 1rem;
  font-weight: 400;
}

.price {
  font-size: 1rem;
}

.price-sale {
  color: #d6001c;
}

.price-old {
  margin-right: .625rem;
  color: #767676;
  text-decoration: line-through;
}

.review-star {
  width: 9px;
  height: 9px;
  margin-right: .25rem;
  fill: #ffc78b;
}

.pc__btn-wl {
  color: #767676;
}

.js-add-wishlist.active {
  color: #193174 !important;
}

.js-add-wishlist.active.btn-hover-red {
  color: #fff !important;
  background-color: #193174 !important;
}

.js-add-wishlist.active.btn-hover-primary {
  color: #fff !important;
  background-color: #222222 !important;
}

.js-add-wishlist.active.theme-bg-color.text-white {
  color: #193174 !important;
  background-color: #fff !important;
}

.js-add-wishlist.active.bg-transparent.text-white {
  color: #193174 !important;
  background-color: #fff !important;
}

.js-add-wishlist.active.bg-black.text-white {
  color: #fff !important;
  background-color: #193174 !important;
}

.pc__btn-wl .flaticon,
.btn-link .flaticon {
  display: block;
  font-size: 1rem;
  line-height: 1.7143;
}

.pc__atc {
  left: 0.625rem;
  width: calc(100% - 1.25rem);
  padding-right: 0.625rem;
  padding-left: 0.625rem;
  white-space: nowrap;
}

.pc__atc:hover {
  filter: brightness(0.95);
}

@media (max-width: 767.98px) {
  .pc__atc {
    padding-top: .625rem;
    padding-bottom: .375rem;
    font-size: .75rem;
  }
}

.pc__swatch-color {
  display: block;
  position: relative;
  width: 1.25rem;
  height: 1.25rem;
  margin-right: .375rem;
  margin-bottom: .375rem;
  border-radius: 50%;
}

.pc__swatch-color:after {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
  border-radius: 100%;
  background-color: currentColor;
  color: inherit;
  content: '';
}

.pc__swatch-color.swatch_active {
  border: 2px solid #222222;
}

.pc-labels {
  padding: 0.625rem;
  z-index: 3;
}

.pc-label {
  padding: 0.25rem 0.625rem 0.125rem;
  font-size: .75rem;
}

@media (min-width: 768px) {
  .pc-label {
    font-size: 0.875rem;
  }
}

.pc-label_sale {
  background-color: #d6001c;
}

.pc-label_sale-text {
  background-color: #222222;
  color: #fff;
}

.product-card_style3 .pc__img-wrapper {
  border-radius: 0.625rem;
}

.product-card_style6 {
  transition: all 0.2s ease;
  overflow: initial;
}

.product-card_style6 .pc__info {
  margin: 0;
  padding: 0.875rem 1.125rem;
  transition: all 0.2s ease;
  z-index: 1;
}

.product-card_style6 .hover__content {
  min-width: auto;
  box-shadow: none;
}

@media (max-width: 575.98px) {
  .product-card_style6 .hover__content {
    position: relative;
    opacity: 1;
    visibility: visible;
  }
}

.product-card_style6:hover,
.product-card_style6:active {
  box-shadow: 0 8px 15px 0 rgba(140, 152, 164, 0.1);
}

.product-card_style6:hover .pc__info,
.product-card_style6:active .pc__info {
  margin-top: -2.5rem;
}

.product-card_style6:hover .pc__info:after,
.product-card_style6:active .pc__info:after {
  content: '';
  position: absolute;
  bottom: -2.5rem;
  left: 0;
  width: 100%;
  height: 2.5rem;
  z-index: 1;
}

.product-card_style8 {
  border: 1px solid transparent;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.product-card_style8.border-1 {
  border-color: #eee;
}

.product-card_style8 .pc__info {
  margin: 0.875rem .5rem .625rem;
}

@media (min-width: 768px) {
  .product-card_style8 .pc__info {
    margin: 0.875rem 1.25rem 1.5rem;
  }
}

.product-card_style8 .pc__title {
  font-size: 0.9375rem;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
  overflow: hidden;
  line-height: 1.5;
}

.product-card_style8 .reviews-note {
  font-size: 0.8125rem;
}

.product-card_style8 .product-card__price {
  margin-top: 0.625rem;
  color: #0046be;
}

.product-card_style8:hover {
  border-color: #0046be;
  box-shadow: 0 0 20px 0 rgba(0, 70, 190, 0.1);
}

.product-card_style8 .js-add-wishlist,
.product-card_style8 .js-add-cart,
.product-card_style8 .js-quick-view {
  color: #0046be;
}

.product-card_style9 {
  transition: all 0.2s ease;
  border: 1px solid transparent;
  border-radius: 0.25rem;
}

.product-card_style9 .pc__info {
  margin: 0.875rem .5rem .625rem;
}

@media (min-width: 768px) {
  .product-card_style9 .pc__info {
    margin: 0.875rem 1.25rem 0.8125rem;
  }
}

.product-card_style9 .pc__title {
  font-size: 0.9375rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-card_style9 .reviews-note {
  font-size: 0.8125rem;
}

.product-card_style9 .product-card__price {
  margin-top: 0.625rem;
  color: #86bc42;
}

.product-card_style9:hover {
  box-shadow: 0 0 30px 0 rgba(0, 0, 0, 0.1);
}

.product-card_style9:hover .anim_appear-bottom {
  bottom: 0;
}

.product-card_style9 .js-add-wishlist,
.product-card_style9 .js-add-cart,
.product-card_style9 .js-quick-view {
  background-color: #f3e8d6;
  color: #074e37;
}

.product-card_style9 .js-add-wishlist:hover,
.product-card_style9 .js-add-cart:hover,
.product-card_style9 .js-quick-view:hover {
  background-color: #86bc42;
  color: #fff;
}

.product-card_style9.type2 {
  border: 0;
  border-radius: 0;
}

.product-card_style9.type2 .pc__title {
  font-size: 1rem;
  white-space: initial;
  overflow: initial;
  text-overflow: initial;
  line-height: 1.5;
}

.product-card_style9.type2 .pc__title a {
  color: #193174;
}

.product-card_style9.type2:hover {
  box-shadow: none;
}

.product-card_style9.type2 .js-add-wishlist,
.product-card_style9.type2 .js-add-cart,
.product-card_style9.type2 .js-quick-view {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #E4F5F2;
  color: #193174;
}

.product-card_style9.type2 .js-add-wishlist:hover,
.product-card_style9.type2 .js-add-cart:hover,
.product-card_style9.type2 .js-quick-view:hover {
  background-color: #193174;
  color: #fff;
}

.product-card_style9.type2 .product-card__price {
  color: #193174;
  font-size: 1rem;
}

.product-card_style10 {
  transition: background-color .3s ease;
}

.product-card_style10:hover {
  background-color: #F7F7F7;
}

.product-card__actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: #fff;
  white-space: nowrap;
}

.product-card__actions>* {
  display: none;
}

@media (min-width: 1200px) {
  .product-card__actions>* {
    display: block;
  }
}

.product-card__actions>*:first-child {
  display: block;
}

.product-card:hover .anim_appear-bottom.product-card__actions {
  bottom: 0;
}

.aside {
  position: fixed;
  top: 0;
  width: 26.25rem;
  max-width: 100%;
  height: 100vh;
  height: -webkit-fill-available;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
  background-color: #ffffff;
  opacity: .7;
  z-index: 1050;
}

@media (min-width: 576px) {
  .aside {
    padding: 0 1.25rem;
  }
}

.aside_visible {
  opacity: 1;
}

.aside_left {
  left: -26.25rem;
}

.aside_left.aside_visible {
  left: 0;
}

.aside_right {
  right: -26.25rem;
}

.aside_right.aside_visible {
  right: 0;
}

.aside-header {
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  padding: 2.125rem 2.5rem 1.75rem;
  background-color: #faf9f8;
}

.aside-content {
  margin: 1.875rem 0;
  padding: 0 1.25rem;
}

.customer-forms__wrapper {
  left: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.customer__login,
.customer__register {
  min-width: 100%;
}

.search-field__actor svg {
  transition: opacity 0.15s linear;
}

@media (prefers-reduced-motion: reduce) {
  .search-field__actor svg {
    transition: none;
  }
}

.search-field__actor .btn-close-lg {
  position: absolute;
  top: 3px;
  left: 3px;
  padding: 0;
  transition: opacity 0.15s linear;
  opacity: 0;
  visibility: hidden;
}

@media (prefers-reduced-motion: reduce) {
  .search-field__actor .btn-close-lg {
    transition: none;
  }
}

.js-content_visible .search-field__actor svg {
  opacity: 0;
  visibility: hidden;
}

.js-content_visible .search-field__actor .btn-close-lg {
  opacity: 1;
  visibility: visible;
}

.search-popup {
  top: 100%;
  left: 0;
  padding-top: 2.625rem;
  padding-bottom: 2.45rem;
  border-top: 1px solid #e4e4e4;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
}

@media (min-width: 1200px) {
  .search-popup {
    padding-top: 3.75rem;
    padding-bottom: 3.5rem;
  }
}

.search-popup .search-suggestion {
  transition: all 0.28s;
}

.search-popup__reset,
.search-popup__submit {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  position: absolute;
  right: 0;
  bottom: 0;
  height: 100%;
  padding: 0;
  padding-bottom: 0.625rem;
  transition: opacity 0.15s linear;
  color: #767676;
  outline: none;
}

@media (prefers-reduced-motion: reduce) {

  .search-popup__reset,
  .search-popup__submit {
    transition: none;
  }
}

.search-popup__reset {
  opacity: 0;
  visibility: hidden;
}

.search-popup__input {
  padding-bottom: 0.625rem;
  border: 0;
  border-bottom: 2px solid #767676;
  outline: none;
}

.search-field__focused .search-popup__input {
  border-bottom-color: #222222;
}

.search-field__focused .search-popup__reset,
.search-field__focused .search-popup__submit {
  color: #222222;
}

.search-field__focused .search-popup__submit {
  opacity: 0;
  visibility: hidden;
}

.search-field__focused .search-popup__reset {
  opacity: 1;
  visibility: visible;
}

.search-field__focused .search-result {
  position: relative;
  width: auto;
  margin-top: 0;
  transition: all 0.28s;
  opacity: 1;
  visibility: visible;
}

.search-field__focused .search-suggestion {
  position: absolute;
  margin-top: -.5rem;
  opacity: 0;
  visibility: hidden;
}

.search-popup__results {
  margin-top: 1.75rem;
}

.search-result {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  min-height: 14.25rem;
  margin-top: .5rem;
  padding-bottom: 1.2rem;
  opacity: 0;
  visibility: hidden;
}

.search-result .product-card {
  --bs-gutter-x: 1.75rem;
}

.search-result .pc__img-wrapper {
  padding-top: 10.125rem;
}

@media (min-width: 1200px) {
  .search-result {
    min-height: 19rem;
    padding-bottom: 1.6rem;
  }

  .search-result .pc__img-wrapper {
    padding-top: 15rem;
  }
}

@media (min-width: 1500px) {
  .search-result {
    min-height: 23.75rem;
    padding-bottom: 2rem;
  }

  .search-result .pc__img-wrapper {
    padding-top: 18.75rem;
  }
}

.cart-drawer {
  padding-bottom: 22.5rem;
}

.cart-drawer-items-list {
  max-height: 27.675rem;
  overflow-y: auto;
  height: 100%;
}

.cart-drawer-item {
  max-height: 7.5rem;
  overflow: hidden;
}

.cart-drawer-item._removed {
  max-height: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.cart-drawer-item__img {
  width: 7.5rem;
  height: 7.5rem;
  object-fit: cover;
}

.cart-drawer-item__info {
  margin-left: 1.25rem;
}

.cart-drawer-item__title {
  margin: 2px 0 4px;
}

.cart-drawer-item__option {
  margin: 0;
}

.cart-drawer-item__price {
  font-size: 1.125rem;
}

.qty-control {
  width: 3.375rem;
}

.qty-control input::-webkit-outer-spin-button,
.qty-control input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}

.qty-control__number {
  padding: 0;
  width: 100%;
  background-color: #ffffff;
  outline: none;
  -moz-appearance: textfield;
}

.qty-control__reduce,
.qty-control__increase {
  position: absolute;
  top: 0;
  width: .75rem;
  padding: 0;
  cursor: pointer;
  user-select: none;
  -ms-user-select: none;
}

.qty-control__reduce {
  left: 0;
}

.qty-control__increase {
  right: 0;
}

.cart-drawer-divider {
  margin: 1.25rem 0;
  color: #e4e4e4;
  opacity: 1;
}

.cart-drawer-divider._removed {
  height: 0;
  margin: 0;
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.cart-drawer-actions {
  background-color: #ffffff;
  padding-right: 1.25rem;
  padding-bottom: 1.25rem;
  padding-left: 1.25rem;
}

@media (min-width: 576px) {
  .cart-drawer-actions {
    padding-right: 2.5rem;
    padding-bottom: 2.5rem;
    padding-left: 2.5rem;
  }
}

.star-rating__star-icon {
  cursor: pointer;
  transition: all .1s ease;
  fill: #ccc;
}

.star-rating__star-icon path {
  pointer-events: none;
}

.star-rating__star-icon.is-selected {
  fill: #eeba36;
}

.star-rating__star-icon.is-overed {
  fill: #eeba36;
}

.star-rating__star-icon.is-overed~.star-rating__star-icon:not(.is-overed):not(.is-selected) {
  fill: #ccc;
}

.star-rating__star-icon.is-overed~.star-rating__star-icon.is-selected:not(.is-overed) {
  fill: #ffe296;
}

.size-guide.modal-dialog {
  width: 60rem;
  max-width: calc(100% - 1rem);
}

.size-guide .modal-header {
  background-color: #FAF9F8;
  border-bottom: 0;
  padding: 1.75rem 2.5rem;
  text-transform: uppercase;
}

.size-guide .modal-header .modal-title {
  font-size: 1rem;
}

.size-guide .modal-body {
  padding: 2.5rem;
}

.size-guide__wrapper {
  display: flex;
  gap: 2.6875rem;
}

@media (max-width: 767.98px) {
  .size-guide__wrapper {
    flex-direction: column;
  }
}

.size-guide__image {
  flex: 0 0 42%;
  max-width: 42%;
}

@media (max-width: 767.98px) {
  .size-guide__image {
    flex: 0 0 100%;
    max-width: 100%;
  }
}

.size-guide__detail {
  flex: 1;
}

.size-guide__detail>h5,
.size-guide__detail>.h5 {
  margin-bottom: 1.875rem;
}

.size-guide__detail table {
  font-size: 0.875rem;
  margin-bottom: 1.875rem;
  width: 100%;
}

.size-guide__detail table thead th {
  color: #767676;
  padding-bottom: 0.8125rem;
}

.size-guide__detail table tbody td {
  line-height: 2.1875rem;
}

.delivery-modal.modal-dialog {
  width: 37.5rem;
  max-width: calc(100% - 1rem);
}

.delivery-modal .modal-header {
  background-color: #FAF9F8;
  border-bottom: 0;
  padding: 1.75rem 2.5rem;
  text-transform: uppercase;
}

.delivery-modal .modal-header .modal-title {
  font-size: 1rem;
}

.delivery-modal .modal-body {
  padding: 2.5rem;
}

.delivery-modal .modal-body p {
  line-height: 1.875rem;
  margin-right: 3.875rem;
  margin-bottom: 1.875rem;
}

.cookieConsentContainer {
  position: fixed;
  right: 1.25rem;
  bottom: 1.25rem;
  width: 18.75rem;
  max-width: calc(100% - 2.5rem);
  background-color: #222;
  color: #fff;
  padding: 1.875rem;
  z-index: 1050;
}

.cookieConsentContainer .cookieButton a {
  background-color: #5c5c5c;
  color: #fff;
  height: 2.5rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.cookieConsentContainer .cookieDesc p {
  font-size: 0.8125rem;
}

@-webkit-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-moz-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-ms-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-o-keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@keyframes bounceIn {

  from,
  20%,
  40%,
  60%,
  80%,
  to {
    -webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -moz-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -ms-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    -o-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    -webkit-transform: scale3d(0.3, 0.3, 0.3);
    -moz-transform: scale3d(0.3, 0.3, 0.3);
    -ms-transform: scale3d(0.3, 0.3, 0.3);
    -o-transform: scale3d(0.3, 0.3, 0.3);
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    -webkit-transform: scale3d(1.1, 1.1, 1.1);
    -moz-transform: scale3d(1.1, 1.1, 1.1);
    -ms-transform: scale3d(1.1, 1.1, 1.1);
    -o-transform: scale3d(1.1, 1.1, 1.1);
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    -webkit-transform: scale3d(0.9, 0.9, 0.9);
    -moz-transform: scale3d(0.9, 0.9, 0.9);
    -ms-transform: scale3d(0.9, 0.9, 0.9);
    -o-transform: scale3d(0.9, 0.9, 0.9);
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    -webkit-transform: scale3d(1.03, 1.03, 1.03);
    -moz-transform: scale3d(1.03, 1.03, 1.03);
    -ms-transform: scale3d(1.03, 1.03, 1.03);
    -o-transform: scale3d(1.03, 1.03, 1.03);
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    -webkit-transform: scale3d(0.97, 0.97, 0.97);
    -moz-transform: scale3d(0.97, 0.97, 0.97);
    -ms-transform: scale3d(0.97, 0.97, 0.97);
    -o-transform: scale3d(0.97, 0.97, 0.97);
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    -webkit-transform: scale3d(1, 1, 1);
    -moz-transform: scale3d(1, 1, 1);
    -ms-transform: scale3d(1, 1, 1);
    -o-transform: scale3d(1, 1, 1);
    transform: scale3d(1, 1, 1);
  }
}

@-webkit-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-moz-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-ms-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-o-keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes spin {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@-webkit-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-moz-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-ms-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-o-keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@keyframes marquee {
  0% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }
}

@-webkit-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-moz-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-ms-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-o-keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@keyframes marquee-right {
  0% {
    -webkit-transform: translateX(-100%) translateZ(0);
    -moz-transform: translateX(-100%) translateZ(0);
    -ms-transform: translateX(-100%) translateZ(0);
    -o-transform: translateX(-100%) translateZ(0);
    transform: translateX(-100%) translateZ(0);
  }

  100% {
    -webkit-transform: translateX(0) translateZ(0);
    -moz-transform: translateX(0) translateZ(0);
    -ms-transform: translateX(0) translateZ(0);
    -o-transform: translateX(0) translateZ(0);
    transform: translateX(0) translateZ(0);
  }
}

@-webkit-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-moz-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-ms-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-o-keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@keyframes mouseoverLineContainer {
  0% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }

  20% {
    -webkit-transform: translateX(100%);
    -moz-transform: translateX(100%);
    -ms-transform: translateX(100%);
    -o-transform: translateX(100%);
    transform: translateX(100%);
  }

  21% {
    -webkit-transform: translateX(-110%);
    -moz-transform: translateX(-110%);
    -ms-transform: translateX(-110%);
    -o-transform: translateX(-110%);
    transform: translateX(-110%);
  }

  100% {
    -webkit-transform: translateX(0%);
    -moz-transform: translateX(0%);
    -ms-transform: translateX(0%);
    -o-transform: translateX(0%);
    transform: translateX(0%);
  }
}

@-webkit-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-moz-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-ms-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-o-keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@keyframes snt_shake {

  from,
  to {
    -webkit-transform: translate3d(0, 0, 0);
    -moz-transform: translate3d(0, 0, 0);
    -ms-transform: translate3d(0, 0, 0);
    -o-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
  }

  17%,
  50%,
  83% {
    -webkit-transform: translate3d(-5px, 0, 0);
    -moz-transform: translate3d(-5px, 0, 0);
    -ms-transform: translate3d(-5px, 0, 0);
    -o-transform: translate3d(-5px, 0, 0);
    transform: translate3d(-5px, 0, 0);
  }

  33%,
  67% {
    -webkit-transform: translate3d(5px, 0, 0);
    -moz-transform: translate3d(5px, 0, 0);
    -ms-transform: translate3d(5px, 0, 0);
    -o-transform: translate3d(5px, 0, 0);
    transform: translate3d(5px, 0, 0);
  }
}

@-webkit-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-moz-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-ms-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-o-keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@keyframes snt_pulse {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(2);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-webkit-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-moz-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-ms-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@-o-keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

@keyframes snt_pulse_no_scale {
  0% {
    transform: scale(1);
  }

  50% {
    transform: scale(1);
  }

  100% {
    transform: scale(1);
    opacity: 0;
  }
}

.effect {
  position: relative;
}

.effect:before,
.effect:after {
  pointer-events: none;
}

.normal-effect::before {
  position: absolute;
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  .normal-effect::before {
    transition: none;
  }
}

.normal-effect:hover::before {
  opacity: .3;
}

.normal-effect.dark-bg::before {
  background-color: #000;
}

.plus-zoom::before,
.plus-zoom::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  margin: auto;
  width: 100%;
  height: 100%;
  transition: all 0.5s ease;
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {

  .plus-zoom::before,
  .plus-zoom::after {
    transition: none;
  }
}

.plus-zoom:hover::before {
  width: 0;
  background-color: rgba(255, 255, 255, 0.5);
}

.plus-zoom:hover::after {
  height: 0;
  background-color: rgba(255, 255, 255, 0.5);
}

.overlay-plus::before,
.overlay-plus::after,
.overlay-cross::before,
.overlay-cross::after,
.overlay-horizontal::before,
.overlay-horizontal::after,
.overlay-vertical::before,
.overlay-vertical::after {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.15);
}

@media (prefers-reduced-motion: reduce) {

  .overlay-plus::before,
  .overlay-plus::after,
  .overlay-cross::before,
  .overlay-cross::after,
  .overlay-horizontal::before,
  .overlay-horizontal::after,
  .overlay-vertical::before,
  .overlay-vertical::after {
    transition: none;
  }
}

.overlay-plus.overlay-dark::before,
.overlay-plus.overlay-dark::after,
.overlay-cross.overlay-dark::before,
.overlay-cross.overlay-dark::after,
.overlay-horizontal.overlay-dark::before,
.overlay-horizontal.overlay-dark::after,
.overlay-vertical.overlay-dark::before,
.overlay-vertical.overlay-dark::after {
  background-color: rgba(0, 0, 0, 0.15);
}

.overlay-plus::before,
.overlay-plus::after {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.overlay-plus:not(:hover)::before {
  width: 0;
}

.overlay-plus:not(:hover)::after {
  height: 0;
}

.overlay-cross::before {
  top: 0;
  left: 0;
}

.overlay-cross::after {
  bottom: 0;
  right: 0;
}

.overlay-cross:not(:hover)::before,
.overlay-cross:not(:hover)::after {
  width: 0;
  height: 0;
}

.overlay-horizontal::before {
  top: 0;
  left: 0;
  bottom: 0;
}

.overlay-horizontal::after {
  top: 0;
  right: 0;
  bottom: 0;
}

.overlay-horizontal:not(:hover)::before,
.overlay-horizontal:not(:hover)::after {
  width: 0;
}

.overlay-vertical::before {
  top: 0;
  left: 0;
  right: 0;
}

.overlay-vertical::after {
  left: 0;
  right: 0;
  bottom: 0;
}

.overlay-vertical:not(:hover)::before,
.overlay-vertical:not(:hover)::after {
  height: 0;
}

.overlay-fade::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.3);
}

@media (prefers-reduced-motion: reduce) {
  .overlay-fade::before {
    transition: none;
  }
}

.overlay-fade.overlay-dark::before {
  background-color: rgba(0, 0, 0, 0.3);
}

.overlay-fade:not(:hover)::before {
  opacity: 0;
  visibility: hidden;
}

.overlay-scale-left-top::before,
.overlay-scale-right-top::before,
.overlay-scale-left-bottom::before,
.overlay-scale-right-bottom::before,
.overlay-scale-left::before,
.overlay-scale-right::before,
.overlay-scale-top::before,
.overlay-scale-bottom::before,
.overlay-scale-center::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  margin: auto;
  transition: all 0.5s ease;
  z-index: 2;
  background-color: rgba(255, 255, 255, 0.3);
}

@media (prefers-reduced-motion: reduce) {

  .overlay-scale-left-top::before,
  .overlay-scale-right-top::before,
  .overlay-scale-left-bottom::before,
  .overlay-scale-right-bottom::before,
  .overlay-scale-left::before,
  .overlay-scale-right::before,
  .overlay-scale-top::before,
  .overlay-scale-bottom::before,
  .overlay-scale-center::before {
    transition: none;
  }
}

.overlay-scale-left-top.overlay-dark::before,
.overlay-scale-right-top.overlay-dark::before,
.overlay-scale-left-bottom.overlay-dark::before,
.overlay-scale-right-bottom.overlay-dark::before,
.overlay-scale-left.overlay-dark::before,
.overlay-scale-right.overlay-dark::before,
.overlay-scale-top.overlay-dark::before,
.overlay-scale-bottom.overlay-dark::before,
.overlay-scale-center.overlay-dark::before {
  background-color: rgba(0, 0, 0, 0.3);
}

.overlay-scale-left-top::before {
  top: 0;
  left: 0;
}

.overlay-scale-left-top:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-right-top::before {
  top: 0;
  right: 0;
}

.overlay-scale-right-top:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-left-bottom::before {
  bottom: 0;
  left: 0;
}

.overlay-scale-left-bottom:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-right-bottom::before {
  bottom: 0;
  right: 0;
}

.overlay-scale-right-bottom:not(:hover)::before {
  width: 0;
  height: 0;
}

.overlay-scale-center::before {
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: auto;
  height: auto;
}

.overlay-scale-center:not(:hover)::before {
  top: 50%;
  left: 50%;
  right: 50%;
  bottom: 50%;
}

.overlay-scale-left::before {
  top: 0;
  left: 0;
  bottom: 0;
}

.overlay-scale-left:not(:hover)::before {
  width: 0;
}

.overlay-scale-right::before {
  top: 0;
  right: 0;
  bottom: 0;
}

.overlay-scale-right:not(:hover)::before {
  width: 0;
}

.overlay-scale-top::before {
  top: 0;
  left: 0;
  right: 0;
}

.overlay-scale-top:not(:hover)::before {
  height: 0;
}

.overlay-scale-bottom::before {
  bottom: 0;
  left: 0;
  right: 0;
}

.overlay-scale-bottom:not(:hover)::before {
  height: 0;
}

.border-zoom {
  overflow: hidden;
}

.border-zoom::before,
.border-zoom::after {
  position: absolute;
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  transition: all 0.5s ease;
  z-index: 2;
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {

  .border-zoom::before,
  .border-zoom::after {
    transition: none;
  }
}

.border-zoom::before {
  background-color: #000;
}

.border-zoom::after {
  top: -15px;
  bottom: -15px;
  left: -15px;
  right: -15px;
  border: 2px solid #fff;
}

.border-zoom:hover::before {
  opacity: .3;
}

.border-zoom:hover::after {
  top: 15px;
  bottom: 15px;
  left: 15px;
  right: 15px;
  opacity: 1;
}

.border-plus,
.border-scale {
  background-color: #000;
}

.border-plus .image-effect,
.border-plus img,
.border-scale .image-effect,
.border-scale img {
  transition: all 0.3s ease;
}

@media (prefers-reduced-motion: reduce) {

  .border-plus .image-effect,
  .border-plus img,
  .border-scale .image-effect,
  .border-scale img {
    transition: none;
  }
}

.border-plus:hover .image-effect,
.border-plus:hover img,
.border-scale:hover .image-effect,
.border-scale:hover img {
  opacity: .7;
}

.border-plus::before,
.border-plus::after,
.border-scale::before,
.border-scale::after {
  content: '';
  position: absolute;
  z-index: 2;
  border: solid #fff;
  top: 15px;
  bottom: 15px;
  left: 15px;
  right: 15px;
  margin: auto;
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .border-plus::before,
  .border-plus::after,
  .border-scale::before,
  .border-scale::after {
    transition: none;
  }
}

.border-plus::before,
.border-scale::before {
  border-width: 2px 0;
}

.border-plus::after,
.border-scale::after {
  border-width: 0 2px;
}

.border-plus.s2::before,
.border-scale.s2::before {
  top: 30px;
  bottom: 30px;
}

.border-plus.s2::after,
.border-scale.s2::after {
  left: 30px;
  right: 30px;
}

.border-scale:not(:hover)::before {
  left: 50%;
  right: 50%;
}

.border-scale:not(:hover)::after {
  top: 50%;
  bottom: 50%;
}

.border-plus:not(:hover)::before {
  top: 30%;
  bottom: 30%;
  opacity: 0;
}

.border-plus:not(:hover)::after {
  left: 30%;
  right: 30%;
  opacity: 0;
}

.flashlight::before,
.flashlight::after {
  content: '';
  position: absolute;
  top: 0;
  bottom: 0;
  background-color: #000;
  z-index: 2;
}

.flashlight::before {
  left: 0;
  width: 100%;
}

.flashlight::after {
  right: 0;
  width: 0;
  opacity: .5;
}

.flashlight:hover::before {
  width: 0;
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {
  .flashlight:hover::before {
    transition: none;
  }
}

.flashlight:hover::after {
  width: 100%;
  transition: all 0.8s ease;
}

@media (prefers-reduced-motion: reduce) {
  .flashlight:hover::after {
    transition: none;
  }
}

.bounce-in:hover .image-effect,
.bounce-in:hover img {
  -webkit-animation: bounceIn 0.5s ease;
  -moz-animation: bounceIn 0.5s ease;
  -ms-animation: bounceIn 0.5s ease;
  -o-animation: bounceIn 0.5s ease;
  animation: bounceIn 0.5s ease;
}

.faded-in .image-effect,
.faded-in img {
  transition: opacity 0.2s ease;
}

@media (prefers-reduced-motion: reduce) {

  .faded-in .image-effect,
  .faded-in img {
    transition: none;
  }
}

.faded-in:not(:hover) .image-effect,
.faded-in:not(:hover) img {
  opacity: 0.3;
}

.background-zoom {
  overflow: hidden;
}

.background-zoom .image-effect,
.background-zoom img {
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-zoom .image-effect,
  .background-zoom img {
    transition: none;
  }
}

.background-zoom.slow .image-effect,
.background-zoom.slow img {
  transition: all 10s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-zoom.slow .image-effect,
  .background-zoom.slow img {
    transition: none;
  }
}

.background-zoom:hover .image-effect,
.background-zoom:hover img {
  -webkit-transform: scale(1.1);
  -moz-transform: scale(1.1);
  -ms-transform: scale(1.1);
  -o-transform: scale(1.1);
  transform: scale(1.1);
}

.background-slide {
  overflow: hidden;
}

.background-slide .image-effect,
.background-slide img {
  position: relative;
  width: calc(100% + 60px);
  max-width: calc(100% + 60px);
  left: 50%;
  -webkit-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -o-transform: translateX(-50%);
  transform: translateX(-50%);
  transition: all 0.4s ease;
}

@media (prefers-reduced-motion: reduce) {

  .background-slide .image-effect,
  .background-slide img {
    transition: none;
  }
}

.background-slide:hover .image-effect,
.background-slide:hover img {
  margin-left: 30px;
}

.grayscale {
  overflow: hidden;
}

.grayscale .image-effect,
.grayscale img {
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
  transition: all 0.5s ease;
}

@media (prefers-reduced-motion: reduce) {

  .grayscale .image-effect,
  .grayscale img {
    transition: none;
  }
}

.grayscale.slow .image-effect,
.grayscale.slow img {
  transition: all 10s ease;
}

@media (prefers-reduced-motion: reduce) {

  .grayscale.slow .image-effect,
  .grayscale.slow img {
    transition: none;
  }
}

.grayscale:hover .image-effect,
.grayscale:hover img {
  -webkit-filter: grayscale(0);
  -moz-filter: grayscale(0);
  -ms-filter: grayscale(0);
  -o-filter: grayscale(0);
  filter: grayscale(0);
}

.grayscale.revert .image-effect,
.grayscale.revert img {
  -webkit-filter: grayscale(0);
  -moz-filter: grayscale(0);
  -ms-filter: grayscale(0);
  -o-filter: grayscale(0);
  filter: grayscale(0);
}

.grayscale.revert:hover .image-effect,
.grayscale.revert:hover img {
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
}

.rotate-left,
.rotate-right {
  overflow: hidden;
}

.rotate-left .image-effect,
.rotate-left img,
.rotate-right .image-effect,
.rotate-right img {
  transition: all 0.7s ease;
}

@media (prefers-reduced-motion: reduce) {

  .rotate-left .image-effect,
  .rotate-left img,
  .rotate-right .image-effect,
  .rotate-right img {
    transition: none;
  }
}

.rotate-left:hover .image-effect,
.rotate-left:hover img {
  -webkit-transform: scale(1.2) rotate(-5deg);
  -moz-transform: scale(1.2) rotate(-5deg);
  -ms-transform: scale(1.2) rotate(-5deg);
  -o-transform: scale(1.2) rotate(-5deg);
  transform: scale(1.2) rotate(-5deg);
}

.rotate-right:hover .image-effect,
.rotate-right:hover img {
  -webkit-transform: scale(1.2) rotate(5deg);
  -moz-transform: scale(1.2) rotate(5deg);
  -ms-transform: scale(1.2) rotate(5deg);
  -o-transform: scale(1.2) rotate(5deg);
  transform: scale(1.2) rotate(5deg);
}

.navigation__list {
  margin-bottom: 0;
}

@media (min-width: 992px) {
  .navigation__item {
    margin: 0 5px;
  }

  .navigation__item:hover::before {
    display: block;
    position: absolute;
    top: 0;
    width: 7.5rem;
    height: 100%;
    background-color: transparent;
    content: '';
  }
}

.navigation__link {
  display: inline-block;
  position: relative;
  padding-top: 2px;
  padding-bottom: 2px;
  color: #222222;
  font-weight: 500;
  line-height: 1.5rem;
  text-decoration: none;
  text-transform: uppercase;
}

.navigation__link:after {
  content: '';
  display: block;
  position: absolute;
  top: 100%;
  left: 0.7rem;
  width: 0;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.navigation__link:hover:after {
  width: 2em;
}

@media (min-width: 992px) {
  .navigation__link {
    padding-right: 0.7rem;
    padding-left: 0.7rem;
  }
}

@media (min-width: 1200px) {
  .navigation__link {
    padding-right: 1rem;
    padding-left: 1rem;
  }

  .navigation__link:after {
    left: 1rem;
  }
}

.sub-menu__title {
  display: block;
  margin-bottom: .75rem;
  color: #767676;
  font-weight: 500;
  text-transform: uppercase;
}

.menu-link {
  display: inline-block;
  position: relative;
  padding: 0.5em 0;
  color: #222222;
  line-height: 1.5em;
}

.menu-link_us-s:after {
  content: '';
  display: block;
  position: absolute;
  top: 2em;
  left: 0;
  width: 0;
  height: 2px;
  transition: width 0.28s cubic-bezier(0.47, 0, 0.745, 0.715);
  background-color: currentColor;
}

.menu-link_us-s:hover:after,
.menu-link_us-s.menu-link_active:after {
  width: 2em;
}

.default-menu {
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 16.25rem;
  padding: 1.5rem 1.875rem 1rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .default-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.box-menu {
  display: flex;
  display: -ms-flexbox;
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 49.6875rem;
  padding: 2.5rem 3.75rem 2rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .box-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.mega-menu {
  border-top: 1px solid #e4e4e4;
  position: absolute;
  top: calc(100% + .75rem);
  left: 0;
  width: 100%;
  padding: 2.5rem 0 2.75rem;
  background-color: #ffffff;
  box-shadow: 0 0.625rem 1.5625rem 0 rgba(34, 34, 34, 0.05);
  z-index: 1000;
  transition: all 0.28s;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
}

.navigation__item:hover .mega-menu {
  top: 100%;
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.sub-menu__list+.sub-menu__title {
  margin-top: 1.875rem;
}

.mega-menu__media {
  flex: 2 0 0;
  max-width: 25.625rem;
}

.mega-menu__img {
  max-width: 100%;
}

.sitemap {
  height: 100vh;
  background-color: #ffffff;
  z-index: 1030;
}

.sitemap__bg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.sitemap__links .modal-header {
  background: #faf9f8;
  border: 0;
}

.sitemap__links .modal-body ::-webkit-scrollbar {
  margin-right: 1.25rem;
  width: .25rem;
  background-color: #ffffff;
}

.sitemap__links .modal-body ::-webkit-scrollbar-thumb {
  border-radius: .25rem;
  background-color: #e4e4e4;
}

.sitemap__links .nav {
  padding-left: calc(var(--bs-gutter-x) / 2);
}

.sitemap__links .nav-link_rline {
  padding-left: 0;
  font-size: 1.25rem;
  line-height: 1.5em;
}

.header {
  display: none;
  position: relative;
  background-color: #ffffff;
  z-index: 2;
}

.header .form-select {
  border: 0;
  box-shadow: none;
  height: 2.5rem;
  padding: 0.375rem 2.025rem 0.3rem 1.125rem;
  background-image: url('data:image/svg+xml,%3csvg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"%3e%3cg clip-path="url%28%23clip0_34_1038%29"%3e%3cpath d="M5.57201 9.11914C5.8052 9.35233 6.1948 9.35233 6.42858 9.11914L11.8229 3.73866C12.059 3.50248 12.059 3.11947 11.8229 2.88389C11.5867 2.64771 11.2031 2.64771 10.9669 2.88389L6.00002 7.83695L1.03375 2.88329C0.796978 2.64711 0.413959 2.64711 0.177183 2.88329C-0.0589957 3.11947 -0.0589957 3.50248 0.177183 3.73806L5.57201 9.11914Z" fill="%23222222"/%3e%3c/g%3e%3cdefs%3e%3cclipPath id="clip0_34_1038"%3e%3crect width="12" height="12" fill="white" transform="translate%2812 12%29 rotate%28-180%29"/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e');
}

.header .form-select.color-white {
  background-image: url('data:image/svg+xml,%3csvg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"%3e%3cg clip-path="url%28%23clip0_34_1038%29"%3e%3cpath d="M5.57201 9.11914C5.8052 9.35233 6.1948 9.35233 6.42858 9.11914L11.8229 3.73866C12.059 3.50248 12.059 3.11947 11.8229 2.88389C11.5867 2.64771 11.2031 2.64771 10.9669 2.88389L6.00002 7.83695L1.03375 2.88329C0.796978 2.64711 0.413959 2.64711 0.177183 2.88329C-0.0589957 3.11947 -0.0589957 3.50248 0.177183 3.73806L5.57201 9.11914Z" fill="white"/%3e%3c/g%3e%3cdefs%3e%3cclipPath id="clip0_34_1038"%3e%3crect width="12" height="12" fill="white" transform="translate%2812 12%29 rotate%28-180%29"/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e');
}

.header .form-select option {
  color: #222222;
}

@media (min-width: 992px) {
  .header {
    display: block;
  }
}

.header.header-transparent-bg:not(.header_sticky-active) {
  background: transparent;
}

.header.header_dark {
  background-color: #222222;
}

.header.header_dark .navigation__link {
  color: #fff;
}

.header.header_dark .header-tools__item {
  color: #fff;
}

.header-desk {
  display: flex;
  align-items: center;
}

.header-fullwidth {
  padding: 0 1.75rem;
  width: 100%;
}

@media (min-width: 1500px) {
  .header-fullwidth {
    padding: 0 3.75rem;
  }
}

.header-fullwidth .header-top {
  margin: 0 -1.75rem;
  padding: 0 1.75rem;
}

@media (min-width: 1500px) {
  .header-fullwidth .header-top {
    margin: 0 -3.75rem;
    padding: 0 3.75rem;
  }
}

.logo__image {
  max-width: 100%;
  max-height: 120px;
}

.logo__image2 {
  max-width: 90%;
}

.tifsu_logo_footer {
  max-width: 293px;
  border-radius: 7px;
}

.header-tools {
  margin-right: -0.5rem;
}

.header-tools__item {
  display: flex;
  padding: 0.25rem 0.5rem;
  text-decoration: none;
  color: #222222;
}

.header-tools__item .flaticon::before {
  display: block;
  line-height: 1;
}

.header-tools__item:last-child {
  margin-right: 0;
}

@media (min-width: 1200px) {
  .header-tools__item {
    margin-right: 1rem;
  }
}

.header-tools__cart {
  position: relative;
}

.header-tools__cart .cart-amount {
  top: calc(0.25rem + 1em);
  left: calc(0.5rem + 1.4em);
  width: 1rem;
  height: 1rem;
  border-radius: 100%;
  background: #b9a16b;
  color: #ffffff;
  font-size: 0.625rem;
  line-height: 1rem;
  text-align: center;
}

.header-search {
  display: flex;
  align-items: center;
  padding: 0.75rem 1.25rem 0.625rem 0.875rem;
  border: 1px solid #e4e4e4;
  border-radius: 3px;
  background-color: #ffffff;
}

.header-search> :first-child {
  padding-left: 0;
}

.header-search> :last-child {
  margin-left: 1.25rem;
}

.header-search .hover-container {
  display: none;
}

@media (min-width: 1200px) {
  .header-search .hover-container {
    display: block;
  }
}

.header-search__input {
  padding: 0 0 0 1.25rem;
  border: 0;
  background-color: transparent;
  color: #222222;
  outline: none;
}

.header-search__btn {
  padding: 0;
  border: 0;
  line-height: 1;
}

.header-search__category {
  padding-right: 12px;
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='%23222222' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M2 5l6 6 6-6'/%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0 center;
  background-size: 12px;
  color: #222222;
  outline: none;
}

.header-search__category::placeholder {
  color: #6c757d;
}

.header-search__category-list {
  right: calc(-1.25rem - 1px);
  width: calc(100% + 1.875rem + 1px);
  padding: 0 0.625rem;
  border: 1px solid #e4e4e4;
}

.header_sticky-bg_dark a {
  color: #fff;
}

.header_sticky-bg_dark svg {
  opacity: 1;
}

.header_sticky-bg_dark .btn-close-lg {
  background-image: url("data:image/svg+xml,%3csvg width='16' height='16' viewBox='0 0 16 16' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M0.414336 14.1421L14.5565 0L15.9707 1.41421L1.82855 15.5563L0.414336 14.1421Z' fill='%23fff'/%3e%3cpath d='M1.41421 0.142113L15.5563 14.2842L14.1421 15.6985L0 1.55633L1.41421 0.142113Z' fill='%23fff'/%3e%3c/svg%3e");
}

.header_sticky-bg_dark .mega-menu a,
.header_sticky-bg_dark .box-menu a,
.header_sticky-bg_dark .default-menu a {
  color: #222222;
}

.header-top.bordered {
  border-bottom: 1px solid #e4e4e4;
}

.header-top.bordered-20per {
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
}

.header_transparent {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  background: transparent;
}

.header-desk_type_1 {
  padding: 1.875rem 0 1.5rem 0;
}

.header-desk_type_1 .logo {
  margin-right: 2.1875rem;
}

.header-desk_type_1 .header-tools {
  margin-left: auto;
  margin-right: -0.5rem;
}

.header-fullwidth .header-desk_type_1 {
  padding: 1.25rem 0;
}

.header-fullwidth .header-desk_type_1 .header-search {
  padding-top: 0.6125rem;
  padding-bottom: 0.5rem;
  width: 21.5625rem;
}

.header-desk_type_2 {
  padding: 1.75rem 0;
}

.header-desk_type_2 .logo {
  margin: 0 auto;
  padding: 0 1rem;
}

.header-desk_type_2 .navigation {
  flex: 1;
}

.header-desk_type_2 .header-tools {
  flex: 1;
  justify-content: flex-end;
}

@media (min-width: 992px) and (max-width: 1499.98px) {
  .header-desk_type_2 .navigation__link {
    padding: 2px 0.5rem;
  }

  .header-desk_type_2 .navigation__link:after {
    left: 0.5rem;
  }
}

@media (min-width: 1500px) {
  .header-desk_type_2 {
    padding: 1.875rem 0;
  }
}

.header-desk_type_3 {
  padding: 2.625rem 0 1.5rem 0;
}

.header-desk_type_3 .logo {
  margin-right: 2.375rem;
}

.header-desk_type_3 .header-tools {
  margin-left: auto;
  margin-right: -0.5rem;
}

.header-desk_type_4 {
  padding: 1.875rem 0 1.5rem 0;
}

.header-desk_type_4.header-desk_sm {
  padding: 1.375rem 0;
}

.header-desk_type_4 .navigation {
  margin: 0 auto;
}

.header-desk_type_5 {
  padding: 1.25rem 0;
}

.header-desk_type_5 .logo {
  margin-right: 2.75rem;
}

.header-desk_type_5 .header-search {
  width: 26.625rem;
  margin-right: auto;
}

.header-desk_type_6 {
  border-bottom: 1px solid #e4e4e4;
}

.header-desk_type_6 .header-middle {
  padding: 1.25rem 0;
  border-bottom: 1px solid #e4e4e4;
}

.header-desk_type_6 .logo {
  width: 20.5rem;
  margin-right: 0.9375rem;
}

.header-desk_type_6 .navigation {
  margin: 0 -0.7rem;
  padding: 1.125rem 0 0.75rem 0.9375rem;
}

@media (min-width: 1200px) {
  .header-desk_type_6 .navigation {
    margin: -1rem;
  }
}

.header-desk_type_6 .navigation__item:first-child {
  margin-left: 0;
}

.header-desk_type_6 .navigation__item:last-child {
  margin-right: 0;
}

.header-desk_type_6 .header-search {
  flex-grow: 1;
  margin-left: 0.9375rem;
  margin-right: 0.5rem;
}

@media (min-width: 1200px) {
  .header-desk_type_6 .header-search {
    margin-right: 1.5rem;
  }
}

.header-desk_type_6 .categories-nav {
  width: 13.325rem;
  max-width: 20.5rem;
  margin-right: 0.9375rem;
}

@media (min-width: 1500px) {
  .header-desk_type_6 .categories-nav {
    width: 20.5rem;
  }
}

.header-desk_type_6 .categories-nav__list {
  position: absolute;
  width: 100%;
  left: 0;
  top: 100%;
  background-color: #ffffff;
  transition: all .3s ease;
}

.header-desk_type_6 .categories-nav__title {
  padding: 1.125rem 0 0.75rem 0.9375rem;
  padding-left: 1.8rem;
  padding-right: 1.8rem;
}

@media (min-width: 1500px) {
  .header-desk_type_6 .categories-nav__title {
    padding-left: 3rem;
    padding-right: 3rem;
  }
}

.header-desk_type_6.style2 .header-search {
  padding-left: 1.75rem;
  padding-right: 1.75rem;
}

.header-desk_type_6.style2 .header-bottom {
  background-color: #193174;
}

.header-desk_type_6.style2 .header-bottom .navigation__list>.navigation__item>span {
  color: #ffffff;
}

.header-desk_type_6.style2 .header-bottom .navigation__list>.navigation__item>.navigation__link {
  color: #ffffff;
}

.header-desk_type_6.style2 .navigation {
  margin-right: 0;
}

.header-desk_type_6.style2 .categories-nav__title {
  padding-left: 0;
  padding-right: 0;
  cursor: pointer;
  background-color: #193174;
}

.header-desk_type_6.style2 .categories-nav__title+.categories-nav__list {
  opacity: 0;
  visibility: hidden;
  transition: all .3s ease;
}

.header-desk_type_6.style2 .categories-nav:hover>.categories-nav__list {
  opacity: 1;
  visibility: visible;
}

.header_sticky-active .header-desk_type_6 .categories-nav__list {
  opacity: 0;
  visibility: hidden;
}

.header_sticky-active .header-desk_type_6 .categories-nav:hover .categories-nav__list {
  opacity: 1;
  visibility: visible;
}

.header-desk_type_7 .header-top {
  padding: 1.25rem 0;
  color: #ffffff;
  background-color: #222222;
}

.header-desk_type_7 .header-bottom {
  padding: 1.25rem 0 0.75rem;
  color: #ffffff;
  background-color: #767676;
}

.header-desk_type_7 .logo {
  margin-right: 2.75rem;
}

.header-desk_type_7 .header-search {
  width: 26.625rem;
  margin-right: auto;
}

.header-desk_type_7 .navigation {
  width: 100%;
}

.header-desk_type_7 .navigation__link,
.header-desk_type_7 .header-tools__item {
  color: inherit;
}

.header-desk_type_7 .navigation__item:first-child {
  margin-left: 0;
}

.header-desk_type_7 .navigation__item:first-child .navigation__link {
  padding-left: 0;
}

.header-desk_type_7 .navigation__item:last-child {
  margin-right: 0;
}

.header-desk_type_7 .navigation__item:last-child .navigation__link {
  padding-right: 0;
}

.header-mobile {
  height: 3.75rem;
  min-height: 3.75rem;
  background-color: #ffffff;
  z-index: 1030;
}

.header-mobile .logo {
  margin: 0 auto;
}

.header-mobile .logo__image {
  max-height: 3rem;
}

@media (min-width: 992px) {
  .header-mobile {
    display: none;
  }
}

.header-mobile_sticky {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 8px 25px 0 rgba(140, 152, 164, 0.15);
}

.header-mobile__navigation {
  display: flex;
  flex-direction: column;
  height: 0;
  max-height: 0;
  transition: max-height .35s, height .35s;
  z-index: 1030;
}

.header-mobile__navigation .search-field__input {
  padding: 0.625rem 0.875rem 0.375rem;
}

.header-mobile__navigation .search-result {
  max-height: 30rem;
  overflow: auto;
  background-color: #ffffff;
  z-index: 1;
}

.header-mobile__navigation .search-result .product-card {
  display: flex;
  margin: 0.625rem 0;
}

.header-mobile__navigation .search-result .pc__img-wrapper {
  width: 40%;
  margin-right: 0.875rem;
}

.header-mobile__navigation .navigation__link {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
  font-size: 1rem;
}

.header-mobile__navigation .navigation__link .flaticon {
  font-size: 0.75rem;
}

.header-mobile__navigation .navigation__link:after {
  top: auto;
  bottom: 0.5rem;
  left: 0;
}

.header-mobile__navigation .form-select-sm {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.mobile-nav-activator .nav-icon,
.mobile-nav-activator .btn-close-lg {
  transition: all .24s;
}

.mobile-nav-activator .btn-close-lg {
  transform: rotate(-90deg);
  opacity: 0;
  visibility: hidden;
}

.mobile-menu-opened {
  overflow: hidden;
}

.mobile-menu-opened .header-mobile {
  z-index: 1050;
}

.mobile-menu-opened .header-mobile__navigation {
  height: calc(100vh - 100%);
  max-height: calc(100vh - 100%);
  transition: max-height .35s, height .35s;
  border-top: 1px solid #e4e4e4;
}

.mobile-menu-opened .navigation__list {
  left: 0;
  transition: all .18s ease-in;
}

.mobile-menu-opened .mobile-nav-activator .nav-icon {
  opacity: 0;
  visibility: hidden;
}

.mobile-menu-opened .mobile-nav-activator .btn-close-lg {
  transform: rotate(0);
  opacity: 1;
  visibility: visible;
}

.header_sticky {
  top: 0;
  left: 0;
  width: 100%;
  max-width: 100%;
  z-index: 9;
  transition: all .3s ease;
}

.header_sticky-active {
  position: fixed;
  animation: moveDown .5s;
  background-color: #ffffff;
  box-shadow: 0 8px 25px 0 rgba(140, 152, 164, 0.15);
  z-index: 1020;
}

.header_sticky-active.header_sticky-bg_dark {
  background-color: #222222;
}

.header_sticky-active .header-desk_type_3 {
  padding-top: 1.5rem;
}

.footer-top {
  padding-top: 6.2rem;
}

.footer-top .block-newsletter {
  max-width: 47rem;
  margin: 0 auto;
  text-align: center;
}

.footer-middle {
  padding-top: 3.125rem;
  padding-bottom: 1.625rem;
}

.footer-middle .logo {
  margin-bottom: 2.75rem;
}

@media (min-width: 768px) {
  .footer-middle {
    padding-top: 3.75rem;
    padding-bottom: 2.85rem;
  }
}

@media (min-width: 992px) {
  .footer-middle {
    padding-top: 6.25rem;
    padding-bottom: 4.75rem;
  }
}

.footer-column {
  flex-grow: 1;
}

.footer-address {
  margin-bottom: 0.875rem;
}

.footer__social-link {
  padding: 0.5rem 1rem;
  color: inherit;
}

.footer__social-link .svg-icon {
  fill: currentColor;
}

.footer-newsletter__form .btn-link {
  padding-right: 0.9375rem;
}

.footer-bottom {
  padding-top: 1.25rem;
  padding-bottom: 1rem;
  border-top: 1px solid #cfcdcd;
}

.footer {
  background-color: #e4e4e4;
  color: #222222;
}

.footer .sub-menu__title {
  margin-bottom: 0.875rem;
  color: inherit;
}

@media (min-width: 992px) {
  .footer .sub-menu__title {
    margin-bottom: 1.875rem;
  }
}

.footer .menu-link {
  margin-top: 3px;
  margin-bottom: 2px;
}

.footer .social-links {
  margin-left: -1rem;
}

.footer .form-select {
  color: inherit;
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23222222'/%3e%3c/svg%3e");
}

.footer .form-select:focus {
  box-shadow: none;
  border-color: transparent;
}

@media (max-width: 767.98px) {
  .footer .form-select {
    padding-left: 0;
  }
}

.footer .form-select.color-white {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='white'/%3e%3c/svg%3e");
}

.footer .form-select.color-white option {
  color: #222222;
}

.footer .service-promotion.horizontal {
  border-bottom: 1px solid #cfcdcd;
}

.footer_type_2 {
  background-color: #ffffff;
  color: #c0bfbf;
}

.footer_type_2 .form-select {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23767676'/%3e%3c/svg%3e");
}

.footer_type_2 .footer-select__option {
  background-color: #ffffff;
}

.footer_type_2 .footer-bottom {
  border-color: #e4e4e4;
}

.footer_type_2 .sub-menu__title {
  color: #222222;
}

.footer_type_2.dark {
  background-color: #222222;
  color: #c0bfbf;
}

.footer_type_2.dark .sub-menu__title {
  color: inherit;
}

.footer_type_2.dark .menu-link {
  color: #e4e4e4;
}

.footer_type_2.dark .form-select {
  background-image: url("data:image/svg+xml,%3csvg width='14' height='8' viewBox='0 0 14 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M7.49932 0.360778C7.22726 0.0887249 6.77274 0.0887249 6.49999 0.360778L0.206656 6.638C-0.0688853 6.91355 -0.0688853 7.3604 0.206656 7.63524C0.482197 7.91078 0.929749 7.91078 1.20529 7.63524L6.99997 1.85667L12.794 7.63594C13.0702 7.91148 13.517 7.91148 13.7933 7.63594C14.0688 7.3604 14.0688 6.91355 13.7933 6.6387L7.49932 0.360778Z' fill='%23ffffff'/%3e%3c/svg%3e");
}

.footer_type_2.dark .footer-select__option {
  background-color: #222222;
}

.footer_type_2.dark .footer-bottom {
  border-color: rgba(255, 255, 255, 0.15);
}

.footer_type_2.dark .footer__social-link:hover {
  color: #767676;
}

.footer_type_2.bordered {
  border-top: 1px solid #e4e4e4;
}

.footer_type_3 {
  background-color: #fff;
}

.footer_type_3 .footer-middle {
  padding: 0.875rem 0;
  border-top: 1px solid #cfcdcd;
}

.app-download-link {
  background: #767676;
  display: flex;
  width: 14.1875rem;
  height: 4.375rem;
  border-radius: 0.25rem;
  color: #ffffff;
  align-items: center;
  padding: 0.875rem;
  line-height: 1.4;
  gap: 1.5rem;
  transition: all .3s ease;
}

.app-download-link .app-download-text {
  display: flex;
  flex-direction: column;
  font-size: 0.8125rem;
}

.app-download-link .app-download-text strong {
  font-size: 1rem;
  font-weight: 400;
}

.app-download-link:hover {
  color: #ffffff;
  background-color: #222222;
}

.app-download-link.no-bg {
  width: auto;
  height: auto;
  border-radius: 0;
  color: #222222;
  background-color: transparent;
  padding: 0;
  gap: 1rem;
}

@media (min-width: 992px) {
  .footer-store-info {
    width: 24%;
  }

  .footer-menu {
    width: 17%;
  }

  .footer-menu2 {
    width: 1%;
  }

  .footer-newsletter {
    width: 25%;
  }
}

.footer-mobile {
  max-width: 100%;
  padding-top: 0.625rem;
  padding-bottom: 0.125rem;
  z-index: 1000;
  opacity: 0;
  bottom: -6.25rem;
  transition: all .32s;
}

.footer-mobile .flaticon {
  font-size: 1.125rem;
}

.footer-mobile .cart-amount,
.footer-mobile .wishlist-amount {
  top: -5px;
  left: calc(100% - 5px);
  width: 1rem;
  height: 1rem;
  border-radius: 100%;
  background: #b9a16b;
  color: #ffffff;
  font-size: 0.625rem;
  line-height: 1rem;
  text-align: center;
}

.footer-mobile.position-fixed {
  opacity: 1;
}

.footer-mobile.footer-mobile_initialized {
  bottom: 0;
  transition: all .32s;
}

.footer-mobile__link {
  font-size: 0.8125rem;
}

.slideshow {
  height: 34.5rem;
}

.slideshow.type3 {
  height: 26.25rem;
}

.slideshow.type4 {
  height: 26.25rem;
}

@media (min-width: 992px) {
  .slideshow {
    height: 50rem;
  }

  .slideshow.type2 {
    height: 56rem;
  }

  .slideshow.type3 {
    height: 35rem;
  }

  .slideshow.type4 {
    height: 37.5rem;
  }

  .slideshow.slideshow-lg {
    height: 47.5rem;
  }

  .slideshow.slideshow-md {
    height: 43.75rem;
  }
}

@media (max-width: 575.98px) {
  .slideshow.h-xs-25rem {
    height: 25rem;
  }
}

@media (max-width: 991.98px) {
  .slideshow.minh-100 {
    min-height: calc(100vh - 4rem);
  }
}

@media (max-width: 767.98px) {
  .slideshow.minh-100 {
    min-height: calc(100vh - 7rem);
  }
}

.slideshow_small {
  height: 20rem;
}

@media (min-width: 992px) {
  .slideshow_small {
    height: 28.125rem;
  }
}

.swiper-slide {
  overflow: hidden;
}

.slideshow-bg {
  height: 100%;
}

.slideshow-bg__img {
  width: 100%;
  height: 100%;
}

.slideshow-character__img {
  max-height: 555px;
}

@media (min-width: 992px) {
  .slideshow-character__img {
    max-height: 733px;
  }
}

.slideshow_small .slideshow-character__img {
  max-height: 20rem;
}

@media (min-width: 992px) {
  .slideshow_small .slideshow-character__img {
    max-height: 28.125rem;
  }
}

.character_bg {
  max-width: 140%;
  width: 43.125rem;
  margin-top: -10%;
}

.slideshow-pagination {
  z-index: 10;
}

.slideshow-pagination.type2 .swiper-pagination-bullet::after {
  color: #767676;
}

.slideshow-pagination.type2 .swiper-pagination-bullet-active {
  border-color: transparent;
}

.slideshow-pagination.type2 .swiper-pagination-bullet-active::after {
  color: #222222;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
}

.slideshow-pagination.position-left-center {
  position: absolute;
  left: 50%;
  top: auto;
  bottom: 1rem;
  transform: translateX(-50%);
  display: flex;
  width: auto;
}

@media (min-width: 1700px) {
  .slideshow-pagination.position-left-center {
    left: 3.75rem;
    top: 50%;
    bottom: auto;
    transform: translateY(-50%);
    flex-direction: column;
  }
}

.slideshow-pagination.position-right-center {
  position: absolute;
  left: auto;
  right: 50%;
  top: auto;
  bottom: 1rem;
  transform: translateX(50%);
  display: flex;
  width: auto;
}

@media (min-width: 1500px) {
  .slideshow-pagination.position-right-center {
    right: 3.75rem;
    top: 50%;
    bottom: auto;
    transform: translateY(-50%);
    flex-direction: column;
  }

  .slideshow-pagination.position-right-center.position-right-2 {
    right: 2.6875rem;
  }
}

.lookbook-container .slideshow-pagination.position-right-center {
  position: static;
  align-items: center;
  justify-content: center;
  margin-top: 1rem;
}

@media (min-width: 1500px) {
  .lookbook-container .slideshow-pagination.position-right-center {
    position: absolute;
    right: -3.75rem;
  }

  .lookbook-container .slideshow-pagination.position-right-center.position-right-2 {
    right: -2.6875rem;
  }

  .lookbook-container .slideshow-pagination.position-right-center.position-right-2 .swiper-pagination-bullet {
    margin: 0.25rem 0;
  }
}

.blog-pagination,
.testimonial-pagination,
.products-pagination,
.slideshow-pagination {
  z-index: 10;
}

.blog-pagination.type2 .swiper-pagination-bullet-active,
.testimonial-pagination.type2 .swiper-pagination-bullet-active,
.products-pagination.type2 .swiper-pagination-bullet-active,
.slideshow-pagination.type2 .swiper-pagination-bullet-active {
  border-color: transparent;
}

.blog-pagination.type2 .swiper-pagination-bullet-active::after,
.testimonial-pagination.type2 .swiper-pagination-bullet-active::after,
.products-pagination.type2 .swiper-pagination-bullet-active::after,
.slideshow-pagination.type2 .swiper-pagination-bullet-active::after {
  color: #222222;
  width: 0.625rem;
  height: 0.625rem;
  margin-top: -0.3125rem;
  margin-left: -0.3125rem;
}

.blog-pagination.active-white .swiper-pagination-bullet::after,
.testimonial-pagination.active-white .swiper-pagination-bullet::after,
.products-pagination.active-white .swiper-pagination-bullet::after,
.slideshow-pagination.active-white .swiper-pagination-bullet::after {
  color: #767676;
}

.blog-pagination.active-white .swiper-pagination-bullet-active::after,
.testimonial-pagination.active-white .swiper-pagination-bullet-active::after,
.products-pagination.active-white .swiper-pagination-bullet-active::after,
.slideshow-pagination.active-white .swiper-pagination-bullet-active::after {
  color: #ffffff;
}

.blog-pagination.color-white .swiper-pagination-bullet::after,
.testimonial-pagination.color-white .swiper-pagination-bullet::after,
.products-pagination.color-white .swiper-pagination-bullet::after,
.slideshow-pagination.color-white .swiper-pagination-bullet::after {
  color: #ffffff;
}

.blog-pagination.color-white .swiper-pagination-bullet-active::after,
.testimonial-pagination.color-white .swiper-pagination-bullet-active::after,
.products-pagination.color-white .swiper-pagination-bullet-active::after,
.slideshow-pagination.color-white .swiper-pagination-bullet-active::after {
  color: #ffffff;
}

.slideshow-number-pagination .swiper-pagination-bullet {
  width: auto;
  height: auto;
  border: 0;
  color: #767676;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.slideshow-number-pagination .swiper-pagination-bullet:before {
  content: '';
  border-top: 1px solid #767676;
  width: 2.3125rem;
  display: block;
}

.slideshow-number-pagination .swiper-pagination-bullet:after {
  display: none;
}

.slideshow-number-pagination .swiper-pagination-bullet:first-child:before {
  display: none;
}

.slideshow-number-pagination .swiper-pagination-bullet-active {
  color: #222222;
}

@media (min-width: 1500px) {
  .slideshow-number-pagination.position-xxl-right-center {
    right: 0 !important;
    top: 50% !important;
    bottom: auto !important;
    left: auto !important;
    transform: translateY(-50%);
    flex-direction: column;
    margin: 0 1.125rem;
  }

  .slideshow-number-pagination.position-xxl-right-center .swiper-pagination-bullet {
    flex-direction: column;
  }

  .slideshow-number-pagination.position-xxl-right-center .swiper-pagination-bullet:before {
    border-top: 0;
    border-left: 1px solid #767676;
    width: 1px;
    height: 2.3125rem;
  }
}

.slideshow-navigation {
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.slideshow-navigation .slideshow__prev,
.slideshow-navigation .slideshow__next {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  color: #767676;
  font-weight: 500;
  width: auto;
  opacity: 1;
}

.slideshow-navigation .slideshow__prev:after {
  content: '';
  display: block;
  width: 1.875rem;
  border-bottom: 2px solid;
  transition: all .3s ease;
}

.slideshow-navigation .slideshow__prev:hover {
  color: #222222;
}

.slideshow-navigation .slideshow__prev:hover:after {
  width: 3.125rem;
}

.slideshow-navigation .slideshow__next:before {
  content: '';
  display: block;
  width: 1.875rem;
  border-bottom: 2px solid;
  transition: all .3s ease;
}

.slideshow-navigation .slideshow__next:hover {
  color: #222222;
}

.slideshow-navigation .slideshow__next:hover:before {
  width: 3.125rem;
}

.slideshow__prev,
.slideshow__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  z-index: 1;
  outline: none;
}

.slideshow__prev .flaticon,
.slideshow__next .flaticon {
  font-size: 10px;
}

@media (min-width: 1530px) {

  .slideshow__prev,
  .slideshow__next {
    width: 25px;
    height: 25px;
    margin-top: -0.875rem;
    border: 0;
    transition: opacity .32s;
    opacity: 0.5;
  }

  .slideshow__prev .flaticon,
  .slideshow__next .flaticon {
    font-size: 25px;
  }

  .slideshow__prev:hover,
  .slideshow__next:hover {
    opacity: 1;
  }
}

.slideshow__prev {
  left: 1rem;
}

@media (min-width: 1530px) {
  .slideshow__prev {
    left: 3.5rem;
  }
}

.slideshow__next {
  right: 1rem;
}

@media (min-width: 1530px) {
  .slideshow__next {
    right: 3.5rem;
  }
}

.slideshow-navigation-white-sm .slideshow__prev,
.slideshow-navigation-white-sm .slideshow__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  z-index: 1;
  outline: none;
  background-color: #ffffff;
  display: none !important;
}

@media (min-width: 768px) {

  .slideshow-navigation-white-sm .slideshow__prev,
  .slideshow-navigation-white-sm .slideshow__next {
    display: flex !important;
  }
}

.slideshow-navigation-white-sm .slideshow__prev .flaticon,
.slideshow-navigation-white-sm .slideshow__next .flaticon {
  font-size: 10px;
}

@media (max-width: 767.98px) {
  .slideshow_split {
    height: auto;
  }
}

.slide-split_text {
  flex: 2 2 40%;
}

@media (max-width: 1499.98px) {
  .slide-split_text {
    flex: 2 2 50%;
  }
}

.slide-split_media {
  flex: 1 1 60%;
}

@media (max-width: 1499.98px) {
  .slide-split_media {
    flex: 2 2 50%;
  }
}

.slideshow-social-follow {
  width: 3.75rem;
  z-index: 1;
}

.slideshow-social-follow__title {
  transform: rotate(-90deg);
  white-space: nowrap;
}

.slideshow-scroll {
  width: 3.75rem;
  transform: rotate(-90deg) translateX(30%);
  white-space: nowrap;
  z-index: 3;
}

.slideshow-boxed-right>.slideshow {
  height: 26.25rem;
  background-color: #eee;
  border-radius: 4px;
}

@media (min-width: 992px) {
  .slideshow-boxed-right>.slideshow {
    height: 31.875rem;
    width: 44rem;
    margin-left: auto;
    margin-right: 0;
    margin-top: 1.875rem;
  }
}

@media (min-width: 1200px) {
  .slideshow-boxed-right>.slideshow {
    width: 54rem;
  }
}

@media (min-width: 1500px) {
  .slideshow-boxed-right>.slideshow {
    width: 65.625rem;
  }
}

@media (min-width: 992px) {
  .collections-grid_masonry {
    height: 30rem;
  }
}

@media (min-width: 1500px) {
  .collections-grid_masonry {
    height: 37.5rem;
  }
}

.collections-grid_masonry .collection-grid__item {
  height: 17.8125rem;
}

@media (min-width: 992px) {
  .collections-grid_masonry .collection-grid__item {
    height: auto;
  }
}

.collection-grid__item {
  margin-bottom: 0.9375rem;
}

@media (min-width: 992px) {
  .collection-grid__item {
    margin-bottom: 0;
  }
}

.grid-banner__item_rect {
  min-height: 19.375rem;
}

@media (min-width: 992px) {
  .grid-banner__item_rect {
    min-height: 24.875rem;
  }
}

@media (min-width: 992px) {
  .grid-banner__item_rect_2 {
    min-height: 31.25rem;
  }

  .grid-banner__item_rect_2 .content_abs {
    --content-space: 4.5625rem;
  }
}

.products-grid .row {
  --bs-gutter-x: 0.875rem;
}

@media (min-width: 768px) {
  .products-grid .row {
    --bs-gutter-x: 1.5rem;
  }
}

@media (min-width: 992px) {
  .products-grid .row {
    --bs-gutter-x: 1.875rem;
  }
}

.products-grid .nav {
  margin-left: -var(--bs-gutter-x);
  margin-right: -var(--bs-gutter-x);
}

@media (min-width: 992px) {
  .products-masonry {
    height: 480px;
  }

  .products-masonry .pc__img-wrapper {
    height: 100%;
  }
}

@media (min-width: 1200px) {
  .products-masonry {
    height: 640px;
  }
}

@media (min-width: 1500px) {
  .products-masonry {
    height: 730px;
  }
}

.deal-timer {
  --countdown-space: 1.125rem;
  min-height: 19.375rem;
  margin: 0 0.9375rem;
  padding: 2rem 1rem;
}

.deal-timer .countdown-unit {
  position: relative;
  min-width: 4.375rem;
  padding-right: calc(var(--countdown-space) * 2);
  font-size: 1.125rem;
  line-height: 1;
}

.deal-timer .countdown-word {
  font-size: 0.875rem;
}

.deal-timer .day:after,
.deal-timer .hour:after,
.deal-timer .min:after {
  content: ':';
  display: block;
  position: absolute;
  top: 0;
  right: var(--countdown-space);
}

@media (min-width: 768px) {
  .deal-timer {
    min-height: 25rem;
  }

  .deal-timer .countdown-unit {
    font-size: 1.5rem;
  }
}

@media (min-width: 992px) {
  .deal-timer {
    min-height: 31.25rem;
    padding: 2.5rem 0;
  }

  .deal-timer .countdown-unit {
    min-width: 6.25rem;
    font-size: 1.875rem;
  }

  .deal-timer .countdown-word {
    font-size: 1rem;
  }
}

@media (min-width: 1500px) {
  .deal-timer {
    --countdown-space: 1.375rem;
    min-height: 37.5rem;
    margin: 0 3.75rem;
  }
}

.hot-deals {
  --countdown-space: 0.875rem;
}

.hot-deals .countdown-unit {
  position: relative;
  padding-right: calc(var(--countdown-space) * 2);
  line-height: 1;
  font-size: 1.125rem;
}

.hot-deals .countdown-word {
  font-size: 0.875rem;
}

.hot-deals .day:after,
.hot-deals .hour:after,
.hot-deals .min:after {
  content: ':';
  display: block;
  position: absolute;
  top: 0;
  right: var(--countdown-space);
}

.swiper-slide.product-card {
  width: 50%;
}

@media (min-width: 768px) {
  .swiper-slide.product-card {
    width: 33.33333%;
  }
}

@media (min-width: 992px) {
  .swiper-slide.product-card {
    width: 25%;
  }
}

.products-carousel__prev,
.products-carousel__next {
  width: 35px;
  height: 35px;
  margin-top: -2.2rem;
  transform: translateY(-50%);
  border: 1px solid #e4e4e4;
  border-radius: 100%;
  background-color: #ffffff;
  z-index: 1;
  outline: none;
}

.products-carousel__prev svg,
.products-carousel__next svg {
  color: #767676;
  width: 10px;
  height: auto;
}

.products-carousel__prev.type2,
.products-carousel__next.type2 {
  background-color: #eee;
}

.products-carousel__prev.type2 svg,
.products-carousel__next.type2 svg {
  width: 0.75rem;
}

@media (min-width: 1530px) {

  .products-carousel__prev:not(.navigation-sm),
  .products-carousel__next:not(.navigation-sm) {
    width: 25px;
    height: 25px;
    margin-top: -0.875rem;
    border: 0;
    transition: opacity .32s;
    opacity: 0.5;
  }

  .products-carousel__prev:not(.navigation-sm) svg,
  .products-carousel__next:not(.navigation-sm) svg {
    width: 25px;
  }

  .products-carousel__prev:not(.navigation-sm):hover,
  .products-carousel__next:not(.navigation-sm):hover {
    opacity: 1;
  }

  .products-carousel__prev:not(.navigation-sm).type2,
  .products-carousel__next:not(.navigation-sm).type2 {
    width: 2.8125rem;
    height: 2.8125rem;
  }
}

.products-carousel__prev {
  left: -0.625rem;
}

@media (min-width: 1530px) {
  .products-carousel__prev {
    left: -3rem;
  }

  .products-carousel__prev.type2 {
    left: -4.5rem;
  }
}

.products-carousel__next {
  right: -0.625rem;
}

@media (min-width: 1530px) {
  .products-carousel__next {
    right: -3rem;
  }

  .products-carousel__next.type2 {
    right: -4.5rem;
  }
}

.products-carousel-with-banner .products-carousel__prev svg,
.products-carousel-with-banner .products-carousel__next svg {
  width: 0.9375rem;
  height: auto;
}

.products-carousel-with-banner__category {
  position: absolute;
  right: 0;
  top: 0;
  transform: rotate(-90deg);
  transform-origin: right top;
}

.instagram__img {
  width: 100%;
  max-width: 100%;
  height: 100%;
  object-fit: cover;
}

.instagram .row {
  margin: -7px;
}

@media (min-width: 768px) {
  .instagram .row {
    margin: -3px;
  }
}

.instagram__tile {
  padding: 7px;
}

@media (min-width: 768px) {
  .instagram__tile {
    padding: 3px;
  }
}

.service-promotion__icon .flaticon {
  font-size: 3.25rem;
}

.service-promotion__content {
  font-size: 0.9375rem;
}

.service-promotion.horizontal {
  padding-top: 2.9375rem;
  padding-bottom: 2.3rem;
}

.service-promotion.horizontal .service-promotion__icon .flaticon {
  font-size: 2.8125rem;
}

.shop-banner {
  min-height: 18.5rem;
}

@media (min-width: 1200px) {
  .shop-banner {
    min-height: 21.5rem;
  }
}

@media (min-width: 1200px) {
  .shop-banner {
    min-height: 26.25rem;
  }
}

.shop-acs__select {
  padding-right: 0.9375rem;
  background-position: right center;
  cursor: pointer;
  padding-left: 0;
  box-shadow: none !important;
  text-transform: uppercase;
  font-weight: 500;
}

.shop-asc__seprator {
  width: 2px;
  height: 22px;
}

.aside-filters {
  overflow-x: hidden;
  overflow-y: auto;
}

.shop-acs .multi-select__actor {
  padding-right: 2.8125rem;
}

.shop-acs .filters-container {
  border: 1px solid #e4e4e4;
}

.shop-pages .flaticon {
  font-size: 0.625rem;
}

.shop-sidebar {
  width: 18.75rem;
  min-width: 18.75rem;
}

.aside-filters .accordion-button__icon,
.shop-sidebar .accordion-button__icon {
  width: 0.625rem;
  height: 0.625rem;
}

.shop-list {
  max-width: 100%;
}

@media (min-width: 992px) {
  .shop-list {
    max-width: calc(100% - 22.5rem);
  }
}

.side-sticky {
  position: fixed;
  top: 0;
  right: -26.25rem;
  left: auto;
  width: 26.25rem;
  max-width: 100%;
  height: 100vh;
  padding: 0 1.25rem 1.75rem;
  transition: left .35s, right .35s;
  overflow-x: hidden;
  overflow-y: auto;
  z-index: 1050;
}

.side-sticky.aside_visible {
  right: 0;
}

.side-sticky .accordion {
  padding-left: 1.25rem;
  padding-right: 1.25rem;
}

@media (min-width: 992px) {
  .side-sticky {
    position: sticky;
    top: 0;
    right: auto;
    left: 0;
    width: 18.75rem;
    height: 100%;
    padding: .375rem 0 0;
    margin-right: 3.75rem;
    z-index: 1;
  }

  .side-sticky .accordion {
    padding-left: 0;
    padding-right: 0;
  }
}

.shop-categories {
  --item-space: 0.9375rem;
  padding: calc(var(--item-space) * 2) var(--item-space);
}

@media (min-width: 992px) {
  .shop-categories {
    --item-space: 1.875rem;
    padding: var(--item-space);
  }
}

@media (min-width: 1500px) {
  .shop-categories {
    --item-space: 3.75rem;
  }
}

.shop-categories__list {
  margin: 0 calc(var(--item-space) * -1 / 2);
}

.shop-categories__item,
.shop-categories__item_sm {
  margin-right: calc(var(--item-space) / 2);
  margin-left: calc(var(--item-space) / 2);
  transition: filter .2s;
}

.shop-categories__item:hover,
.shop-categories__item_sm:hover {
  filter: brightness(0.97);
}

.shop-categories__item-img {
  width: 5rem;
  height: 5rem;
  background-color: #e4e4e4;
}

@media (min-width: 992px) {
  .shop-categories__item-img {
    width: 6.25rem;
    height: 6.25rem;
  }
}

@media (min-width: 1500px) {
  .shop-categories__item-img {
    width: 7.5rem;
    height: 7.5rem;
  }

  .shop-categories__item_sm .shop-categories__item-img {
    width: 6.25rem;
    height: 6.25rem;
  }
}

@media (min-width: 576px) {
  .block-newsletter {
    padding: 0 1rem;
  }
}

.block-newsletter .block__title {
  color: #222222;
  margin-bottom: 1.125rem;
}

.block-newsletter p {
  margin-bottom: 1.5rem;
}

.block-newsletter .block-newsletter__form {
  display: flex;
  gap: 1.25rem;
}

.block-newsletter .form-control {
  border-width: 1px;
  border-color: #e4e4e4;
}

.block-newsletter .btn {
  font-size: 0.875rem;
  background-color: #222222;
}

.block-newsletter.dark .block__title {
  color: inherit;
}

.block-newsletter.dark .form-control {
  border-color: #353535;
  background-color: #353535;
  color: #ffffff;
}

.block-newsletter.dark .form-control::placeholder {
  color: #e4e4e4;
}

.block-newsletter.dark .btn {
  border-color: #5C5C5C;
  background-color: #5C5C5C;
  color: #ffffff;
}

.newsletter-popup {
  width: 56.25rem;
  max-width: calc(100% - 1rem);
}

.newsletter-popup .modal-content {
  overflow: hidden;
}

.newsletter-popup .modal-content .btn-close {
  position: absolute;
  right: 0.75rem;
  top: 1rem;
}

.newsletter-popup .block-newsletter {
  padding: 1.875rem 1.25rem;
}

@media (min-width: 768px) {
  .newsletter-popup .block-newsletter {
    padding: 3.5rem 2.5rem;
  }
}

@media (min-width: 1200px) {
  .product-single>.row {
    --bs-gutter-x: 3.75rem;
  }
}

.product-single__media {
  display: flex;
  width: 100%;
  margin: 0 -0.3125rem;
  position: relative;
  flex-direction: column;
  margin-bottom: 3rem;
}

@media (min-width: 992px) {
  .product-single__media {
    flex-direction: row;
    margin-bottom: 0;
  }
}

.product-single__media .swiper-container {
  width: 100%;
  height: 100%;
}

.product-single__media .swiper-button-prev,
.product-single__media .swiper-button-next {
  width: 2.1875rem;
  height: 2.1875rem;
  background-color: #fff;
  border-radius: 2rem;
  font-size: 0.875rem;
  color: #222222;
}

.product-single__media .swiper-button-prev:hover,
.product-single__media .swiper-button-next:hover {
  background-color: #e4e4e4;
}

.product-single__media .swiper-button-prev:after,
.product-single__media .swiper-button-next:after {
  display: none;
}

@media (min-width: 576px) {

  .product-single__media .swiper-button-prev,
  .product-single__media .swiper-button-next {
    width: 2.8125rem;
    height: 2.8125rem;
  }
}

.product-single__media .swiper-button-prev {
  left: 1rem;
  z-index: 1;
}

@media (min-width: 576px) {
  .product-single__media .swiper-button-prev {
    left: 2rem;
  }
}

.product-single__media .swiper-button-next {
  right: 1rem;
  z-index: 1;
}

@media (min-width: 576px) {
  .product-single__media .swiper-button-next {
    right: 2rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image {
  flex: 0 0 85.7142%;
  max-width: 85.7142%;
}

@media (max-width: 991.98px) {
  .product-single__media.vertical-thumbnail .product-single__image {
    flex: 0 0 100%;
    max-width: 100%;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 0.3125rem;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a,
.product-single__media.vertical-thumbnail .product-single__image-item>button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a:hover,
.product-single__media.vertical-thumbnail .product-single__image-item>button:hover {
  background-color: #e4e4e4;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a svg,
.product-single__media.vertical-thumbnail .product-single__image-item>button svg {
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a,
  .product-single__media.vertical-thumbnail .product-single__image-item>button {
    width: 2.1875rem;
    height: 2.1875rem;
    right: 1rem;
    bottom: 1rem;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a svg,
  .product-single__media.vertical-thumbnail .product-single__image-item>button svg {
    width: 0.7775rem;
    height: 0.7775rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.view-video,
.product-single__media.vertical-thumbnail .product-single__image-item>button.view-video {
  bottom: 6rem;
  border: 0;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.view-video .flaticon,
.product-single__media.vertical-thumbnail .product-single__image-item>button.view-video .flaticon {
  font-size: 1rem;
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a.view-video,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.view-video {
    bottom: 4rem;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a.view-video .flaticon,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.view-video .flaticon {
    font-size: 0.75rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree,
.product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree {
  left: 1.875rem;
  top: 1.875rem;
  right: auto;
  bottom: auto;
  background-color: transparent;
  width: auto;
  height: auto;
  padding-top: 0.5rem;
  padding-right: 0.5rem;
}

.product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree .flaticon,
.product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree .flaticon {
  font-size: 2.5rem;
  pointer-events: none;
}

@media (max-width: 575.98px) {

  .product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree {
    left: 1rem;
    top: 1rem;
    right: auto;
    bottom: auto;
  }

  .product-single__media.vertical-thumbnail .product-single__image-item>a.product-degree .flaticon,
  .product-single__media.vertical-thumbnail .product-single__image-item>button.product-degree .flaticon {
    font-size: 1.5rem;
  }
}

.product-single__media.vertical-thumbnail .product-single__image img {
  width: 100%;
}

.product-single__media.vertical-thumbnail .product-single__thumbnail {
  flex: 0 0 100%;
  max-width: 1000%;
  order: 1;
}

@media (min-width: 992px) {
  .product-single__media.vertical-thumbnail .product-single__thumbnail {
    flex: 0 0 14.2857%;
    max-width: 14.2857%;
    order: -1;
  }
}

.product-single__media.vertical-thumbnail .product-single__thumbnail .swiper-slide {
  cursor: pointer;
  opacity: .5;
  border: 0;
}

.product-single__media.vertical-thumbnail .product-single__thumbnail .swiper-slide.swiper-slide-thumb-active {
  opacity: 1;
}

.product-single__media.horizontal-thumbnail {
  flex-direction: column;
}

.product-single__media.horizontal-thumbnail .product-single__image {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 0.3125rem;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a:hover {
  background-color: #e4e4e4;
}

.product-single__media.horizontal-thumbnail .product-single__image-item>a svg {
  pointer-events: none;
}

.product-single__media.horizontal-thumbnail .product-single__image img {
  width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail .swiper-slide {
  cursor: pointer;
  opacity: .5;
  border: 0;
}

.product-single__media.horizontal-thumbnail .product-single__thumbnail .swiper-slide.swiper-slide-thumb-active {
  opacity: 1;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot {
    padding-left: 5.375rem;
  }
}

.product-single__media.vertical-dot .product-single__image {
  flex: 0 0 100%;
  max-width: 100%;
  margin: 0;
  position: static;
}

.product-single__media.vertical-dot .product-single__image .swiper-container {
  position: static;
}

.product-single__media.vertical-dot .product-single__image .swiper-wrapper {
  margin-bottom: 1rem;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot .product-single__image .swiper-wrapper {
    margin-bottom: 0;
  }
}

.product-single__media.vertical-dot .product-single__image-item {
  position: relative;
  display: block !important;
  padding: 1rem;
}

@media (min-width: 576px) {
  .product-single__media.vertical-dot .product-single__image-item {
    padding: 10%;
  }
}

.product-single__media.vertical-dot .product-single__image-item>a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  right: 1.875rem;
  bottom: 1.875rem;
  border-radius: 2rem;
  background-color: #fff;
  transition: all .3s ease;
}

.product-single__media.vertical-dot .product-single__image-item>a:hover {
  background-color: #e4e4e4;
}

.product-single__media.vertical-dot .product-single__image img {
  width: 100%;
}

.product-single__media.vertical-dot .product-single__image .swiper-pagination {
  position: static;
  transform: none;
  flex-direction: row;
  justify-content: center;
  left: 0;
  top: 50%;
  display: flex;
  gap: 0.5rem;
  width: auto;
  bottom: auto;
}

@media (min-width: 992px) {
  .product-single__media.vertical-dot .product-single__image .swiper-pagination {
    position: absolute;
    transform: translateY(-50%);
    flex-direction: column;
  }
}

.product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet:first-child {
  margin-left: 4px;
}

.product-single__media .product-label {
  position: absolute;
  left: auto;
  right: 1rem;
  top: 1rem;
  width: 4.5625rem;
  height: 4.5625rem;
  border-radius: 3rem;
  background-color: #D6001C;
  color: #fff;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  text-transform: uppercase;
  padding: 0.5rem;
  text-align: center;
  line-height: 1.4;
  z-index: 1;
}

@media (min-width: 768px) {
  .product-single__media .product-label {
    right: -1.125rem;
    top: 1.875rem;
  }
}

.product-single__prev-next {
  gap: 1.875rem;
  display: none !important;
}

@media (min-width: 992px) {
  .product-single__prev-next {
    display: flex !important;
  }
}

.product-single__prev-next>a {
  display: flex;
  align-items: center;
  gap: 0.625rem;
}

.product-single__prev-next>a .flaticon {
  font-size: 0.75rem;
}

.product-single__prev-next>a.disabled {
  opacity: .5;
  pointer-events: none;
}

.product-single__name {
  font-size: 1.625rem;
}

.product-single__rating {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  margin-bottom: 0.625rem;
}

.product-single__price {
  font-size: 1.375rem;
  font-weight: 500;
  margin-bottom: 1.6875rem;
}

.product-single__price span.old-price {
  font-size: 1rem;
  color: #767676;
  font-weight: 400;
  text-decoration: line-through;
}

.product-single__price .special-price {
  color: #D6001C;
  margin-left: 0.5rem;
}

.product-single__short-desc {
  margin-bottom: 2.1875rem;
}

.product-single__addtocart {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 2.1875rem;
  flex-wrap: wrap;
}

.product-single__addtocart .qty-control {
  min-width: 7.25rem;
}

.product-single__addtocart .qty-control__number {
  border: 2px solid #E4E4E4;
  height: 3.75rem;
  padding: 0 2rem;
  min-width: 6.5rem;
}

.product-single__addtocart .qty-control__reduce,
.product-single__addtocart .qty-control__increase {
  font-size: 1rem;
  text-align: center;
  top: 50%;
  transform: translateY(-50%);
  width: 2rem;
}

.product-single__addtocart .qty-control__reduce {
  padding-left: 1.25rem;
}

.product-single__addtocart .qty-control__increase {
  padding-right: 1.25rem;
}

.product-single__addtocart .btn-addtocart {
  height: 3.75rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  width: 17.5rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
}

.product-single__addtocart .btn-addtocart.btn-outofstock {
  border: 2px solid #D6001C;
  color: #D6001C;
  background-color: #fff;
  cursor: default;
  pointer-events: none;
}

.product-single__addtocart.product-single__grouped {
  flex-direction: column;
  align-items: normal;
  gap: 0;
}

.product-single__addtocart.product-single__grouped .grouped-item {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  border-top: 1px solid #e4e4e4;
  padding: 1.25rem 0;
}

.product-single__addtocart.product-single__grouped .grouped-item:first-child {
  border-top: 0;
  padding-top: 0;
}

.product-single__addtocart.product-single__grouped .grouped-item__name {
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.product-single__addtocart.product-single__grouped .grouped-item__price {
  margin-left: auto;
  font-weight: 500;
}

.product-single__addtocart.product-single__grouped>div:not(.grouped-item) {
  margin-top: 1.2rem;
}

.product-single__addtolinks {
  font-size: 0.8125rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
}

.product-single__addtolinks>a,
.product-single__addtolinks>.share-button>button {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  padding: 0 0 0.625rem;
  text-transform: uppercase;
  border: 0;
  background-color: transparent;
  font-weight: 500;
}

.product-single__addtolinks>a:hover:after,
.product-single__addtolinks>.share-button>button:hover:after {
  width: 50%;
}

.product-single__addtolinks>a .flaticon,
.product-single__addtolinks>.share-button>button .flaticon {
  font-size: 1rem;
}

.product-single__addtolinks>.add-to-wishlist.active svg {
  color: #193174;
}

.product-single__meta-info {
  font-size: 0.8125rem;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.product-single__meta-info label {
  color: #767676;
  text-transform: uppercase;
}

.product-single__details-tab {
  margin: 6.25rem auto 2.375rem;
  max-width: 58.125rem;
}

.product-single__details-tab>.nav-tabs {
  justify-content: center;
  text-transform: uppercase;
}

@media (max-width: 575.98px) {
  .product-single__details-tab>.nav-tabs {
    flex-direction: column;
  }

  .product-single__details-tab>.nav-tabs .nav-link {
    width: max-content;
  }
}

.product-single__details-tab>.tab-content {
  padding: 3.125rem 0;
}

.product-single__description * {
  line-height: 1.875rem;
}

.product-single__addtional-info>.item {
  margin-bottom: 1.875rem;
}

.product-single__addtional-info>.item label {
  min-width: 8.75rem;
  margin: 0;
}

.product-single__reviews-title {
  font-size: 1.125rem;
  margin-bottom: 1.75rem;
}

.product-single__reviews-list {
  display: flex;
  flex-direction: column;
  gap: 1.87rem;
  margin-bottom: 2.375rem;
}

.product-single__reviews-item {
  display: flex;
  gap: 1.875rem;
  border-bottom: 1px solid #e4e4e4;
}

.product-single__reviews-item:last-child {
  border-bottom: 0;
}

.product-single__reviews-item .customer-avatar {
  flex: 0 0 3.75rem;
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 2rem;
  overflow: hidden;
}

.product-single__reviews-item .customer-avatar>img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.product-single__reviews-item .customer-review .customer-name {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.product-single__reviews-item .customer-review .customer-name>h6,
.product-single__reviews-item .customer-review .customer-name>.h6 {
  margin: 0;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
}

.product-single__reviews-item .customer-review .review-date {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.25rem;
}

.product-single__reviews-item .customer-review .review-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.5rem;
}

.product-single__review-form form>h5,
.product-single__review-form form>.h5 {
  font-size: 1.125rem;
  margin-bottom: 0.375rem;
}

.product-single__review-form form>p {
  font-size: 0.875rem;
  color: #767676;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.product-single__review-form form .select-star-rating {
  margin-bottom: 2rem;
}

.product-single__review-form form button {
  text-transform: uppercase;
  font-size: 0.875rem;
  min-width: 12.5rem;
}

.product-single__swatches .product-swatch {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 2.5rem;
  margin-bottom: 1.875rem;
}

@media (max-width: 1499.98px) {
  .product-single__swatches .product-swatch {
    gap: 1rem;
  }
}

.product-single__swatches .product-swatch>label {
  font-size: 0.875rem;
  font-weight: 500;
  min-width: 3rem;
  text-transform: uppercase;
}

.product-single__swatches .product-swatch .swatch-list {
  display: flex;
  align-items: center;
  gap: 0.625rem;
}

.product-single__swatches .product-swatch .swatch-list>input[type="radio"] {
  display: none;
}

.product-single__swatches .product-swatch .sizeguide-link {
  margin-left: auto;
  font-size: 0.8125rem;
  font-weight: 500;
  text-transform: uppercase;
  line-height: 1.875rem;
  position: relative;
}

@media (max-width: 1499.98px) {
  .product-single__swatches .product-swatch .sizeguide-link {
    margin-left: 0;
  }
}

.product-single__swatches .product-swatch .sizeguide-link:before {
  content: '';
  border-bottom: 2px solid;
  display: block;
  width: 0;
  transition: all .3s ease;
  position: absolute;
  left: 0;
  bottom: 0;
}

.product-single__swatches .product-swatch .sizeguide-link:hover:before {
  width: 100%;
}

.product-single__swatches .product-swatch .swatch {
  transition: all .3s ease;
}

.product-single__swatches .product-swatch.text-swatches .swatch {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 1.875rem;
  border: 1px solid #e4e4e4;
  padding: 0 0.8125rem;
}

.product-single__swatches .product-swatch.text-swatches .swatch.swatch_active,
.product-single__swatches .product-swatch.text-swatches .swatch:hover {
  border-color: #222222;
}

.product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches .swatch-color {
  margin: 0;
  border: 2px solid transparent;
}

.product-single__swatches .product-swatch.color-swatches .swatch-color.swatch_active,
.product-single__swatches .product-swatch.color-swatches .swatch-color:hover {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-color {
  border-color: #222222;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image {
  width: 3.875rem;
  height: 3.875rem;
  border: 1px solid transparent;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image.swatch_active,
.product-single__swatches .product-swatch.color-swatches .swatch-image:hover {
  border-color: #e4e4e4;
}

.product-single__swatches .product-swatch.color-swatches .swatch-image img {
  pointer-events: none;
}

.product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-image {
  border-color: #e4e4e4;
}

.product-single__additional-info {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  align-items: normal;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.product-single__additional-info>a {
  font-size: 0.8125rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  width: max-content;
}

.product-single__additional-info>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__additional-info>a:hover:before {
  width: 100%;
}

@media (min-width: 576px) {
  .product-single__additional-info {
    flex-direction: row;
    align-items: center;
    gap: 1.875rem;
  }
}

@media (min-width: 992px) {
  .product-single__additional-info {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }
}

@media (min-width: 1500px) {
  .product-single__additional-info {
    flex-direction: row;
    align-items: center;
    gap: 1.875rem;
  }
}

.product-single__type-2 .product-single__top-background {
  background-color: #e0e0e0;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch {
  border-color: #222222;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch:hover,
.product-single__type-2 .product-single__swatches .product-swatch.text-swatches .swatch.swatch_active {
  box-shadow: 0 0 0 1px inset #222222;
}

.product-single__type-2 .product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  box-shadow: 0 0 0 1px inset #222222;
  border-color: #222222;
}

.product-single__type-2 .product-single__addtocart .qty-control__number {
  border-color: #222222;
  background-color: transparent;
}

.product-single__type-3 .breadcrumb .menu-link {
  color: #767676;
}

.product-single__type-3 .breadcrumb .menu-link:hover {
  color: #767676;
}

.product-single__type-3 .product-single {
  color: #fff;
}

.product-single__type-3 .product-single__top-background {
  background-color: #222222;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image-item {
  padding: 0;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet:after {
  color: #fff;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet-active {
  border-color: #fff;
}

.product-single__type-3 .product-single__media.vertical-dot .product-single__image .swiper-pagination-bullet-active:after {
  color: #fff;
}

.product-single__type-3 .product-single__prev-next a,
.product-single__type-3 .product-single__prev-next .menu-link {
  color: #767676;
}

.product-single__type-3 .product-single__name {
  color: #fff;
}

.product-single__type-3 .product-single__rating .reviews-note {
  color: #fff !important;
}

.product-single__type-3 .product-single__price {
  color: #fff;
}

.product-single__type-3 .product-single__short-desc {
  color: #e4e4e4;
}

.product-single__type-3 .product-single__swatches label {
  color: #767676;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch {
  border-color: #fff;
  color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch:hover,
.product-single__type-3 .product-single__swatches .product-swatch.text-swatches .swatch.swatch_active {
  box-shadow: 0 0 0 1px inset #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.text-swatches input[type="radio"]:checked+label {
  box-shadow: 0 0 0 1px inset #fff;
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.color-swatches .swatch-color.swatch_active,
.product-single__type-3 .product-single__swatches .product-swatch.color-swatches .swatch-color:hover {
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch.color-swatches input[type="radio"]:checked+label.swatch-color {
  border-color: #fff;
}

.product-single__type-3 .product-single__swatches .product-swatch .sizeguide-link {
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .qty-control__number {
  background: transparent;
  border-color: #767676;
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .qty-control__reduce,
.product-single__type-3 .product-single__addtocart .qty-control__increase {
  color: #fff;
}

.product-single__type-3 .product-single__addtocart .btn-addtocart {
  background-color: #fff;
  color: #222222;
}

.product-single__type-3 .product-single__addtolinks>a {
  color: #fff;
}

.product-single__type-3 .product-single__meta-info label {
  color: #767676;
}

.product-single__type-3 .product-single__meta-info span {
  color: #fff;
}

.product-single__type-3 .product-single__additional-info>a {
  color: #fff;
}

.product-single__type-4 .product-single__media:before {
  content: '';
  height: 100%;
  width: 100vw;
  background-color: #e6e6e6;
  position: absolute;
  right: 0;
  z-index: -1;
}

@media (max-width: 991.98px) {
  .product-single__type-4 .product-single__media:before {
    right: -9.5rem;
    width: calc(100% + 19rem);
  }
}

.product-single__type-4 .product-single__image {
  width: 100%;
  position: relative;
  background-color: #e6e6e6;
}

.product-single__type-4 .product-single__image-item {
  padding-top: 6.25rem;
  height: 100vh;
  scroll-snap-align: center;
}

.product-single__type-4 .product-single__image-item img {
  height: 100%;
  width: 100%;
  object-fit: contain;
}

.product-single__type-5 {
  margin-bottom: 6.25rem;
}

.product-single__type-5 .product-single__image-item img {
  width: 100%;
}

.product-single__type-5 .product-single__swatches .product-swatch {
  gap: 0.5rem;
}

.product-single__type-5 .product-single__swatches .product-swatch>label {
  flex: 0 0 100%;
}

.product-single__type-5 .product-single__additional-info {
  flex-wrap: wrap;
  row-gap: 0.5rem;
}

.product-single__type-6 {
  margin-bottom: 6.25rem;
}

.product-single__type-7 {
  margin-bottom: 6.25rem;
}

.product-single__type-7 .product-single__media {
  margin-bottom: 1.25rem;
}

.product-single__type-7 .product-single__image {
  display: flex;
  flex-wrap: wrap;
  gap: 0.625rem;
}

.product-single__type-7 .product-single__image-item {
  flex: 0 0 calc(50% - 0.3125rem);
  max-width: calc(50% - 0.3125rem);
}

.product-single__type-7 .product-single__image-item:first-child {
  flex: 0 0 100%;
  max-width: 100%;
}

.product-single__type-7 .product-single__details {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 1.875rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.product-single__type-7 .product-single__details>a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  color: #767676;
  transition: all .3s ease;
  white-space: nowrap;
}

.product-single__type-7 .product-single__details>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__type-7 .product-single__details>a:hover {
  color: #222222;
}

.product-single__type-7 .product-single__details>a:hover:before {
  width: 100%;
}

@media (max-width: 575.98px) {
  .product-single__type-7 .product-single__details {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }

  .product-single__type-7 .product-single__details>a {
    width: max-content;
  }
}

.product-single__type-9 {
  margin-bottom: 6.25rem;
}

.product-single__type-9 .product-single__details {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 1.875rem;
  margin-bottom: 1rem;
}

.product-single__type-9 .product-single__details>a {
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  position: relative;
  line-height: 1.5rem;
  color: #767676;
  transition: all .3s ease;
}

.product-single__type-9 .product-single__details>a:before {
  content: '';
  display: block;
  border-bottom: 2px solid;
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 0;
  transition: all .3s ease;
}

.product-single__type-9 .product-single__details>a:hover {
  color: #222222;
}

.product-single__type-9 .product-single__details>a:hover:before {
  width: 100%;
}

@media (max-width: 575.98px) {
  .product-single__type-9 .product-single__details {
    flex-direction: column;
    align-items: normal;
    gap: 0.5rem;
  }

  .product-single__type-9 .product-single__details>a {
    width: max-content;
  }
}

.product-single__aside {
  width: 37.5rem;
  right: -37.5rem;
}

.product-single__aside .aside-content {
  height: calc(100% - 9rem);
  overflow-y: auto;
}

.product-single__details-accordion {
  margin-bottom: 6rem;
}

.product-single__details-accordion .accordion-item {
  margin-bottom: 1.25rem;
}

.product-single__details-accordion .accordion-button {
  text-transform: uppercase;
  border: 0;
  border-bottom: 1px solid #e4e4e4;
  padding: 0.625rem 0;
  color: #767676;
}

.product-single__details-accordion .accordion-collapse {
  border: 0;
}

.product-single__details-accordion .accordion-body {
  padding: 1.5rem 0;
}

.product-single__details-list {
  width: 65.3125rem;
  max-width: 100%;
  margin-top: 1.375rem;
}

.product-single__details-list__title {
  font-size: 1rem;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  margin-bottom: 3.4375rem;
}

.product-single__details-list__title:after {
  content: '';
  display: block;
  width: 2.5rem;
  border-bottom: 2px solid;
}

.product-single__details-list__content {
  padding-left: 7.1875rem;
  margin-bottom: 6.25rem;
}

@media (max-width: 575.98px) {
  .product-single__details-list__content {
    padding-left: 2.1875rem;
  }
}

.header_transparent~main {
  padding-top: 0 !important;
  overflow: hidden;
}

html.snap {
  scroll-snap-type: y mandatory;
  -webkit-overflow-scrolling: touch;
  scroll-snap-points-y: repeat(100%);
}

button.js-add-wishlist.active .flaticon.flaticon-heart,
a.add-to-wishlist.active .flaticon.flaticon-heart {
  color: #d6001c;
}

.quick-view {
  width: 73.125rem;
  max-width: calc(100% - 1rem);
}

.quick-view .product-single {
  display: flex;
  flex-wrap: wrap;
}

.quick-view .product-single__media {
  flex: 0 0 100%;
  max-width: 100%;
}

.quick-view .product-single__media img {
  width: 100%;
}

@media (min-width: 768px) {
  .quick-view .product-single__media {
    flex: 0 0 47%;
    max-width: 47%;
  }
}

.quick-view .product-single__detail {
  flex: 0 0 100%;
  max-width: 100%;
  padding: 1.875rem 1.25rem;
}

@media (min-width: 768px) {
  .quick-view .product-single__detail {
    flex: 0 0 53%;
    max-width: 53%;
    padding: 3.5rem 2.5rem;
  }
}

.quick-view .modal-content {
  overflow: hidden;
}

.quick-view .modal-content .btn-close {
  position: absolute;
  right: 0.75rem;
  top: 1rem;
}

.shop-checkout .page-title {
  font-size: 2.1875rem;
  margin-bottom: 3.125rem;
  text-transform: uppercase;
}

.shop-checkout .checkout-steps {
  display: flex;
  border-bottom: 2px solid #e4e4e4;
}

.shop-checkout .checkout-steps__item {
  flex-grow: 1;
  display: flex;
  gap: 0.75rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid transparent;
  margin-bottom: -2px;
}

.shop-checkout .checkout-steps__item-number {
  font-size: 1.125rem;
  font-weight: 500;
}

.shop-checkout .checkout-steps__item-title {
  display: flex;
  flex-direction: column;
}

.shop-checkout .checkout-steps__item-title>span {
  font-size: 1.125rem;
  font-weight: 500;
  text-transform: uppercase;
}

.shop-checkout .checkout-steps__item-title>em {
  font-size: 0.875rem;
  font-weight: 400;
  font-style: normal;
  color: #767676;
}

.shop-checkout .checkout-steps__item.active {
  border-color: #222222;
}

@media (max-width: 991.98px) {
  .shop-checkout .checkout-steps {
    border-bottom: 0;
    border-left: 2px solid #e4e4e4;
    flex-direction: column;
  }

  .shop-checkout .checkout-steps__item {
    border-left: 2px solid transparent;
    margin-left: -2px;
    border-bottom: 0;
    margin-bottom: 0;
    padding: 0.5rem 1rem;
  }
}

.shopping-cart {
  display: flex;
  flex-direction: column;
  gap: 3.625rem;
}

@media (min-width: 1200px) {
  .shopping-cart {
    flex-direction: row;
  }
}

.shopping-cart .cart-table__wrapper {
  padding-top: 3.125rem;
  flex-grow: 1;
}

.shopping-cart__totals-wrapper .sticky-content {
  padding-top: 3.125rem;
}

.shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .button-wrapper:not(.fixed-btn) {
  padding: 0;
}

.shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
  position: fixed;
  left: var(--bs-gutter-x, 0.9375rem);
  right: var(--bs-gutter-x, 0.9375rem);
  bottom: 4rem;
  width: auto;
}

@media (min-width: 768px) {
  .shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
    bottom: 1rem;
  }
}

@media (min-width: 992px) {
  .shopping-cart__totals-wrapper .mobile_fixed-btn_wrapper .fixed-btn {
    position: static;
  }
}

.shopping-cart__totals-wrapper .btn-checkout {
  width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

.shopping-cart__totals {
  border: 1px solid #222;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 0.5rem;
  max-width: 100%;
}

@media (min-width: 1200px) {
  .shopping-cart__totals {
    width: 26.25rem;
  }
}

.shopping-cart__totals>h3,
.shopping-cart__totals>.h3 {
  font-size: 1rem;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.shopping-cart__totals table {
  width: 100%;
}

.shopping-cart__totals table th,
.shopping-cart__totals table td {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.shopping-cart__totals table th {
  text-transform: uppercase;
  vertical-align: baseline;
}

.shopping-cart__totals table tr:last-child th,
.shopping-cart__totals table tr:last-child td {
  border-bottom: 0;
}

.shopping-cart .cart-table {
  width: 100%;
}

@media (min-width: 768px) {

  .shopping-cart .cart-table th,
  .shopping-cart .cart-table td {
    border-bottom: 1px solid #e4e4e4;
  }
}

.shopping-cart .cart-table thead {
  display: none;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table thead {
    display: table-header-group;
  }
}

.shopping-cart .cart-table thead th {
  font-size: 0.875rem;
  text-transform: uppercase;
  font-weight: 500;
  padding: 0 0 0.625rem;
}

.shopping-cart .cart-table tbody tr {
  position: relative;
  display: block;
  padding: 1.25rem 0;
  border-bottom: 1px solid #e4e4e4;
  transition: all .3s ease;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr {
    display: table-row;
    padding: 0;
    border: 0;
  }
}

.shopping-cart .cart-table tbody tr:first-child {
  border-top: 1px solid #e4e4e4;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr:first-child {
    border: 0;
  }
}

.shopping-cart .cart-table tbody tr:after {
  content: '';
  display: block;
  clear: both;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody tr:after {
    display: none;
  }
}

.shopping-cart .cart-table tbody tr td {
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
}

.shopping-cart .cart-table tbody tr td>* {
  transition: all 0.32s cubic-bezier(0.39, 0.575, 0.565, 1);
  overflow: hidden;
  max-height: 12rem;
}

.shopping-cart .cart-table tbody tr._removed td {
  padding-top: 0;
  padding-bottom: 0;
}

.shopping-cart .cart-table tbody tr._removed td>* {
  max-height: 0;
}

.shopping-cart .cart-table tbody td {
  display: block;
  margin-left: 9.375rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td {
    padding: 1.875rem 0;
    display: table-cell;
    margin: 0;
  }
}

.shopping-cart .cart-table tbody td:first-child {
  width: 9.375rem;
  float: left;
  margin-left: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td:first-child {
    float: none;
  }
}

.shopping-cart .cart-table tbody td .shopping-cart__product-price {
  display: none;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .shopping-cart__product-price {
    display: block;
  }
}

.shopping-cart .cart-table tbody td .shopping-cart__subtotal {
  float: right;
  display: block;
  margin-top: -2.2rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .shopping-cart__subtotal {
    float: none;
    margin: 0;
  }
}

.shopping-cart .cart-table tbody td .remove-cart {
  position: absolute;
  right: 0;
  top: 1rem;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table tbody td .remove-cart {
    position: static;
  }
}

.shopping-cart .cart-table .qty-control {
  margin: 0.5rem 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control {
    width: 7.25rem;
    margin: 0;
  }
}

.shopping-cart .cart-table .qty-control__number {
  border: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__number {
    border: 2px solid #e4e4e4;
    height: 3.125rem;
    padding: 0 2rem;
    min-width: 6.875rem;
  }
}

.shopping-cart .cart-table .qty-control__reduce,
.shopping-cart .cart-table .qty-control__increase {
  font-size: 1rem;
  text-align: center;
  top: 50%;
  transform: translateY(-50%);
}

.shopping-cart .cart-table .qty-control__reduce {
  left: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__reduce {
    left: 1.25rem;
  }
}

.shopping-cart .cart-table .qty-control__increase {
  right: 0;
}

@media (min-width: 768px) {
  .shopping-cart .cart-table .qty-control__increase {
    right: 1.25rem;
  }
}

.shopping-cart .cart-table-footer {
  display: flex;
  justify-content: space-between;
  padding-top: 1.875rem;
  gap: 1.875rem;
  flex-wrap: wrap;
}

.shopping-cart .cart-table-footer form {
  max-width: 100%;
}

.shopping-cart .cart-table-footer .form-control {
  width: 23.125rem;
  max-width: 100%;
  height: 3.875rem;
}

.shopping-cart .cart-table-footer button {
  height: 3.875rem;
}

.shopping-cart__product-item {
  display: flex;
  align-items: center;
  gap: 1.875rem;
}

.shopping-cart__product-item img {
  width: 7.5rem;
  height: auto;
}

.shopping-cart__product-item__detail h4,
.shopping-cart__product-item__detail .h4 {
  font-size: 1rem;
  font-weight: 400;
  margin-bottom: 0;
}

.shopping-cart__product-item__options {
  list-style: none;
  padding: 0;
  margin: 0;
  margin-top: 0.5rem;
}

.shopping-cart__product-item__options li {
  font-size: 0.875rem;
  color: #767676;
}

.shopping-cart__product-price {
  font-size: 1rem;
  color: #767676;
}

.shopping-cart__subtotal {
  font-size: 1rem;
  font-weight: 500;
}

.checkout-form {
  display: flex;
  gap: 3.625rem;
}

@media (max-width: 1199.98px) {
  .checkout-form {
    flex-direction: column;
  }
}

.checkout-form .billing-info__wrapper {
  padding-top: 3.125rem;
  flex-grow: 1;
}

.checkout-form .billing-info__wrapper .form-floating>label,
.checkout-form .billing-info__wrapper .form-label-fixed>.form-label {
  color: #767676;
}

.checkout-form .checkout__totals-wrapper .sticky-content {
  padding-top: 3.125rem;
}

.checkout-form .checkout__totals-wrapper .btn-checkout {
  width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

.checkout-form .checkout__payment-methods {
  border: 1px solid #e4e4e4;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 1.5rem;
  width: 26.25rem;
}

@media (max-width: 1199.98px) {
  .checkout-form .checkout__payment-methods {
    width: 100%;
  }
}

.checkout-form .checkout__payment-methods label {
  font-size: 1rem;
  line-height: 1.5rem;
}

.checkout-form .checkout__payment-methods label .option-detail {
  font-size: 0.875rem;
  margin: 0.625rem 0 0;
  display: none;
}

.checkout-form .checkout__payment-methods .form-check-input:checked~label .option-detail {
  display: block;
}

.checkout-form .checkout__payment-methods .policy-text {
  font-size: 0.75rem;
  line-height: 1.5rem;
}

.checkout-form .checkout__payment-methods .policy-text>a {
  color: #c32929;
}

.checkout__totals {
  border: 1px solid #222;
  margin-bottom: 1.25rem;
  padding: 2.5rem 2.5rem 0.5rem;
  width: 26.25rem;
}

@media (max-width: 1199.98px) {
  .checkout__totals {
    width: 100%;
  }
}

.checkout__totals>h3,
.checkout__totals>.h3 {
  font-size: 1rem;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}

.checkout__totals table {
  width: 100%;
}

.checkout__totals .checkout-cart-items thead th {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.checkout__totals .checkout-cart-items tbody td {
  padding: 0.40625rem 0;
  color: #767676;
}

.checkout__totals .checkout-cart-items tbody tr:first-child td {
  padding-top: 0.8125rem;
}

.checkout__totals .checkout-cart-items tbody tr:last-child td {
  padding-bottom: 0.8125rem;
  border-bottom: 1px solid #e4e4e4;
}

.checkout__totals .checkout-totals th,
.checkout__totals .checkout-totals td {
  border-bottom: 1px solid #e4e4e4;
  padding: 0.875rem 0;
  font-size: 0.875rem;
  font-weight: 500;
}

.checkout__totals .checkout-totals tr:last-child th,
.checkout__totals .checkout-totals tr:last-child td {
  border-bottom: 0;
}

.order-complete {
  width: 56.25rem;
  max-width: 100%;
  margin: 3.125rem auto;
  display: flex;
  flex-direction: column;
  gap: 2.25rem;
}

.order-complete__message {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.order-complete__message svg {
  margin-bottom: 1.25rem;
}

.order-complete__message h3,
.order-complete__message .h3 {
  font-size: 2.1875rem;
  text-align: center;
}

.order-complete__message p {
  color: #767676;
  margin-bottom: 0;
  text-align: center;
}

.order-complete .order-info {
  width: 100%;
  border: 2px dashed #767676;
  padding: 2.5rem;
  display: flex;
  gap: 1rem;
}

@media (max-width: 767.98px) {
  .order-complete .order-info {
    flex-direction: column;
  }
}

.order-complete .order-info__item {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex-grow: 1;
}

.order-complete .order-info__item label {
  font-size: 0.875rem;
  font-weight: 400;
  color: #767676;
}

.order-complete .order-info__item span {
  font-size: 1rem;
  font-weight: 500;
}

.order-complete .checkout__totals {
  width: 100%;
}

.order-complete .checkout__totals .checkout-cart-items thead th:last-child {
  text-align: right;
}

.order-tracking {
  width: 31.25rem;
  max-width: 100%;
  margin: 0 auto;
  text-align: center;
}

.order-tracking .btn-track {
  height: 3.75rem;
  font-size: 0.875rem;
}

.my-account .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
}

.my-account .account-nav {
  list-style: none;
  padding: 0;
  padding-top: 2.5rem;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  text-transform: uppercase;
  font-size: 0.875rem;
  font-weight: 500;
}

.my-account .account-nav .menu-link.menu-link_active {
  pointer-events: none;
  color: #c32929;
}

.my-account .page-content {
  padding-top: 2.5rem;
}

.my-account__dashboard p {
  width: 43.125rem;
  max-width: 100%;
}

.my-account__dashboard .unerline-link {
  text-decoration: underline;
}

.my-account__orders-list {
  overflow-x: auto;
  width: 100%;
}

.my-account .orders-table {
  border: 1px solid #e4e4e4;
  width: 100%;
}

.my-account .orders-table thead th {
  background-color: #e4e4e4;
  padding: 1rem 1.875rem;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.my-account .orders-table tbody td {
  border-top: 1px solid #e4e4e4;
  padding: 1.875rem;
}

.my-account .orders-table tbody td:first-child {
  text-decoration: underline;
}

.my-account .orders-table tbody td:last-child {
  width: 12.5rem;
}

.my-account .orders-table tbody td .btn {
  height: 3.125rem;
  font-size: 0.875rem;
}

.my-account__address .notice {
  margin-bottom: 3.75rem;
}

.my-account__address-list {
  display: flex;
  gap: 5.625rem;
}

@media (max-width: 767.98px) {
  .my-account__address-list {
    flex-direction: column;
  }
}

.my-account__address-item {
  flex-grow: 1;
}

.my-account__address-item__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  line-height: 1.5rem;
  text-transform: uppercase;
  margin-bottom: 0.875rem;
  font-weight: 500;
}

.my-account__address-item__title h5,
.my-account__address-item__title .h5 {
  font-size: 1.125rem;
  margin: 0;
}

.my-account__address-item__title a {
  font-size: 0.8125rem;
  border-bottom: 2px solid;
}

.my-account__address-item__detail {
  line-height: 1.5rem;
}

.my-account__address-item__detail p {
  margin: 0;
}

.my-account__edit .btn-primary {
  width: 18.75rem;
  height: 3.75rem;
  max-width: 100%;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.my-account__wishlist .btn-remove-from-wishlist {
  position: absolute;
  left: 1.25rem;
  top: 1.25rem;
  z-index: 2;
  border: 0;
  background-color: #fff;
  width: 2.5rem;
  height: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 4px;
  transition: all .3s ease;
  box-shadow: 0 0 1px rgba(0, 0, 0, 0.1);
  opacity: 0;
  visibility: hidden;
}

.my-account__wishlist .product-card:hover .btn-remove-from-wishlist {
  opacity: 1;
  visibility: visible;
}

.blog-page-title {
  width: 112.5rem;
  height: 16rem;
  max-width: calc(100% - 1.875rem);
  border: 2px solid #e4e4e4;
  margin: 0 auto;
  background-size: cover;
  position: relative;
  display: flex;
  align-items: center;
  padding: 1.25rem;
}

.blog-page-title .page-title {
  font-size: calc(1.5rem + 3vw);
  font-weight: 700;
  text-transform: uppercase;
}

@media (min-width: 1200px) {
  .blog-page-title .page-title {
    font-size: 3.75rem;
  }
}

.blog-page-title .title-bg {
  display: block;
  position: absolute;
  left: 0.5rem;
  right: 0.5rem;
  top: 0.5rem;
  bottom: 0.5rem;
  z-index: -1;
}

.blog-page-title .title-bg img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

@media (min-width: 576px) {
  .blog-page-title {
    height: 27.5rem;
    padding: 0;
  }
}

.blog-page .flaticon {
  font-size: 0.625rem;
}

.blog__filter {
  display: flex;
  gap: 1rem;
  row-gap: 0;
  flex-wrap: wrap;
}

.blog__filter>a {
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: 500;
}

.blog-grid__item {
  margin-bottom: 2.75rem;
}

.blog-grid__item-image {
  margin-bottom: 1.25rem;
}

.blog-grid__item-image img {
  display: block;
  width: 100%;
}

.blog-grid__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 0.25rem;
  white-space: nowrap;
}

.blog-grid__item-title {
  font-size: 1.625rem;
  margin-bottom: 1.875rem;
  line-height: 1.5;
}

@media (max-width: 991.98px) {
  .blog-grid__item-title {
    font-size: 1.125rem;
    margin-bottom: 1.25rem;
  }
}

.blog-grid__item-content p {
  margin-bottom: 0.625rem;
}

.blog-grid__item-content .readmore-link {
  text-transform: uppercase;
  position: relative;
  display: inline-block;
  font-weight: 500;
}

.blog-grid__item-content .readmore-link:after {
  content: '';
  display: block;
  width: 70%;
  border-bottom: 2px solid;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.blog-grid__item-content .readmore-link:hover:after {
  width: 100%;
}

.blog-grid.row-cols-xl-3 .blog-grid__item-title {
  font-size: 1.125rem;
  margin-bottom: 1.25rem;
}

.blog-list {
  margin-bottom: 3.125rem;
}

@media (min-width: 992px) {
  .blog-list {
    margin-bottom: 6.25rem;
  }
}

.blog-list__item {
  margin-bottom: 1.875rem;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 1.25rem;
}

@media (min-width: 992px) {
  .blog-list__item {
    flex-direction: row;
    align-items: center;
    gap: 3.125rem;
  }
}

.blog-list__item-image {
  flex: 0 0 100%;
  width: 100%;
}

@media (min-width: 992px) {
  .blog-list__item-image {
    flex: 0 0 calc(50% - 1.5625rem);
  }
}

.blog-list__item-image img {
  display: block;
  width: 100%;
}

.blog-list__item-detail {
  flex: 0 0 100%;
  padding: 0;
}

@media (min-width: 992px) {
  .blog-list__item-detail {
    flex: 0 0 calc(50% - 1.5625rem);
    padding: 1.875rem 0;
  }
}

.blog-list__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 0.25rem;
}

.blog-list__item-title {
  font-size: 1.125rem;
  margin-bottom: 1.25rem;
  line-height: 1.5;
}

@media (min-width: 992px) {
  .blog-list__item-title {
    font-size: 1.625rem;
    margin-bottom: 1.875rem;
  }
}

.blog-list__item-content p {
  margin-bottom: 0.625rem;
}

.blog-list__item-content .readmore-link {
  text-transform: uppercase;
  position: relative;
  display: inline-block;
  font-weight: 500;
}

.blog-list__item-content .readmore-link:after {
  content: '';
  display: block;
  width: 70%;
  border-bottom: 2px solid;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.blog-list__item-content .readmore-link:hover:after {
  width: 100%;
}

.blog-single .page-title {
  margin-bottom: 0.875rem;
}

.blog-single__reviews-title {
  font-size: 1.125rem;
  margin-bottom: 1.75rem;
}

.blog-single__reviews-list {
  display: flex;
  flex-direction: column;
  gap: 1.87rem;
  margin-bottom: 2.375rem;
}

.blog-single__reviews-item {
  display: flex;
  gap: 1.875rem;
  border-bottom: 1px solid #e4e4e4;
}

.blog-single__reviews-item:last-child {
  border-bottom: 0;
}

.blog-single__reviews-item .customer-avatar {
  flex: 0 0 3.75rem;
  width: 3.75rem;
  height: 3.75rem;
  border-radius: 2rem;
  overflow: hidden;
}

.blog-single__reviews-item .customer-avatar>img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.blog-single__reviews-item .customer-review .customer-name {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.blog-single__reviews-item .customer-review .customer-name>h6,
.blog-single__reviews-item .customer-review .customer-name>.h6 {
  margin: 0;
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
}

.blog-single__reviews-item .customer-review .review-date {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.25rem;
}

.blog-single__reviews-item .customer-review .review-text {
  font-size: 0.875rem;
  font-weight: 400;
  line-height: 1.5rem;
  color: #767676;
  margin-bottom: 1.5rem;
}

.blog-single__review-form form>h5,
.blog-single__review-form form>.h5 {
  font-size: 1.125rem;
  margin-bottom: 0.375rem;
}

.blog-single__review-form form>p {
  font-size: 0.875rem;
  color: #767676;
  line-height: 1.5rem;
  margin-bottom: 1.875rem;
}

.blog-single__review-form form .select-star-rating {
  margin-bottom: 2rem;
}

.blog-single__review-form form button {
  text-transform: uppercase;
  font-size: 0.875rem;
  min-width: 12.5rem;
  height: 3.75rem;
}

.blog-single__item-meta {
  display: flex;
  gap: 1.5rem;
  text-transform: uppercase;
  color: #767676;
  margin-bottom: 2.625rem;
}

.blog-single__item-pagination {
  padding-top: 2.8125rem;
  border-top: 1px solid #e4e4e4;
  border-bottom: 1px solid #e4e4e4;
  margin-bottom: 3.125rem;
}

.blog-single__item-pagination p {
  margin-bottom: 2.625rem !important;
}

.blog-single__item-pagination a {
  color: #767676;
}

.blog-single p {
  margin-bottom: 1.875rem;
}

.blog-single p img {
  margin-bottom: 3.25rem;
}

.blog-single h5,
.blog-single .h5 {
  margin-bottom: 1.875rem;
}

.blog-single .text-list {
  margin-bottom: 1.875rem;
}

.blog-single .text-list__item {
  line-height: 1.875rem;
}

.blog-single__item-share {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 3.125rem;
  flex-direction: column;
}

@media (min-width: 992px) {
  .blog-single__item-share {
    flex-direction: row;
  }
}

.blog-single .btn-share {
  width: 13.75rem;
  height: 3.125rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.875rem;
  color: #fff;
  padding: 0;
}

.blog-single .btn-share.btn-facebook {
  background-color: #306199;
}

.blog-single .btn-share.btn-twitter {
  background-color: #26C4F1;
}

.blog-single .btn-share.btn-pinterest {
  background-color: #E82B2D;
}

.blog-single .btn-share.btn-more {
  background-color: #222222;
  font-size: 1.5625rem;
  padding: 0;
  width: 3.125rem;
}

.about-us .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.about-us__content {
  line-height: 1.875rem;
}

.brands-carousel .swiper-slide {
  display: flex;
  align-items: center;
  justify-content: center;
}

.google-map__wrapper {
  height: 34.375rem;
  position: relative;
}

.google-map__wrapper>div {
  height: 100%;
}

.google-map__marker-detail {
  position: absolute;
  left: 10rem;
  top: 50%;
  transform: translateY(-50%);
  padding: 1.6875rem 1.875rem 1.25rem;
  width: auto;
  height: auto !important;
  background-color: #fff;
  border-radius: 4px;
  transition: all .3s ease;
}

@media (max-width: 767.98px) {
  .google-map__marker-detail {
    display: none;
  }
}

.google-map__marker-detail.hide {
  opacity: 0;
  visibility: hidden;
}

.google-map__marker-detail .btn-close {
  background: none;
  padding: 0;
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
}

.google-map__marker-detail__content a {
  display: none;
}

.contact-us .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.contact-us__form input.form-control {
  height: 3.4375rem;
}

.contact-us__form .btn {
  min-width: 12.5rem;
  height: 3.75rem;
  text-transform: uppercase;
  font-size: 0.875rem;
}

.lookbook .page-title {
  font-size: calc(1.34375rem + 1.125vw);
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

@media (min-width: 1200px) {
  .lookbook .page-title {
    font-size: 2.1875rem;
  }
}

.lookbook-collection__item {
  display: block;
  padding-top: 57.68%;
}

.lookbook-collection__item.size-lg {
  padding-top: 119.7%;
}

.lookbook-collection__item-image {
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
}

.lookbook-collection__item-image img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.popover-point {
  padding: 1rem;
  border: 0;
  background-color: transparent;
}

.popover-point>span {
  display: block;
  width: 1.5rem;
  height: 1.5rem;
  border: 0.3rem solid #fff;
  background-color: #b9a16b;
  border-radius: 1rem;
}

.popover-point.type2 {
  padding: 0.2rem;
}

@media (min-width: 768px) {
  .popover-point.type2 {
    padding: 1rem;
  }
}

.popover-point.type2>span {
  background-color: #ffffff;
  border-radius: 3rem;
  border: 0;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 0.625rem;
  height: 0.625rem;
  box-shadow: 0 0 0 0.2625rem rgba(255, 255, 255, 0.3);
  font-size: 0.5625rem;
  padding-bottom: 0.05rem;
}

@media (min-width: 768px) {
  .popover-point.type2>span {
    width: 2.625rem;
    height: 2.625rem;
    box-shadow: 0 0 0 0.5625rem rgba(255, 255, 255, 0.3);
    font-size: 1.5625rem;
    padding-bottom: 0.2rem;
  }
}

.popover-point.type3 {
  padding: 0.2rem;
}

@media (min-width: 768px) {
  .popover-point.type3 {
    padding: 1rem;
  }
}

.popover-point.type3>span {
  background-color: #ffffff;
  border-radius: 3rem;
  border: 0;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 0.625rem;
  height: 0.625rem;
  box-shadow: 0 0 0 0.2625rem rgba(255, 255, 255, 0.3);
  font-size: 0.5625rem;
  padding-bottom: 0.05rem;
}

@media (min-width: 768px) {
  .popover-point.type3>span {
    width: 1.75rem;
    height: 1.75rem;
    box-shadow: 0 0 0 0.375rem rgba(255, 255, 255, 0.3);
    font-size: 1.5625rem;
    padding-bottom: 0.2rem;
  }
}

.lookbook-products>h2,
.lookbook-products>.h2 {
  pointer-events: none;
}

.store-location .page-title {
  font-size: 2.1875rem;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 2.5rem;
}

.store-location__search {
  position: relative;
  width: 100%;
}

.store-location__search-input {
  padding: 1.25rem 3.875rem 1rem 1.25rem;
  height: 3.75rem;
  border: 1px solid #e4e4e4;
  font-size: 0.875rem;
  width: 100%;
}

.store-location__search-btn {
  position: absolute;
  right: 1.25rem;
  top: 50%;
  transform: translateY(-50%);
  padding: 0;
}

.store-location__search-result__item {
  padding: 1.875rem 0;
  border-top: 1px solid #e4e4e4;
}

.store-location__search-result__item:first-child {
  border-top: 0;
}

.store-location__search-result__item h5,
.store-location__search-result__item .h5 {
  margin-bottom: 0.8125rem;
}

.store-location__search-result__item a {
  font-size: 0.8125rem;
  line-height: 1.5rem;
  display: inline-block;
  position: relative;
  text-transform: uppercase;
  font-weight: 500;
}

.store-location__search-result__item a:after {
  content: '';
  display: block;
  border-bottom: 2px solid;
  width: 0;
  position: absolute;
  bottom: -2px;
  left: 0;
  transition: all .3s ease;
}

.store-location__search-result__item a:hover:after {
  width: 75%;
}

.store-location .google-map__wrapper {
  height: 46.875rem;
  max-height: 100vh;
}

.login-register {
  width: 40.625rem;
  max-width: 100%;
  padding: 0 4.6875rem;
}

@media (max-width: 767.98px) {
  .login-register {
    padding: 0 1rem;
  }
}

.login-register .nav-tabs {
  justify-content: center;
  text-transform: uppercase;
}

.login-register .btn {
  font-size: 0.875rem;
  height: 3.75rem;
  font-weight: 500;
}

.login-register p {
  color: #767676;
}

body.not-found-page {
  background: url(../../images/pattern_bg.png) center no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

body.not-found-page .header {
  background: transparent;
}

.page-not-found {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5rem;
}

.page-not-found .content {
  width: 31.25rem;
  max-width: 100%;
  text-align: center;
}

.page-not-found .content h2,
.page-not-found .content .h2 {
  font-size: calc(1.75rem + 6vw);
  font-weight: 700;
}

@media (min-width: 1200px) {

  .page-not-found .content h2,
  .page-not-found .content .h2 {
    font-size: 6.25rem;
  }
}

.page-not-found .content .btn {
  width: 21.25rem;
  max-width: 100%;
  height: 3.75rem;
  font-size: 0.875rem;
}

body.coming-soon-page {
  background: url(../../images/pattern_bg.png) center no-repeat;
  background-size: cover;
  background-attachment: fixed;
}

body.coming-soon-page .header {
  background: transparent;
}

.coming-soon {
  position: absolute;
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 5rem;
}

.coming-soon .content {
  width: 46.875rem;
  max-width: 100%;
  text-align: center;
}

.coming-soon .content h2,
.coming-soon .content .h2 {
  font-size: calc(1.75rem + 6vw);
  font-weight: 700;
  letter-spacing: -0.05em;
}

@media (min-width: 1200px) {

  .coming-soon .content h2,
  .coming-soon .content .h2 {
    font-size: 6.25rem;
  }
}

.coming-soon .content p {
  width: 29.75rem;
  max-width: 100%;
  margin: 0 auto;
}

.coming-soon .js-countdown {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

@media (min-width: 768px) {
  .coming-soon .js-countdown {
    gap: 3.625rem;
  }
}

.coming-soon .js-countdown .countdown-num {
  font-size: 1.875rem;
}

.coming-soon .js-countdown .countdown-word {
  font-size: 1rem;
}

.coming-soon .js-countdown .countdown-unit {
  position: relative;
  min-width: 3.625rem;
}

.coming-soon .js-countdown .countdown-unit:before {
  content: ':';
  display: block;
  position: absolute;
  font-size: 1.875rem;
  left: -1rem;
}

@media (min-width: 768px) {
  .coming-soon .js-countdown .countdown-unit:before {
    left: -2rem;
  }
}

.coming-soon .js-countdown .countdown-unit:first-child:before {
  display: none;
}

.coming-soon .block-newsletter .block-newsletter__form {
  height: 3.75rem;
}

.coming-soon .block-newsletter .block-newsletter__form button {
  font-weight: 400;
  font-size: 0.875rem;
}

.image-banner {
  position: relative;
  min-height: 18.75rem;
  display: flex;
  align-items: center;
}

@media (min-width: 576px) {
  .image-banner {
    min-height: 30rem;
  }
}

@media (min-width: 992px) {
  .image-banner {
    min-height: 43.75rem;
  }
}

.image-banner__content {
  position: relative;
  z-index: 1;
  text-align: center;
}

.image-banner__content h2,
.image-banner__content .h2 {
  font-size: calc(1.5rem + 3vw);
  font-weight: 700;
  text-transform: uppercase;
}

@media (min-width: 1200px) {

  .image-banner__content h2,
  .image-banner__content .h2 {
    font-size: 3.75rem;
  }
}

.category-banner__item {
  position: relative;
}

.category-banner__item-content {
  position: absolute;
  left: 12.2%;
  right: 12.2%;
  bottom: -2.3125rem;
  background-color: white;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 1.5rem 2rem;
}

@media (min-width: 1200px) {
  .category-banner__item-content {
    padding: 2.6875rem 2rem 1.625rem;
  }
}

.category-banner__item-content h2,
.category-banner__item-content .h2 {
  margin: 0;
}

.category-banner__item-mark {
  background: #d6001c;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  text-transform: uppercase;
  color: #fff;
  padding: 0.75rem 1rem 0.5rem;
  text-align: center;
  line-height: 1.5;
  position: absolute;
  font-size: 0.9375rem;
  width: 6.25rem;
  height: 6.25rem;
  border-radius: 6.25rem;
  right: 1.875rem;
  top: 1.875rem;
}

.category-masonry__title {
  font-size: calc(1.4375rem + 2.25vw);
  line-height: 1.5;
}

@media (min-width: 1200px) {
  .category-masonry__title {
    font-size: 3.125rem;
  }
}

.category-masonry__item {
  position: relative;
}

.category-masonry__item-category {
  position: absolute;
  left: 0;
  top: 0;
  transform: rotate(-90deg) translate(-100%, -100%);
  transform-origin: left top;
}

.video-banner {
  height: 100vh;
  max-height: 43.75rem;
}

.video-banner:before {
  content: '';
  display: block;
  width: 100%;
  height: 100%;
  position: absolute;
  left: 0;
  top: 0;
  background-color: rgba(0, 0, 0, 0.5);
}

.btn-video-player {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.5rem;
  height: 2.5rem;
  border: 0.125rem solid;
  border-radius: 4rem;
  padding-left: 0.125rem;
  transition: all .3s ease;
  background-color: transparent;
}

.btn-video-player:hover {
  background-color: rgba(0, 0, 0, 0.2);
}

.btn-video-player .flaticon {
  font-size: 1rem;
}

@media (min-width: 768px) {
  .btn-video-player {
    width: 4.375rem;
    height: 4.375rem;
    border: 0.25rem solid;
    padding-left: 0.25rem;
  }

  .btn-video-player .flaticon {
    font-size: 1.25rem;
  }
}

.btn-video-player svg {
  display: block;
}

.btn-video-player svg.btn-pause {
  display: none;
}

.btn-video-player svg.btn-play {
  margin-left: 0.3rem;
}

.btn-video-player.playing svg.btn-play {
  display: none;
}

.btn-video-player.playing svg.btn-pause {
  display: block;
}

/* Style the custom dropdown container */
.custom-dropdown {
  position: relative;
  display: inline-block;
  z-index: 3; /* Set a higher z-index to ensure it appears above other elements */
  text-align: center; /* Center the content horizontally */
}

/* Style the selected option */
.selected-option {
  display: inline-block;
  padding: 15px 15px; /* Adjust the padding as needed */
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 1px;
  cursor: pointer;
  font-size: 14px; /* Adjust the font size as needed */
  white-space: nowrap; /* Prevent text wrapping */
  height: 35px; /* Set a fixed height to maintain consistency */
  line-height: 5px; /* Adjust line-height for vertical centering */
  width: 140px;
}


/* Style the dropdown list */
.dropdown-list {
  list-style: none;
  font-size: 13px; /* Adjust the font size as needed */
  padding: 15px;
  margin: 0;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: white;
  border: 1px solid #ccc;
  border-top: none;
  border-radius: 0 0 1px 1px;
  display: none;
}

/* Style the dropdown list items */
.dropdown-list li {
  padding: 1px;
  cursor: pointer;
}

/* Add a hover effect to the dropdown list items */
.dropdown-list li:hover {
  background-color: #f0f0f0;
}

/* Show the dropdown list on hover */
.custom-dropdown:hover .dropdown-list {
  display: block;
}

/* Brands */
.text-above-image {
  position: relative;
  z-index: 2;
}

.brandimage {
  position: relative;
  z-index: 1;
}

.large-heading {
  font-size: 36px; /* Adjust the font size as needed */
  display: inline;
}

.vision-heading {
  display: inline;
}

.image-container {
  flex-shrink: 0;
  width: 200px; /* Adjust the width of the image container as needed */
}

.section-image {
  max-width: 100%;
  height: auto;
}"""

# Find the differences
difference1, difference2 = find_difference(css_block1, css_block2)

# Output the differences
print("Lines in CSS block 1 but not in CSS block 2:")
for line in difference1:
    print(line)

print("\nLines in CSS block 2 but not in CSS block 1:")
for line in difference2:
    print(line)