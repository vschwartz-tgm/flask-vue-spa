describe('Vue Client Test', function () {
  it('Visits Vue Client', function () {
    cy.visit('http://localhost:8080/')
    cy.wait(700)
  })
  it('presses button', function () {
    cy.get('[data-cy="random"]').click()
    cy.wait(100)
  })
  it('pressess button multiple times', function () {
    cy.get('[data-cy="random"]').click()
    cy.wait(100)
    cy.get('[data-cy="random"]').click()
    cy.wait(100)
    cy.get('[data-cy="random"]').click()
  })
})
