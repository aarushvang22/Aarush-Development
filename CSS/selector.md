## 🎯 CSS Selectors and Their Symbols

### 1. **`.` (Dot) — Class Selector**

* Selects all elements with a specific `class` attribute.

#### Example:

```html
<div class="box"></div>
```

```css
.box {
  background-color: lightblue;
}
```

✅ Targets all elements with `class="box"`.

---

### 2. **`#` (Hash) — ID Selector**

* Selects the **one element** with a specific `id`.

#### Example:

```html
<div id="main-banner"></div>
```

```css
#main-banner {
  background-color: yellow;
}
```

✅ Targets the element with `id="main-banner"`.

---

### 3. **`*` — Universal Selector**

* Selects **all elements** on the page.

#### Example:

```css
* {
  margin: 0;
  padding: 0;
}
```

✅ Useful for resetting default styles.

---

### 4. **Element Selector (no symbol)**

* Targets all HTML elements of a certain type.

#### Example:

```css
p {
  font-size: 16px;
}
```

✅ Targets all `<p>` elements.

---

### 5. **`element1, element2` — Group Selector**

* Applies the same styles to multiple selectors.

#### Example:

```css
h1, h2, p {
  color: navy;
}
```

✅ Styles all `<h1>`, `<h2>`, and `<p>` tags the same way.

---

### 6. **`element1 element2` — Descendant Selector**

* Targets `element2` **inside** `element1`.

#### Example:

```css
div p {
  color: green;
}
```

✅ Styles only `<p>` tags **inside a `<div>`**.

---

### 7. **`element:hover` — Pseudo-class Selector**

* Targets an element **on hover** or based on state.

#### Example:

```css
a:hover {
  color: red;
}
```

✅ Changes link color when hovered.

---

## 🧠 Summary Table

| Symbol | Meaning                   | Example    |
| ------ | ------------------------- | ---------- |
| `.`    | Class selector            | `.btn`     |
| `#`    | ID selector               | `#header`  |
| `*`    | Universal selector        | `*`        |
| (none) | Element selector          | `div`, `p` |
| `,`    | Group multiple selectors  | `h1, p`    |
| `:`    | Pseudo-class (like hover) | `a:hover`  |
