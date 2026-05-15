<template>
  <div class="logo-quantia">
    <div class="logo-icon">
      <div class="bar bar-1"></div>
      <div class="bar bar-2"></div>
      <div class="bar bar-3"></div>
      <div class="bar bar-4"></div>
    </div>

    <div class="logo-text">
      <strong>Quantia</strong>
      <span>Vivienda</span>
    </div>
  </div>
</template>

<style scoped>
.logo-quantia {
  display: inline-flex;
  align-items: center;
  gap: 14px;
}

.logo-icon {
  width: 62px;
  height: 62px;
  border-radius: 20px;
  position: relative;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 4px;
  padding: 10px 11px;
  background: linear-gradient(135deg, rgba(88, 220, 255, 0.28), rgba(134, 73, 255, 0.32));
  border: 2px solid rgba(255,255,255,0.2);
  box-shadow: inset 0 0 18px rgba(255,255,255,0.08);
}

.logo-icon::before {
  content: "";
  position: absolute;
  inset: -6px;
  border-radius: 24px;
  border: 2px solid rgba(140, 233, 255, 0.45);
}

.bar {
  width: 7px;
  border-radius: 999px;
  background: linear-gradient(180deg, #8fe8ff 0%, #8b5cf6 100%);
  box-shadow: 0 0 12px rgba(143, 232, 255, 0.3);
}

.bar-1 { height: 15px; }
.bar-2 { height: 24px; }
.bar-3 { height: 33px; }
.bar-4 { height: 42px; }

.logo-text {
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.logo-text strong {
  font-size: 2.1rem;
  color: #ffffff;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.logo-text span {
  margin-top: 6px;
  color: rgba(246, 246, 255, 0.9);
  font-size: 1.15rem;
  font-weight: 500;
}
</style>