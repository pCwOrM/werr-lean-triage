# WERR-Lean-Triage v0.3: Live Lean 4.36.0 Verification Report

- **Timestamp (UTC):** `2026-11-22T11:26:56Z`
- **Target Toolchain:** `leanprover/lean4:v4.36.0` / Mathlib `fc4f59e577fe`
- **Official Mathlib Deprecation Dictionary:** `5703` entries (`v4.33.1 -> v4.36.0`)
- **Evaluated System-1 Candidate Failures:** `269`
- **Live Compiled & Verified Fixes (`0 sorry`, exit 0):** **`77 / 269` (`28.62%`)**
- **Wall Time:** `953.66s` (`8` parallel Lean 4.36.0 workers, `0 Bytes VRAM`, `$0` LLM API cost)

## Breakdown by Compiler Error Category

| Category | Verified Fixed Count |
| :--- | ---: |
| `unknown_constant` | 38 |
| `unknown_identifier` | 36 |
| `no_goals_to_be_solved` | 3 |

## Breakdown by Mechanical Repair Operation

| Operation | Applications Across 77 Fixed Modules |
| :--- | ---: |
| `rename` | 85 |
| `prune_closed` | 3 |

## All 77 Verified `0 sorry` Modules (`leanprover/lean4:v4.36.0`, exit 0)

| # | Module ID | Module | Mechanical Repair Applied | Time (s) |
| :-: | :--- | :--- | :--- | ---: |
| 1 | `M002162` | `Development.AbelianVarietyTheory.BlockTheory.DivisorBase.MultiplicationKernelIdentity` | `rename:Polynomial.eval₂_finset_prod->Polynomial.eval₂_finsetProd` | 28.42 |
| 2 | `M006411` | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.EntireApplyEqOfPeriodicOfSpanReal` | `rename:Polynomial.eval_finset_sum->Polynomial.eval_finsetSum` | 20.72 |
| 3 | `M008087` | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ContDiffCompactAverageOfClosedPartials` | `rename:integral_finset_sum->integral_finsetSum` | 23.58 |
| 4 | `M012739` | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.CompCMulMap` | `rename:AddMonoidHom.finset_sum_apply->AddMonoidHom.finsetSum_apply` | 19.41 |
| 5 | `M014160` | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.UnitOnProductEqOne` | `rename:Finsupp.coe_finset_sum->Finsupp.coe_finsetSum` | 55.06 |
| 6 | `M019614` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ContinuousAtCharSeriesCoefZero` | `rename:tendsto_finset_sum->tendsto_finsetSum` | 20.46 |
| 7 | `M020197` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CurveLieLatticeDegree` | `rename:Ideal.bot_prime->Ideal.isPrime_bot` | 18.94 |
| 8 | `M020874` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DenseAnalyticGrowthSchwartz` | `rename:SchwartzMap.fourierTransformCLE->FourierTransform.fourierCLE` | 18.3 |
| 9 | `M021551` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DixmierSchurOfRankLeAleph0` | `rename:eval_finset_sum->eval_finsetSum` | 17.01 |
| 10 | `M021587` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DoubleCosetSumFundamentalDomain` | `rename:continuous_mul_right->continuous_mul_const; rename:integral_finset_sum->integral_finsetSum` | 17.21 |
| 11 | `M023687` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsBasisModN` | `rename:IsLocalization.map_comap->IsLocalization.map_under` | 20.91 |
| 12 | `M026341` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsInjectiveNormLeOne` | `rename:Polynomial.eval₂_finset_sum->Polynomial.eval₂_finsetSum` | 14.44 |
| 13 | `M026517` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsInvariantPosDefHermitian` | `rename:continuous_finset_sum->continuous_finsetSum` | 21.7 |
| 14 | `M028335` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPowEqOneIsUnitOneSubPow` | `rename:Polynomial.eval_finset_sum->Polynomial.eval_finsetSum` | 14.03 |
| 15 | `M030617` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExpSumCoeffEqZeroOfVanishing` | `rename:integral_finset_sum->integral_finsetSum; rename:tendsto_finset_sum->tendsto_finsetSum; rename:tendsto_finset_prod->tendsto_finsetProd` | 113.04 |
| 16 | `M031586` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankEqZeroOfDualKilledByTensor` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 22.82 |
| 17 | `M034778` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSumConjClassesRegroupWithInvariantSelection` | `rename:summable_of_finite_support->summable_of_hasFiniteSupport` | 17.2 |
| 18 | `M036410` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsAlt` | `rename:IsLocalization.map_comap->IsLocalization.map_under` | 15.45 |
| 19 | `M037018` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralDoubleSeriesInterchange` | `rename:integral_finset_sum->integral_finsetSum; rename:integrable_finset_sum->integrable_finsetSum` | 22.57 |
| 20 | `M037067` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralFundamentalDomainEqSum` | `rename:integrable_finset_sum->integrable_finsetSum; rename:integral_finset_sum->integral_finsetSum` | 16.49 |
| 21 | `M037084` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralHasSumEqIntegralIndicatorHasSum` | `rename:integral_finset_sum->integral_finsetSum` | 14.73 |
| 22 | `M037633` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsAlgebraicOfFiniteTypeOfComapEqBot` | `rename:IsLocalization.map_comap->IsLocalization.map_under` | 22.92 |
| 23 | `M038222` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsIntegralConeRingOfForallValuationSubring` | `rename:Polynomial.eval₂_finset_sum->Polynomial.eval₂_finsetSum` | 21.56 |
| 24 | `M040219` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LatticeCountIntegrableBound` | `rename:lintegral_finset_sum->lintegral_finsetSum` | 14.75 |
| 25 | `M042170` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LocallyConstantCompactSupportInvariantOpenAddSub` | `rename:continuous_add_left->continuous_const_add` | 14.98 |
| 26 | `M043370` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MemSubfieldOfBilinFormBasisMonomials` | `rename:AddSubmonoidClass.coe_finset_sum->AddSubmonoidClass.coe_finsetSum` | 20.05 |
| 27 | `M044247` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NilpotentExpLogSeries` | `rename:eval_finset_sum->eval_finsetSum` | 16.55 |
| 28 | `M044251` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NilpotentTwistCharacterContinuous` | `rename:continuous_finset_sum->continuous_finsetSum` | 15.66 |
| 29 | `M044618` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormUnitLeOfEsymm` | `rename:Polynomial.eval_finset_sum->Polynomial.eval_finsetSum` | 13.97 |
| 30 | `M046242` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PosDefExistsConjTransposeMulMulEqOne` | `prune_closed:L[48]` | 14.64 |
| 31 | `M046252` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PosSemidefQuadraticAdjointPairBound` | `rename:AddMonoidHom.finset_sum_apply->AddMonoidHom.finsetSum_apply` | 23.01 |
| 32 | `M046318` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PowDivMemOfEsymmPowDivMem` | `rename:eval_finset_sum->eval_finsetSum` | 15.24 |
| 33 | `M049661` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemilinearRankComparison` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 39.43 |
| 34 | `M050649` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SpanRangeInfKerEqSpanRationalKer` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 17.67 |
| 35 | `M053808` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TotalDegreeLeOfIntegralAtInfinity` | `rename:totalDegree_finset_sum->totalDegree_finsetSum` | 20.68 |
| 36 | `M055002` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnipotentMatrixCoefficientsMem` | `rename:continuous_finset_sum->continuous_finsetSum` | 17.7 |
| 37 | `M055799` | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.VanishingOfProjectionSupport` | `rename:lintegral_finset_sum->lintegral_finsetSum` | 28.55 |
| 38 | `M058666` | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.IntegralNonnegOfSums` | `rename:integral_finset_sum->integral_finsetSum; rename:integrable_finset_sum->integrable_finsetSum` | 26.92 |
| 39 | `M062550` | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ImportsAlt` | `rename:eval₂_finset_sum->eval₂_finsetSum` | 16.62 |
| 40 | `M062816` | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.JetRelOfWeierstrassSystem` | `prune_closed:L[40]` | 17.17 |
| 41 | `M063176` | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.MonicFactorCoeffNatDegreeLe` | `rename:finset_sum_coeff->finsetSum_coeff` | 16.32 |
| 42 | `M063878` | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.SummableRpowOfFibreCardLe` | `rename:Real.finset_prod_rpow->Real.finsetProd_rpow` | 15.41 |
| 43 | `M067292` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CenterMonoidAlgebraLeSpanCentralIntegral` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply; rename:MonoidAlgebra.mapRangeRingHom_single->MonoidAlgebra.mapRingHom_single` | 16.52 |
| 44 | `M068383` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.EmbeddingIntegralContinuous` | `rename:eval_finset_sum->eval_finsetSum` | 18.88 |
| 45 | `M069187` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsIdempotentSubMemOfPowSubMem` | `rename:continuous_mul_right->continuous_mul_const` | 17.52 |
| 46 | `M069416` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsLinearRelationDescendBaseField` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 16.2 |
| 47 | `M070042` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsWittVectorGhostEqFrobeniusIterate` | `prune_closed:L[52]` | 16.29 |
| 48 | `M070165` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FiniteFreeModuleCompactAdicDvr` | `rename:continuous_finset_sum->continuous_finsetSum` | 16.66 |
| 49 | `M072948` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NormHasSumEqOfDominant` | `rename:NormedAddCommGroup.tendsto_nhds_zero->NormedAddGroup.tendsto_nhds_zero` | 15.54 |
| 50 | `M073027` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NotDvdCoeffAevalOneAddXPowSubOne` | `rename:Polynomial.finset_sum_coeff->Polynomial.finsetSum_coeff` | 17.07 |
| 51 | `M073039` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NotXPowSuccDvdDetOfFirstOrderKernelEqZero` | `rename:Polynomial.finset_sum_coeff->Polynomial.finsetSum_coeff` | 20.9 |
| 52 | `M074483` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TendstoRatioBoxCountsProdOne` | `rename:tendsto_finset_prod->tendsto_finsetProd` | 15.33 |
| 53 | `M074506` | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TensorProductBasisCoordinates` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 18.13 |
| 54 | `M076736` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.DifferentiableAtDet` | `rename:HasDerivAt.fun_finset_prod->HasDerivAt.fun_finsetProd` | 14.97 |
| 55 | `M076841` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.DvrMapOfCodimOnePrime` | `rename:Localization.AtPrime.comap_maximalIdeal->Localization.AtPrime.under_maximalIdeal` | 14.97 |
| 56 | `M079543` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HeightComapFlatHeightOne` | `rename:Ideal.bot_prime->Ideal.isPrime_bot` | 14.69 |
| 57 | `M079546` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HeightOneComapMinimal` | `rename:Ideal.bot_prime->Ideal.isPrime_bot` | 14.68 |
| 58 | `M081032` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.MvPolynomialClearDenominatorsEval` | `rename:mem_vars->mem_vars_iff_mem_support` | 16.66 |
| 59 | `M081155` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.NormPowSubPowLe` | `rename:eval_finset_sum->eval_finsetSum` | 18.3 |
| 60 | `M081483` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PolynomialApproxUniqueness` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply; rename:Polynomial.eval_finset_sum->Polynomial.eval_finsetSum; rename:Polynomial.finset_sum_coeff->Polynomial.finsetSum_coeff` | 18.67 |
| 61 | `M081519` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PosDefUniformBoundsNearPoint` | `rename:tendsto_finset_sum->tendsto_finsetSum` | 16.55 |
| 62 | `M082067` | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.SchurOrthogonalitySubgroupMeasureOne` | `rename:integral_finset_sum->integral_finsetSum` | 19.03 |
| 63 | `M084222` | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.NormSumEigenprojectorLeOfResolventBound` | `rename:continuousOn_finset_sum->continuousOn_finsetSum` | 19.83 |
| 64 | `M085774` | `Development.AbelianVarietyTheory.Proofs.ModuliProofs.MvPowerSeriesVariablesSyzygySocle` | `rename:Finsupp.finset_sum_apply->Finsupp.finsetSum_apply` | 20.32 |
| 65 | `M088887` | `Development.AbelianVarietyTheory.Proofs.SatakeParameters.NormLeOfRecurrenceGrowth` | `rename:Polynomial.eval_finset_sum->Polynomial.eval_finsetSum` | 15.87 |
| 66 | `M090551` | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.CardHomVanishingOfDiagBasis` | `rename:Finsupp.coe_finset_sum->Finsupp.coe_finsetSum` | 20.19 |
| 67 | `M090564` | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.DifferentiableOnCoordOfLinearIndependent` | `rename:HasFDerivAt.finset_prod->HasFDerivAt.finsetProd` | 16.88 |
| 68 | `M091463` | `Development.AbelianVarietyTheory.Proofs.ToricGeometry.SeriesApplyEqZeroOfFace` | `rename:continuous_finset_sum->continuous_finsetSum` | 49.77 |
| 69 | `M091646` | `Development.AbelianVarietyTheory.Proofs.TorusHaarMeasure.MeasureUnivLeTwoMulSublevelOfDrift` | `rename:lintegral_finset_sum->lintegral_finsetSum` | 18.88 |
| 70 | `M091697` | `Development.AbelianVarietyTheory.Proofs.TorusHaarMeasure.TraceMemPrimeOfPowMulVecMemSmul` | `rename:LinearMap.exists_monic_and_coeff_mem_pow_and_aeval_eq_zero_of_range_le_smul->LinearMap.exists_monic_and_natDegree_eq_and_coeff_mem_pow_and_aeval_eq_zero` | 26.05 |
| 71 | `M094302` | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.FourierUniquenessOfOpenSubgroup` | `rename:continuous_add_left->continuous_const_add; rename:integral_finset_sum->integral_finsetSum` | 15.76 |
| 72 | `M096209` | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.NewtonRecursionPolyUnique` | `rename:eval_finset_sum->eval_finsetSum; rename:finset_sum_coeff->finsetSum_coeff` | 16.81 |
| 73 | `M101428` | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.ContinuousContractNth` | `rename:continuous_finset_sum->continuous_finsetSum` | 24.34 |
| 74 | `M102182` | `Development.AutomorphicArithmetic.AutomorphicVarieties.BuildingsResidueChars.ExistsEquivariantProjectionsOfSumIrreducible` | `rename:DFinsupp.finset_sum_apply->DFinsupp.finsetSum_apply` | 20.12 |
| 75 | `M102188` | `Development.AutomorphicArithmetic.AutomorphicVarieties.BuildingsResidueChars.ExistsFixedRotationBasisOfCharpoly` | `rename:linearIndependent_fin_cons->linearIndependent_finCons` | 23.94 |
| 76 | `M106289` | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.IntegralStabilizers.FinSAbs` | `rename:Finsupp.coe_finset_sum->Finsupp.coe_finsetSum` | 22.37 |
| 77 | `M109930` | `Development.AutomorphicArithmetic.CyclotomicBounds.DeRhamLattices.FiltrationEqSpanOfEisensteinPowBasisChange` | `rename:AddMonoidHom.finset_sum_apply->AddMonoidHom.finsetSum_apply` | 15.02 |
