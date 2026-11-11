# Apple Design System: Android & Jetpack Compose Adaptation

A practical engineering guide for bringing Apple's design craft, typographic clarity, and fluid ergonomics to Android applications without violating native Android conventions.

---

## 1. The Core Philosophy: Avoiding the "Uncanny Valley"

The most critical mistake when designing cross-platform apps is building a literal 1:1 replica of iOS on Android (e.g., rendering iOS-style switches, iOS back chevrons, or disabling the Android system back button). This creates an "uncanny valley" experience that feels broken to Android users.

### The Craft Translation Rule
> **Adopt Apple's Standards of Craft, Not Its Platform Idiosyncrasies.**
>
> - **Borrow**: Generous whitespace, 8dp spatial discipline, clear typographic contrast, subtle ambient occlusion shadows, hairline borders, and physical spring physics.
> - **Respect**: Android's Material 3 interaction model, predictive back gesture, system navigation bar, and native component affordances.

---

## 2. Platform Architecture Mapping

| Design Element | Apple iOS Standard | Android / Jetpack Compose Adaptation |
| :--- | :--- | :--- |
| **Grid & Spacing** | 8pt grid / 16pt margin | `8dp` grid / `16dp` margin (`Spacer(Modifier.height(8.dp))`) |
| **Touch Target** | Minimum 44×44 pt | Minimum `48×48 dp` (`Modifier.sizeIn(minWidth = 48.dp, minHeight = 48.dp)`) |
| **Large Title** | Collapsing Large Navigation Bar | `LargeTopAppBar` with `exitUntilCollapsedScrollBehavior` |
| **Bottom Navigation** | iOS Tab Bar | `NavigationBar` + `NavigationBarItem` with active indicator pill |
| **Back Interaction** | Left edge-swipe only | **Predictive Back Gesture** (left/right edge) + `BackHandler` |
| **Material / Blur** | `UIBlurEffect` / Translucency | `Modifier.blur(20.dp)` (API 31+) or subtle tonal container fill |
| **Animation Physics** | Damped interactive springs | `spring(dampingRatio = 0.75f, stiffness = 400f)` |
| **Dividers** | Hairline with text-indent | `HorizontalDivider(modifier = Modifier.padding(start = 56.dp))` |

---

## 3. Jetpack Compose Component Recipes

### A. Apple-Grade Button Hierarchy in Compose

```kotlin
// 1. Primary Action (Apple "Filled" Button equivalent)
Button(
    onClick = onPrimaryClick,
    shape = RoundedCornerShape(14.dp), // Apple squircle approximation
    colors = ButtonDefaults.buttonColors(
        containerColor = MaterialTheme.colorScheme.primary,
        contentColor = MaterialTheme.colorScheme.onPrimary
    ),
    elevation = ButtonDefaults.buttonElevation(defaultElevation = 0.dp), // Apple prefers flat + tonal
    modifier = Modifier
        .fillMaxWidth()
        .heightIn(min = 50.dp)
) {
    Text(text = "Continue", style = MaterialTheme.typography.titleMedium)
}

// 2. Secondary Action (Apple "Tinted" Button equivalent)
FilledTonalButton(
    onClick = onSecondaryClick,
    shape = RoundedCornerShape(14.dp),
    colors = ButtonDefaults.filledTonalButtonColors(
        containerColor = MaterialTheme.colorScheme.primaryContainer.copy(alpha = 0.4f),
        contentColor = MaterialTheme.colorScheme.primary
    ),
    modifier = Modifier
        .fillMaxWidth()
        .heightIn(min = 50.dp)
) {
    Text(text = "View Details", style = MaterialTheme.typography.titleMedium)
}
```

### B. Inset Grouped Card (Apple Settings Layout in Compose)

```kotlin
@Composable
fun InsetGroupedSection(
    title: String,
    content: @Composable ColumnScope.() -> Unit
) {
    Column(modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp)) {
        // Section Header (Apple Caption Style)
        Text(
            text = title.uppercase(),
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(start = 12.dp, bottom = 6.dp)
        )

        // Rounded Grouped Container
        Card(
            shape = RoundedCornerShape(16.dp),
            colors = CardDefaults.cardColors(
                containerColor = MaterialTheme.colorScheme.surfaceContainer
            ),
            border = BorderStroke(
                width = 1.dp,
                color = MaterialTheme.colorScheme.outlineVariant.copy(alpha = 0.35f)
            ),
            elevation = CardDefaults.cardElevation(defaultElevation = 0.dp)
        ) {
            Column(content = content)
        }
    }
}
```

---

## 4. Jetpack Compose Spring Dynamics

Replace standard `tween` transitions with Compose springs matching Apple HIG kinematics:

```kotlin
val scale by animateFloatAsState(
    targetValue = if (isPressed) 0.96f else 1f,
    animationSpec = spring(
        dampingRatio = Spring.DampingRatioLowBouncy, // Damping ~ 0.75
        stiffness = Spring.StiffnessMediumLow        // Stiffness ~ 400
    ),
    label = "springScale"
)

Box(
    modifier = Modifier
        .graphicsLayer {
            scaleX = scale
            scaleY = scale
        }
)
```

---

## 5. Navigation & Predictive Back Handling

Never break Android navigation gestures:

```kotlin
// Handle back navigation cleanly in Compose
BackHandler(enabled = hasUnsavedChanges) {
    // Show confirmation dialog before discarding draft
    showDiscardConfirmationDialog = true
}
```

---

## 6. Haptic Feedback Integration

Apple interfaces rely heavily on tactile confirmation. In Android, use Compose's haptic abstraction:

```kotlin
val haptic = LocalHapticFeedback.current

Button(onClick = {
    haptic.performHapticFeedback(HapticFeedbackType.TextHandleMove) // Subtle tick
    onAction()
}) {
    Text("Confirm")
}
```
