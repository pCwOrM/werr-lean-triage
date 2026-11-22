# Depth-0 modules that fail unchanged on the port target

451 of 2,940 triaged depth-0 modules fail to compile unchanged on `leanprover/lean4:v4.36.0` + Mathlib `fc4f59e577`. Full compiler output is in `results.json` (`excerpt`). Pick work with `python3 tracker/port.py next`.

| ID | Packet | Module | Errors | First error |
|---|---|---|---:|---|
| M000028 | P0001 | `CompanionTheory.AutomorphicTheory.BesselWaveGrids.InterlacingGrids.CloudProd` | 2 | line 39: Function expected at |
| M000030 | P0001 | `CompanionTheory.AutomorphicTheory.BesselWaveGrids.InterlacingGrids.GridSum` | 2 | line 24: failed to synthesize |
| M000031 | P0001 | `CompanionTheory.AutomorphicTheory.BesselWaveGrids.InterlacingGrids.LagSum` | 1 | line 15: failed to synthesize |
| M000069 | P0001 | `CompanionTheory.AutomorphicTheory.HeckeStandardModules.ExistsCen` | 1 | line 176: Application type mismatch: The argument |
| M000495 | P0001 | `CompanionTheory.HarishChandraModules.BesselParameterIntegrals.ContDiffOnExpPartialHomeomorphSymm` | 2 | (not in excerpt) |
| M000526 | P0001 | `CompanionTheory.HarishChandraModules.KFiniteAnalyticVectors.AdmissibleSmoothVectors.IwaChol` | 1 | (not in excerpt) |
| M000920 | P0001 | `CompanionTheory.SpectralGeometry.LocalGlobalProofs.AdelicAnalysis.FiniteCovolumeUnimodular` | 1 | line 40: unsolved goals |
| M002046 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.AdelicCMFields.UnitaryHeckeCharacterIdele` | 6 | line 170: Application type mismatch: The argument |
| M002162 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.DivisorBase.MultiplicationKernelIdentity` | 2 | line 33: unsolved goals |
| M002315 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.GlobalSignature.StabiliserCardinality` | 1 | line 38: Application type mismatch: The argument |
| M002358 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.HeightDefect.SchurLatticeConjugates` | 1 | (not in excerpt) |
| M002361 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.HeightDefect.SphereBlockLogMean` | 9 | line 37: unsolved goals |
| M002399 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.JetGauges.NodalSeriesPeriods` | 2 | line 147: Application type mismatch: The argument |
| M002408 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.JetGauges.RelativeDifferentValues` | 2 | line 80: Type mismatch |
| M002422 | P0001 | `Development.AbelianVarietyTheory.BlockTheory.JetGauges.TraceFormDualSystem` | 1 | (not in excerpt) |
| M002620 | P0002 | `Development.AbelianVarietyTheory.BlockTheory.TorsionBlocks.LowerUnipotentMinors` | 2 | (not in excerpt) |
| M002899 | P0002 | `Development.AbelianVarietyTheory.Counterexamples.LevelGroupExamples.RightInvariantOfCovolume` | 1 | line 104: unsolved goals |
| M003856 | P0002 | `Development.AbelianVarietyTheory.Definitions.Divisors.PlacesOverU` | 2 | (not in excerpt) |
| M004039 | P0002 | `Development.AbelianVarietyTheory.Definitions.Foundations.ExistsFinsetOfEventually` | 4 | line 178: Type mismatch |
| M004114 | P0002 | `Development.AbelianVarietyTheory.Definitions.Foundations.MemUnitaryGroupIffIsIsometry` | 3 | line 358: (deterministic) timeout at 'whnf', maximum number of heartbeats (4000000) has been reached |
| M004210 | P0002 | `Development.AbelianVarietyTheory.Definitions.GaloisGeometry.FiniteResidueFieldPadicInt` | 10 | line 22: 'span_eq_top' is not a field of structure 'Submodule.IsLattice' |
| M005486 | P0003 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ExistsIsUnitFormSelfOfNotMem` | 2 | line 26: Application type mismatch: The argument |
| M005526 | P0003 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ExistsPrimeInvolutionOfRingInvolution` | 2 | line 44: 'simp' made no progress |
| M005629 | P0004 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.HasSumLogZetaSqMul` | 2 | line 71: Tactic 'rfl' failed: The left-hand side |
| M005661 | P0004 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.ImportsBis` | 1 | line 23: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M005725 | P0004 | `Development.AbelianVarietyTheory.Proofs.AdelicLatticeProofs.LandauSummableOfExpDirichletSeriesEntire` | 2 | (not in excerpt) |
| M006137 | P0004 | `Development.AbelianVarietyTheory.Proofs.CharacterTheory.OneMemOfMulMemOfForallPrimeNotDvd` | 1 | line 12: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M006184 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.AlternatingMapSumSmulEqDetSmul` | 1 | line 66: Application type mismatch: The argument |
| M006203 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ContractMultilinearApply` | 12 | line 21: Application type mismatch: The argument |
| M006224 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ExistsBasicOpenEqZeroOfMemIInfPowSmul` | 1 | line 150: Invalid alternative name 'zero': There are no unhandled alternatives |
| M006243 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ExistsIsRegularQuotSMulTop` | 7 | line 52: Application type mismatch: The argument |
| M006244 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ExistsLinearEquivMapLatticeEq` | 9 | line 16: unsolved goals |
| M006249 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ExistsMvPolynomialOfIteratedBackwardDifferenceVa` | 13 | line 230: Application type mismatch: The argument |
| M006268 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.ExistsUnitSmulEqOfBijectiveToSpanSingleton` | 9 | line 195: Invalid alternative name 'zero': There are no unhandled alternatives |
| M006303 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.IsDiscreteValuationRingLocalizationOfIsDedekindD` | 2 | line 99: Application type mismatch: The argument |
| M006318 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.IsWeaklyRegularMapCAppendMapLinForm` | 2 | line 297: Invalid projection: Projection operates on types of the form 'C ...' where C is a constant. The expr |
| M006330 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.LengthRestrictScalarsEqSumInertiaDegOfSubset` | 1 | (not in excerpt) |
| M006334 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.MapSpanBaseChangeEquivSubmoduleOf` | 2 | line 132: Invalid alternative name 'zero': There are no unhandled alternatives |
| M006336 | P0004 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.MemRangeOfForallHeightEqOneOfIsReflexive` | 5 | line 49: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg |
| M006368 | P0005 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.RingKrullDimQuotientEqOfMemMinimalPrimes` | 3 | line 76: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg |
| M006398 | P0005 | `Development.AbelianVarietyTheory.Proofs.CoherentCohomologyProofs.WeightAddLeOfMemSupportDividedContraction` | 9 | line 16: Type mismatch |
| M006411 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.EntireApplyEqOfPeriodicOfSpanReal` | 1 | (not in excerpt) |
| M006412 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.EqZeroOfEvalGridEqZeroOfTotalDegreeLe` | 3 | line 123: unsolved goals |
| M006421 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.ExistsIsFundamentalDomainAndQuotMeasureEq` | 1 | line 143: Invalid field notation: Function 'Measure.QuasiMeasurePreserving.ae' does not have a usable paramete |
| M006422 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.ExistsIsUnitEvalOfMapResidueNeZero` | 2 | line 164: No goals to be solved |
| M006429 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.ExistsOrthonormalOfLinearIndependent` | 7 | line 26: Function expected at |
| M006430 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.ExistsQr` | 1 | (not in excerpt) |
| M006435 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.FiniteAndFinrankLeOfPointwise` | 4 | line 96: unsolved goals |
| M006436 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.FiniteAndNcardSetOfSubmoduleLeRelIndexEqLe` | 2 | (not in excerpt) |
| M006438 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.FinrankMulDiscrRpowLeSumSqOfMemTraceDual` | 1 | line 90: Type mismatch: After simplification, term |
| M006455 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.IntegralConjInnerMulInnerOfIsEmptyEquiv` | 3 | line 54: unsolved goals |
| M006467 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.L2OpNormConjTransposeExpMulSignMulExpSubLe` | 4 | line 94: unsolved goals |
| M006470 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.LinearIndependentRealOfIntOfDiscrete` | 4 | line 33: Function expected at |
| M006475 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.LintegralProdPartialSums` | 1 | line 30: failed to prove positivity/nonnegativity/nonzeroness |
| M006479 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.NatCastMulCoeffOfPderivEq` | 28 | line 36: Type mismatch |
| M006484 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.OneLeDetOneAdd` | 1 | line 22: Function expected at |
| M006488 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.ResidueNormValuationSubringEqZeroIff` | 2 | line 29: Function expected at |
| M006494 | P0005 | `Development.AbelianVarietyTheory.Proofs.CovolumeBounds.SummablePiProd` | 2 | line 23: Function expected at |
| M007041 | P0005 | `Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.ColumnDegreeLe` | 7 | line 58: unsolved goals |
| M007174 | P0005 | `Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.ExistsNatSmulCoeffIsIntegral` | 1 | (not in excerpt) |
| M007439 | P0005 | `Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.ProdLeadMinorDiagonal` | 1 | line 290: 'simp' made no progress |
| M007455 | P0005 | `Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.RowAddGenericRowAddTerm` | 1 | line 26: (deterministic) timeout at 'isDefEq', maximum number of heartbeats (4000000) has been reached |
| M008087 | P0006 | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ContDiffCompactAverageOfClosedPartials` | 2 | line 37: unsolved goals |
| M009000 | P0006 | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.ExistsZsmulMemLattice` | 2 | line 17: unsolved goals |
| M009059 | P0006 | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.FiniteDimensionalSpanMultilinearValues` | 3 | line 7: Application type mismatch: The argument |
| M009701 | P0006 | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.IntegralKernelLiftsFubiniSigmaFinite` | 2 | line 88: Invalid '⟨...⟩' notation: The expected type |
| M010384 | P0006 | `Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.MatrixFieldStableRangeOneDetNeZero` | 1 | line 53: failed to synthesize |
| M012739 | P0006 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.CompCMulMap` | 1 | (not in excerpt) |
| M012833 | P0006 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsArithFrobeniusAbsGalois` | 1 | line 36: typeclass instance problem is stuck |
| M012954 | P0006 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsFormLimitIdeal` | 4 | line 15: unsolved goals |
| M013024 | P0006 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsIntegralExtIsAlgClosedResidueField` | 1 | line 152: Application type mismatch: The argument |
| M013289 | P0006 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.ExistsSubMemMaximalIdeal` | 9 | line 16: Application type mismatch: The argument |
| M013928 | P0007 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.SimilitudeDefiniteFormIsAlgebraicOnVector` | 4 | line 87: Function expected at |
| M014160 | P0007 | `Development.AbelianVarietyTheory.Proofs.DegenerationProofs.UnitOnProductEqOne` | 2 | line 60: unsolved goals |
| M014783 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.AddValuationNatCastEqPadicValNat` | 2 | line 49: Invalid argument name 'p' for function 'pow_padicValNat_dvd' |
| M015092 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.AdjoinRootUniformiserIsDVR` | 6 | line 14: Type mismatch |
| M015094 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.AdjoinRootXPowSubUniformizerIsDomain` | 1 | line 17: Type mismatch |
| M015143 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.AeMeasureSetOfSmulMemEqZero` | 1 | line 16: Application type mismatch: The argument |
| M015310 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.AlgebraMapEqMk` | 37 | line 12: Application type mismatch: The argument |
| M016244 | P0007 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.BasisApply` | 3 | line 103: Not a definitional equality: the left-hand side |
| M016856 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CardFiberDoubleCosetMapEqCardInfConj` | 6 | line 29: Application type mismatch: The argument |
| M018204 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CoeffAllOnesProdOneAddMul` | 4 | (not in excerpt) |
| M018205 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CoeffAllOnesSumAlgEquivMkDerivation` | 5 | (not in excerpt) |
| M018207 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CoeffAnnihilatedOfAevalMemKerPow` | 14 | line 115: unsolved goals |
| M018378 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ColengthDvdOfNeZero` | 1 | line 15: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M018458 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CommensurableConjRangeGLSubring` | 2 | line 105: Application type mismatch: The argument |
| M018460 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CommensurableMapConjProdPi` | 4 | line 55: Application type mismatch: The argument |
| M019614 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ContinuousAtCharSeriesCoefZero` | 1 | (not in excerpt) |
| M020197 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.CurveLieLatticeDegree` | 3 | (not in excerpt) |
| M020874 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DenseAnalyticGrowthSchwartz` | 2 | line 64: unsolved goals |
| M020963 | P0008 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DerivationExtendMvPolynomial` | 7 | line 17: Failed to rewrite using equation theorems for 'coeffDerivFun' |
| M021111 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DetMulExpandAlt` | 1 | line 13: Application type mismatch: The argument |
| M021396 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DirectedSystemEtaleBaseChangePolynomial` | 1 | (not in excerpt) |
| M021398 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DirichletSeriesIntegralHolomorphic` | 2 | line 53: (deterministic) timeout at 'whnf', maximum number of heartbeats (4000000) has been reached |
| M021551 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DixmierSchurOfRankLeAleph0` | 1 | (not in excerpt) |
| M021585 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DoubleCosetSemidirectRepSurjective` | 2 | line 17: Function expected at |
| M021587 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DoubleCosetSumFundamentalDomain` | 2 | (not in excerpt) |
| M021818 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DualHopfOrderGaussSum` | 1 | (not in excerpt) |
| M021990 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.DvrLocPrincipalPrime` | 4 | line 32: could not synthesize default value for parameter 'h₂' using tactics |
| M022868 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleIntegralClosureTensorOfEtaleOfIsIntegral` | 1 | line 21: Invalid alternative name 'zero': There are no unhandled alternatives |
| M022900 | P0009 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.EtaleLocalizationAtPrimeOfHeightOne` | 1 | (not in excerpt) |
| M023679 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsBasisAdaptedToCartanInvolution` | 2 | line 70: 'simp' made no progress |
| M023687 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsBasisModN` | 1 | (not in excerpt) |
| M024668 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDerivationExtendingKernelFormOfLifting` | 4 | line 21: Application type mismatch: The argument |
| M024812 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsDominatingDvrContainingFinset` | 1 | line 57: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M025052 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsEtaleModelOfIsColimit` | 3 | line 69: No goals to be solved |
| M026341 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsInjectiveNormLeOne` | 2 | line 28: unsolved goals |
| M026364 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIntSmulMemOfIsLattice` | 1 | line 9: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter of |
| M026381 | P0010 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIntegrableDensityOfBoundByIntegralCompactA` | 1 | line 40: unsolved goals |
| M026435 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIntegralInvOneAddPrimeMulPadic` | 1 | line 16: Application type mismatch: The argument |
| M026517 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsInvariantPosDefHermitian` | 1 | (not in excerpt) |
| M026561 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIsAlgebraicRatFuncFractionRingDedekind` | 2 | line 19: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M026632 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsIsLocalHomAdicCompletionExtend` | 3 | line 40: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg |
| M027309 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsLocalHomAdicCompletionExtend` | 7 | line 19: could not synthesize default value for parameter 'h₂' using tactics |
| M028264 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPolyAnnihilatesCommutingLinearCombination` | 4 | line 12: unsolved goals |
| M028335 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPowEqOneIsUnitOneSubPow` | 2 | line 32: invalid '▸' notation, expected result type of cast is  |
| M028442 | P0011 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsPrimitiveAnnihilator` | 1 | line 103: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M028855 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExistsRingEquivExtendingOfKerLe` | 2 | line 40: failed to synthesize |
| M030616 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExpNegLeNormTprodOneSubInv` | 1 | line 49: Function expected at |
| M030617 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ExpSumCoeffEqZeroOfVanishing` | 2 | (not in excerpt) |
| M030920 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FibreGoingDownTensor` | 1 | (not in excerpt) |
| M031183 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FiniteDimensionalSpanAdjoin` | 5 | line 27: unsolved goals |
| M031187 | P0012 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FiniteDimensionalSpanCommutant` | 5 | (not in excerpt) |
| M031572 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankDvdOfRingOfIntegersToIntMatrix` | 2 | line 26: Application type mismatch: The argument |
| M031583 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankEqRankMulDegree` | 1 | (not in excerpt) |
| M031586 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinrankEqZeroOfDualKilledByTensor` | 1 | (not in excerpt) |
| M031719 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinsetMemRangeLocalizationAwayOfDvd` | 1 | (not in excerpt) |
| M031730 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FinsumDoubleCosetEqFinprodLocalSums` | 13 | line 16: Application type mismatch: The argument |
| M032472 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FlowDerivativeIntegralByParts` | 1 | line 70: Type mismatch: After simplification, term |
| M033268 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FundamentalDomainFlowIntegralIdentity` | 2 | line 17: Application type mismatch: The argument |
| M033291 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FundamentalDomainSubgroupMeasureConst` | 1 | line 62: Type mismatch |
| M033295 | P0013 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FundamentalDomainTranslate` | 1 | line 13: Type mismatch: After simplification, term |
| M033297 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.FundamentalDomainUnfoldSubgroup` | 1 | (not in excerpt) |
| M034302 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.HaarMeasureProductGroups` | 2 | line 69: unsolved goals |
| M034778 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasSumConjClassesRegroupWithInvariantSelection` | 1 | (not in excerpt) |
| M035368 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.HermitianEndoMatrixRationalInLatticeBasis` | 1 | line 42: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M036410 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsAlt` | 1 | (not in excerpt) |
| M036421 | P0014 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsExtraLast` | 1 | line 10: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M036431 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsFurtherLast` | 4 | line 12: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M036454 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsMoreTail` | 5 | line 34: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg |
| M036455 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsMoreTer` | 1 | line 9: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter of |
| M036484 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ImportsTerRest` | 1 | (not in excerpt) |
| M036781 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.InjectiveOfMapPderivEqAndMapOneNeZero` | 2 | (not in excerpt) |
| M036919 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralBasisChangeDeterminant` | 4 | line 36: could not synthesize default value for parameter 'h₂' using tactics |
| M037018 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralDoubleSeriesInterchange` | 1 | (not in excerpt) |
| M037067 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralFundamentalDomainEqSum` | 3 | line 116: unsolved goals |
| M037084 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralHasSumEqIntegralIndicatorHasSum` | 2 | line 11: unsolved goals |
| M037221 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IntegralRowSpaceBasisExists` | 4 | line 54: Application type mismatch: The argument |
| M037368 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.InvDer` | 2 | line 18: Application type mismatch: The argument |
| M037580 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsAdicCompleteOfLeOfIsNoetherianRing` | 1 | line 17: Application type mismatch: The argument |
| M037629 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsAlgebraicInt` | 1 | line 16: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M037633 | P0015 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsAlgebraicOfFiniteTypeOfComapEqBot` | 1 | (not in excerpt) |
| M038222 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsIntegralConeRingOfForallValuationSubring` | 2 | line 49: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M038591 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IsOpenConnectedComponentOfIsLocallyNoetherian` | 1 | line 28: Invalid projection: Projection operates on types of the form 'C ...' where C is a constant. The expre |
| M039401 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IteratedDerivativeHomogeneousBound` | 2 | line 56: Function expected at |
| M039413 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.IteratedFderivParametricUniformBound` | 2 | line 36: Function expected at |
| M039724 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.KerCounitAlgHomBaseChangeField` | 1 | line 20: Invalid alternative name 'zero': There are no unhandled alternatives |
| M040219 | P0016 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LatticeCountIntegrableBound` | 1 | (not in excerpt) |
| M040511 | P0017 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LeMulSetIntegralImage2OfForallLe` | 2 | line 32: No goals to be solved |
| M042170 | P0017 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LocallyConstantCompactSupportInvariantOpenAddSub` | 1 | (not in excerpt) |
| M042249 | P0017 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LogConcaveMultiplicativeGrowthBound` | 1 | line 66: failed to synthesize |
| M042505 | P0017 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.LuDecompositionUnitriangularUnique` | 2 | line 9: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M042562 | P0017 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MapHaarEqOfLattice` | 1 | line 20: Application type mismatch: The argument |
| M042965 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MaximalIdealPowNatCastDvdFiniteIntegersAlgebra` | 2 | line 15: Application type mismatch: The argument |
| M043285 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MemOfMapMemSpanIntegralClosure` | 1 | line 107: Function expected at |
| M043370 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MemSubfieldOfBilinFormBasisMonomials` | 2 | line 88: Type mismatch |
| M043792 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MonicSplitsValuationSubringOfSeparableReduction` | 1 | (not in excerpt) |
| M043932 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MulTensorInjectiveOfFlatBaseChangeKerInf` | 2 | line 99: Invalid alternative name 'zero': There are no unhandled alternatives |
| M043951 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MultilinearMemSpanImagePartial` | 3 | line 7: Application type mismatch: The argument |
| M043955 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MultilinearVanishOfProdVanish` | 3 | line 9: Application type mismatch: The argument |
| M044082 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.MvPolynomialIdealEqBotOfPderivStableNoConstants` | 1 | (not in excerpt) |
| M044247 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NilpotentExpLogSeries` | 1 | (not in excerpt) |
| M044251 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NilpotentTwistCharacterContinuous` | 1 | (not in excerpt) |
| M044258 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NoCommonZeroSpreadsConstructibleNbhd` | 2 | line 141: unsolved goals |
| M044265 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NoetherNormalizationFiniteAevalPowAdd` | 1 | line 12: Type mismatch |
| M044388 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NonvanishingSectionQuotientLimit` | 2 | line 78: No goals to be solved |
| M044443 | P0018 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormCompHomogeneousIsHomogeneous` | 3 | (not in excerpt) |
| M044512 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormIteratedFDerivCexpPhaseLe` | 2 | line 49: No goals to be solved |
| M044535 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormLeOneOfExtension` | 3 | (not in excerpt) |
| M044581 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormRootLeMaxOneSumNormCoeff` | 2 | line 13: Function expected at |
| M044618 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.NormUnitLeOfEsymm` | 2 | line 9: unsolved goals |
| M044933 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.OneSubProdLeSumOfLe` | 4 | line 19: Function expected at |
| M045131 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PAdicAlgebraicApproximation` | 2 | line 21: No goals to be solved |
| M045845 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PluckerMinorsProportional` | 2 | line 41: unsolved goals |
| M046080 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PolarizationDerivativeVanish` | 3 | line 9: unsolved goals |
| M046112 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PolarizationSymmetricFormIdentity` | 1 | line 8: Application type mismatch: The argument |
| M046242 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PosDefExistsConjTransposeMulMulEqOne` | 1 | line 48: No goals to be solved |
| M046245 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PosDefRealGramPairHermitianForms` | 1 | line 73: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M046252 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PosSemidefQuadraticAdjointPairBound` | 2 | line 194: Type mismatch |
| M046312 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PowCardLeNormProd` | 2 | line 27: linarith failed to find a contradiction |
| M046318 | P0019 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PowDivMemOfEsymmPowDivMem` | 2 | line 11: unsolved goals |
| M046423 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PreirreducibleSpaceFibreHypersurfaceSpectrumIff` | 2 | line 67: failed to synthesize |
| M046430 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.PrescribedValuationDifferenceElements` | 1 | line 34: unsolved goals |
| M046624 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProdArgRealUnitEqOne` | 1 | line 64: Function expected at |
| M046672 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ProdRpowDecayIsBigOCocompact` | 1 | line 43: Function expected at |
| M047375 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RTensorInjectiveOfPowSmulEqBot` | 5 | line 25: Invalid alternative name 'zero': There are no unhandled alternatives |
| M047391 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RamificationIdxDvdOfGaloisDegreeDvdUnitDvr` | 2 | line 34: (deterministic) timeout at 'whnf', maximum number of heartbeats (4000000) has been reached |
| M047730 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RealCompactPartitionUnity` | 1 | line 74: Application type mismatch: The argument |
| M048086 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RelIndexMapNsmulComapEqAbsNormDet` | 2 | line 11: Type mismatch |
| M048155 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RenameSwapOfEqualPartials` | 5 | line 31: unsolved goals |
| M048164 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RepTraceEqMulTrace` | 2 | line 47: Application type mismatch: The argument |
| M048248 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ResidueFieldAtPrimeIsSepClosedOfFiniteType` | 1 | line 17: Type mismatch |
| M048265 | P0020 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ResidueNormalOfProfiniteInvariants` | 1 | line 23: Application type mismatch: The argument |
| M048561 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.RootModelPointHeightDegree` | 2 | line 19: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M048999 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzFamilyPairingIntegralCommute` | 2 | line 38: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M049031 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzIntegralEqOfBounds` | 5 | line 144: failed to synthesize |
| M049073 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzSeminormTranslateSubLineDerivLe` | 1 | line 28: No goals to be solved |
| M049089 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzTaylorPartialSumDerivBound` | 2 | line 23: Function expected at |
| M049091 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzTaylorSeriesConverges` | 3 | line 73: Application type mismatch: The argument |
| M049109 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SchwartzVanishingDecomposition` | 3 | line 94: 'simp' made no progress |
| M049661 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SemilinearRankComparison` | 1 | (not in excerpt) |
| M049733 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SetIntegralLeOfExpanding` | 2 | line 48: Invalid projection: Projection operates on types of the form 'C ...' where C is a constant. The expre |
| M050613 | P0021 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SpanCoeffProdLinear` | 1 | (not in excerpt) |
| M050649 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SpanRangeInfKerEqSpanRationalKer` | 1 | (not in excerpt) |
| M051301 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.StoneWeierstrassFiniteRep` | 6 | line 95: No goals to be solved |
| M051503 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SumLogDivSubOneLeThreeMulLogAddOne` | 1 | line 12: Application type mismatch: The argument |
| M051526 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.SumPadicValNatLogEqLog` | 2 | line 18: Application type mismatch: The argument |
| M052277 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TendstoLintegralPoissonKernelBoundary` | 1 | line 14: 'fun_prop' was unable to prove 'ContinuousOn (fun s ↦ { cauchy := 1 * (1 + -s.cauchy + t.cauchy) * (1 |
| M053438 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsionBasisRelationsDivisible` | 1 | line 46: Application type mismatch: The argument |
| M053457 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsionCountLogConcavePrimePowers` | 3 | line 97: Application type mismatch: The argument |
| M053524 | P0022 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TorsionLiftNumberFieldModule` | 4 | line 11: unsolved goals |
| M053808 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TotalDegreeLeOfIntegralAtInfinity` | 1 | (not in excerpt) |
| M054319 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TruncatedMonomialsLinearIndependentOverConstants` | 11 | line 40: unsolved goals |
| M054376 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TwistOkAll` | 1 | line 36: Type mismatch |
| M054516 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.TwistedNormFixedDecomposition` | 3 | line 10: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M054699 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UltrametricRootLe` | 3 | line 33: Function expected at |
| M054704 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnfoldIntegralFundamentalDomain` | 1 | line 86: Type mismatch |
| M054706 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnfoldPoincareSeriesLatticeFourier` | 1 | line 181: Application type mismatch: The argument |
| M055002 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnipotentMatrixCoefficientsMem` | 1 | (not in excerpt) |
| M055445 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.UnitaryTensorPlacesSlots` | 2 | line 32: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M055692 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ValuationLeExpNegCardInertiaOfInertiaFixed` | 1 | (not in excerpt) |
| M055728 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ValuationUniformizerIntegralClosureEqExpNegRamif` | 1 | line 28: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M055799 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.VanishingOfProjectionSupport` | 2 | line 141: unsolved goals |
| M056615 | P0023 | `Development.AbelianVarietyTheory.Proofs.DivisorProofs.ZetaTermTsumLeTwo` | 1 | line 29: failed to synthesize |
| M056687 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.AestronglyMeasurableCompRep` | 3 | line 140: unsolved goals |
| M057045 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.CoeSmulMem` | 2 | line 50: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M057323 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.DiscreteSubgroupCountableAndExistsStrictFundamen` | 3 | (not in excerpt) |
| M057575 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsHaarMapProdEq` | 1 | line 16: unsolved goals |
| M057590 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsIntSmulEqInteger` | 1 | line 17: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M057593 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsIntSmulMemLattice` | 1 | line 20: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M057666 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsMapMulRightEqSmul` | 1 | line 54: unsolved goals |
| M057680 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExistsMeasurableLintegralCosetEqOneClosedSubgrou` | 2 | line 38: Type mismatch |
| M057897 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ExtendAeLinearOfLocalSqBoundDense` | 3 | line 17: unsolved goals |
| M058569 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ImportsBisBis` | 1 | line 13: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M058574 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ImportsBisSide` | 1 | line 9: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter of |
| M058579 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ImportsLast` | 2 | line 22: Function expected at |
| M058581 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ImportsRest` | 1 | line 10: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M058647 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.IntegrableExpNegMulOfSublevelGrowth` | 1 | line 49: Type mismatch |
| M058666 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.IntegralNonnegOfSums` | 1 | (not in excerpt) |
| M058770 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsLatticeComapSubtype` | 1 | line 47: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M058792 | P0024 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.IsRadicalSpanPrimeOfNcardPrimesOverEqFinrank` | 2 | line 39: Application type mismatch: The argument |
| M059338 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.MeasurePreimageReindexScaleComplexLe` | 6 | line 37: Application type mismatch: The argument |
| M059343 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.MeasurePreservingCons` | 6 | line 75: Application type mismatch: The argument |
| M059621 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.PackingGeometricMeanSeparated` | 1 | line 114: Function expected at |
| M060034 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.SesqEqZeroOfDiagEqZero` | 1 | line 118: (deterministic) timeout at 'whnf', maximum number of heartbeats (4000000) has been reached |
| M060065 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.SizeIntegralsAndCardCompositions` | 2 | line 74: Function expected at |
| M060110 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.SpanInfEq` | 1 | line 11: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M060235 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.SummableAndTsumLeOfBoxCount` | 1 | line 44: Function expected at |
| M060254 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.TendstoOfSqueeze` | 1 | line 76: Application type mismatch: The argument |
| M060627 | P0025 | `Development.AbelianVarietyTheory.Proofs.FlagMeasures.ZetaProdSphereVolumeBounds` | 2 | line 102: No goals to be solved |
| M060854 | P0025 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.AbsNormSqOfMulConjEqDifferentIdeal` | 3 | line 6: unsolved goals |
| M061523 | P0025 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsBimultiplicativeOfSecondQuotConst` | 1 | line 302: Invalid alternative name 'zero': There are no unhandled alternatives |
| M061741 | P0025 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsIntGeneratorsCardEqOfIsLatticePi` | 1 | line 11: Application type mismatch: The argument |
| M061774 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsIsDiscreteValuationRingOfMaximalIdealEqSpa` | 5 | line 26: Type mismatch |
| M061875 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsNormForm` | 2 | (not in excerpt) |
| M061926 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsPosFiniteDensityOfAlmostTranslationInvaria` | 2 | line 89: Invalid projection: Projection operates on types of the form 'C ...' where C is a constant. The expre |
| M061929 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsPowSmulMemRangeOfSurjectiveBaseChange` | 2 | (not in excerpt) |
| M061967 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsRepresentativesQuotientRangeMulVecLin` | 4 | line 106: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M062046 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsUniqueAlgEquivOfCompatibleQuotient` | 4 | line 15: Invalid alternative name 'zero': There are no unhandled alternatives |
| M062055 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ExistsUnitAlgebraMapEqOfValuationEqOne` | 4 | line 53: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hyg |
| M062134 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.FiniteMaximalSpectrumOfFiniteOfIsLocalRing` | 4 | line 34: Invalid alternative name 'zero': There are no unhandled alternatives |
| M062135 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.FiniteOfIsClosedTorusZariskiOfPowEqOne` | 3 | line 214: Application type mismatch: The argument |
| M062550 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ImportsAlt` | 2 | line 8: unsolved goals |
| M062731 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.IsLeftCoactionIffIsCoactionComm` | 4 | line 62: Invalid alternative name 'zero': There are no unhandled alternatives |
| M062800 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.IterateDerivativeFunMulSubstLeibniz` | 2 | line 35: cannot coerce to function |
| M062816 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.JetRelOfWeierstrassSystem` | 1 | line 40: No goals to be solved |
| M063176 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.MonicFactorCoeffNatDegreeLe` | 3 | line 26: unsolved goals |
| M063198 | P0026 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.MvPowerSeriesThreeEqZeroOfSubstLines` | 2 | line 9: unsolved goals |
| M063438 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.PowFixedOfAlgebraic` | 2 | line 67: unsolved goals |
| M063505 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.ProdPrimesBelowZetaTwoAddLeTwo` | 2 | line 53: failed to synthesize |
| M063547 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.RangeAlgebraMapEqIInfDiscreteValuationSubring` | 7 | line 159: Application type mismatch: The argument |
| M063781 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.SplitHeightSummableExpNegAbs` | 1 | line 22: Function expected at |
| M063878 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.SummableRpowOfFibreCardLe` | 2 | line 45: unsolved goals |
| M063921 | P0027 | `Development.AbelianVarietyTheory.Proofs.FoundationProofs.TensorProductNondegeneratePairing` | 1 | line 25: Application type mismatch: The argument |
| M064282 | P0027 | `Development.AbelianVarietyTheory.Proofs.GenericRegularity.ContDiffEvalFun` | 2 | line 16: Type mismatch |
| M064324 | P0027 | `Development.AbelianVarietyTheory.Proofs.GenericRegularity.ExistsEigenProjectorRingOfIntegers` | 2 | line 52: Tactic 'rcases' failed: 'x✝ : ?m.446' is not an inductive datatype |
| M064573 | P0027 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.BdIntEqZeroOfPrimitive` | 3 | line 143: unsolved goals |
| M064785 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsInterpolationExteriorSmallCoeffs` | 2 | line 35: Function expected at |
| M064800 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.ExistsLeNormLFunctionOne` | 1 | line 302: 'gcongr' did not make progress. |
| M065051 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.IntegralNormSqLp` | 2 | line 107: unsolved goals |
| M065131 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.LFunctionEqTsumOfOneLt` | 1 | line 222: Type mismatch |
| M065412 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.QuadraticUnramifiedIffInertOrSplit` | 4 | line 44: Application type mismatch: The argument |
| M065552 | P0028 | `Development.AbelianVarietyTheory.Proofs.GlobalInterpolation.SumIntervalIntegralLeOfSpaced` | 4 | line 68: unsolved goals |
| M066417 | P0029 | `Development.AbelianVarietyTheory.Proofs.HermitianTraceForms.IsLocallyConstantRankAtStalkEigenSub` | 2 | (not in excerpt) |
| M066424 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.BijectiveRestrictPointsOfEtaleOfHenselian` | 4 | line 269: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hy |
| M066441 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.ExistsIsKroneckerCharOfDiscr` | 1 | line 155: This extensionality tactic only applies to equalities, not |
| M066446 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.ExistsOneTmulOfForallFixed` | 3 | line 20: Tactic 'split_ifs' failed: no if-then-else conditions to split |
| M066454 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.ExistsUniqueFactorCompletedStalkOfMap` | 3 | line 100: could not synthesize default value for parameter 'x._@.Mathlib.Data.List.TFAE.4142160432._hygCtx._hy |
| M066459 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.ExistsValuationSubringLiftOfSpecialFibre` | 4 | line 331: could not synthesize default value for parameter 'h₁' using tactics |
| M066465 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.FinrankOfIsStandardSmoothOfRelativeDimension` | 6 | line 202: Invalid alternative name 'zero': There are no unhandled alternatives |
| M066467 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.FormallyUnramifiedRingOfIntegers` | 12 | line 32: Invalid alternative name 'zero': There are no unhandled alternatives |
| M066483 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.IsDomainAndIsIntegrallyClosedAtPrimeOfSmoothOfCo` | 2 | line 110: Invalid alternative name 'zero': There are no unhandled alternatives |
| M066489 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.IsIsoNormalizationPullbackOfToIntegralClosure` | 86 | line 715: Application type mismatch: The argument |
| M066506 | P0029 | `Development.AbelianVarietyTheory.Proofs.HomogeneousIdeals.RestrictScalarsMapEqSpan` | 1 | line 21: Type mismatch |
| M067292 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CenterMonoidAlgebraLeSpanCentralIntegral` | 4 | (not in excerpt) |
| M067505 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CoeffDetGenericSumMemOfCharpolyCoeffMem` | 2 | (not in excerpt) |
| M067529 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.CoeffZeroSmulMemMap` | 1 | (not in excerpt) |
| M068202 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DetMemSpanAdjugate` | 3 | line 95: unsolved goals |
| M068206 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.DetOneAddSmulBlkMem` | 4 | line 66: unsolved goals |
| M068383 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.EmbeddingIntegralContinuous` | 2 | line 14: Application type mismatch: The argument |
| M068779 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsCorestrictionCocycle` | 2 | line 25: No goals to be solved |
| M068938 | P0030 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsExponentStrictlyLeastWeight` | 1 | line 15: Function expected at |
| M068972 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsFiniteGaloisContainsRootsOfUnits` | 1 | line 35: Type mismatch |
| M069072 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsGLOfSpanRangeEqLocalRing` | 2 | line 48: failed to synthesize |
| M069187 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsIdempotentSubMemOfPowSubMem` | 1 | (not in excerpt) |
| M069337 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsIsPrimitiveRootSubIsUnitOfDvdSubOne` | 2 | line 53: Ambiguous term |
| M069416 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsLinearRelationDescendBaseField` | 2 | line 29: Type mismatch |
| M069479 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsMonicAevalEqZero` | 2 | line 59: Function expected at |
| M069724 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsRootMulPowApprox` | 1 | line 76: Type mismatch: After simplification, term |
| M070042 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ExistsWittVectorGhostEqFrobeniusIterate` | 1 | line 52: No goals to be solved |
| M070165 | P0031 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.FiniteFreeModuleCompactAdicDvr` | 1 | (not in excerpt) |
| M070632 | P0032 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.GaloisLinearDisjoint` | 3 | line 124: Type mismatch |
| M071447 | P0032 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.IsAdicCompleteOfFinite` | 2 | line 46: Application type mismatch: The argument |
| M071673 | P0032 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.IsMulRightInvariantOfCovolumeOne` | 5 | line 60: unsolved goals |
| M071852 | P0032 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.IwahoriFactorisation` | 1 | line 17: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M072513 | P0032 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.MapPiEqOfMapAddHaarEq` | 1 | line 12: unsolved goals |
| M072737 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.MonicDvdXPowCardSubOneExistsRoot` | 2 | line 28: Application type mismatch: The argument |
| M072938 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NormEvalLeSumNormCoeff` | 3 | line 14: Function expected at |
| M072948 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NormHasSumEqOfDominant` | 1 | (not in excerpt) |
| M072974 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NormOneAddEqOne` | 2 | line 29: Function expected at |
| M073027 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NotDvdCoeffAevalOneAddXPowSubOne` | 1 | (not in excerpt) |
| M073039 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.NotXPowSuccDvdDetOfFirstOrderKernelEqZero` | 2 | (not in excerpt) |
| M073057 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.OneAddXMulDerivativeBin` | 12 | line 154: Application type mismatch: The argument |
| M073059 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.OneAddXPowPrimePowSubOneMemSpan` | 2 | line 20: Application type mismatch: The argument |
| M073361 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.ProdOneSubBoundedBelowOfSummable` | 3 | line 49: Function expected at |
| M073708 | P0033 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.RingHomApplyEqPow` | 2 | line 13: Application type mismatch: The argument |
| M074334 | P0034 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.SummableFinprodOfFiniteSupportEulerSum` | 1 | line 61: Function expected at |
| M074483 | P0034 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TendstoRatioBoxCountsProdOne` | 2 | line 8: unsolved goals |
| M074506 | P0034 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TensorProductBasisCoordinates` | 1 | (not in excerpt) |
| M074747 | P0034 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TransferContinuousOfContinuousOn` | 2 | line 9: No goals to be solved |
| M074795 | P0034 | `Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.TsumSetIntegralProdEqZeroOfInner` | 2 | (not in excerpt) |
| M075606 | P0034 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.AevalTotalDegreeLe` | 2 | line 13: No goals to be solved |
| M076736 | P0034 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.DifferentiableAtDet` | 1 | (not in excerpt) |
| M076841 | P0035 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.DvrMapOfCodimOnePrime` | 1 | (not in excerpt) |
| M078022 | P0035 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsMatrixBasisLatticeUpToDenominatorNotMem` | 7 | line 24: 'span_eq_top' is not a field of structure 'Submodule.IsLattice' |
| M078284 | P0035 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsQuasiFinitePolynomialMap` | 9 | line 123: (deterministic) timeout at 'whnf', maximum number of heartbeats (4000000) has been reached |
| M078442 | P0035 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ExistsSmulEqZeroOfCrossed` | 13 | line 78: unsolved goals |
| M079002 | P0035 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.FlatMapColonIdeal` | 5 | line 8: unsolved goals |
| M079228 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.GaussianPhaseCriticalValueBlocksGeneral` | 1 | line 51: unsolved goals |
| M079543 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HeightComapFlatHeightOne` | 2 | (not in excerpt) |
| M079546 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.HeightOneComapMinimal` | 1 | (not in excerpt) |
| M079732 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ImportsFurther` | 1 | line 18: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M080123 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.IsReducedOfNonZeroDivisorMemJacobsonOfAssociated` | 1 | line 51: Application type mismatch: The argument |
| M080892 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.MemSpanMapOfEvalMemOfNeZero` | 5 | line 11: unsolved goals |
| M081032 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.MvPolynomialClearDenominatorsEval` | 1 | (not in excerpt) |
| M081079 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.NonemptyAlgHomAlgebraicClosure` | 1 | line 99: Function expected at |
| M081155 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.NormPowSubPowLe` | 2 | line 52: unsolved goals |
| M081159 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.NormSmulLeOneOfPrimitiveBoundedPowers` | 2 | line 42: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M081483 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PolynomialApproxUniqueness` | 4 | line 129: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M081519 | P0036 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.PosDefUniformBoundsNearPoint` | 2 | (not in excerpt) |
| M081899 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.ResidueFieldIsAlgebraicOfEtale` | 1 | line 16: Application type mismatch: The argument |
| M081935 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.RiemannZetaNeZeroOfMemIoo` | 2 | line 141: Type mismatch |
| M081949 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.RingKrullDimLtTopOfEssFiniteType` | 1 | line 31: mod_cast has type |
| M082067 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.SchurOrthogonalitySubgroupMeasureOne` | 2 | (not in excerpt) |
| M082758 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.TotalDegreeAevalLeOfLinear` | 2 | line 15: No goals to be solved |
| M082791 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.TrdegLeGenerators` | 1 | line 41: failed to synthesize |
| M083123 | P0037 | `Development.AbelianVarietyTheory.Proofs.IwasawaDecomposition.VecMulVecComm` | 3 | line 31: Application type mismatch: The argument |
| M083449 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.CoeffProdXSubCNormLe` | 5 | line 16: unsolved goals |
| M083482 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.ContDiffOnIffLocalExtension` | 1 | line 42: Type mismatch |
| M083696 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.ExistsIsLocalHomExtension` | 6 | line 42: could not synthesize default value for parameter 'h₂' using tactics |
| M083736 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.ExistsNormSubEqOne` | 4 | line 21: Tactic 'rcases' failed: 'x✝ : ?m.110' is not an inductive datatype |
| M083956 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.HomValueCongruentIntModPrime` | 3 | line 50: Application type mismatch: The argument |
| M084063 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.IteratedFDerivProdCoordAt` | 3 | line 18: unsolved goals |
| M084153 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.MemLpTwoAndTendstoOfCauchyOfAeTendsto` | 6 | line 22: Invalid projection: Projections extract constructor fields for one-constructor inductive types. The e |
| M084222 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.NormSumEigenprojectorLeOfResolventBound` | 1 | (not in excerpt) |
| M084307 | P0037 | `Development.AbelianVarietyTheory.Proofs.JetHarmonics.ProdLeOfInterlacingPairing` | 2 | line 81: Function expected at |
| M085251 | P0038 | `Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsSmoothPeriodicPartitionOfUnity` | 3 | line 20: Invalid argument name 'H' for function 'AddSubgroup.isClosed_of_discrete' |
| M085325 | P0038 | `Development.AbelianVarietyTheory.Proofs.ModuliProofs.ExistsUniformRegularityBound` | 21 | line 139: Invalid projection: Projection operates on types of the form 'C ...' where C is a constant. The expr |
| M085773 | P0038 | `Development.AbelianVarietyTheory.Proofs.ModuliProofs.MvPolynomialMapMaximalIdealIsPrime` | 1 | line 27: unsolved goals |
| M085774 | P0038 | `Development.AbelianVarietyTheory.Proofs.ModuliProofs.MvPowerSeriesVariablesSyzygySocle` | 1 | (not in excerpt) |
| M087191 | P0038 | `Development.AbelianVarietyTheory.Proofs.SatakeParameters.EqOneOfNormOneValuationSubOneSmall` | 2 | line 54: Function expected at |
| M087417 | P0038 | `Development.AbelianVarietyTheory.Proofs.SatakeParameters.ExistsIntertwiningFunctional` | 1 | line 186: No goals to be solved |
| M088887 | P0039 | `Development.AbelianVarietyTheory.Proofs.SatakeParameters.NormLeOfRecurrenceGrowth` | 1 | (not in excerpt) |
| M089722 | P0039 | `Development.AbelianVarietyTheory.Proofs.SatakeParameters.TraceQuotientEqOfProjective` | 1 | line 42: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M090282 | P0039 | `Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.LintegralMulRight` | 2 | (not in excerpt) |
| M090404 | P0039 | `Development.AbelianVarietyTheory.Proofs.SiegelThetaTransformation.SummableProdPi` | 1 | line 24: failed to synthesize |
| M090551 | P0039 | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.CardHomVanishingOfDiagBasis` | 2 | line 75: Application type mismatch: The argument |
| M090564 | P0039 | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.DifferentiableOnCoordOfLinearIndependent` | 1 | (not in excerpt) |
| M090578 | P0039 | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.ExistsAlgHomNeZeroOfCountable` | 1 | line 72: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M090667 | P0039 | `Development.AbelianVarietyTheory.Proofs.ThetaLawProofs.ExistsPrimeDimensionLEOneAvoiding` | 1 | line 143: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M091320 | P0039 | `Development.AbelianVarietyTheory.Proofs.ThetaShiftProofs.SummableExpNegSumAbs` | 2 | line 36: Function expected at |
| M091463 | P0040 | `Development.AbelianVarietyTheory.Proofs.ToricGeometry.SeriesApplyEqZeroOfFace` | 2 | (not in excerpt) |
| M091646 | P0040 | `Development.AbelianVarietyTheory.Proofs.TorusHaarMeasure.MeasureUnivLeTwoMulSublevelOfDrift` | 1 | (not in excerpt) |
| M091697 | P0040 | `Development.AbelianVarietyTheory.Proofs.TorusHaarMeasure.TraceMemPrimeOfPowMulVecMemSmul` | 2 | line 68: Tactic 'rcases' failed: 'x✝ : ?m.488' is not an inductive datatype |
| M091702 | P0040 | `Development.AbelianVarietyTheory.Proofs.TorusHaarMeasure.UniformLogExpansionOfPointwise` | 2 | line 115: No goals to be solved |
| M091932 | P0040 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.AffineChangeFundamentalDomainMeanPeriodic` | 2 | line 28: unsolved goals |
| M093542 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsMultilinearSlotwiseExtensionOfEquivariant` | 14 | line 14: Application type mismatch: The argument |
| M093564 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsNonzeroIntSmulMemOfIsLattice` | 1 | line 16: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M093574 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsNsmulMemLattice` | 1 | line 30: Invalid field notation: Function 'Submodule.IsLattice.span_eq_top' does not have a usable parameter o |
| M093753 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsSmoothMulExtensionOfContinuousChar` | 2 | line 69: Type mismatch |
| M093949 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.FiniteAndNcardMinpolyCoeffHeightLe` | 1 | (not in excerpt) |
| M094302 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.FourierUniquenessOfOpenSubgroup` | 2 | (not in excerpt) |
| M094472 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.GradedSeriesContinuationDominated` | 2 | line 26: unsolved goals |
| M094631 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.HasSumCosetsEulerProduct` | 1 | line 265: Function expected at |
| M094974 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.InnerMapEqConstMulProdInner` | 2 | line 9: Application type mismatch: The argument |
| M095049 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.IntegralHaarEqZeroOfFibreIntegralsEqZero` | 1 | line 13: Type mismatch |
| M095588 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.LatticeSumProdNormLeOfProdNormLowerBound` | 4 | line 185: Function expected at |
| M095754 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.LintegralHaarEqCompactSubgroupTransversal` | 1 | line 77: unsolved goals |
| M095854 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.MainThm` | 5 | line 48: Function expected at |
| M096209 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.NewtonRecursionPolyUnique` | 4 | line 45: Tactic 'apply' failed: could not unify the conclusion of 'sum_congr rfl' |
| M096317 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.NullMeasurableSetShearImage` | 2 | line 57: Function expected at |
| M097481 | P0041 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.SummableNonnegFamilyOfDifferentiableOn` | 3 | line 25: Application type mismatch: The argument |
| M097941 | P0042 | `Development.AbelianVarietyTheory.Proofs.TwistedOperators.TsumSetIntegralFundamentalDomainEqZeroByOrbits` | 1 | line 148: Type mismatch |
| M098693 | P0042 | `Development.AbelianVarietyTheory.Proofs.UniformizationProofs.ExistsGradedRingKernelLift` | 1 | line 116: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M099910 | P0042 | `Development.AbelianVarietyTheory.Proofs.UnitaryExistence.MapRestrictSubgroupEqCommonSmulHaar` | 3 | line 72: unsolved goals |
| M101080 | P0042 | `Development.AbelianVarietyTheory.PublishedTheorems.TwistedTraceFormula.RealMetaplecticRepresentation` | 3 | line 77: Invalid '⟨...⟩' notation: The expected type |
| M101260 | P0042 | `Development.AutomorphicArithmetic.AdelicQuotients.ExistsNatCombinationIsUnitOfIsUnitCombination` | 4 | (not in excerpt) |
| M101428 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.ContinuousContractNth` | 1 | (not in excerpt) |
| M101500 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.HidaCompleteRings.FinCompl` | 1 | line 76: Application type mismatch: The argument |
| M101501 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.HidaCompleteRings.FinMax` | 1 | line 19: Application type mismatch: The argument |
| M101618 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.OrdExt` | 1 | line 11: Application type mismatch: The argument |
| M101634 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.SmithZeroOne` | 8 | line 21: No goals to be solved |
| M101638 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.AlgebraTools.SqrtOneAdd` | 1 | line 25: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M102182 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.BuildingsResidueChars.ExistsEquivariantProjectionsOfSumIrreducible` | 1 | (not in excerpt) |
| M102188 | P0043 | `Development.AutomorphicArithmetic.AutomorphicVarieties.BuildingsResidueChars.ExistsFixedRotationBasisOfCharpoly` | 1 | (not in excerpt) |
| M102734 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.CommutativeAlgebraHeight.GHommem` | 6 | line 85: unsolved goals |
| M103037 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.CurveDVRSpecialization.SelfTwistEigenvalues.UnipTorsion` | 3 | line 17: Application type mismatch: The argument |
| M104090 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.HermiteNormalForms.Hadam` | 1 | line 28: Function expected at |
| M104619 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.ReductionBoundsTorsion.CompactLocalSets.SimpBdM` | 7 | line 65: No goals to be solved |
| M104621 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.ReductionBoundsTorsion.CompactLocalSets.UnfoldM` | 1 | line 42: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M104667 | P0044 | `Development.AutomorphicArithmetic.AutomorphicVarieties.LiteratureResults.KTheoryStability.ReductionBoundsTorsion.MomentEntryBounds.SubLeSumAbsConsecutiveDiff` | 1 | line 58: Tactic 'rewrite' failed: Did not find an occurrence of the pattern |
| M105581 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.InductionEstimates.UnipotentBlockMatrices.ClosureOrbits.FinClosure` | 1 | line 77: Application type mismatch: The argument |
| M106289 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.GlobalUnitaryForms.IntegralStabilizers.FinSAbs` | 2 | line 120: unsolved goals |
| M106499 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.SymmetricPowerTransfer.TraceFormulaEigenvalues.TraceNil` | 3 | line 45: Tactic 'rcases' failed: 'x✝ : ?m.51' is not an inductive datatype |
| M108461 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.TheoremsMuLinked.HidaOrdinaryHecke.ClosedSub` | 1 | line 24: Application type mismatch: The argument |
| M108510 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.TheoremsMuLinked.SpectralEigenvalues.Dlam` | 2 | line 8: Application type mismatch: The argument |
| M108992 | P0045 | `Development.AutomorphicArithmetic.AutomorphicVarieties.WeakShimuraTheory.FibreTraces.FibTrdeg` | 3 | line 9: unsolved goals |
| M109299 | P0045 | `Development.AutomorphicArithmetic.CMTraceForms.ProdPrimeFactorsPowCeilPadicValNatMulEqPow` | 2 | line 13: Application type mismatch: The argument |
| M109792 | P0045 | `Development.AutomorphicArithmetic.CyclotomicBounds.ClassNumberBounds.AdditiveValuation.UnramExtY` | 5 | line 30: Application type mismatch: The argument |
| M109821 | P0046 | `Development.AutomorphicArithmetic.CyclotomicBounds.ClassNumberBounds.HeckeCharacterChoice.TendstoUnderCofinite` | 6 | line 80: Application type mismatch: The argument |
| M109930 | P0046 | `Development.AutomorphicArithmetic.CyclotomicBounds.DeRhamLattices.FiltrationEqSpanOfEisensteinPowBasisChange` | 2 | line 29: Type mismatch |
| M110130 | P0046 | `Development.AutomorphicArithmetic.DivisorFrames.EqTopOfCircleSup` | 1 | line 32: Invalid rewrite argument: Expected an equality or iff proof or definition name, but 'ha ?b' is a proo |
| M110174 | P0046 | `Development.AutomorphicArithmetic.DivisorFrames.ExistsNsmulMemSumImageLatticeOfSurjectiveMod` | 1 | line 78: Invalid argument name 'H' for function 'AddSubgroup.isClosed_of_discrete' |
| M110469 | P0046 | `Development.AutomorphicArithmetic.EtaleIdempotents.GaloisEquivariantTensorDescentOfPrimePowerUnits` | 3 | line 18: Invalid alternative name 'zero': There are no unhandled alternatives |
| M110751 | P0046 | `Development.AutomorphicArithmetic.Foundations.Convolution.ConvolutionKernels.PresOfOrder` | 1 | line 17: unsolved goals |
| M111007 | P0046 | `Development.AutomorphicArithmetic.Foundations.Convolution.PolynomialCoefficientBounds.MatrixEntryAbsSumUnitaryLieCoordinatesSplit` | 2 | line 15: unsolved goals |
| M114956 | P0047 | `Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.AeTranslateEq` | 1 | line 9: Invalid field notation: Function 'MeasureTheory.Measure.QuasiMeasurePreserving.ae' does not have a usa |
| M114967 | P0047 | `Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.AlgebraSmulCommClassComplex` | 1 | line 124: Application type mismatch: The argument |
| M114978 | P0047 | `Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.BiHomSum` | 1 | (not in excerpt) |
| M114992 | P0047 | `Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.CapelliComplements.FirstLemmaA` | 3 | line 22: unsolved goals |
| M114996 | P0047 | `Development.AutomorphicArithmetic.IntegralCasts.CapelliIdentities.CapelliComplements.FirstLemmaE` | 2 | line 24: Function expected at |
